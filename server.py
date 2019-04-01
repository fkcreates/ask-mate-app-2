import data_manager
import util
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/list')
@app.route('/')
def list_question():
    data = data_manager.get_questions()

    return render_template('list_questions.html',
                           data = data,
                           title = "List questions")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
