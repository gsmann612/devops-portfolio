from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, welcome to DevOps Zero To Hero (Junoon  Batch 9)'

@app.route('/health')
def health():
    return 'Server is up and running'

if __name__ == "__main__":
    # host="0.0.0.0" allows external access
    # port=80 so Docker -p 80:80 works
    app.run(host="0.0.0.0", port=80)

