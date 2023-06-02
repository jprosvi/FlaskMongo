from flask import Flask, jsonify, request
from pymongo import MongoClient



myserver = MongoClient('mymongo')
mydb = myserver.carsDB
mycol = mydb.cars

app = Flask('__name__')

@app.route('/cars', methods=['POST'])
def createCar():
    mycol.insert_one({
         "brand": request.json['brand'],
         "model": request.json['model'],
         "year": request.json['year']
    })
    return "Works"


@app.route('/cars', methods=['GET'])
def getCars():
    carList = []
    for car in mycol.find():
          carList.append({
               "brand": car['brand'],
               "model": car['model'],
               "year": car['year']
          })
    
    return jsonify(carList)


if __name__== '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)





