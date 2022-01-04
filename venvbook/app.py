from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# db에 dbsparta라는 폴더 만들기(값이 들어가야 생김)
client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
# 리뷰 저장하기
@app.route('/review', methods=['POST'])
def write_review():
    # index.html의 makeRiview()로부터 입력된 data 받아오기
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # db에 데이터 공간 만들기
    doc = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    }

    # db의 bookreview폴더에 데이터 저장
    db.bookreview.insert_one(doc)

    # 완료되면 나오는 alert메세지
    return jsonify({'msg': '이 요청은 POST!'})


# API 역할을 하는 부분
# 리뷰 보여주기
@app.route('/review', methods=['GET'])
def read_reviews():

    # db에서 가져와서 reviews라는 변수에 담는다
    reviews = list(db.bookreview.find({}, {'_id': False}))

    # 담은 것을 all_reviews라는 이름으로 index.html로 보낸다
    return jsonify({'all_reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
