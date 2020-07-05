from flask import Flask, redirect, url_for, render_template, request, flash 

app = Flask(__name__)
app.secret_key = "hello"


#home page
@app.route("/")
def home():
    return render_template("index.html")

#results page 
@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST": 
        data = request.form["data"]
        sentiment = classify(data)
        return render_template("results.html")
    else:
        return render_template("index.html")

# handle the classification
def classify(data):
    ...

#run the app 
if __name__ == "__main__":
    app.run(debug=True)
