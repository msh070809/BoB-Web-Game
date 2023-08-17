from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'  # MySQL 연결 정보 입력
db = SQLAlchemy(app)

# 모델 클래스 임포트
from model import User

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/report', methods=['POST'])
def report():
    userid = request.form['userid']
    userpw = request.form['userpw']

    lower_letter = any(c.islower() for c in userpw)
    upper_letter = any(c.isupper() for c in userpw)
    num_end = userid[-1].isdigit()
    report = lower_letter & upper_letter & num_end

    if report:
        new_user = User(username=userid, userpw=userpw)
        db.session.add(new_user)
        db.session.commit()

    return render_template('report.html', userid=userid, userpw=userpw, lower=lower_letter, upper=upper_letter, num_end=num_end, report=report)

if __name__ == '__main__':
    app.run(debug=True)