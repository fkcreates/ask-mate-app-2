import connection


@connection.connection_handler
def list_questions(cursor):
    cursor.execute("""
                    SELECT * FROM question;
                    """)
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def display_question(cursor, question_id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE id = %(question_id)s;
                    """,
                   {'question_id': question_id})
    question = cursor.fetchall()
    return question

@connection.connection_handler
def route_edit_question(cursor, question_id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE id = %(question_id)s;
                    """,
                   {'question_id': question_id})

    question_to_edit = cursor.fetchall()
    return question_to_edit[0]

@connection.connection_handler
def edit_question(cursor, question_id, edited_title, edited_message):
    cursor.execute("""
                    UPDATE question
                    SET title = %(edited_title)s, message = %(edited_message)s
                    WHERE id = %(question_id)s;
                    """,
                   {'question_id': question_id,
                    'edited_title': edited_title,
                    'edited_message': edited_message})


"""
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


def update_edited_answer(edited_answer, answer_id):
    updated_data = connection.update_edited_answer(edited_answer, answer_id)

    return updated_data


def delete_question(question_id):
    return connection.delete_question(connection.QUESTION_FILE_PATH, question_id)


def delete_answers_for_deleted_question(question_id):
    return connection.delete_answers_for_deleted_question(connection.ANSWER_FILE_PATH, question_id)


def update_question_vote_number(dictionary):
    connection.update_question_vote_number(dictionary, connection.QUESTION_FILE_PATH, connection.QUESTIONS_HEADER)


def update_answer_vote_number(dictionary):
    connection.update_question_vote_number(dictionary,connection.ANSWER_FILE_PATH, connection.ANSWERS_HEADER)


def delete_answer_by_answer_id(answer_id):
    connection.delete_answer_by_answer_id(answer_id)"""


