from flask import Flask, render_template
import socket
import os


app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def display_page():
    hostname = socket.gethostname()    
    ip = socket.gethostbyname(hostname)
    return render_template("index.html", IP=ip, HOST=hostname)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
