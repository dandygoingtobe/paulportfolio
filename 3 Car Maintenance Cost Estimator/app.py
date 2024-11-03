from flask import Flask, render_template, request

app = Flask(__name__)


class MaintenanceCostEstimator:
    def __init__(self):
        self.costs = {
            "oil_change": 40,
            "tire_rotation": 25,
            "brake_inspection": 50,
            "transmission_service": 150
        }

    def calculate_cost(self, maintenance_type):
        return self.costs.get(maintenance_type, 0)

@app.route("/", methods=["GET", "POST"])
def index():
    cost_info = None
    if request.method == "POST":
        mileage = int(request.form["mileage"])
        maintenance_type = request.form["maintenance_type"]
        estimator = MaintenanceCostEstimator()
        cost_info = estimator.calculate_cost(maintenance_type)

    return render_template("index.html", cost_info=cost_info)

if __name__ == "__main__":
    app.run(debug=True)
