adress = 0 
print("1. 중구, 2. 서구, 3. 동구, 4. 영도구, 5. 부산진구, 6. 동래구, 7. 남구, 8. 북구, 9. 해운대구, 10. 사하구, 11. 금정구, 12. 강서구, 13. 연제구, 14.수영구, 15. 사상구, 16. 기장구") #기타를 만들지 고민중
adresses = []
    #while adress==0:
    
adress = int(input("주소를 선택해 주세요"))

if adress == 1:
        adress = "중구"
        adresses.append(adress)
            
        adress=0
        print("1. 영주동, 2. 대창동, 3. 중앙동, 4. 동광동, 5. 대청동, 6. 보수동, 7. 부평동, 8. 신창동, 9. 창선동, 10. 광복동, 11. 남포동") #12."되돌아가기"
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "영주동"
            adresses.append(adress)
        elif adress == 2:
            adress = "대창동"
            adresses.append(adress)
        elif adress == 3:
            adress = "중앙동"
            adresses.append(adress)
        elif adress == 4:
            adress = "동광동"
            adresses.append(adress)
        elif adress == 5:
            adress = "대청동"
            adresses.append(adress)
        elif adress == 6:
            adress = "보수동"
            adresses.append(adress)
        elif adress == 7:
            adress = "부평동"
            adresses.append(adress)
        elif adress == 8:
            adress = "신창동"
            adresses.append(adress)
        elif adress == 9:
            adress = "창선동"
            adresses.append(adress)
        elif adress == 10:
            adress = "광복동"
            adresses.append(adress)
        elif adress == 11:
            adress = "남포동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
            
