import connection


def get_answers():
    data = connection.get_data_from_file(connection.ANSWER_FILE_PATH)

    return data

def get_questions():
    data = connection.get_data_from_file(connection.QUESTION_FILE_PATH)

    return data