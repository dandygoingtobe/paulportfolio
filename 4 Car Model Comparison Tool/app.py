from flask import Flask, render_template, request

app = Flask(__name__)


car_data = {
    "S Class": {"engine": "V8", "horsepower": 503, "price": "$120,000"},
    "Model 3": {"engine": "Electric", "horsepower": 283, "price": "$40,000"},
    "Mustang": {"engine": "V6", "horsepower": 450, "price": "$55,000"}
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_cars = []
    if request.method == "POST":
        selected_cars = request.form.getlist("car_models")
    return render_template("index.html", car_data=car_data, selected_cars=selected_cars)

if __name__ == "__main__":
    app.run(debug=True)
