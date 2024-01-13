import streamlit as st

st.write('Hello world!')
pip install flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Public Health Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        header {
            text-align: center;
            padding: 20px;
            background-color: #4CAF50;
            color: white;
        }
        section {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Public Health Website</h1>
    </header>
    <section>
        <h2>Welcome to our Public Health Portal</h2>
        <p>This website provides information about public health, diseases, and prevention measures.</p>
    </section>
    <section>
        <h2>Contact Us</h2>
        <p>Email: info@publichealth.com</p>
        <p>Phone: 123-456-7890</p>
    </section>
</body>
</html>
python app.py

