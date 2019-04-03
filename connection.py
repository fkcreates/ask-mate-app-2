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