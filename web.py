from flask import Flask, request
from script import convert

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result_text = ""
    if request.method == "POST":
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        amount = request.form["amount"]
        result = convert(from_currency, to_currency, amount)
        result_text = f"<p>{amount} {from_currency} = {result} {to_currency}</p>"
    return f"""
    <form method="POST">
        <input type="text" name="from_currency" placeholder="From currency">
        <input type="text" name="to_currency" placeholder="To currency">
        <input type="text" name="amount" placeholder="Amount">
        <button type="submit">Convert</button>
    </form>
    {result_text}
    """

if __name__ == "__main__":
    app.run(debug=True)