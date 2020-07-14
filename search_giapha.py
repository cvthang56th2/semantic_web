# Load Ontology
from owlready2 import *
onto = get_ontology("./qlgiapha.owl").load()

print("***************************************")
# print(list(onto.classes()))
print(list(onto.Father.instances()))
print("***************************************")

# Region web
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def search():
  # Get Queries
  keyword = request.args.get('keyword')
  searchClass = request.args.get('searchClass')
  searchDataProp = request.args.get('searchDataProp')
  searchObjProp = request.args.get('searchObjProp')
  sortType = request.args.get('sortType')
  
  # Get dropdowns
  ontoClasses = []
  ontoDataProps = []
  ontoObjProps = []
  for item in list(onto.classes()):
    ontoClasses.append(item.name)
  for item in list(onto.data_properties()):
    ontoDataProps.append(item.name)
  for item in list(onto.object_properties()):
    ontoObjProps.append(item.name)

  # Doing search
  searchResult = []
  # Todo: init data for search
  print("***************************************")
  print("***************************************")
  print(list(getattr(onto, searchClass).instances()))
  print("***************************************")
  print("***************************************")

  if keyword is None:
    keyword = ''
    for item in onto.search(iri = "*"):
      searchResult.append(item.name)
  else:
    for item in onto.search(iri = "*"+ keyword +"*"):
      searchResult.append(item.name)

  return render_template('search_giapha.html',
    keyword = keyword,
    searchResult = searchResult,
    searchClass = searchClass,
    searchDataProp = searchDataProp,
    searchObjProp = searchObjProp,
    sortType = sortType,
    ontoClasses = ontoClasses,
    ontoDataProps = ontoDataProps,
    ontoObjProps = ontoObjProps
  )

if __name__ == "__main__":
  app.run()