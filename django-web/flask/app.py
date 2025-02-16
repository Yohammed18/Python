from flask import Flask, request, render_template, Response

app = Flask(__name__)

stores = [
    {
        "name": "Walgreens",
        "items": [
            {
                "name":"chair",
                "price": 15.99
            },
            {
                "name":"soap",
                "price": 5.99
            },
        ]
    }
]

@app.get('/')
def hello():
    return 'Welcome to the store app.'

@app.get("/stores")
def store_list():
    return stores

@app.post('/store')
def create_store():
    request_data = request.get_json()
    print(request_data)
    new_store = {
        "name": request_data["name"], 
        "items":request_data["items"]
    }
    
    stores.append(new_store)
    return new_store, 201


@app.post("/<string:name>/item")
def create_items(name):
    data = request.get_json()

    for store in stores:
        if store['name'] == name:
            store["items"].append(data)
            return stores, 201
    
    return {"message": "Store not found"}, 404


@app.get("/home")
def home_page():
    return render_template("index.html")


