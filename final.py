import csv
import main_test
# visit = 첫방문질문 리스트
# visits = 대답받는 리스트
# visit_num = 대답받는 값
visits = []
sexs = []
births = []
p_nums = []
whys = []
agrees = []
names = []
num_input = 0


# 입력칸 나오게 하는거

# step 1
if num_input_save == 1: 
    print("처음 방문이신 가요?")
    print("1.예 2.아니오")  # 만약에 재방문이면 step4 에서 step 9로 이동
    visit = ['예', '아니오']
    numsize = len(visit)
    # 답변 숫자 입력한 후 다음 누름
    visit_num = num_input

    visits.append(visit[visit_num - 1])
    visit_num = 0
    num_input = 0
    numsuze = 0
    print(visits)

if visits[0] == '예':
    # step 2

    if num_input_save == 1:
        print("이름을 입력해 주세요")
        name = num_input #이름 입력받아야함
        # 답변 숫자 입력한 후 다음 누름
        names.append(name[name_num-1])
        num_input = 0
        print(names)

    # step 3

    if num_input_save == 1:
        print("성별을 선택해 주세요")
        print("1. 남, 2. 여")
        sex = ['남', '여']
        numsize = len(sex)
        sex_num = num_input
        # 답변 숫자 입력한 후 다음 누름
        sexs.append(sex[sex_num - 1])
        sex_num = 0
        numsize = 0
        num_input = 0
        print(sexs)

    # step 4

    if num_input_save == 1:
        print("생년월일을 입력해 주세요")
        birth = num_input
        # 답변 숫자 입력한 후 다음 누름
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

    if num_input_save == 1:
        print("전화번호를 입력해주세요")
        p_num = num_input
        # 답변 숫자 입력한 후 다음 누름
        p_nums.append(p_num)
        p_num = 0
        num_input = 0
        print(p_nums)
        wr.writerow([2, '전화번호', p_nums[0]])

    # setp 6

    if num_input_save == 1:
        print(
            "1. 중구, 2. 서구, 3. 동구, 4. 영도구, 5. 부산진구, 6. 동래구, 7. 남구, 8. 북구, 9. 해운대구, 10. 사하구, 11. 금정구, 12. 강서구, 13. 연제구, 14.수영구, 15. 사상구, 16. 기장구")

        adress = []  # 주소추가되는 리스트

        ad = ['중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구', '사상구',
              '기장구']
        ad_len = len(ad)
        # num input받고
        ad_num = num_input

        adress.append(ad[ad_num - 1])
        print(adress)
        ad_num = 0
        num_input = 0
        # ad_num 초기화

    # step 7

    if num_input_save == 1:
        if ad[0] in adress:  # 중구
            print("1. 영주동, 2. 대창동, 3. 중앙동, 4. 동광동, 5. 대청동, 6. 보수동, 7. 부평동, 8. 신창동, 9. 창선동, 10. 광복동, 11. 남포동")
            ad_jg = ['영주동', '대창동', '중앙동', '동광동', '대창동', '보수동', '부평동', '신창동', '창선동', '광복동', '남포동']
            print("주소를 선택해 주세요")
            numsize = len(ad_jg)
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
            numsize = len(ad_ydg)
            adress.append(ad_ydg[ad_num - 1])
            ad_num = 0
            num_input = 0
            print(adress)

        elif ad[4] in adress:  # 부산진구
            print("1. 양정동, 2. 전포동, 3. 부전동, 4. 범천동, 5. 범전동, 6. 연지동, 7. 초읍동, 8.부암동, 9. 당감동, 10. 가야동, 11. 개금동")
            ad_jg = ['양정동', '전포동', '부전동', '범천동', '범전동', '연지동', '초읍동', '부암동', '당감동', '가야동', '개금동']
            print("주소를 선택해 주세요")
            ad_num = num_input
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

        # 나가고

    # step 8

    if num_input_save == 1:
        print("상세주소를 입력해 주세요")
        # 주소 입력받기
        adress.append(num_input)
        print(adress)
        #ad_num=num_input 주소받기

        wr.writerow([3, '주소', adress[0]])

    # step 9

    if num_input_save == 1:
        print("검사경위(이유)가 무었인가요?")
        print("1. 자가격리, 2. 유증상자, 3. 보건소 재난문자 연락, 4. 해외입국자, 5. 집단발생지 방문자, 6. 확진자접촉, 7. 본인판단")
        why = ['자가격리', '유증상자', '보건소 재난문자 연락', '해외입국자', '집단발생지 방문자', '확진자접촉', '본인판단']
        numsize = len(why)
        why_num = num_input
        whys.append(why[why_num - 1])
        # num_input = 0 여기서는 초기화 하면 x
        wr.writerow([4, '검사경위', whys[0]])

    # step 10
    if num_input_save == 1:
        
        if num_input == 3:
            symptom = 0
            print("증상을 선택해 주세요")
            print(
                "1. 고열(37.5이상), 2. 기침, 3. 호흡곤란, 4. 가슴통증, 5. 인후통, 6. 후각상실, 7. 가래, 8. 근육, 9. 오한, 10. 콧물, 11. 두통 12. 설사 13. 미각상실 14.증상없음 ")  # 기타를 만들지 고민중
            symptom = ['고열(37.5이상)', '기침', '호흡곤란', '가슴통증', '인후통', '후각상실', '가래', '근육', '오한', '콧물', '두통', '설사', '미각상실','증상없음']
            numsize = len(symptom)
            symptoms = []
            while symptom == 0:
                symptom_num = num_input  # 사이사이에 다음버튼 넣기
                if symptom_num == 1:
                    symptom = "고열(37.5이상)"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 2:
                    symptom = "기침"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 3:
                    symptom = "가래"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 4:
                    symptom = "호흡곤란"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 5:
                    symptom = "두통"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 6:
                    symptom = "근육통"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 7:
                    symptom = "오한"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 8:
                    symptom = "인후통"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 9:
                    symptom = "후각상실"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 10:
                    symptom = "미각상실"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 11:
                    symptom = "설사"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 12:
                    symptom = "콧물"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 13:
                    break

                symptom = 0
                num_input = 0
                print(symptoms)

        wr.writerow([4.5, '증상', symptoms])

    # step 11
    if num_input_save == 1:
        print("개인정보 수집에 동의하십니까?")
        print("1.예, 2.아니오")
        agree = ['예', '아니오']
        umsize = len(agree)
        agree_num = num_input
        agrees.append(agree[agree_num - 1])
        wr.writerow([5, '개인정보 수집 동의여부', agrees[0]])

        print(agrees)

    f.close()

