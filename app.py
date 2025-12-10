from flask import Flask, send_from_directory

app = Flask(__name__)

# Rute for nettsiden
@app.route("/")
def index():
    return send_from_directory("/nettside.html")

# Ruter for andre sider
@app.route("/<path:filename>")
def send_file(filename):
    return send_from_directory("", filename)

# Start webserver
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
