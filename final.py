
import jamo
from switch_jamo_assemble import jamo_assemble
import RPi.GPIO as GPIO      # gpio 라이브러리
from time import sleep       # sleep 라이브러리
from hangul_utils import join_jamos 
from jamo import j2h 
from jamo import j2hcj
from jamo import h2j

import numpy as np           #numpy는 행렬,배열에 이용할 함수

import switch_button_input
import switch_button_revise
import switch_jamo_assemble
import switch_button_next_before

visits = []
sexs = []
births = []
p_nums = []
whys = []
agrees = []
names = []
num_input = 0


Button_start = 24   #시작 버튼, 18
Button_revise = 17    #정정 버튼, 11
Button_conso = 27     #자음 버튼, 13
Button_vowel = 22     #모음 버튼, 15
Button_num = 23       #숫자 버튼, 16
Button_down = 25       #아래 버튼, 22
Button_up = 5       #위 버튼, 29
Button_input = 6     #입력 버튼, 31
Button_back = 13      #뒤로/다시 버튼, 33
Button_next = 19      #다음/네 버튼, 35

input_mode = 0        #mode  1: 자음 2: 모음 3: 숫자
                      #방향키로 조절할 숫자의 최대, 그때 그때 받아오기

count_updown = 0        #방향키로 조절할 때 조절될 숫자


num_input = 0           #입력 버튼 -  저장될 값
num_input_save = 0      #다음 버튼 - 저장될 값

chosung_index = ""       #문자열로 선언 해주어야 하나
jungsung_index = ""
jongsung_index = ""
sung_index_1 = []
sung_index_2 = []
sung_index_3 = []
sung_index_4 = []
sung_index_5 = []
sung_index = ""         #필요한가??  #겹받침 없을때에 문자 인덱스
sung_index_gyup = ""    #필요한가??  #겹받침 검사용 문자 인덱스


chosung = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
jungsung = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
jongsung = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

hangul = []


jamo_join_final_1 = ''
jamo_join_final_2 = ''
jamo_join_final_3 = ''
jamo_join_final_4 = ''

jamo_index = []
jamo_join_input = ''            #입력버튼 - 저장될 문자
jamo_join_input_index = []      #입력버튼 - 글자가 완성되면 저장
jamo_join_input_save = ''       #다음버튼 - 저장될 문자
jamo_join_input_index_save = [] #다음버튼 - 저장될 문자

jamo_join_input_save = ''
jamo_join_input_index_save = []
jamo_join_input_index_save_index = []

adress_input = []



syllables = np.array([chr(code) for code in range(44032, 55204)])
syllables = syllables.reshape(19, 21, 28)
      




GPIO.setmode(GPIO.BCM)      # GPIO BCM 모드 셋    #GPIO.setmode(GPIO.BOARD) board모드 셋

GPIO.setup(Button_start, GPIO.IN) # 버튼 입력으로 설정 GPIO.setup(Button_start, GPIO.IN, initial = 1)로 초기값 설정 가능
GPIO.setup(Button_revise, GPIO.IN)
GPIO.setup(Button_conso, GPIO.IN)
GPIO.setup(Button_vowel, GPIO.IN)
GPIO.setup(Button_num, GPIO.IN)
GPIO.setup(Button_down, GPIO.IN)
GPIO.setup(Button_up, GPIO.IN)
GPIO.setup(Button_input, GPIO.IN)
GPIO.setup(Button_back, GPIO.IN)
GPIO.setup(Button_next, GPIO.IN)

print ('Start the GPIO App')  # 시작을 알리자!
print ("Press the button (CTRL-C to exit)")



#버튼이 눌릴때 설정
GPIO.wait_for_edge(pin/port number, GPIO.FALLING, timeout=5000) #falling edge 감지, 스위치는 평상시 1, 눌렸을때 0 인데 1에서 0으로 값이 떨어지는(Falling) 경우가 스위치를 누른 동작에 해당
GPIO.add_event_detect(Button_up, GPIO.RISING, callback=count_up, bouncetime=300) # Botton_up이 rising될때 count_up함수 호출, 디바운싱 300

GPIO.add_event_detect(Button_start, GPIO.RISING, bouncetime=300) # Botton_up이 rising될때 count_up함수 호출, 디바운싱 300
GPIO.add_event_detect(Button_revise, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_conso, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_vowel, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_num, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_down, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_up, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_input, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_back, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_next, GPIO.RISING, bouncetime=300)


# print('input_mode : ',input_mode)
# print('count_updown : ', count_updown)

# step 0

# step 1
# keypad2()



        
print("안녕하세요 이길입니다")
print("처음 방문이신 가요?")
print("1.예 2.아니오")  # 만약에 재방문이면 step4 에서 step 9로 이동
visit = ['예', '아니오']
    

while True:
                
            if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
            else:
                    pass

            
                            
            if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
            else:
                    pass
            
            
            #button_up&down부분
            
            if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
            else:
                    pass
            
                            
                            
            if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
            else:
                    pass
            
            
            
            
            #수정버튼 부분
            if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
            else:
                    pass
            
            
            #다음버튼
            if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
            if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
            if keyboard.read_key() == Button_start:
    
                     break
            sleep(0.1)

        
                # num_input = num_input_save
                # jamo_join_input_index = jamo_join_input_index_save
                # return num_input_save
                # return jamo_join_input_index_save
                
  
       
            
            # keypad2()
            # num_size = len(visit)
            # 답변 숫자 입력한 후 다음 누름
visit_num = num_input

visits.append(visit[visit_num - 1])
visit_num = 0
num_input = 0

print(visits)
    
# step 2

