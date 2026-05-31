import json
import re
import sys
from datetime import datetime

result = None


def sanitize_filename(text):
    cleaned = re.sub(r'[\\/:*?"<>|]', "_", text).strip()
    cleaned = re.sub(r"\s+", "_", cleaned)
    return cleaned if cleaned else "main"


def create_questions_file():
    ans_yes = ["y", "yes", "네", "예", "Y", "YES"]
    make_json = input("질문 파일을 업데이트 하시겠습니까? [(y)es|(n)o]")
    if make_json not in ans_yes:
        return None

    question_list = []
    question_id = 1
    while True:
        contents_question = input(
            '질문 내용을 적으세요 (종료하고 싶다면 "end"를 작성하세요) :'
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
        question_list.append(question_dict)
        print("질문 추가 성공!")
        question_id += 1

    print("현재까지의 내용을 기준으로 questions.json을 저장하겠습니다.")
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(question_list, file, indent=4, ensure_ascii=False)

    return question_list


try:
    while True:
        try:
            with (
                open("questions.json", "r", encoding="utf-8") as f
            ):  # questions이라는 질문 내용 모음은 json형식으로 읽기 및 쓸 수 있습니다.
                questions = json.load(f)
            break
        except (
            FileNotFoundError
        ):  # questions.json 파일이 없을 경우 : 스스로 작성이 가능하게끔..
            print("질문 파일이 없습니다!")
            created_questions = create_questions_file()
            if created_questions is None:
                print("질문 파일 생성이 취소되었습니다.")
                sys.exit(1)

    main = input(
        "핵심 문제를 기록하세요 :"
    )  # main : 핵심 문제, 제일 처음에 다뤄질 Big Problem

    sub_problem = []

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
        message_list = []
        for question in questions:
            message = input(
                f"{question['question']} ?\n"
            )  # 각 질문(question)은 questions.json에 정의된 질문입니다.
            message_list.append(
                {
                    "id": question.get("id"),
                    "question": question.get("question"),
                    "category": question.get("category"),
                    "answer": message,
                }
            )
        sub_problem.append({"sub_problem": sub, "responses": message_list})

    result = {"main": main, "sub_problems": sub_problem}
    file_name = (
        f"{sanitize_filename(main)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
    print(f"결과가 저장되었습니다: {file_name}")
except KeyboardInterrupt as e:  # ^C 입력 시 행동
    print(e)
    print("강제 중단되었습니다.")
    sys.exit(0)
finally:
    if result is not None:  # FileNotFoundError, KeyboardInterrupt 와 Normal 포함
        print(result, end="\n")
    print("안전하게 종료되었습니다.")
