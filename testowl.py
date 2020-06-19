from owlready2 import *
onto = get_ontology("./qlsv.owl").load()
text = ""
searchResult = onto.search(iri = "*")
for x in searchResult:
  text += " " + x.name

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return text

if __name__ == "__main__":
  app.run()