while True:
        if keyboard.read_key() ==Button_start:
            print("이름을 입력해 주세요")
            
            while True:
                        
                                        
                        # 버튼이 눌릴 때 실행할 것들
                        if keyboard.read_key() ==Button_conso:
                                input_mode = 1
                                count_updown = 0
                                #자음이라는 말 출력
                                print('input_mode : ', input_mode)
                                pass
                        else:
                                pass
                        
                        
                        if keyboard.read_key() ==Button_vowel:
                                input_mode = 2
                                count_updown = 0
                                #모음이라는 말 출력
                                
                                print('input_mode : ', input_mode)
                                pass
                        else:
                                pass
                        
                        
                        if keyboard.read_key() ==Button_num:
                                input_mode = 3
                                count_updown = 0
                                #숫자라는 말 출력        
                                
                                print('input_mode : ', input_mode)
                                pass
                        else:
                                pass

                        
                                        
                        if keyboard.read_key() == Button_input:
                                
                                print('Button_input is pushed')
                                
                                #count_updown 숫자에 따라 자음 설정
                                if input_mode == 1 :
                                        

                                        sung = switch_button_input.push_Button_input_conso(count_updown) 
                                        
                                        sung_index_1.append(sung)                                          #설정된 자음 sung_index에 추가
                                        sung_index_2.append(sung)
                                        sung_index_3.append(sung)
                                        sung_index_4.append(sung)
                                        sung_index_5.append(sung)
                                        
                                        jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                        jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                        jamo_join_final_3 = switch_jamo_assemble.jamo_assemble(sung_index_3)
                                        jamo_join_final_4 = switch_jamo_assemble.jamo_assemble(sung_index_4)
                                        jamo_join_final_5 = switch_jamo_assemble.jamo_assemble(sung_index_5)
                                        
                                        print('jamo_join_final_1,jamo_join_final_2',jamo_join_final_1,jamo_join_final_2)                                         
                                                                        
                                        #jamo-join_final 읽어주기       
                                                
                                
                                elif input_mode == 2 :
                                        
                                        sung = switch_button_input.push_Button_input_vowel(count_updown)
                                        
                                        sung_index_1.append(sung)
                                        sung_index_2.append(sung)
                                        sung_index_3.append(sung)
                                        sung_index_4.append(sung)
                                        sung_index_5.append(sung)
                                        
                                        jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                        jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                        jamo_join_final_3 = switch_jamo_assemble.jamo_assemble(sung_index_3)
                                        jamo_join_final_4 = switch_jamo_assemble.jamo_assemble(sung_index_4)
                                        jamo_join_final_5 = switch_jamo_assemble.jamo_assemble(sung_index_5)
                                        
                                        print('jamo_join_final_1,jamo_join_final_2',jamo_join_final_1,jamo_join_final_2)
                                        
                                        #jamo-join_final 읽어주기
                                        
                                        
                                else  :                                                 #숫자 input
                                        num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                                        #num_input 읽어주기
                                        # return num_input
                                
                        
                                if len(sung_index_1) == 4:    
                                        if sung_index_1[3] in jungsung:
                                                
                                                sung_index_1 = sung_index_1[:2]
                                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                                jamo_join_input_index = jamo_join_input_index[:-1]
                                                jamo_join_input_index.append(jamo_join_final_1)
                                                
                                                
                                                sung_index_1 = sung_index_2[2:]
                                                sung_index_2 = sung_index_2[2:]
                                                sung_index_3 = sung_index_2[2:]
                                                sung_index_4 = sung_index_2[2:]
                                                jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                                jamo_join_input_index.append(jamo_join_final_2)
                                                
                                        
                                                                
                                                
                                        else:
                                                jamo_join_input_index = jamo_join_input_index[:-1]
                                                jamo_join_input_index.append(jamo_join_final_1)
                                                
                                elif len(sung_index_1) == 5:               
                                        if sung_index_1[4] in jungsung:
                                                
                                                sung_index_2 = sung_index_2[:3]
                                                jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                                print('jjjjamo_join_final_2',jamo_join_final_2)
                                                jamo_join_input_index = jamo_join_input_index[:-1]
                                                jamo_join_input_index.append(jamo_join_final_2)
                                                sung_index_1 = sung_index_3[3:]
                                                sung_index_2 = sung_index_3[3:]
                                                sung_index_3 = sung_index_3[3:]
                                                sung_index_4 = sung_index_3[3:]
                                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                                jamo_join_input_index.append(jamo_join_final_1)
                                        
                                        elif sung_index_1[4] in chosung:
                                                
                                                sung_index_1 = sung_index_1[:4]
                                                jamo_join_final_4 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                                print('jjjjamo_join_final_4',jamo_join_final_4)
                                                jamo_join_input_index = jamo_join_input_index[:-1]
                                                jamo_join_input_index.append(jamo_join_final_4)
                                                sung_index_1 = sung_index_3[4:]
                                                sung_index_2 = sung_index_3[4:]
                                                sung_index_3 = sung_index_3[4:]
                                                sung_index_4 = sung_index_3[4:]
                                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                                jamo_join_input_index.append(jamo_join_final_1)
                                                
                                        
                                        else:
                                                jamo_join_input_index = jamo_join_input_index[:-1]
                                                jamo_join_input_index.append(jamo_join_final_1)
                                
                                elif  len(sung_index_2)==6:      
                                        if sung_index_2[5] in jungsung:
                                                
                                                sung_index_3 = sung_index_3[:3]
                                                jamo_join_final_3 = switch_jamo_assemble.jamo_assemble(sung_index_3)
                                                print('jamo_join_final_3:',jamo_join_final_3)
                                                jamo_join_input_index = jamo_join_input_index[:-1]
                                                jamo_join_input_index.append(jamo_join_final_1)
                                                sung_index_1 = sung_index_2[4:]
                                                sung_index_2 = sung_index_2[4:]
                                                sung_index_3 = sung_index_2[4:]
                                                sung_index_4 = sung_index_2[4:]
                                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                                jamo_join_input_index.append(jamo_join_final_1)
                                        else :
                                                jamo_join_input_index = jamo_join_input_index[:-1]
                                                jamo_join_input_index.append(jamo_join_final_1)
                                        
                                                
                                else : 
                                        if len(sung_index_1) == 1:
                                                jamo_join_input_index.append(jamo_join_final_1)
                                        else:
                                                jamo_join_input_index = jamo_join_input_index[:-1]
                                                jamo_join_input_index.append(jamo_join_final_1)
                                
                                
                                      
                                
                                print('jamo_join_input_index : ', jamo_join_input_index)
                                jamo_join_input = ''

                                                        
                                print('sung_index_1,sung_index_2,sung_index_3,sung_index_4',sung_index_1,sung_index_2,sung_index_3,sung_index_4)
                                count_updown = 0
                                print('jamo_join_input 3 : ',jamo_join_input)
                                print('num_input:',num_input)
                                print('count_updown: ',count_updown)
                                print('jamo_join_input_index:',jamo_join_input_index)
                                sleep(0.5)
                                pass
                        else:
                                pass
                        
                

                        
                        
                        
                        #button_up&down부분
                        
                        if keyboard.read_key() ==Button_up:
                                count_updown = count_updown + 1
                                
                                if input_mode == 1:
                                        count_updown = count_updown % 19 
                                        sung = switch_button_input.push_Button_input_conso(count_updown)
                                        print('sung:',sung)
                                        #sung 읽어주기
                                        
                                        pass
                                
                                        
                                elif input_mode == 2:
                                        count_updown = count_updown % 21
                                        sung = switch_button_input.push_Button_input_vowel(count_updown)
                                        print('sung:',sung)
                                        #sung 읽어주기
                                        pass
                                        
                                        
                                else :
                                        count_updown = count_updown % num_size                                                          #num_size가 최대값
                                        print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                                        #count_updown 읽어주기
                                        pass
                                
                                
                        
                        else:
                                pass
                        
                                        
                                        
                        if keyboard.read_key() ==Button_down:                                                 
                                count_updown = count_updown - 1

                                if input_mode == 1:
                                        count_updown = count_updown % 19 
                                        sung = switch_button_input.push_Button_input_conso(count_updown)
                                        print('sung:',sung)
                                        #sung 읽어주기
                                        pass
                                
                                        
                                elif input_mode == 2:
                                        count_updown = count_updown % 21
                                        sung = switch_button_input.push_Button_input_vowel(count_updown)
                                        print('sung:',sung)
                                        #sung 읽어주기
                                        pass
                                        
                                        
                                else :
                                        count_updown = count_updown % num_size  
                                        print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                                        #count_updown 읽어주기
                                        pass
                        else:
                                pass
                        
                        
                        
                        
                        #수정버튼 부분
                        if keyboard.read_key() ==Button_revise:
                                
                                if jamo_join_input_index != []:
                                        jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                                        
                                        print(jamo_join_input)
                                        pass
                                        
                                        
                                elif  num_input != 0:
                                        num_input = switch_button_revise.push_Button_revise_num(num_input)
                                        print(num_input)
                                        pass
                                else :
                                        pass
                        else:
                                pass
                        
                        
                       #다음버튼
                        if keyboard.read_key() ==Button_next:
                                
                                #step 올리기
                                
                                if jamo_join_input != '' or jamo_join_input_index != []:
                                        jamo_join_input_save = jamo_join_input
                                        
                                        jamo_join_input_index_save = jamo_join_input_index
                                        jamo_join_input_index_save_index = jamo_join_input_index
                                        jamo_join_input_index_save = ''.join(jamo_join_input_index)
                                        
                                        jamo_join_input = ''
                                        jamo_join_input_index = []
                                        
                                        count_updown = 0

                                else :
                                        num_input_save = num_input
                
                                        num_input = 0
                                        
                                        count_updown = 0
                                        
                                print('jamo_join_input 5 : ',jamo_join_input)
                                print('jamo_join_input_index : ',jamo_join_input_index)
                                print('jamo_join_input_save',jamo_join_input_save)
                                print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                                
                                print('num_input : ',num_input)
                                print('num_input_save : ', num_input_save)
                        
                        # return num_input        
                                
                        
                                
                        #뒤로버튼                
                        if keyboard.read_key() == Button_back:
                                #step 내리기!!
                                
                                if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                                        jamo_join_input_index = jamo_join_input_index_save_index
                                        print(''.join(jamo_join_input_index_save))
                                        #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                                        
                                        count_updown = 0

                                else :
                                        print(num_input_save)
                                        #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                                        num_input = num_input_save
                                        
                                        
                                        count_updown = 0
                        
                                print('jamo_join_input 5 : ',jamo_join_input)
                                print('jamo_join_input_index : ',jamo_join_input_index)
                                print('jamo_join_input_save',jamo_join_input_save)
                                print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                                
                                print('num_input : ',num_input)
                                print('num_input_save : ', num_input_save)
                        
                        
                                        
                        sleep(0.1)
        
                        if keyboard.read_key() == Button_start:
                                break
            
            name = jamo_join_input_index #이름 입력받아야함
            #답변 숫자 입력한 후 다음 누름
            names.append(name)
            num_input = 0
            print(names)    
            



    # step 3

