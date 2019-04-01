import connection


def get_answers():
    data = connection.get_data_from_file(connection.ANSWER_FILE_PATH)

    return data

def get_questions():
    data = connection.get_data_from_file(connection.QUESTION_FILE_PATH)

    return data

def write_answer_to_file(dictionary):
    data = connection.write_data_to_file(dictionary, connection.ANSWER_FILE_PATH, connection.ANSWERS_HEADER)


def write_question_to_file(dictionary):
    data = connection.write_data_to_file(dictionary, connection.QUESTION_FILE_PATH, connection.QUESTIONS_HEADER)



