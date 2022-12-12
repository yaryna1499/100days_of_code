import datetime

from flask import Flask, render_template
import requests
from post_class import Post
from datetime import datetime

todays_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
current_year = datetime.now().strftime("%Y")

data = requests.get("https://api.npoint.io/52ee0b74d3b5b001d4d0").json()

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    post_objects = []
    for p in data:
        post_object = Post(p["id"], p["body"], p["title"], p["subtitle"])
        post_objects.append(post_object)
    return render_template("index.html", post_objects=post_objects, todays_date=todays_date, current_year=current_year)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