while True:
    if keyboard.read_key() ==Button_start:
        print("성별을 선택해 주세요")
        print("1. 남, 2. 여")
        sex = ['남', '여']
        if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
        else:
                    pass

            
                            
        if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
        else:
                    pass
            
            
            #button_up&down부분
            
        if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
        else:
                    pass
            
                            
                            
        if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
        else:
                    pass
            
            
            
            
            #수정버튼 부분
        if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
        else:
                    pass
            
            
            #다음버튼
        if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
        if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
        if keyboard.read_key() == Button_start:
    
                     break
        sleep(0.1)
        sex_num = num_input
        # 답변 숫자 입력한 후 다음 누름
        sexs.append(sex[sex_num - 1])
        sex_num = 0
        
        num_input = 0
        print(sexs)

     # step 4

while True:
    
    if keyboard.read_key() ==Button_start:
        
        print("생년월일을 입력해 주세요")
        
        if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
        else:
                    pass

            
                            
        if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
        else:
                    pass
            
            
            #button_up&down부분
            
        if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
        else:
                    pass
            
                            
                            
        if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
        else:
                    pass
            
            
            
            
            #수정버튼 부분
        if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
        else:
                    pass
            
            
            #다음버튼
        if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
        if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
        if keyboard.read_key() == Button_start:
    
                     break
        sleep(0.1)
        
        birth = num_input
        births.append(birth)
        birth = 0
        num_input = 0
        print(births)

    # step 4.5

    file_name = names[0] + births[0] + sexs[0]
    f = open(file_name, 'w', encoding='utf-8')
    wr = csv.writer(f)
    wr.writerow([1, '이름 생년월일 성별', names[0] + births[0] + sexs[0]])

    # step 5

