import data_manager
import util
from flask import render_template, Flask, url_for, request, redirect

app = Flask(__name__)

@app.route('/list')
@app.route('/')
def list_question():
    data = data_manager.get_questions()

    return render_template('list_questions.html',
                           data = data,
                           title = "List questions")

@app.route('/question/<question_id>')
def display_question(question_id):
    answers = data_manager.get_answers()
    questions = data_manager.get_questions()

    return render_template("display_question.html",
                           question_id=question_id,
                           answers=answers,
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
                    "submission_time" : "date",
                    "view_number" : 0,
                    "vote_number" : 0,
                    "title" : request.form.get("title"),
                    "message": request.form.get("message"),
                    "image" : None,

    }


    data_manager.write_question_to_file(new_question)


    return redirect(url_for("list_question"))

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
