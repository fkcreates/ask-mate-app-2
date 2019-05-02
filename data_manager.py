import connection


@connection.connection_handler
def list_questions(cursor, order_by, order):
    cursor.execute(f"""
                    SELECT * FROM question 
                    ORDER BY {order_by} {order};
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
def get_answers_for_question(cursor, question_id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE question_id = %(question_id)s
                    ORDER BY vote_number DESC;
                    """,
                   {'question_id': question_id})
    answers = cursor.fetchall()
    return answers


@connection.connection_handler
def get_answer_by_answer_id(cursor, answer_id):
    cursor.execute("""
                    SELECT submission_time, vote_number, message FROM answer
                    WHERE id = %(answer_id)s;
                    """,
                   {'answer_id': answer_id})

    answer = cursor.fetchall()
    return answer


@connection.connection_handler
def question_by_answer_id(cursor, answer_id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE id = %(answer_id)s;
                    """,
                   {'answer_id': answer_id})

    answer = cursor.fetchall()
    return answer[0]


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


@connection.connection_handler
def increase_view_number(cursor, question_id):
    cursor.execute("""
                   UPDATE question
                   SET view_number = view_number + 1
                   WHERE id = %(question_id)s;
                   """,
                   {'question_id': question_id})


@connection.connection_handler
def add_new_data_to_table(cursor, dict, type):
    from datetime import datetime
    dt = datetime.now().strftime("%Y-%m-%d %H:%M")

    if type == "question":
        cursor.execute("""
                        INSERT INTO question(submission_time, view_number, vote_number, title, message, image, user_id)
                        VALUES(%(submission_time)s, %(view_number)s, %(vote_number)s, %(title)s, %(message)s, %(image)s, %(user_id)s);
                         """,
                       {'submission_time': dt,
                        'view_number': dict['view_number'],
                        'vote_number': dict['vote_number'],
                        'title': dict['title'],
                        'message': dict['message'],
                        'image': dict['image'],
                        'user_id': dict['user_id']})

    elif type == "answer":
        cursor.execute("""
                        INSERT INTO answer(submission_time, vote_number, question_id, message, image, user_id)
                        VALUES(%(submission_time)s, %(vote_number)s, %(question_id)s, %(message)s, %(image)s, %(user_id)s);
                        """,
                       {'submission_time': dt,
                        'vote_number': dict['vote_number'],
                        'question_id': dict['question_id'],
                        'message': dict['message'],
                        'image': dict['image'],
                        'user_id': dict['user_id']})

    elif type == "comment":
        cursor.execute("""
                        INSERT INTO comment(question_id, answer_id, message, submission_time, edited_count, user_id)
                        VALUES(%(question_id)s, %(answer_id)s, %(message)s, %(submission_time)s, %(edited_count)s, %(user_id)s);
                        """,
                       {'question_id': dict['question_id'],
                        'answer_id': dict['answer_id'],
                        'message': dict['message'],
                        'submission_time': dt,
                        'edited_count': dict['edited_count'],
                        'user_id': dict['user_id']})
    elif type == "userdata":
        cursor.execute("""
                        INSERT INTO userdata(user_name, hashed_pw, reg_date, reputation)
                        VALUES(%(user_name)s, %(hashed_pw)s, %(reg_date)s, %(reputation)s);
                        """,
                       {'user_name': dict['user_name'],
                        'hashed_pw': dict['hashed_pw'],
                        'reg_date': dt,
                        'reputation': 0})


@connection.connection_handler
def delete_answer(cursor, answer_id):
    cursor.execute("""
                DELETE FROM comment
                WHERE answer_id = %(answer_id)s;
                DELETE FROM answer
                WHERE id = %(answer_id)s;
                """,
                   {'answer_id': answer_id})


@connection.connection_handler
def get_question_vote_number(cursor, question_id):
    cursor.execute("""
                    SELECT vote_number FROM question
                    WHERE id = %(question_id)s;
                    """,
                   {'question_id': question_id})
    vote_number = cursor.fetchall()
    return vote_number[0]


@connection.connection_handler
def update_question_vote_number(cursor, question_id, vote_number):
    cursor.execute("""
                    UPDATE question
                    SET vote_number = %(vote_number)s
                    WHERE id = %(question_id)s;
                    """,
                   {'question_id': question_id,
                    'vote_number': vote_number})


@connection.connection_handler
def get_answer_vote_number(cursor, question_id, answer_id):
    cursor.execute("""
                    SELECT vote_number FROM answer
                    WHERE question_id = %(question_id)s AND id = %(answer_id)s;
                    """,
                   {'question_id': question_id,
                    'answer_id': answer_id})
    vote_number = cursor.fetchall()
    return vote_number[0]


@connection.connection_handler
def update_answer_vote_number(cursor, question_id, answer_id, vote_number):
    cursor.execute("""
                    UPDATE answer
                    SET vote_number = %(vote_number)s
                    WHERE question_id = %(question_id)s AND id = %(answer_id)s;
                    """,
                   {'question_id': question_id,
                    'answer_id': answer_id,
                    'vote_number': vote_number})


@connection.connection_handler
def get_answer_for_question_by_id(cursor, answer_id, question_id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE id = %(answer_id)s AND question_id = %(question_id)s;
                    """,
                   {'answer_id': answer_id, 'question_id': question_id})
    question_answers_data = cursor.fetchall()
    return question_answers_data


