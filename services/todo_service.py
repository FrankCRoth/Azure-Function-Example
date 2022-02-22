import connexion
from flask import render_template

app = connexion.App(__name__, specification_dir="./")

app.add_api("openapi.yml")

# For home page

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)