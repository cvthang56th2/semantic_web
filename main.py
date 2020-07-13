# Load Ontology
from owlready2 import *
onto = get_ontology("./qlgiapha.owl").load()

# Region web
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def search():
  searchResult = []
  keyword = request.args.get('keyword')
  if keyword is None:
    keyword = ''
    for item in onto.search(iri = "*"):
      searchResult.append(item.name)
  else:
    for item in onto.search(iri = "*" + keyword + "*"):
      searchResult.append(item.name)
  return render_template('home.html', keyword = keyword, searchResult = searchResult)

if __name__ == "__main__":
  app.run()