from flask import Flask,jsonify, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/', methods=['GET'])
def index():
    return jsonify({'app':'v1'})

@app.route('/engs', methods=['GET'])
def get_engs():
    resp_data = []
    engs = db.get_engs()
    resp_data = []
    for eng in engs:
        resp_data.append({'name': eng[0], 'lastName': eng[1], 'role': eng[2]})
    return jsonify({'engs':resp_data})

@app.route('/engs', methods=['POST'])
def add_engs():
    insert_values = (request.json['name'], request.json['lastName'], request.json['role'])
    db.add_eng(insert_values)
    return jsonify({'msg': 'added'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)