while True:
    if keyboard.read_key() == Button_start:
        print("전화번호를 입력해주세요")
        p_num = num_input
        
        if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
        else:
                    pass

            
                            
        if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
        else:
                    pass
            
            
            #button_up&down부분
            
        if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
        else:
                    pass
            
                            
                            
        if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
        else:
                    pass
            
            
            
            
            #수정버튼 부분
        if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
        else:
                    pass
            
            
            #다음버튼
        if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
        if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
        if keyboard.read_key() == Button_start:
    
                     break
        sleep(0.1)
        
        p_nums.append(p_num)
        p_num = 0
        num_input = 0
        print(p_nums)
        wr.writerow([2, '전화번호', p_nums[0]])

    # setp 6

while True:
    if keyboard.read_key() == Button_start:
        print(
            "1. 중구, 2. 서구, 3. 동구, 4. 영도구, 5. 부산진구, 6. 동래구, 7. 남구, 8. 북구, 9. 해운대구, 10. 사하구, 11. 금정구, 12. 강서구, 13. 연제구, 14.수영구, 15. 사상구, 16. 기장구")

        adress = []  # 주소추가되는 리스트

        ad = ['중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구', '사상구',
              '기장구']
        ad_len = len(ad)
        
        if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
        else:
                    pass

            
                            
        if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
        else:
                    pass
            
            
            #button_up&down부분
            
        if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
        else:
                    pass
            
                            
                            
        if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
        else:
                    pass
            
            
            
            
            #수정버튼 부분
        if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
        else:
                    pass
            
            
            #다음버튼
        if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
        if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
        if keyboard.read_key() == Button_start:
    
                    break
        
        ad_num = num_input

        adress.append(ad[ad_num - 1])
        print(adress)
        ad_num = 0
        num_input = 0
        # ad_num 초기화

