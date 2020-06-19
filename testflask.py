from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html', content=['thang', 'thang cao'])

if __name__ == "__main__":
  app.run()