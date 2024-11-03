from flask import Flask, render_template, request

app = Flask(__name__)




class MaintenanceScheduler:
    def __init__(self):
        self.schedule = {
            "engine": {
                "interval": 5000,
                "description": "Change oil and inspect engine components."
            },
            "brakes": {
                "interval": 10000,
                "description": "Check brake pads, rotors, and fluid levels."
            },
            "suspension": {
                "interval": 15000,
                "description": "Inspect shocks, struts, and suspension components."
            },
            "transmission": {
                "interval": 30000,
                "description": "Replace transmission fluid and inspect transmission parts."
            },
            "coolingSystem": {
                "interval": 25000,
                "description": "Flush and replace coolant, check hoses and radiator."
            }
        }

    def get_schedule(self, mileage, part):
        part_schedule = self.schedule.get(part, {})
        if part_schedule:
            due_mileage = ((mileage // part_schedule["interval"]) + 1) * part_schedule["interval"]
            return {
                "message": f"For the {part.capitalize()}, next maintenance is at {due_mileage} miles. Task: {part_schedule['description']}"
            }
        else:
            return {"message": "Invalid part selected."}

@app.route("/", methods=["GET", "POST"])
def index():
    schedule_info = None
    if request.method == "POST":
        model = request.form["model"]
        mileage = int(request.form["mileage"])
        part = request.form["part"]
        scheduler = MaintenanceScheduler()
        schedule_info = scheduler.get_schedule(mileage, part)

    return render_template("index.html", schedule_info=schedule_info)

if __name__ == "__main__":
    app.run(debug=True)
