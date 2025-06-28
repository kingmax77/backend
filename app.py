from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    loan_amount = data.get('amount')
    interest = data.get('interest')
    years = data.get('years')

    if not all([loan_amount, interest, years]):
        return jsonify({'error': 'Missing fields'}), 400

    monthly_rate = interest / 100 / 12
    months = years * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)

    return jsonify({'monthly_payment': round(monthly_payment, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
