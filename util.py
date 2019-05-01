import data_manager
import bcrypt
from flask import session


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def vote_up_or_down(vote_number, vote_type):
    if vote_type == 'up':
        vote_number['vote_number'] += 1
    else:
        vote_number['vote_number'] -= 1
    return vote_number['vote_number']


def deciding_where_to_redirect(comments, comment_id, answer_id, question_id):
    for comment in comments:
        if comment["question_id"] == int(question_id) and comment["id"] == comment_id:
            return "question"

        elif comment["answer_id"] == int(answer_id) and comment["id"] == comment_id:
            return "answer"


def order_questions(order_by, order):
    if order is not None:
        questions = data_manager.list_questions(order_by, order)
    else:
        order_by = 'submission_time'
        order = 'DESC'
        questions = data_manager.list_questions(order_by, order)
    return questions

def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)

def get_user_name_and_id(session):
    return {
        'user_name': session['user_name'],
        'user_id': session['user_id']
    }

def check_if_logged_in():
    user = None
    if 'user_id' in session:
        user = get_user_name_and_id(session)
    return user