# Load Ontology
from owlready2 import *
onto = get_ontology("./qlsv.owl").load()

# Region web
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def search():
  searchResult = []
  keyword = request.args.get('keyword')
  searchBy = request.args.get('searchBy')
  sortType = request.args.get('sortType')
  if keyword is None:
    keyword = ''
    for item in onto.search(iri = "*"):
      searchResult.append(item.name)
  else:
    monHoc = onto.search_one(Ten = "*"+ keyword +"*")
    if monHoc:
      for item in onto.search(Hoc = monHoc):
        searchResult.append(item.name)

  return render_template('index.html', keyword = keyword, searchResult = searchResult, searchBy = searchBy, sortType = sortType)

if __name__ == "__main__":
  app.run()