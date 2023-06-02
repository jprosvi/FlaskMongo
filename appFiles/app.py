from flask import Flask, jsonify, request
from pymongo import MongoClient

myserver = MongoClient('mymongo')
db = myserver.studentsDB
col = db.students

app = Flask(__name__)
@app.route('/users', methods=['GET'])
def getusers():
    #x = jsonify(
    #    name="Jota",
    #    lname= "Rosvi"

    users = []
    for user in col.find():
        users.append({
            "name": user['name'],
            "lname": user['lname'],
            "age": user['age']
        })

    #[print(x) for x in users]    
    #return "'Hi'"
    return jsonify(users)


@app.route('/users', methods=['POST'])
def createUser():
    col.insert_one({
         "name": request.json['name'], 
         "lname": request.json['lname'],
         "age": request.json['age']
    })

    return "Request received"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
