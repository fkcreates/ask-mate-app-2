import data_manager
import util
from flask import render_template, Flask, url_for, request, redirect


app = Flask(__name__)


@app.route('/')
def get_last_5_questions_by_time():
    questions = data_manager.get_last_five_question_by_time()
    return render_template("list_questions.html", data=questions, title="Last five questions")


@app.route('/list')
def list_question():
    questions = data_manager.list_questions()
    return render_template("list_questions.html", data=questions, title="List questions")


@app.route('/question/<int:question_id>')
def display_question(question_id):
    question = data_manager.display_question(question_id)
    answers = data_manager.list_answers_for_question(question_id)
    return render_template("display_question.html",
                           question_id=question_id,
                           question=question,
                           answers=answers,
                           title="Display question")


@app.route('/add-question', methods=["GET"])
def route_question():
    return render_template("add_question.html",
                           title="Add question",
                           )


@app.route('/add_question', methods=["POST"])
def add_question():

    new_question = {
                    "view_number": 0,
                    "vote_number": 0,
                    "title": request.form.get("title"),
                    "message": request.form.get("message"),
                    "image": None,
                    }

    data_manager.add_new_data_to_table(new_question, 'question')
    return redirect(url_for("list_question"))


@app.route('/question/<question_id>/are-you-sure', methods=["GET"])
def confirm_delete_question(question_id):

    return render_template("confirm_delete_question.html",
                           question_id=question_id,
                           title="Are you sure you want to delete this question?")


@app.route('/question/<question_id>/are-you-sure', methods=["POST"])
def delete_question(question_id):
    data_manager.delete_question(question_id)
    # data_manager.delete_answers_for_deleted_question(question_id)

    return redirect(url_for("list_question"))


@app.route('/question/<question_id>/new-answer', methods=["GET"])
def route_new_answer(question_id):

    return render_template("new_answer.html",
                           question_id=question_id,
                           title="New answer")


@app.route('/question/<question_id>/new-answer', methods=["POST"])
def post_answer(question_id):

    new_answer = {
                  "vote_number": 0,
                  "question_id": question_id,
                  "message": request.form.get("message"),
                  "image": None,
                  }

    data_manager.add_new_data_to_table(new_answer, 'answer')
    return redirect(url_for("display_question", question_id=question_id))


@app.route('/question/<int:question_id>/edit', methods=["GET"])
def route_edit_question(question_id):

    question_to_edit = data_manager.route_edit_question(question_id)

    return render_template("edit_question.html",
                           title="Edit question",
                           question=question_to_edit,
                           question_id=question_id)

    """
    ide kell egy beolvaso query sqlbol, adott questionhoz
    kap egy question id-t,
    returnolje az edit question htmlt

    regi kod:
    questions = data_manager.get_questions()

    for question in questions:
        if question["id"] == question_id:
            question_to_edit = question

    return render_template("edit_question.html",
                           title = "Edit question",
                           question = question_to_edit,
                           question_id=question_id)"""


@app.route('/question/<question_id>/edit', methods=["POST"])
def edit_question(question_id):

    edited_title = request.form["title"]
    edited_message = request.form["message"]

    data_manager.edit_question(question_id, edited_title, edited_message)

    return redirect(url_for("display_question",
                            question_id=question_id))

    """
    itt tud a user editalni, azaz egy UPDATE query kell sqlbol,
    es vigyen vissza az adott question id-ju kerdes oldalra (display_question.html)

    regi kod:
    questions = data_manager.get_questions()

    for question in questions:
        if question["id"] == question_id:

            updated_question = {"id" : question_id,
                            "submission_time" : util.generate_timestamp(),
                            "view_number" : question["view_number"],
                            "vote_number" : question["vote_number"],
                            "title" : request.form.get("title"),
                            "message": request.form.get("message"),
                            "image" : None,
                            }

    data_manager.update_edited_question(updated_question, question_id)

    return redirect(url_for("display_question", question_id=question_id))"""


@app.route('/question/<int:question_id>/vote-up')
def vote_for_question(question_id):
    vote_type = request.args.get('vote_type')
    vote_number = data_manager.get_question_vote_number(question_id)
    increases_or_decreases_vote_number = util.vote_up_or_down(vote_number, vote_type)
    data_manager.update_question_vote_number(question_id, increases_or_decreases_vote_number)

    return redirect(url_for("list_question"))


@app.route('/answer/<answer_id>/vote-down')
def vote_for_answer(answer_id):
    question_id = request.args.get('question_id')
    vote_type = request.args.get('vote_type')
    vote_number = data_manager.get_answer_vote_number(question_id, answer_id)
    increases_or_decreases_vote_number = util.vote_up_or_down(vote_number, vote_type)
    data_manager.update_answer_vote_number(question_id, answer_id, increases_or_decreases_vote_number)

    return redirect(url_for("display_question", question_id=question_id))


@app.route('/answer/<answer_id>/edit', methods=["GET"])
def route_edit_answer(answer_id):
    question_id = request.args.get('question_id')
    answers = data_manager.get_question_answers_data(answer_id, question_id)
    return render_template('edit_answer.html', answers=answers, answer_id=answer_id, question_id=question_id)

    """
    ide kell egy SELECT query az adott answerhez,
    vigyen at az edit_answer htmlre

    regi kod:

    answers = data_manager.get_answers()
    question_id = request.args.get("question_id")

    return render_template("edit_answer.html",
                           title="Edit answer",
                           answers=answers,
                           answer_id=answer_id,
                           question_id=question_id)"""


@app.route('/answer/<answer_id>/edit', methods=["POST"])
def edit_answer(answer_id):
    question_id = request.args.get('question_id')
    new_answer = {
                'id': answer_id,
                'question_id': question_id,
                'message': request.form.get('message'),
                'image': None
                }
    data_manager.update_question_answer(new_answer)
    return redirect(url_for("display_question", question_id=question_id))


@app.route('/answer/<int:answer_id>/are-you-sure', methods=["GET"])
def confirm_delete_answer(answer_id):
    question_id = request.args.get("question_id")
    return render_template("confirm_delete_answer.html",
                           answer_id=answer_id,
                           question_id=question_id,
                           title="Are you sure you want to delete this answer?")

    """
    UGYANAZ, MINT A DELETE QUESTIONNEL, CSAK ANSWER

    REGI KOD:
    question_id = request.args.get("question_id")

    return render_template("confirm_delete_answer.html",
                           answer_id=answer_id,
                           question_id=question_id,
                           title="Are you sure you want to delete this answer?")"""


@app.route('/answer/<int:answer_id>/delete', methods=["GET", "POST"])
def delete_answer(answer_id):

    question_id = request.args.get("question_id")

    data_manager.delete_answer(answer_id)

    return redirect(url_for("display_question",
                            question_id=question_id))

    """
    UGYANAZ, MINT A DELETE QUESTIONNEL, CSAK ANSWER


    REGI KOD:
    question_id = request.args.get("question_id")

    data_manager.delete_answer_by_answer_id(answer_id)

    return redirect(url_for("display_question", question_id=question_id))"""


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
