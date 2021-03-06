from flask import Flask, jsonify, request
import utils

app = Flask(__name__)


@app.route("/categories", methods=["GET"])
def get_categories():
    rows = utils.get_all("select * from category")
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "name": r[1],
            "url": r[2]
        })

    return jsonify({"categories": data})


@app.route("/news", methods=["GET"])
def get_news():
    rows = utils.get_all("select * from news")
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "subject": r[1],
            "description": r[2],
            "image": r[3],
            "original_url": r[4]
        })

    return jsonify({"news": data})


@app.route("/news/<int:news_id>", methods=["GET"])
def get_news_by_id(news_id):
    r = utils.get_news_by_id(news_id)
    data = {
        "subject": r[0],
        "description": r[1],
        "image": r[2],
        "original_url": r[3],
        "category_name": r[4],
        "category_url": r[5]
    }

    return jsonify({"product": data})


@app.route("/news/<int:news_id>", methods=["POST"])
def insert_comments(news_id):
    if request.form.get("content"):
        utils.add_comment(news_id, request.form["content"])
        return jsonify({"status": 1, "message": "Success"})

    return jsonify({"status": 0, "message": "Fail"})


@app.route("/news/add", methods=["POST"])
def insert_news():
    pass


if __name__ == "__main__":
    app.run()
