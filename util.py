import data_manager
import connection
from datetime import datetime


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


def generate_timestamp():

    timestamp = int(datetime.now().timestamp())

    return timestamp

def convert_timestamp_to_date(data):

    for row in data:
        time = int(row["submission_time"])
        row["submission_time"] = datetime.utcfromtimestamp(time).strftime("%Y-%m-%d %H:%m")

    return data

def sort_data_by_time(data):


    sorted_data = sorted(data, key=lambda x: x["submission_time"], reverse=True)

    return sorted_data


generate_timestamp()