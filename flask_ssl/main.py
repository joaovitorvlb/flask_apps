from flask import Flask, jsonify
from OpenSSL import SSL

app = Flask(__name__)
context = SSL.Context(SSL.TLSv1_1_METHOD)
context.use_privatekey_file("server.key")
context.use_certificate_file("server.crt")


@app.route("/")
def index():
    return "Flask is running!"


@app.route("/data")
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == "__main__":
    app.run(ssl_context=context)
