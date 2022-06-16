from flask import Flask, redirect, url_for, render_template, request
import pyodbc as pyo
import pandas as pd

app = Flask(__name__)

cnn_azure = (
    r"Driver={SQL Server};Server=sample137"
    ".database.windows.net;Database=sampledb;UID=pavanchow;PWD=Khiladi@786"
)

cnn = pyo.connect(cnn_azure)

sql = "Select * From dbo.people"
pf = pd.read_sql(sql, cnn)
cnn.close()

print(pf.head(10))

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")    

@app.route("/Queries")
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
	return f"Hello {name}!"

@app.route("/admin")
def admin():
	return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"

if __name__ == "__main__":
	app.run()