import csv

ANSWER_FILE_PATH = "answers.csv"
QUESTION_FILE_PATH = "questions.csv"

ANSWERS_HEADER = ["id", "submission_time", "vote_number", "question_id", "message", "image"]
QUESTIONS_HEADER = [ "id", "submission_time", "view_number", "vote_number", "title", "message", "image"]


def get_data_from_file(filename):
    data = []

    with open(filename) as file:

        reader = csv.DictReader(file)

        for row in reader:
            data.append(dict(row))

    return data


def write_data_to_file(dictionary, filename, fieldnames):
    data = get_data_from_file(filename)

    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

        writer.writerow(dictionary)


def update_edited_question(edited_question, question_id):
    data = get_data_from_file(QUESTION_FILE_PATH)

    with open(QUESTION_FILE_PATH, "w") as file:
        writer = csv.DictWriter(file, fieldnames=QUESTIONS_HEADER)
        writer.writeheader()

        for question in data:
            if question["id"] == question_id:
                writer.writerow(edited_question)
            else:
                writer.writerow(question)

    return data


<<<<<<< HEAD
def delete_question(filename, question_id):

    data = get_data_from_file(QUESTION_FILE_PATH)
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, QUESTIONS_HEADER)
        writer.writeheader()

        for row in data:
            if row["id"] != question_id:
                writer.writerow(row)


def delete_answers_for_deleted_question(filename, question_id):
    data = get_data_from_file(ANSWER_FILE_PATH)

    with open(filename, "w") as file:
        writer = csv.DictWriter(file, ANSWERS_HEADER)
        writer.writeheader()

        for row in data:
            if row["question_id"] != question_id:
                writer.writerow(row)

    return data
=======
def update_question_vote_number(dictionary, filename, fieldnames):
    data = get_data_from_file(filename)

    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            if row["id"] == dictionary["id"]:
                row = dictionary
            writer.writerow(row)
>>>>>>> 32db992cf3e0710bd5d7dc9cae92c449156fe9bc
