adress = 0 
print("1. 중구, 2. 서구, 3. 동구, 4. 영도구, 5. 부산진구, 6. 동래구, 7. 남구, 8. 북구, 9. 해운대구, 10. 사하구, 11. 금정구, 12. 강서구, 13. 연제구, 14.수영구, 15. 사상구, 16. 기장구") #기타를 만들지 고민중
adresses = []
    #while adress==0:
    
adress = int(input("주소를 선택해 주세요"))

if adress == 1:
        adress = "중구"
        adresses.append(adress)
            
        adress=0
        print("1. 영주동, 2. 대창동, 3. 중앙동, 4. 동광동, 5. 대청동, 6. 보수동, 7. 부평동, 8. 신창동, 9. 창선동, 10. 광복동, 11. 남포동", 12."되돌아가기")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "영주동"
            adresses.append(adress)
        elif adress = 2:
        adress = "대창동"
        adresses.append(adress)
            elif adress = 3:
                adress = "중앙동"
                adresses.append(adress)
            elif adress = 4:
                adress = "동광동"
                adresses.append(adress)
            elif adress = 5:
                adress = "대청동"
                adresses.append(adress)
            elif adress = 6:
                adress = "보수동"
                adresses.append(adress)
            elif adress = 7:
                adress = "부평동"
                adresses.append(adress)
            elif adress = 8:
                adress = "신창동"
                adresses.append(adress)
            elif adress = 9:
                adress = "창선동"
                adresses.append(adress)
            elif adress = 10:
                adress = "광복동"
                adresses.append(adress)
            elif adress = 11:
                adress = "남포동"
                adresses.append(adress)
            elif adress = 12:
                return adress = 0
                
           
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