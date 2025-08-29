from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Hsharks Academy")

@app.route("/about")
def about():
    return render_template("about.html", title="About Hsharks")

@app.route("/sports")
def sports():
    return render_template("sports.html", title="Sports at Hsharks")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Hsharks")

if __name__ == "__main__":
    app.run(debug=True)