@connection.connection_handler
def update_question_answer(cursor, dict):
    cursor.execute("""
                    UPDATE answer
                    SET message = %(message)s, image = %(image)s
                    WHERE id = %(answer_id)s AND question_id = %(question_id)s;
                    """,
                   {'answer_id': dict['id'],
                    'question_id': dict['question_id'],
                    'message': dict['message'],
                    'image': dict['image']})


@connection.connection_handler
def get_last_five_question_by_time(cursor):
    cursor.execute("""
                    SELECT * FROM question
                    ORDER BY submission_time DESC
                    LIMIT 5;
                    """)
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def delete_question(cursor, question_id):
    cursor.execute("""
                   DELETE FROM comment
                   WHERE question_id = %(question_id)s;
                   
                   DELETE FROM answer
                   WHERE question_id = %(question_id)s;
                   
                   DELETE FROM question_tag
                   WHERE question_id = %(question_id)s;
                   
                   DELETE FROM question
                   WHERE id = %(question_id)s;
                   """,
                   {'question_id': question_id})


@connection.connection_handler
def get_comments_for_question(cursor, question_id):
    cursor.execute("""
                    SELECT * FROM comment
                    WHERE question_id = %(question_id)s;
                    """,
                   {'question_id': question_id})
    comments = cursor.fetchall()
    return comments


@connection.connection_handler
def get_comments_for_answer(cursor, answer_id):
    cursor.execute("""
                    SELECT * FROM comment
                    WHERE answer_id = %(answer_id)s;
                    """,
                   {'answer_id': answer_id})
    comments = cursor.fetchall()
    return comments


@connection.connection_handler
def get_all_comments(cursor):
    cursor.execute("""
                    SELECT * FROM comment;
                    """)

    comments = cursor.fetchall()
    return comments


@connection.connection_handler
def delete_comment(cursor, comment_id):
    cursor.execute("""
                    DELETE FROM comment
                    WHERE id = %(comment_id)s;
                    """,
                   {'comment_id': comment_id})


@connection.connection_handler
def route_edit_comment(cursor, comment_id):
    cursor.execute("""
                    SELECT message, submission_time, edited_count FROM comment
                    WHERE id = %(comment_id)s;
                    """,
                   {'comment_id': comment_id})
    comment_to_edit = cursor.fetchall()
    return comment_to_edit


@connection.connection_handler
def edit_comment(cursor, comment_id, message):
    from datetime import datetime
    dt = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute("""
                    UPDATE comment
                    SET submission_time = %(submission_time)s, message = %(message)s, edited_count = edited_count + 1
                    WHERE id = %(comment_id)s;
                    """,
                   {'comment_id': comment_id,
                    'message': message,
                    'submission_time': dt})


@connection.connection_handler
def get_hashed_pw(cursor, user_name):
    cursor.execute("""
                    SELECT hashed_pw from userdata
                    WHERE user_name = %(user_name)s;
                    """,
                   {'user_name': user_name})

    hashed_pw = cursor.fetchall()

    if len(hashed_pw) > 0:
        return hashed_pw[0]
    else:
        return None


@connection.connection_handler
def get_user_id_by_name(cursor, user_name):
    cursor.execute("""
                    SELECT id FROM userdata
                    WHERE user_name = %(user_name)s;
                    """,
                   {'user_name': user_name})

    # user_id = cursor.fetchone()['id']
    user_id = cursor.fetchall()
    return user_id


@connection.connection_handler
def check_if_username_in_the_database(cursor, user_name):
    cursor.execute("""
                    SELECT user_name FROM userdata
                    WHERE user_name = %(user_name)s;
                    ;
                    """,
                   {'user_name': user_name})
    check_data = cursor.fetchall()
    return check_data


@connection.connection_handler
def search_for_text_in_question(cursor, text):
    cursor.execute(f"""
                    SELECT id, submission_time, view_number, vote_number, title, message FROM question
                    WHERE LOWER (title) LIKE '%{text}%'
                    ORDER BY vote_number DESC ;
                    """)
    result = cursor.fetchall()
    return result

@connection.connection_handler
def get_users(cursor):
    cursor.execute("""
                        SELECT user_name, reg_date, reputation
                        FROM userdata;
                        """, )
    # {'user_name': user_name,
    #  'reg_date': reg_date,
    #  'reputation': reputation})

    return cursor.fetchall()


@connection.connection_handler
def get_data_by_user_id(cursor, user_id, type):
    if type == 'question':
        cursor.execute("""
                        SELECT * FROM question
                        WHERE user_id = %(user_id)s;
                        """,
                       {'user_id': user_id})
        data = cursor.fetchall()
        return data
    if type == 'answer':
        cursor.execute("""
                        SELECT * FROM answer
                        WHERE user_id = %(user_id)s;""",
                       {'user_id': user_id})
        data = cursor.fetchall()
        return data
    if type == 'comment':
        cursor.execute("""
                        SELECT * FROM comment
                        WHERE user_id = %(user_id)s;""",
                       {'user_id': user_id})
        data = cursor.fetchall()
        return data