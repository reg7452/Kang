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

    #adress = input("주소를 찾아주세요") # 주소찾기 만들기 #이까지는 계속 유지되는 정보
    #wr.writerow([3,'주소',adress])
    
    #adress = 0 
    print("1. 중구, 2. 서구, 3. 동구, 4. 영도구, 5. 부산진구, 6. 동래구, 7. 남구, 8. 북구, 9. 해운대구, 10. 사하구, 11. 금정구, 12. 강서구, 13. 연제구, 14.수영구, 15. 사상구, 16. 기장구") #기타를 만들지 고민중
    adresses = []
    #while adress==0:
    
    adress = int(input("주소를 선택해 주세요"))

    if adress == 1:
            adress = "중구"
            adresses.append(adress)
            adress=0
            print("1. 영주동, 2. 대창동, 3. 중앙동, 4. 동광동, 5. 대청동, 6. 보수동, 7. 부평동, 8. 신창동, 9. 창선동, 10. 광복동, 11. 남포동")
            adresses.append(adress)
            
            if adress = 
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
            adress=0
    print(adress)   
    
    wr.writerow([4,'1차 문진표'])

    body_temp = input("현재 체온을 작성해 주세요") #여기서부터는 새로 받을 것
    wr.writerow([5,'체온',body_temp])

    
    print("14일 이내에 해외여행 방문경험이 있나요?")
    overseas = int(input("1. 예, 2. 아니오"))
    if overseas == 1:
        overseas = "예"
        wr.writerow([6,'해외방문경험',overseas])

    elif overseas ==2:
        overseas ="아니오"
        wr.writerow([6,'해외방문경험',overseas])

    print("확진자와 접촉이 있었나요?")
    contact = int(input("1. 예, 2. 아니오"))
    if contact == 1:
        contact = "예"
        wr.writerow([7,'확진자 접촉 유무',contact])

    elif contact ==2:
        contact ="아니오"
        wr.writerow([7,'확진자 접촉 유무',contact])

    print("확진자발생 장소에 방문한 적이 있나요?")
    contact_place = int(input("1. 예, 2. 아니오"))
    if contact_place == 1:
        contact_place = "예"
        wr.writerow([8,'동선겹침 유무',contact_place])

    elif contact_place ==2:
        contact_place ="아니오"
        wr.writerow([8,'동선겹침 유무',contact_place])
    
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

    wr.writerow([9,'증상',symptoms])

    print("개인정보 수집에 동의하십니까?")
    agree = int(input("1. 예, 2. 아니오"))
    if agree == 1:
        agree = "예"
        wr.writerow([10,'개인정보 수집 동의여부',agree])

    elif agree ==2:
        agree ="아니오"
        wr.writerow([10,'개인정보 수집 동의여부',agree])

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

    body_temp = input("현재 체온을 작성해 주세요")
    wr.writerow([5,'체온',body_temp])

    
    print("14일 이내에 해외여행 방문경험이 있나요?")
    overseas = int(input("1. 예, 2. 아니오"))
    if overseas == 1:
        overseas = "예"
        wr.writerow([6,'해외방문경험',overseas])

    elif overseas ==2:
        overseas ="아니오"
        wr.writerow([6,'해외방문경험',overseas])

    print("확진자와 접촉이 있었나요?")
    contact = int(input("1. 예, 2. 아니오"))
    if contact == 1:
        contact = "예"
        wr.writerow([7,'확진자 접촉 유무',contact])

    elif contact ==2:
        contact ="아니오"
        wr.writerow([7,'확진자 접촉 유무',contact])

    print("확진자발생 장소에 방문한 적이 있나요?")
    contact_place = int(input("1. 예, 2. 아니오"))
    if contact_place == 1:
        contact_place = "예"
        wr.writerow([8,'동선겹침 유무',contact_place])

    elif contact_place ==2:
        contact_place ="아니오"
        wr.writerow([8,'동선겹침 유무',contact_place])
    
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

    wr.writerow([9,'증상',symptoms])

    print("개인정보 수집에 동의하십니까?")
    agree = int(input("1. 예, 2. 아니오"))
    if agree == 1:
        agree = "예"
        wr.writerow([10,'개인정보 수집 동의여부',agree])

    elif agree ==2:
        agree ="아니오"
        wr.writerow([10,'개인정보 수집 동의여부',agree])

    f.close()