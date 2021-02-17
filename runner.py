import requests
import sys

if len(sys.argv) <= 1:
    print("Insira pelo menos uma palavra para buscarmos por um titulo!")
else:
    queryString = ""
    sys.argv.pop(0)
    for args in sys.argv:
        queryString += args
        queryString += " "

    response = requests.get('http://172.17.0.2:8000/books?key=' + queryString)
    responseJSON = response.json()

    numberOfResults = responseJSON["NumFound"]
    books = responseJSON["Docs"]

    print("Você pesquisou por: " + queryString)
    print("Encontramos " + str(numberOfResults) + " titulos com essa pesquisa.\nAqui estão os principais:")

    for i in range(len(books)):
        print(str(i+1) + ": " + books[i]["Title"])
