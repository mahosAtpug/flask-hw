from flask import Flask , jsonify , request

app = Flask(__name__)

tasks = [{
            "id": 1,
            "name" : u"Soham",
            "contact" : u"9849494859",
            "done" : False
        },
        {
            "id": 2,
            "name": u"Raj",
            "contact" : u"4893849304",
            "done" : False
        }

    ]

@app.route("/get-data")
def get_tasks():
    return jsonify({
        "data" : tasks
    })

@app.route("/add-data" , methods = ["POST"])
def add_tasks():
    if not request.json:
        return jsonify({
            "status" : "ERROR",
            "message": "Please Provide Data"

        }, 400)

    task = {"id":tasks[-1]["id"]+1,
            "name" : request.json["name"],
            "contact" : request.json.get("contact" , ""),
            "done" : False}

    tasks.append(task)
    return jsonify({
        "status" : "Success",
        "message": "Task added Successfully!!!"
    })

if(__name__ == "__main__"):
    app.run(debug = True)