if visits[0] == '아니오':

    # step 2

    if checking_gpio == 1:
        print("이름을 입력해 주세요")
        # name = num_input 이름 입력받아야함
        # 답변 숫자 입력한 후 다음 누름
        # names.append(name[name_num-1])
        num_input = 0
        print(names)

    # step 3

    if checking_gpio == 1:
        print("성별을 선택해 주세요")
        print("1. 남, 2. 여")
        sex = ['남', '여']
        numsize = len(sex)
        sex_num = num_input
        # 답변 숫자 입력한 후 다음 누름
        sexs.append(sex[sex_num - 1])
        sex_num = 0
        numsize = 0
        num_input = 0
        print(sexs)

    # step 4

    if checking_gpio == 1:
        print("생년월일을 입력해 주세요")
        birth = num_input
        # 답변 숫자 입력한 후 다음 누름
        births.append(birth)
        birth = 0
        num_input = 0
        print(births)
    file_name = names[0] + births[0] + sexs[0]
    # f = open(file_name,'r', encoding='utf-8')
    f = open(file_name, 'a', encoding='utf-8')
    # lines = csv.reader(f)
    wr = csv.writer(f)

    if checking_gpio == 1:
        print("검사경위(이유)가 무었인가요?")
        print(
            "1. 자가격리, 2. 자가격리 해제전, 3. 유증상자, 4. 보건소 재난문자 연락, 5. 해외입국자, 6. 해외입국자접촉자, 7. 집단발생지 방문자, 8. 확진자접촉, 9. 선제검사, 10. 본인판단")
        why = ['자가격리', '자가격리 해제전', '유증상자', '보건소 재난문자 연락', '해외입국자', '해외입국자접촉자', '집단발생지 방문자', '확진자접촉', '선제검사', '본인판단']
        numsize = len(why)
        why_num = num_input
        whys.append(why[why_num - 1])
        # num_input = 0 여기서는 초기화 하면 x
        wr.writerow([4, '검사경위', whys[0]])

    # step 10
    if checking_gpio == 1:

        if num_input == 3:
            symptom = 0
            print("증상을 선택해 주세요")
            print(
                "1. 고열(37.5이상), 2. 기침, 3. 가래, 4. 호흡곤란, 5. 두통, 6. 근육통, 7. 오한, 8. 인후통, 9. 후각상실, 10. 미각상실, 11. 없음 ")  # 기타를 만들지 고민중
            symptom = ['고열(37.5이상)', '기침', '가래', '호흡곤란', '두통', '근육통', '오한', '인후통', '후각상실', '미각상실', '없음']
            numsize = len(symptom)
            symptoms = []
            while symptom == 0:
                symptom_num = num_input  # 사이사이에 다음버튼 넣기
                if symptom_num == 1:
                    symptom = "고열(37.5이상)"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 2:
                    symptom = "기침"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 3:
                    symptom = "가래"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 4:
                    symptom = "호흡곤란"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 5:
                    symptom = "두통"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 6:
                    symptom = "근육통"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 7:
                    symptom = "오한"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 8:
                    symptom = "인후통"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 9:
                    symptom = "후각상실"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 10:
                    symptom = "미각상실"
                    symptoms.append(symptom)
                    symptom = 0
                    num_input = 0
                elif symptom_num == 11:
                    break

                symptom = 0
                num_input = 0
                print(symptoms)

        wr.writerow([4.5, '증상', symptoms])

        # step 11
    if checking_gpio == 1:
        print("개인정보 수집에 동의하십니까?")
        print("1.예, 2.아니오")

        agree = ['예', '아니오']
        umsize = len(agree)
        agree_num = num_input
        agrees.append(agree[agree_num - 1])
        wr.writerow([5, '개인정보 수집 동의여부', agrees[0]])

        print(agrees)

    f.close()