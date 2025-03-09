from flask import Flask, request, jsonify, render_template
from sympy import sympify, solve, diff, integrate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve_equation():
    data = request.json
    expression = data.get("expression")
    operation = data.get("operation")

    try:
        expr = sympify(expression)
        if operation == "solve":
            result = solve(expr)
        elif operation == "derivative":
            result = diff(expr)
        elif operation == "integrate":
            result = integrate(expr)
        else:
            return jsonify({"error": "Operation not supported"}), 400

        return jsonify({"result": str(result)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
