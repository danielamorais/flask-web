from flask import Flask, render_template, Response
import pymongo
from bson.json_util import dumps
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getAll', methods=['GET'])
def getAll():
    try:
        conn = pymongo.MongoClient()
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e
    db = conn['local']
    collection = db.persons
    myList = []
    for d in collection.find():
        myList.append(dumps(d))
    return "[" + ",".join(myList) + "]"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
