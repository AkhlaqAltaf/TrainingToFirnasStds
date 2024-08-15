from flask import Flask, render_template
# from flask import Flask 

app = Flask(__name__)

@app.route('/login')
def login():
    return "hi"

if __name__ == '__main__':
    app.run()