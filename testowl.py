from owlready2 import *
onto = get_ontology("./qlsv.owl").load()
text = ""
searchResult = onto.search(Hoc = onto.search_one(Ten = "Sematic Web"))
print(searchResult)
for x in searchResult:
  text += " " + x.name

print(text)