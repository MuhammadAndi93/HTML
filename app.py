from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def kalkulasi(a, b, op):
    a = float(a)
    b = float(b)
    if op == 'add':
        return a + b
    elif op == 'subtract':
        return a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        if b == 0:
            return "Error: Tidak bisa dibagi 0"
        return a / b
    else:
        return "Operasi tidak dikenal"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hitung", methods=["POST"])
def hitung():
    data = request.json
    num1 = data.get("num1")
    num2 = data.get("num2")
    op = data.get("operation")
    try:
        result = kalkulasi(num1, num2, op)
    except Exception as e:
        result = f"Error: {e}"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
