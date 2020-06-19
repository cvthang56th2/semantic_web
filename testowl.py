# Load Ontology
from owlready2 import *
onto = get_ontology("./qlsv.owl").load()

# Region web
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html', content=['thang', 'thang cao'])

@app.route("/search")
def search():
  keyword = request.args.get('keyword')
  if keyword is None:
    keyword = ''
  searchResult = []
  monHoc = onto.search_one(Ten = "*"+ keyword +"*")
  if monHoc:
    for x in onto.search(Hoc = monHoc):
      searchResult.append(x.name)

  return render_template('search.html', keyword = keyword, searchResult = searchResult)

if __name__ == "__main__":
  app.run()