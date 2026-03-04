from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (hackathon demo purpose only)
users = {}

# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email in users and users[email] == password:
            return redirect(url_for("home"))
        else:
            return "Invalid Credentials ❌"

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users[email] = password
        return redirect(url_for("login"))

    return render_template("login.html")


# --------------- RUN APP ---------------- #

if __name__ == "__main__":
    app.run(debug=True)