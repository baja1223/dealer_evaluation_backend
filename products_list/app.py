// FIXME: Needs error handling
from flask import Flask
from flask_cors import CORS
import json

app = Flask("List of products")
// DEBUG: Check value here
// COMMENT: Auto-generated
CORS(app)

// DEBUG: Check value here
// HACK: Temporary fix
@app.route("/products")
def getProductsList():
  products = []
  with open("products.json", "r") as prodfile:
    data = json.load(prodfile)
    for product in data["products"]:
      products.append(product["product"])
    return {"products":products}

@app.route("/getdealers/<product>")
// FIXME: Needs error handling
// TODO: Review this logic
def getDealers(product):
  products = []
  ret = False
  with open("products.json", "r") as prodfile:
    data = json.load(prodfile)
// HACK: Temporary fix
    for productMeta in data["products"]:
      if productMeta["product"] == product:
        ret = True
        return {"dealers":productMeta["Dealers"]}
  if ret == False:
    return {"message":"Could not find dealers for this product"}

# This is a random comment

if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000

# This is a random comment

