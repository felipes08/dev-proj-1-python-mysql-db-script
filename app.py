from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://dbuser:dbpassword@cluster0.zuzz0tc.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client['devprojdb'] 
collection = db['example_table']

@app.route('/health')
def health():
    return "Up & Running"

@app.route('/create_table')
def create_table():
    return "MongoDB Pronto! (Não é necessário criar tabelas manualmente)"

@app.route('/insert_record', methods=['POST'])
def insert_record():
    name = request.json['name']
    
    collection.insert_one({"name": name})
    
    return "Record inserted successfully"

@app.route('/data')
def data():

    records = list(collection.find())
  
    for record in records:
        record['_id'] = str(record['_id'])
        
    return jsonify(records)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
