from flask import Flask, render_template, request
from spam import predict_spam

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    output = predict_spam(message)

    return render_template(
        'result.html',
        prediction=output["result"],
        quote=output["quote"],
        gif=output["gif"]
    )

if __name__ == "__main__":
    app.run(debug=True)


