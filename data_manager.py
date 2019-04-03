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


def update_edited_question(edited_question, question_id):
    updated_data = connection.update_edited_question(edited_question, question_id)

    return updated_data


def delete_question(question_id):
    return connection.delete_question(connection.QUESTION_FILE_PATH, question_id)


def delete_answers_for_deleted_question(question_id):
    return connection.delete_answers_for_deleted_question(connection.ANSWER_FILE_PATH, question_id)