elif adress == 2:
        adress = "서구"
        adresses.append(adress)
            
        adress=0
        print("1. 동대신동, 2. 서대신동, 3. 부용동, 4. 부민동, 5. 토성동, 6. 아미동, 7. 조장동, 8. 충무동, 9. 남부민동, 10. 암남동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "동대신동"
            adresses.append(adress)
        elif adress == 2:
            adress = "서대신동"
            adresses.append(adress)
        elif adress == 3:
            adress = "부용동"
            adresses.append(adress)
        elif adress == 4:
            adress = "부민동"
            adresses.append(adress)
        elif adress == 5:
            adress = "토성동"
            adresses.append(adress)
        elif adress == 6:
            adress = "아미동"
            adresses.append(adress)
        elif adress == 7:
            adress = "조장동"
            adresses.append(adress)
        elif adress == 8:
            adress = "충무동"
            adresses.append(adress)
        elif adress == 9:
            adress = "남부민동"
            adresses.append(adress)
        elif adress == 10:
            adress = "암남동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
            
elif adress == 3:
        adress = "동구"
        adresses.append(adress)
            
        adress=0
        print("1. 초량동, 2. 수정동, 3. 좌천동, 4. 범일동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "초량동"
            adresses.append(adress)
        elif adress == 2:
            adress = "수정동"
            adresses.append(adress)
        elif adress == 3:
            adress = "좌천동"
            adresses.append(adress)
        elif adress == 4:
            adress = "범일동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
            
elif adress == 4:
        adress = "영도구"
        adresses.append(adress)
            
        adress=0
        print("1. 대교동, 2. 대평동, 3. 남항동, 4. 영선동, 5. 신성동, 6. 봉래동, 7. 청학동, 8. 동삼동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "대교동"
            adresses.append(adress)
        elif adress == 2:
            adress = "대평동"
            adresses.append(adress)
        elif adress == 3:
            adress = "남항동"
            adresses.append(adress)
        elif adress == 4:
            adress = "영선동"
            adresses.append(adress)
        elif adress == 5:
            adress = "신성동"
            adresses.append(adress)
        elif adress == 6:
            adress = "봉래동"
            adresses.append(adress)
        elif adress == 7:
            adress = "청학동"
            adresses.append(adress)
        elif adress == 8:
            adress = "동삼동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==5:
        adress = "부산진구"
        adresses.append(adress)
            
        adress=0
        print("1. 양정동, 2. 전포동, 3. 부전동, 4. 범천동, 5. 범전동, 6. 연지동, 7. 초읍동, 8.부암동, 9. 당감동, 10. 가야동, 11. 개금동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "양정동"
            adresses.append(adress)
        elif adress == 2:
            adress = "전포동"
            adresses.append(adress)
        elif adress == 3:
            adress = "부전동"
            adresses.append(adress)
        elif adress == 4:
            adress = "범천동"
            adresses.append(adress)
        elif adress == 5:
            adress = "범전동"
            adresses.append(adress)
        elif adress == 6:
            adress = "연지동"
            adresses.append(adress)
        elif adress == 7:
            adress = "초읍동"
            adresses.append(adress)
        elif adress == 8:
            adress = "부암동"
            adresses.append(adress)
        elif adress == 9:
            adress = "당감동"
            adresses.append(adress)
        elif adress == 10:
            adress = "가야동"
            adresses.append(adress)
        elif adress == 11:
            adress = "개금동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==6:
        adress = "동래구"
        adresses.append(adress)
            
        adress=0
        print("1. 명장동, 2. 안락동, 3. 칠산동, 4. 낙민동, 5. 복천동, 6. 수안동, 7. 명륜동, 8. 온천동, 9. 사직동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "명장동"
            adresses.append(adress)
        elif adress == 2:
            adress = "안락동"
            adresses.append(adress)
        elif adress == 3:
            adress = "칠산동"
            adresses.append(adress)
        elif adress == 4:
            adress = "낙민동"
            adresses.append(adress)
        elif adress == 5:
            adress = "복천동"
            adresses.append(adress)
        elif adress == 6:
            adress = "수안동"
            adresses.append(adress)
        elif adress == 7:
            adress = "명륜동"
            adresses.append(adress)
        elif adress == 8:
            adress = "온천동"
            adresses.append(adress)
        elif adress == 9:
            adress = "사직동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==7:
        adress = "남구"
        adresses.append(adress)
            
        adress=0
        print("1. 대연동, 2. 용호동, 3. 용당동, 4. 문현동, 5. 우암동, 6. 감만동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "대연동"
            adresses.append(adress)
        elif adress == 2:
            adress = "용호동"
            adresses.append(adress)
        elif adress == 3:
            adress = "용당동"
            adresses.append(adress)
        elif adress == 4:
            adress = "문현동"
            adresses.append(adress)
        elif adress == 5:
            adress = "우암동"
            adresses.append(adress)
        elif adress == 6:
            adress = "감만동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==8:
        adress = "북구"
        adresses.append(adress)
            
        adress=0
        print("1. 금곡동, 2. 화명동, 3. 만덕동, 4. 덕천동, 5. 구포동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "금곡동"
            adresses.append(adress)
        elif adress == 2:
            adress = "화명동"
            adresses.append(adress)
        elif adress == 3:
            adress = "만덕동"
            adresses.append(adress)
        elif adress == 4:
            adress = "덕천동"
            adresses.append(adress)
        elif adress == 5:
            adress = "구포동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==9:
        adress = "해운대구"
        adresses.append(adress)
            
        adress=0
        print("1. 반송동, 2. 석대동, 3. 반여동, 4. 재송동, 5. 우동, 6. 중동, 7. 좌동, 8. 송정동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "반송동"
            adresses.append(adress)
        elif adress == 2:
            adress = "석대동"
            adresses.append(adress)
        elif adress == 3:
            adress = "반여동"
            adresses.append(adress)
        elif adress == 4:
            adress = "재송동"
            adresses.append(adress)
        elif adress == 5:
            adress = "우동"
            adresses.append(adress)
        elif adress == 6:
            adress = "중동"
            adresses.append(adress)
        elif adress == 7:
            adress = "좌동"
            adresses.append(adress)
        elif adress == 8:
            adress = "송정동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==10:
        adress = "사하구"
        adresses.append(adress)
            
        adress=0
        print("1. 괴정동, 2. 당리동, 3. 하단동, 4. 신평동, 5. 장림동, 6. 다대동, 7. 구평동, 8. 감천동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "괴정동"
            adresses.append(adress)
        elif adress == 2:
            adress = "당리동"
            adresses.append(adress)
        elif adress == 3:
            adress = "하단동"
            adresses.append(adress)
        elif adress == 4:
            adress = "신평동"
            adresses.append(adress)
        elif adress == 5:
            adress = "장림동"
            adresses.append(adress)
        elif adress == 6:
            adress = "다대동"
            adresses.append(adress)
        elif adress == 7:
            adress = "구평동"
            adresses.append(adress)
        elif adress == 8:
            adress = "감천동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==11:
        adress = "금정구"
        adresses.append(adress)
            
        adress=0
        print("1. 두구동, 2. 노포동, 3. 청룡동, 4. 남산동, 5. 선동, 6. 오륜동, 7. 구서동, 8. 장전동, 9. 부곡동, 10. 서동, 11. 금사동, 12. 회동동, 13. 금성동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "두구동"
            adresses.append(adress)
        elif adress == 2:
            adress = "노포동"
            adresses.append(adress)
        elif adress == 3:
            adress = "청룡동"
            adresses.append(adress)
        elif adress == 4:
            adress = "남산동"
            adresses.append(adress)
        elif adress == 5:
            adress = "선동"
            adresses.append(adress)
        elif adress == 6:
            adress = "오륜동"
            adresses.append(adress)
        elif adress == 7:
            adress = "구서동"
            adresses.append(adress)
        elif adress == 8:
            adress = "장전동"
            adresses.append(adress)
        elif adress == 9:
            adress = "부곡동"
            adresses.append(adress)
        elif adress == 10:
            adress = "서동"
            adresses.append(adress)
        elif adress == 11:
            adress = "금사동"
            adresses.append(adress)
        elif adress == 12:
            adress = "회동동"
            adresses.append(adress)
        elif adress == 13:
            adress = "금성동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==12:
        adress = "강서구"
        adresses.append(adress)
            
        adress=0
        print("1. 대저1동, 2. 강동동, 3. 명지동, 4. 죽림동, 5. 식만동, 6. 죽동동, 7. 봉림동, 8. 송정동, 9. 화전동, 10. 녹산동, 11. 생곡동, 12.구랑동, 13. 지사동, 14. 미음동, 15. 범방동, 16. 신호동, 17. 동선동, 18. 성북동, 19. 눌차동, 20. 천성동, 21. 대항동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "대저1동"
            adresses.append(adress)
        elif adress == 2:
            adress = "강동동"
            adresses.append(adress)
        elif adress == 3:
            adress = "명지동"
            adresses.append(adress)
        elif adress == 4:
            adress = "죽림동"
            adresses.append(adress)
        elif adress == 5:
            adress = "식만동"
            adresses.append(adress)
        elif adress == 6:
            adress = "죽동동"
            adresses.append(adress)
        elif adress == 7:
            adress = "봉림동"
            adresses.append(adress)
        elif adress == 8:
            adress = "송정동"
            adresses.append(adress)
        elif adress == 9:
            adress = "화전동"
            adresses.append(adress)
        elif adress == 10:
            adress = "녹산동"
            adresses.append(adress)
        elif adress == 11:
            adress = "생곡동"
            adresses.append(adress)
        elif adress == 12:
            adress = "구랑동"
            adresses.append(adress)
        elif adress == 13:
            adress = "지사동"
            adresses.append(adress)
        elif adress == 14:
            adress = "미음동"
            adresses.append(adress)
        elif adress == 15:
            adress = "범방동"
            adresses.append(adress)
        elif adress == 16:
            adress = "신호동"
            adresses.append(adress)
        elif adress == 17:
            adress = "동선동"
            adresses.append(adress)
        elif adress == 18:
            adress = "성북동"
            adresses.append(adress)
        elif adress == 19:
            adress = "눌차동"
            adresses.append(adress)
        elif adress == 20:
            adress = "천성동"
            adresses.append(adress)
        elif adress == 21:
            adress = "대항동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==13:
        adress = "연제구"
        adresses.append(adress)
            
        adress=0
        print("1. 거제동, 2. 연산동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "거제동"
            adresses.append(adress)
        elif adress == 2:
            adress = "연산동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==14:
        adress = "수영구"
        adresses.append(adress)
            
        adress=0
        print("1. 망미동, 2. 수영동, 3. 민락동, 4. 광안동, 5. 남천동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "망미동"
            adresses.append(adress)
        elif adress == 2:
            adress = "수영동"
            adresses.append(adress)
        elif adress == 3:
            adress = "민락동"
            adresses.append(adress)
        elif adress == 4:
            adress = "광안동"
            adresses.append(adress)
        elif adress == 5:
            adress = "남천동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==15:
        adress = "사상구"
        adresses.append(adress)
            
        adress=0
        print("1. 삼락동, 2. 모라동, 3. 덕포동, 4. 괘법동, 5. 감전동, 6. 주례동, 7. 학장동, 8. 엄궁동")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "삼락동"
            adresses.append(adress)
        elif adress == 2:
            adress = "모라동"
            adresses.append(adress)
        elif adress == 3:
            adress = "덕포동"
            adresses.append(adress)
        elif adress == 4:
            adress = "괘법동"
            adresses.append(adress)
        elif adress == 5:
            adress = "감전동"
            adresses.append(adress)
        elif adress == 6:
            adress = "주례동"
            adresses.append(adress)
        elif adress == 7:
            adress = "학장동"
            adresses.append(adress)
        elif adress == 8:
            adress = "엄궁동"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0
elif adress ==16:
        adress = "기장군"
        adresses.append(adress)
            
        adress=0
        print("1. 기장읍, 2. 장안읍, 3. 정관읍, 4. 일광면, 5. 철마면")
        adress = int(input("주소를 선택해 주세요"))
            
        if adress == 1:
            adress = "기장읍"
            adresses.append(adress)
        elif adress == 2:
            adress = "장안읍"
            adresses.append(adress)
        elif adress == 3:
            adress = "정관읍"
            adresses.append(adress)
        elif adress == 4:
            adress = "일광면"
            adresses.append(adress)
        elif adress == 5:
            adress = "철마면"
            adresses.append(adress)
        else :
            print("잘못입력하셨습니다")
            adress=0