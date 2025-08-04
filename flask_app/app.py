from flask import Flask, request, render_template
import pymongo

app = Flask(__name__)

# 🟢 MongoDB Setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]  # Database
collection = db["todos"]  # Collection

# 🟠 Route to display the form (linked to HTML)
@app.route("/")
def home():
    return render_template("todo_form.html")

# 🔵 Route to handle form submission
@app.route("/submittodoitem", methods=["POST"])
def submit_item():
    itemName = request.form["itemName"]
    itemDescription = request.form["itemDescription"]

    # Create a dictionary and insert into MongoDB
    todo_item = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    collection.insert_one(todo_item)

    return f"✅ Item submitted successfully: {itemName}"

# 🔁 Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5004)
