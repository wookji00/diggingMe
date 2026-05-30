import json
import sys

try:
    with open(
        "questions.json", "r"
    ) as f:  # questions이라는 질문 내용 모음은 json형식으로 읽기 및 쓸 수 있습니다.
        questions = json.load(f)
    main = input(
        "핵심 문제를 기록하세요 :"
    )  # main : 핵심 문제, 제일 처음에 다뤄질 Big Problem

    sub_problem = [main]  # main 이 부모가 되고 sub_problem 이 자식이 됩니다.

    """
    print(subs)
    print()
    print(len(subs))
    """  # sub_problem 출력 확인 및 디버깅 완료

    while True:
        sub = input(
            "부분 문제를 기록하세요 :"
        )  # sub : main의 자식이 되는 문제, main을 한번 쪼갠 작은 문제입니다.
        if sub == "":
            break
        deviding = [
            sub
        ]  # 1개의 sub에 질문을 정해진대로 출력하고, 이에 각각 comment를 달아주는 행동을
        message_list = []  # user 에게 요구하는 목표입니다.
        for question in questions:
            message = input(
                f"{question['question']} ?\n"
            )  # 각 질문(question)은 questions.json에 정의된 질문입니다.
            message_list.append(message)
        deviding.append(message_list)
        sub_problem.append(
            deviding
        )  # 최종적으로 형태는 [main, [sub, [question, message],][sub2, [question, message],]] 형태
except (
    FileNotFoundError
):  # questions.json 파일이 없을 경우 : 스스로 작성이 가능하게끔..
    print("질문 파일이 없습니다!")
    ans_yes = ["y", "yes", "네", "예", "Y", "YES"]
    make_json = input("질문 파일을 업데이트 하시겠습니까? [(y)es|(n)o]")
    if make_json in ans_yes:
        question_list = []
        question_id = 1
        while True:
            contents_question = input(
                '질문 내용을 적으세요 : (종료하고 싶다면 "end"를 작성하세요'
            )
            if contents_question == "end":
                print("질문 입력이 종료되었습니다.")
                break
            contents_category = input("질문 유형을 적으세요 :")
            question_dict = {
                "id": question_id,
                "question": contents_question,
                "category": contents_category,
            }
            question_list += [question_dict]
            print("질문 추가 성공!")
            question_id += 1

        print("현재까지의 내용을 기준으로 questions.json을 저장하겠습니다.")
        file_path = "questions.json"
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(question_list, file, indent=4, ensure_ascii=False)
    sys.exit(1)
except KeyboardInterrupt as e:  # ^C 입력 시 행동
    print(e)
    print("강제 중단되었습니다.")
    sys.exit(0)
finally:
    if "sub_problem" in locals():  # FileNotFoundError, KeyboardInterrupt 와 Normal 포함
        print(sub_problem, end="\n")
    print("안전하게 종료되었습니다.")
