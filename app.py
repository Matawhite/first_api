from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#home page
@app.route("/")
def home():
	return render_template("search.html")

#the actual function
@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method == "POST":
		url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
		response_dict = requests.get(url).json()
		return render_template("results.html", api_data=response_dict)
	else:
		return render_template("search.html")

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found. Are you lost?", 404

app.run(debug=True)