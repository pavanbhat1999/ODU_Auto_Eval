from flask import Flask, render_template, request
from firebase import firebase
import configurations
import pyrebase

app = Flask(__name__)
email = "null"

firebsevar = pyrebase.initialize_app(config=configurations.config)
db = firebsevar.database()


@app.route('/')
def Base_qstn_paper_set():
    return render_template('first.html')




@app.route('/get_answers', methods=['POST', 'GET'])
def get_answers():
    if request.method == 'POST':
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']

        email = request.form['emailID']

        ans = {"a1": first, "a2": second, "a3": third, "email": email}

        result = db.child("/answers1").push(ans)

        
    return render_template('first.html')




if __name__ == '__main__':
    app.run()
