first = 0
import csv

print("처음 방문이신 가요?")
first = int(input("1.예 2. 아니오"))    

if first == 1: #처음방문이다
    name = input("이름을 입력해주세요 : ")
    birth = input("생년월일을 입력해주세요: ")
    print("1. 남, 2. 여")
    sex = int(input("성별을 선택하여 주세요"))
    if sex == 1:
        sex = "남"
    else :
        sex = "여"   

    file_name = name+(birth)+sex
    f = open(file_name,'w', encoding='utf-8')
    wr = csv.writer(f)

    wr.writerow([1,'이름 생년월일 성별',name+birth+sex])

    p_num = input("전화번호를 입력해주세요: ")
    wr.writerow([2,'전화번호',p_num])

    adress = input("주소를 찾아주세요") # 주소찾기 만들기 #이까지는 계속 유지되는 정보
    wr.writerow([3,'주소',adress]) #주소찾기 만드는중 (엑셀로 만들예정)
    
    wr.writerow([4,'1차 문진표'])

    #body_temp = input("현재 체온을 작성해 주세요") #여기서부터는 새로 받을 것
    #wr.writerow([5,'체온',body_temp])

    print("검사경위(이유)가 무었인가요?")
    why = 0
    while why == 0:
        why = int(input("1. 자가격리, 2. 자가격리 해제전, 3. 유증상자, 4. 보건소 재난문자 연락, 5. 해외입국자, 6. 해외입국자접촉자, 7. 집단발생지 방문자, 8. 확진자접촉, 9. 선제검사, 10. 본인판단"))
    
        if why == 1:
            why = "자가격리"
            wr.writerow([6,'자가격리',why])
            print (why)
            break
        
        elif why ==2:
            why ="아니오"
            wr.writerow([6,'자가격리 해제전',why])
            print (why)
            break

        elif why ==3:
            why ="유증상자"
            wr.writerow([6,'유증상자',why])
            print (why)
            
            symptom = 0
            print("1. 고열(37.5이상), 2. 기침, 3. 가래, 4. 호흡곤란, 5. 두통, 6. 근육통, 7. 오한, 8. 인후통, 9. 후각상실, 10. 미각상실 11.없음") #기타를 만들지 고민중
            symptoms = []
            while symptom==0:
    
                symptom = int(input("증상을 선택하여주세요(복수선택가능)"))

                if symptom == 1:
                    symptom = "고열(37.5이상)"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 2:
                    symptom = "기침"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 3:
                    symptom = "가래"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 4:
                    symptom = "호흡곤란"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 5:
                    symptom = "두통"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 6:
                    symptom = "근육통"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 7:
                    symptom = "오한"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 8:
                    symptom = "인후통"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 9:
                    symptom = "후각상실"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 10:
                    symptom = "미각상실"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 11:
                    break
                else :
                    print("잘못입력하셨습니다")
                symptom=0
                
                print(symptoms)   

                wr.writerow([6-3,'증상',symptoms])    
            
            break
        
        
        elif why ==4:
            why ="보건소 재난문자 연락"
            wr.writerow([6,'보건소 재난문자 연락',why])
            print (why)
            break
        
        elif why ==5:
            why ="해외입국자"
            wr.writerow([6,'해외입국자',why]) #해외어딘지
            print (why)
            break
        
        elif why ==6:
            why ="해외입국자 접촉자"
            wr.writerow([6,'해외입국자 접촉자',why]) #해외어딘지
            print (why)
            break
        
        elif why ==7:
            why ="집단발생지" #어딘지?
            wr.writerow([6,'집단발생지',why])
            print (why)
            break
        
        elif why ==8:
            why ="확진자접촉"
            wr.writerow([6,'확진자접촉',why])
            print (why)
            break
        
        elif why ==9:
            why ="선제검사"
            wr.writerow([6,'선제검사',why])
            print (why)
            break
        
        elif why ==10:
            why ="본인판단"
            wr.writerow([6,'본인판단',why])
            print (why)
            break
        
        else :
            print("잘못 입력하셨습니다.")
            why = 0

    print("개인정보 수집에 동의하십니까?")
    agree = int(input("1. 예, 2. 아니오"))
    if agree == 1:
        agree = "예"
        wr.writerow([7,'개인정보 수집 동의여부',agree])

    elif agree ==2:
        agree ="아니오"
        wr.writerow([7,'개인정보 수집 동의여부',agree])

    f.close()