#     # step 7

    if keyboard.read_key() == Button_start:
        if ad[0] in adress:  # 중구
            print("1. 영주동, 2. 대창동, 3. 중앙동, 4. 동광동, 5. 대청동, 6. 보수동, 7. 부평동, 8. 신창동, 9. 창선동, 10. 광복동, 11. 남포동")
            ad_jg = ['영주동', '대창동', '중앙동', '동광동', '대창동', '보수동', '부평동', '신창동', '창선동', '광복동', '남포동']
            print("주소를 선택해 주세요")
            numsize = len(ad_jg)
            if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
        else:
                    pass

            
                            
        if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
        else:
                    pass
            
            
            #button_up&down부분
            
        if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
        else:
                    pass
            
                            
                            
        if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
        else:
                    pass
            
            
            
            
            #수정버튼 부분
        if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
        else:
                    pass
            
            
            #다음버튼
        if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
        if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
        if keyboard.read_key() == Button_start:
    
                    break
        ad_num = num_input
        adress.append(ad_jg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[1] in adress:  # 서구
            print("1. 동대신동, 2. 서대신동, 3. 부용동, 4. 부민동, 5. 토성동, 6. 아미동, 7. 조장동, 8. 충무동, 9. 남부민동, 10. 암남동")
            ad_sg = ['동대신동', '서대신동', '부용동', '부민동', '토성동', '아미동', '조장동', '충무동', '남부민동', '암남동']
            print("주소를 선택해 주세요")
            ad_num = num_input
            if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
            else:
                    pass

            
                            
            if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
            else:
                    pass
            
            
            #button_up&down부분
            
            if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
            else:
                    pass
            
                            
                            
            if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
            else:
                    pass
            
            
            
            
            #수정버튼 부분
            if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
            else:
                    pass
            
            
            #다음버튼
            if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
            if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
            if keyboard.read_key() == Button_start:
    
                    break
            numsize = len(ad_sg)
            adress.append(ad_sg[ad_num - 1])
            ad_num = 0
            num_input = 0
            print(adress)

    elif ad[2] in adress:  # 동구
            print("1. 초량동, 2. 수정동, 3. 좌천동, 4. 범일동")
            ad_dg = ['초량동', '수정동', '좌천동', '범일동']
            print("주소를 선택해 주세요")
            ad_num = num_input
            if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
            else:
                    pass

            
                            
            if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
            else:
                    pass
            
            
            #button_up&down부분
            
            if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
            else:
                    pass
            
                            
                            
            if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
            else:
                    pass
            
            
            
            
            #수정버튼 부분
            if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
            else:
                    pass
            
            
            #다음버튼
            if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
            if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
            if keyboard.read_key() == Button_start:
    
                    break
            numsize = len(ad_dg)
            adress.append(ad_dg[ad_num - 1])
            ad_num = 0
            num_input = 0
            print(adress)

    elif ad[3] in adress:  # 영도구
            print("1. 대교동, 2. 대평동, 3. 남항동, 4. 영선동, 5. 신성동, 6. 봉래동, 7. 청학동, 8. 동삼동")
            ad_ydg = ['대교동', '대평동', '남항동', '영선동', '신성동', '봉래동', '청학동', '동삼동']
            print("주소를 선택해 주세요")
            ad_num = num_input
            
            if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
            else:
                    pass

            
                            
            if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
            else:
                    pass
            
            
            #button_up&down부분
            
            if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
            else:
                    pass
            
                            
                            
            if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
            else:
                    pass
            
            
            
            
            #수정버튼 부분
            if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
            else:
                    pass
            
            
            #다음버튼
            if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
            if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
            if keyboard.read_key() == Button_start:
    
                    break
            numsize = len(ad_ydg)
            adress.append(ad_ydg[ad_num - 1])
            ad_num = 0
            num_input = 0
            print(adress)
            if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
            else:
                    pass

            
                            
            if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
            else:
                    pass
            
            
            #button_up&down부분
            
            if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
            else:
                    pass
            
                            
                            
            if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
            else:
                    pass
            
            
            
            
            #수정버튼 부분
            if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
            else:
                    pass
            
            
            #다음버튼
            if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
            if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
            if keyboard.read_key() == Button_start:
    
                    break
    elif ad[4] in adress:  # 부산진구
            print("1. 양정동, 2. 전포동, 3. 부전동, 4. 범천동, 5. 범전동, 6. 연지동, 7. 초읍동, 8.부암동, 9. 당감동, 10. 가야동, 11. 개금동")
            ad_jg = ['양정동', '전포동', '부전동', '범천동', '범전동', '연지동', '초읍동', '부암동', '당감동', '가야동', '개금동']
            print("주소를 선택해 주세요")
            ad_num = num_input
            if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
            else:
                    pass

            
                            
            if keyboard.read_key() == Button_input:
                        
                        print('Button_input is pushed')
                        if input_mode ==3  :                                                 #숫자 input
                                num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                                #num_input 읽어주기
                                
                        sleep(0.5)
                        pass
            else:
                    pass
                
                
                #button_up&down부분
                
            if keyboard.read_key() ==Button_up:
                        count_updown = count_updown + 1
                        
                        if input_mode == 3:
                                count_updown = count_updown % num_size                                                          #num_size가 최대값
                                print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                                
                                pass
                        else:
                            pass
            else:
                        pass
                
                                
                                
            if keyboard.read_key() ==Button_down:                                                 
                        count_updown = count_updown - 1
                                    
                        if input_mode == 3:
                                count_updown = count_updown % num_size  
                                print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                                #count_updown 읽어주기
                                pass
            else:
                        pass
                
                
                
                
                #수정버튼 부분
            if keyboard.read_key() ==Button_revise:
                        
                        if jamo_join_input_index != []:
                                jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                                
                                print(jamo_join_input)
                                pass
                                
                                
                        elif  num_input != 0:
                                num_input = switch_button_revise.push_Button_revise_num(num_input)
                                print(num_input)
                                pass
                        else :
                                pass
            else:
                        pass
                
                
                #다음버튼
            if keyboard.read_key() ==Button_next:
                        
                        #step 올리기
                        
                        if jamo_join_input != '' or jamo_join_input_index != []:
                                jamo_join_input_save = jamo_join_input
                                
                                jamo_join_input_index_save = jamo_join_input_index
                                jamo_join_input_index_save_index = jamo_join_input_index
                                jamo_join_input_index_save = ''.join(jamo_join_input_index)
                                
                                jamo_join_input = ''
                                jamo_join_input_index = []
                                
                                count_updown = 0

                        else :
                                num_input_save = num_input
        
                                num_input = 0
                                
                                count_updown = 0
                                
                        print('jamo_join_input 5 : ',jamo_join_input)
                        print('jamo_join_input_index : ',jamo_join_input_index)
                        print('jamo_join_input_save',jamo_join_input_save)
                        print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                        
                        print('num_input : ',num_input)
                        print('num_input_save : ', num_input_save)
                
                        
                        
                
                        
                                
            if keyboard.read_key() == Button_back:
                        #step 내리기!!
                        
                        if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                                jamo_join_input_index = jamo_join_input_index_save_index
                                print(''.join(jamo_join_input_index_save))
                                #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                                
                                count_updown = 0

                        else :
                                print(num_input_save)
                                #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                                num_input = num_input_save
                                
                                
                                count_updown = 0
                
                        print('jamo_join_input 5 : ',jamo_join_input)
                        print('jamo_join_input_index : ',jamo_join_input_index)
                        print('jamo_join_input_save',jamo_join_input_save)
                        print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                        
                        print('num_input : ',num_input)
                        print('num_input_save : ', num_input_save)
                
            if keyboard.read_key() == Button_start:
        
                        break
            numsize = len(ad_jg)
            adress.append(ad_jg[ad_num - 1])
            ad_num = 0
            num_input = 0
            print(adress)

    elif ad[5] in adress:  # 동래구
        print("1. 명장동, 2. 안락동, 3. 칠산동, 4. 낙민동, 5. 복천동, 6. 수안동, 7. 명륜동, 8. 온천동, 9. 사직동")
        ad_drg = ['명장동', '안락동', '칠산동', '낙민동', '복천동', '수안동', '명륜동', '온천동', '사직동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_drg)
        adress.append(ad_drg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[6] in adress:  # 남구
        print("1. 대연동, 2. 용호동, 3. 용당동, 4. 문현동, 5. 우암동, 6. 감만동")
        ad_ng = ['대연동', '용호동', '용당동', '문현동', '우암동', '감만동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_ng)
        adress.append(ad_ng[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[7] in adress:  # 북구
        print("1. 금곡동, 2. 화명동, 3. 만덕동, 4. 덕천동, 5. 구포동")
        ad_bg = ['금곡동', '화명동', '만덕동', '덕천동', '구포동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_bg)
        adress.append(ad_bg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[8] in adress:  # 해운대구
        print("1. 반송동, 2. 석대동, 3. 반여동, 4. 재송동, 5. 우동, 6. 중동, 7. 좌동, 8. 송정동")
        ad_hudg = ['반송동', '석대동', '반여동', '재송동', '우동', '중동', '좌동', '송정동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_hudg)
        adress.append(ad_hudg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[9] in adress:  # 사하구
        print("1. 괴정동, 2. 당리동, 3. 하단동, 4. 신평동, 5. 장림동, 6. 다대동, 7. 구평동, 8. 감천동")
        ad_shg = ['괴정동', '당리동', '하단동', '신평동', '장림동', '다대동', '구평동', '감천동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_shg)
        adress.append(ad_shg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[10] in adress:  # 금정구
        print(
            "1. 두구동, 2. 노포동, 3. 청룡동, 4. 남산동, 5. 선동, 6. 오륜동, 7. 구서동, 8. 장전동, 9. 부곡동, 10. 서동, 11. 금사동, 12. 회동동, 13. 금성동")
        ad_gjg = ['두구동', '노포동', '청룡동', '남산동', '선동', '오륜동', '구서동', '장전동', '부곡동', '서동', '금사동', '회동동', '금성동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_gjg)
        adress.append(ad_gjg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[11] in adress:  # 강서구
        print(
            "1. 대저1동, 2. 강동동, 3. 명지동, 4. 죽림동, 5. 식만동, 6. 죽동동, 7. 봉림동, 8. 송정동, 9. 화전동, 10. 녹산동, 11. 생곡동, 12.구랑동, 13. 지사동, 14. 미음동, 15. 범방동, 16. 신호동, 17. 동선동, 18. 성북동, 19. 눌차동, 20. 천성동, 21. 대항동")
        ad_gsg = ['대저1동', '강동동', '명지동', '죽림동', '식만동', '죽동동', '봉림동', '송정동', '화전동', '녹산동', '생곡동', '구랑동', '지사동', '미음동',
                '범방동', '신호동', '동선동', '성북동', '눌차동', '천성동', '대항동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_gsg)
        adress.append(ad_gsg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[12] in adress:  # 연제구
        print("1. 거제동, 2. 연산동")
        ad_yjg = ['거제동', '연산동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_yjg)
        adress.append(ad_yjg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[13] in adress:  # 수영구
        print("1. 망미동, 2. 수영동, 3. 민락동, 4. 광안동, 5. 남천동")
        ad_syg = ['망미동', '수영동', '민락동', '광안동', '남천동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_syg)
        adress.append(ad_syg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[14] in adress:  # 사상구
        print("1. 삼락동, 2. 모라동, 3. 덕포동, 4. 괘법동, 5. 감전동, 6. 주례동, 7. 학장동, 8. 엄궁동")
        ad_ssg = ['삼락동', '모라동', '덕포동', '괘법동', '감전동', '주례동', '학장동', '엄궁동']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_ssg)
        adress.append(ad_ssg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

    elif ad[15] in adress:  # 기장구
        print("1. 기장읍, 2. 장안읍, 3. 정관읍, 4. 일광면, 5. 철마면")
        ad_kjg = ['기장읍', '장안읍', '정관읍', '일광면', '철마면']
        print("주소를 선택해 주세요")
        ad_num = num_input

        numsize = len(ad_kjg)
        adress.append(ad_kjg[ad_num - 1])
        ad_num = 0
        num_input = 0
        print(adress)

#         # 나가고

#     # step 8
while True:
    if keyboard.read_key() == Button_start:
        print("상세주소를 입력해 주세요")
                   
                        # 버튼이 눌릴 때 실행할 것들
        if keyboard.read_key() ==Button_conso:
                input_mode = 1
                count_updown = 0
                #자음이라는 말 출력
                print('input_mode : ', input_mode)
                pass
        else:
                pass
        
        
        if keyboard.read_key() ==Button_vowel:
                input_mode = 2
                count_updown = 0
                #모음이라는 말 출력
                
                print('input_mode : ', input_mode)
                pass
        else:
                pass
        
        
        if keyboard.read_key() ==Button_num:
                input_mode = 3
                count_updown = 0
                #숫자라는 말 출력        
                
                print('input_mode : ', input_mode)
                pass
        else:
                pass

        
                        
        if keyboard.read_key() == Button_input:
                
                print('Button_input is pushed')
                
                #count_updown 숫자에 따라 자음 설정
                if input_mode == 1 :
                        

                        sung = switch_button_input.push_Button_input_conso(count_updown) 
                        
                        sung_index_1.append(sung)                                          #설정된 자음 sung_index에 추가
                        sung_index_2.append(sung)
                        sung_index_3.append(sung)
                        sung_index_4.append(sung)
                        sung_index_5.append(sung)
                        
                        jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                        jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                        jamo_join_final_3 = switch_jamo_assemble.jamo_assemble(sung_index_3)
                        jamo_join_final_4 = switch_jamo_assemble.jamo_assemble(sung_index_4)
                        jamo_join_final_5 = switch_jamo_assemble.jamo_assemble(sung_index_5)
                        
                        print('jamo_join_final_1,jamo_join_final_2',jamo_join_final_1,jamo_join_final_2)                                         
                                                        
                        #jamo-join_final 읽어주기       
                                
                
                elif input_mode == 2 :
                        
                        sung = switch_button_input.push_Button_input_vowel(count_updown)
                        
                        sung_index_1.append(sung)
                        sung_index_2.append(sung)
                        sung_index_3.append(sung)
                        sung_index_4.append(sung)
                        sung_index_5.append(sung)
                        
                        jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                        jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                        jamo_join_final_3 = switch_jamo_assemble.jamo_assemble(sung_index_3)
                        jamo_join_final_4 = switch_jamo_assemble.jamo_assemble(sung_index_4)
                        jamo_join_final_5 = switch_jamo_assemble.jamo_assemble(sung_index_5)
                        
                        print('jamo_join_final_1,jamo_join_final_2',jamo_join_final_1,jamo_join_final_2)
                        
                        #jamo-join_final 읽어주기
                        
                        
                else  :                                                 #숫자 input
                        num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                        #num_input 읽어주기
                        # return num_input
                
        
                if len(sung_index_1) == 4:    
                        if sung_index_1[3] in jungsung:
                                
                                sung_index_1 = sung_index_1[:2]
                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                jamo_join_input_index = jamo_join_input_index[:-1]
                                jamo_join_input_index.append(jamo_join_final_1)
                                
                                
                                sung_index_1 = sung_index_2[2:]
                                sung_index_2 = sung_index_2[2:]
                                sung_index_3 = sung_index_2[2:]
                                sung_index_4 = sung_index_2[2:]
                                jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                jamo_join_input_index.append(jamo_join_final_2)
                                
                        
                                                
                                
                        else:
                                jamo_join_input_index = jamo_join_input_index[:-1]
                                jamo_join_input_index.append(jamo_join_final_1)
                                
                elif len(sung_index_1) == 5:               
                        if sung_index_1[4] in jungsung:
                                
                                sung_index_2 = sung_index_2[:3]
                                jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                print('jjjjamo_join_final_2',jamo_join_final_2)
                                jamo_join_input_index = jamo_join_input_index[:-1]
                                jamo_join_input_index.append(jamo_join_final_2)
                                sung_index_1 = sung_index_3[3:]
                                sung_index_2 = sung_index_3[3:]
                                sung_index_3 = sung_index_3[3:]
                                sung_index_4 = sung_index_3[3:]
                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                jamo_join_input_index.append(jamo_join_final_1)
                        
                        elif sung_index_1[4] in chosung:
                                
                                sung_index_1 = sung_index_1[:4]
                                jamo_join_final_4 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                print('jjjjamo_join_final_4',jamo_join_final_4)
                                jamo_join_input_index = jamo_join_input_index[:-1]
                                jamo_join_input_index.append(jamo_join_final_4)
                                sung_index_1 = sung_index_3[4:]
                                sung_index_2 = sung_index_3[4:]
                                sung_index_3 = sung_index_3[4:]
                                sung_index_4 = sung_index_3[4:]
                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                jamo_join_input_index.append(jamo_join_final_1)
                                
                        
                        else:
                                jamo_join_input_index = jamo_join_input_index[:-1]
                                jamo_join_input_index.append(jamo_join_final_1)
                
                elif  len(sung_index_2)==6:      
                        if sung_index_2[5] in jungsung:
                                
                                sung_index_3 = sung_index_3[:3]
                                jamo_join_final_3 = switch_jamo_assemble.jamo_assemble(sung_index_3)
                                print('jamo_join_final_3:',jamo_join_final_3)
                                jamo_join_input_index = jamo_join_input_index[:-1]
                                jamo_join_input_index.append(jamo_join_final_1)
                                sung_index_1 = sung_index_2[4:]
                                sung_index_2 = sung_index_2[4:]
                                sung_index_3 = sung_index_2[4:]
                                sung_index_4 = sung_index_2[4:]
                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                jamo_join_input_index.append(jamo_join_final_1)
                        else :
                                jamo_join_input_index = jamo_join_input_index[:-1]
                                jamo_join_input_index.append(jamo_join_final_1)
                        
                                
                else : 
                        if len(sung_index_1) == 1:
                                jamo_join_input_index.append(jamo_join_final_1)
                        else:
                                jamo_join_input_index = jamo_join_input_index[:-1]
                                jamo_join_input_index.append(jamo_join_final_1)
                
                
                        
                
                print('jamo_join_input_index : ', jamo_join_input_index)
                jamo_join_input = ''

                                        
                print('sung_index_1,sung_index_2,sung_index_3,sung_index_4',sung_index_1,sung_index_2,sung_index_3,sung_index_4)
                count_updown = 0
                print('jamo_join_input 3 : ',jamo_join_input)
                print('num_input:',num_input)
                print('count_updown: ',count_updown)
                print('jamo_join_input_index:',jamo_join_input_index)
                sleep(0.5)
                pass
        else:
                pass
        


        
        
        
        #button_up&down부분
        
        if keyboard.read_key() ==Button_up:
                count_updown = count_updown + 1
                
                if input_mode == 1:
                        count_updown = count_updown % 19 
                        sung = switch_button_input.push_Button_input_conso(count_updown)
                        print('sung:',sung)
                        #sung 읽어주기
                        
                        pass
                
                        
                elif input_mode == 2:
                        count_updown = count_updown % 21
                        sung = switch_button_input.push_Button_input_vowel(count_updown)
                        print('sung:',sung)
                        #sung 읽어주기
                        pass
                        
                        
                else :
                        count_updown = count_updown % num_size                                                          #num_size가 최대값
                        print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                        #count_updown 읽어주기
                        pass
                
                
        
        else:
                pass
        
                        
                        
        if keyboard.read_key() ==Button_down:                                                 
                count_updown = count_updown - 1

                if input_mode == 1:
                        count_updown = count_updown % 19 
                        sung = switch_button_input.push_Button_input_conso(count_updown)
                        print('sung:',sung)
                        #sung 읽어주기
                        pass
                
                        
                elif input_mode == 2:
                        count_updown = count_updown % 21
                        sung = switch_button_input.push_Button_input_vowel(count_updown)
                        print('sung:',sung)
                        #sung 읽어주기
                        pass
                        
                        
                else :
                        count_updown = count_updown % num_size  
                        print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                        #count_updown 읽어주기
                        pass
        else:
                pass
        
        
        
        
        #수정버튼 부분
        if keyboard.read_key() ==Button_revise:
                
                if jamo_join_input_index != []:
                        jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                        
                        print(jamo_join_input)
                        pass
                        
                        
                elif  num_input != 0:
                        num_input = switch_button_revise.push_Button_revise_num(num_input)
                        print(num_input)
                        pass
                else :
                        pass
        else:
                pass
        
        
        #다음버튼
        if keyboard.read_key() ==Button_next:
                
                #step 올리기
                
                if jamo_join_input != '' or jamo_join_input_index != []:
                        jamo_join_input_save = jamo_join_input
                        
                        jamo_join_input_index_save = jamo_join_input_index
                        jamo_join_input_index_save_index = jamo_join_input_index
                        jamo_join_input_index_save = ''.join(jamo_join_input_index)
                        
                        jamo_join_input = ''
                        jamo_join_input_index = []
                        
                        count_updown = 0

                else :
                        num_input_save = num_input

                        num_input = 0
                        
                        count_updown = 0
                        
                print('jamo_join_input 5 : ',jamo_join_input)
                print('jamo_join_input_index : ',jamo_join_input_index)
                print('jamo_join_input_save',jamo_join_input_save)
                print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                
                print('num_input : ',num_input)
                print('num_input_save : ', num_input_save)
        
        # return num_input        
                
        
                
        #뒤로버튼                
        if keyboard.read_key() == Button_back:
                #step 내리기!!
                
                if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                        jamo_join_input_index = jamo_join_input_index_save_index
                        print(''.join(jamo_join_input_index_save))
                        #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                        
                        count_updown = 0

                else :
                        print(num_input_save)
                        #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                        num_input = num_input_save
                        
                        
                        count_updown = 0
        
                print('jamo_join_input 5 : ',jamo_join_input)
                print('jamo_join_input_index : ',jamo_join_input_index)
                print('jamo_join_input_save',jamo_join_input_save)
                print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                
                print('num_input : ',num_input)
                print('num_input_save : ', num_input_save)
        
        
                        
        sleep(0.1)

        if keyboard.read_key() == Button_start:
                break
    
        adress.append(jamo_join_input_index)
        
        print(adress)
        # ad_num=num_input 주소받기

        wr.writerow([3, '주소', adress[0]])

#     # step 9
while True:
    if keyboard.read_key() == Button_start:
        print("검사경위(이유)가 무었인가요?")
        print("1. 자가격리, 2. 유증상자, 3. 보건소 재난문자 연락, 4. 해외입국자, 5. 집단발생지 방문자, 6. 확진자접촉, 7. 본인판단")
        why = ['자가격리', '유증상자', '보건소 재난문자 연락', '해외입국자', '집단발생지 방문자', '확진자접촉', '본인판단']
        numsize = len(why)
        
        if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
        else:
                    pass

            
                            
        if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
        else:
                    pass
            
            
            #button_up&down부분
            
        if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
        else:
                    pass
            
                            
                            
        if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
        else:
                    pass
            
            
            
            
            #수정버튼 부분
        if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
        else:
                    pass
            
            
            #다음버튼
        if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
        if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
        if keyboard.read_key() == Button_start:
    
                    break
        
        why_num = num_input
        whys.append(why[why_num - 1])
        # num_input = 0 여기서는 초기화 하면 x
        wr.writerow([4, '검사경위', whys[0]])

 
while True:
    if keyboard.read_key() == Button_start:
        print("개인정보 수집에 동의하십니까?")
        print("1.예, 2.아니오")
        agree = ['예', '아니오']
        umsize = len(agree)
        
        if keyboard.read_key() ==Button_num:
                    input_mode = 3
                    count_updown = 0
                    #숫자라는 말 출력        
                    
                    print('input_mode : ', input_mode)
                    pass
    else:
                    pass

            
                            
    if keyboard.read_key() == Button_input:
                    
                    print('Button_input is pushed')
                    if input_mode ==3  :                                                 #숫자 input
                            num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                            #num_input 읽어주기
                            
                    sleep(0.5)
                    pass
        else:
                    pass
            
            
            #button_up&down부분
            
        if keyboard.read_key() ==Button_up:
                    count_updown = count_updown + 1
                    
                    if input_mode == 3:
                            count_updown = count_updown % num_size                                                          #num_size가 최대값
                            print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                            
                            pass
                    else:
                        pass
        else:
                    pass
            
                            
                            
        if keyboard.read_key() ==Button_down:                                                 
                    count_updown = count_updown - 1
                                
                    if input_mode == 3:
                            count_updown = count_updown % num_size  
                            print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                            #count_updown 읽어주기
                            pass
        else:
                    pass
            
            
            
            
            #수정버튼 부분
        if keyboard.read_key() ==Button_revise:
                    
                    if jamo_join_input_index != []:
                            jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                            
                            print(jamo_join_input)
                            pass
                            
                            
                    elif  num_input != 0:
                            num_input = switch_button_revise.push_Button_revise_num(num_input)
                            print(num_input)
                            pass
                    else :
                            pass
        else:
                    pass
            
            
            #다음버튼
        if keyboard.read_key() ==Button_next:
                    
                    #step 올리기
                    
                    if jamo_join_input != '' or jamo_join_input_index != []:
                            jamo_join_input_save = jamo_join_input
                            
                            jamo_join_input_index_save = jamo_join_input_index
                            jamo_join_input_index_save_index = jamo_join_input_index
                            jamo_join_input_index_save = ''.join(jamo_join_input_index)
                            
                            jamo_join_input = ''
                            jamo_join_input_index = []
                            
                            count_updown = 0

                    else :
                            num_input_save = num_input
    
                            num_input = 0
                            
                            count_updown = 0
                            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
            
                    
                    
            
                    
                            
        if keyboard.read_key() == Button_back:
                    #step 내리기!!
                    
                    if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                            jamo_join_input_index = jamo_join_input_index_save_index
                            print(''.join(jamo_join_input_index_save))
                            #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                            
                            count_updown = 0

                    else :
                            print(num_input_save)
                            #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
                            num_input = num_input_save
                            
                            
                            count_updown = 0
            
                    print('jamo_join_input 5 : ',jamo_join_input)
                    print('jamo_join_input_index : ',jamo_join_input_index)
                    print('jamo_join_input_save',jamo_join_input_save)
                    print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                    
                    print('num_input : ',num_input)
                    print('num_input_save : ', num_input_save)
                    
                    agree_num = num_input
                    agrees.append(agree[agree_num - 1])
                    wr.writerow([5, '개인정보 수집 동의여부', agrees[0]])
                    print(agrees)
                    
    if keyboard.read_key() == Button_start:
            break
        
        

        

            f.close()