import data_manager
import util
from flask import render_template, Flask, url_for, request, redirect


app = Flask(__name__)


@app.route('/list')
@app.route('/')
def list_question():

    questions = data_manager.get_questions()
    sorted_questions = util.sort_data_by_time(questions)
    converted_questions = util.convert_timestamp_to_date(sorted_questions)

    return render_template("list_questions.html", data=converted_questions, title="List questions")


@app.route('/question/<question_id>')
def display_question(question_id):
    questions = data_manager.get_questions()

    answers = data_manager.get_answers()
    sorted_answers = util.sort_data_by_time(answers)
    converted_answers = util.convert_timestamp_to_date(sorted_answers)


    return render_template("display_question.html",
                           question_id=question_id,
                           answers=converted_answers,
                           questions=questions,
                           title="Display question")


@app.route('/add-question', methods = ["GET"])
def route_question():

    return render_template("add_question.html",
                           title="Add question",
                           )


@app.route('/add_question', methods = ["POST"])
def add_question():
    new_question = {"id" : util.id_generator("question"),
                    "submission_time" : util.generate_timestamp(),
                    "view_number" : 0,
                    "vote_number" : 0,
                    "title" : request.form.get("title"),
                    "message": request.form.get("message"),
                    "image" : "no image",
                    }


    data_manager.write_question_to_file(new_question)


    return redirect(url_for("list_question"))


@app.route('/question/<question_id>/are-you-sure', methods=["GET"])
def confirm_delete_question(question_id):

    return render_template("confirm_delete_question.html",
                           question_id=question_id,
                           title="Are you sure you want to delete this question?")


@app.route('/question/<question_id>/are-you-sure', methods=["POST"])
def delete_question(question_id):

    data_manager.delete_question(question_id)
    data_manager.delete_answers_for_deleted_question(question_id)

    return redirect(url_for("list_question"))


@app.route('/question/<question_id>/new-answer', methods = ["GET"])
def route_new_answer(question_id):

    return render_template("new_answer.html",
                           question_id=question_id,
                           title="New answer")


@app.route('/question/<question_id>/new-answer', methods = ["POST"])
def post_answer(question_id):
    new_answer = {"id": util.id_generator("answer"),
                  "submission_time" : util.generate_timestamp(),
                  "vote_number" : 0,
                  "question_id" : question_id,
                  "message" : request.form.get("message"),
                  "image" : "no image"
                  }

    data_manager.write_answer_to_file(new_answer)

    return redirect(url_for("display_question", question_id=question_id))


@app.route('/question/<question_id>/edit', methods=["GET"])
def route_edit_question(question_id):
    questions = data_manager.get_questions()

    for question in questions:
        if question["id"] == question_id:
            question_to_edit = question

    return render_template("edit_question.html",
                           title = "Edit question",
                           question = question_to_edit,
                           question_id=question_id)


@app.route('/question/<question_id>/edit', methods=["POST"])
def edit_question(question_id):
    updated_question = {"id" : question_id,
                    "submission_time" : util.generate_timestamp(),
                    "view_number" : 0,
                    "vote_number" : 0,
                    "title" : request.form.get("title"),
                    "message": request.form.get("message"),
                    "image" : None,
                    }

    data_manager.update_edited_question(updated_question, question_id)

    return redirect(url_for("display_question", question_id=question_id))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
