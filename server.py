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

    return render_template('list_questions.html',
                           data = converted_questions,
                           title = "List questions")


@app.route('/question/<question_id>')
def display_question(question_id):
    answers = data_manager.get_answers()
    questions = data_manager.get_questions()

    sorted_answers = util.sort_data_by_time(answers)
    converted_answers = util.convert_timestamp_to_date(sorted_answers)


    return render_template("display_question.html",
                           question_id=question_id,
                           answers=converted_answers,
                           questions=questions,
                           title = "Display question")

@app.route('/add-question', methods = ["GET"])
def route_question():

    return render_template("add_question.html",
                           title = "Add question",
                           )

@app.route('/add_question', methods = ["POST"])
def add_question():
    new_question = {"id" : util.id_generator("question"),
                    "submission_time" : util.generate_timestamp(),
                    "view_number" : 0,
                    "vote_number" : 0,
                    "title" : request.form.get("title"),
                    "message": request.form.get("message"),
                    "image" : None,
                    }


    data_manager.write_question_to_file(new_question)


    return redirect(url_for("list_question"))


@app.route('/question/<question_id>/new-answer', methods = ["GET"])
def route_new_answer(question_id):

    return render_template("new_answer.html",
                           question_id = question_id,
                           title = "New answer")


@app.route('/question/<question_id>/new-answer', methods = ["POST"])
def post_answer(question_id):
    new_answer = {"id": util.id_generator("answer"),
                  "submission_time" : util.generate_timestamp(),
                  "vote_number" : 0,
                  "question_id" : question_id,
                  "message" : request.form.get("message"),
                  "image" : None
                  }

    data_manager.write_answer_to_file(new_answer)

    return redirect(url_for("display_question", question_id=question_id))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
