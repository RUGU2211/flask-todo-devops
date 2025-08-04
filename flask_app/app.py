from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['todo_db']
todo_collection = db['todos']

@app.route('/')
def home():
    return render_template('todo_form.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_item():
    itemName = request.form['itemName']
    itemDescription = request.form['itemDescription']
    todo = {
        'itemName': itemName,
        'itemDescription': itemDescription
    }
    todo_collection.insert_one(todo)
    return "✅ Item submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True, port=5004)
