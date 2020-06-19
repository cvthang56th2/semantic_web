from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html', content=['thang', 'thang cao'])

@app.route("/search")
def search():
  keyword = request.args.get('keyword')
  return render_template('search.html', keyword = keyword)

if __name__ == "__main__":
  app.run()