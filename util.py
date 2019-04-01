import data_manager
import connection


def id_generator(id_to_check):
    if id_to_check == "answer":
        answers = data_manager.get_answers()
        answer_ids = [int(answer["id"]) for answer in answers]

        new_id = max(answer_ids) + 1
        return new_id


    elif id_to_check == "question":
        questions = data_manager.get_questions()
        question_ids = [int(question["id"]) for question in questions]

        new_id = max(question_ids) + 1
        return new_id

    else:
        return None


