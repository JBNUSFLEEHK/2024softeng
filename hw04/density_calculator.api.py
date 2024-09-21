from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    html_str = """
    <!DOCTYPE html>
    <html lang="kr">
    <head>
    <meta charset="UTF-8">
    <title>밀도 계산기</title>
    </head>
    <body>
    <form method="GET" action="/density">
    <h2>밀도 계산하기</h2>
    <label>질량 (Kg):
    <input type="text" name="mass">
    </label><br><br>
    <label>부피 (m**3):
    <input type="text" name="volume">
    </label><br><br>
    <button type="submit">계산</button>
    </form>
    </body>
    </html>
    """
    return html_str


@app.route("/density/")
def density_calculator():
    mass = float(request.args.get("mass"))
    volume = float(request.args.get("volume"))
    density = mass / volume
    html_str = f"""
    <strong>밀도 계산 결과<br>
    밀도: <strong>{density:.2f}<strong> kg/m³
    """
    return html_str

if __name__ == "__main__":
    app.run(debug=True)