else : #방문경험이 있다

    name = input("이름을 입력해주세요 : ")
    birth = input("생년월일을 입력해주세요: ")
    print("1. 남, 2. 여")
    sex = int(input("성별을 선택하여 주세요"))
    if sex == 1:
        sex = "남"
    else :
        sex = "여"  

    file_name = name+(birth)+sex
    #f = open(file_name,'r', encoding='utf-8')
    f = open(file_name,'a', encoding='utf-8')
    #lines = csv.reader(f)
    wr = csv.writer(f)

    n=int(input("몇번째 방문이십니까?"))

    wr.writerow([4,n+'차 문진표'])#새로받을부분

    #body_temp = input("현재 체온을 작성해 주세요")
    #wr.writerow([5,'체온',body_temp])

    
    print("검사경위(이유)가 무었인가요?")
    why = 0
    while why == 0:
        why = int(input("1. 자가격리, 2. 자가격리 해제전, 3. 유증상자, 4. 보건소 재난문자 연락, 5. 해외입국자, 6. 해외입국자접촉자, 7. 집단발생지 방문자, 8. 확진자접촉, 9. 선제검사, 10. 본인판단"))
    
        if why == 1:
            why = "자가격리"
            wr.writerow([6,'자가격리',why])
            print (why)
            break
        
        elif why ==2:
            why ="아니오"
            wr.writerow([6,'자가격리 해제전',why])
            print (why)
            break

        elif why ==3:
            why ="유증상자"
            wr.writerow([6,'유증상자',why])
            print (why)
            
            symptom = 0
            print("1. 고열(37.5이상), 2. 기침, 3. 가래, 4. 호흡곤란, 5. 두통, 6. 근육통, 7. 오한, 8. 인후통, 9. 후각상실, 10. 미각상실 11.없음") #기타를 만들지 고민중
            symptoms = []
            while symptom==0:
    
                symptom = int(input("증상을 선택하여주세요(복수선택가능)"))

                if symptom == 1:
                    symptom = "고열(37.5이상)"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 2:
                    symptom = "기침"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 3:
                    symptom = "가래"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 4:
                    symptom = "호흡곤란"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 5:
                    symptom = "두통"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 6:
                    symptom = "근육통"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 7:
                    symptom = "오한"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 8:
                    symptom = "인후통"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 9:
                    symptom = "후각상실"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 10:
                    symptom = "미각상실"
                    symptoms.append(symptom)
                    symptom=0
                elif symptom == 11:
                    break
                else :
                    print("잘못입력하셨습니다")
                symptom=0
                
                print(symptoms)   

                wr.writerow([6-3,'증상',symptoms])    
            
            break
        
        
        elif why ==4:
            why ="보건소 재난문자 연락"
            wr.writerow([6,'보건소 재난문자 연락',why])
            print (why)
            break
        
        elif why ==5:
            why ="해외입국자"
            wr.writerow([6,'해외입국자',why]) #해외어딘지
            print (why)
            break
        
        elif why ==6:
            why ="해외입국자 접촉자"
            wr.writerow([6,'해외입국자 접촉자',why]) #해외어딘지
            print (why)
            break
        
        elif why ==7:
            why ="집단발생지" #어딘지?
            wr.writerow([6,'집단발생지',why])
            print (why)
            break
        
        elif why ==8:
            why ="확진자접촉"
            wr.writerow([6,'확진자접촉',why])
            print (why)
            break
        
        elif why ==9:
            why ="선제검사"
            wr.writerow([6,'선제검사',why])
            print (why)
            break
        
        elif why ==10:
            why ="본인판단"
            wr.writerow([6,'본인판단',why])
            print (why)
            break
        
        else :
            print("잘못 입력하셨습니다.")
            why = 0

    print("개인정보 수집에 동의하십니까?")
    agree = int(input("1. 예, 2. 아니오"))
    if agree == 1:
        agree = "예"
        wr.writerow([7,'개인정보 수집 동의여부',agree])

    elif agree ==2:
        agree ="아니오"
        wr.writerow([7,'개인정보 수집 동의여부',agree])

    f.close()