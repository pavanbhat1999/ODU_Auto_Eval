from flask import Flask, render_template, request,url_for,redirect
from firebase import firebase
import configurations
import pyrebase
import sys
import os
# sys.path.append(os.path.abspath("/root/ODU/Subjective-Answer- mod/Modules"))
from givVal import eval,givVal
import cosine_similarity as keywordVal
import configurations
from fuzzywuzzy import fuzz
import nav_test

app = Flask(__name__)


firebsevar = pyrebase.initialize_app(config=configurations.config)
db = firebsevar.database()


@app.route('/')
def init():
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

        
    return render_template("app_teacher.html")
       
@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        eval()
        return render_template('result.html')
@app.route('/get_results', methods=['POST', 'GET'])
def get_results():
    if request.method=='POST':
        email=request.form['name']
        all_answers = db.child("answers").get()
        for each_users_answers in all_answers.each():
            if email==each_users_answers.val()['email']:
                print("email found")
                marks1=str(each_users_answers.val()['result1'])
                marks2=str(each_users_answers.val()['result2'])
                marks3=str(each_users_answers.val()['result3'])
                                
    return render_template('out.html',email=email,marks1=marks1,marks2=marks2,marks3=marks3)
if __name__ == '__main__':
    app.run(debug=True)