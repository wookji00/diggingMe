import json
import sys

try:
    with open("questions.json", "r") as f:
        questions = json.load(f)
    main = input("핵심 문제를 기록하세요 :")

    sub_problem = [main]

    """
    print(subs)
    print()
    print(len(subs))
    """
    while True:
        sub = input("부분 문제를 기록하세요 :")
        if sub == "":
            break
        deviding = [sub]
        message_list = []
        for question in questions:
            message = input(f"{question['question']} ?\n")
            message_list.append(message)
        deviding.append(message_list)
        sub_problem.append(deviding)
except FileNotFoundError:
    print("질문 파일이 없습니다!")
    ans_yes = ['y', 'yes', '네', '예', 'Y','YES']
    make_json = input("질문 파일을 업데이트 하시겠습니까? [(y)es|(n)o]")
    if make_json in ans_yes:
        question_list = []
        question_id = 1
        while True:
            contents_question = input("질문 내용을 적으세요 : (종료하고 싶다면 \"end\"를 작성하세요")
            if contents_question == 'end':
                print("질문 입력이 종료되었습니다.")
                break
            contents_category = input("질문 유형을 적으세요 :")
            question_dict = {
                 "id": question_id,
                 "question": contents_question,
                 "category": contents_category
            }
            question_list += [question_dict]
            print("질문 추가 성공!")
            question_id += 1

        print("현재까지의 내용을 기준으로 questions.json을 저장하겠습니다.")
        file_path = "questions.json"
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(question_list, file, indent=4, ensure_ascii=False)
    sys.exit(1)
except KeyboardInterrupt as e:
    print(e)
    print("강제 중단되었습니다.")
    sys.exit(0)
finally:
    if "sub_problem" in locals():
        print(sub_problem, end="\n")
    print("안전하게 종료되었습니다.")
