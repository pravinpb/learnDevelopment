from flask import Flask, render_template, url_for, request, jsonify
from flask.views import MethodView
import psycopg2

# testlist = {10,20,30,40,50,60,70,80,90,100}

app = Flask(__name__)

# @app.route("/")
# def index():
#     return testlist

# @app.route("/about")
# def about():
#     return "About Page"

# @app.route("/career/<career_type>")
# def career(career_type):
#     return career_type

# @app.route("/contact")
# def contact():
#     return "Contact Page"


# @app.route("/test", methods=["GET", "POST", "PUT","DELETE"])
# def test():

#     products = [{"name":"product1", "price":100}, {"name":"product2", "price":200}, {"name":"product3", "price":300}]

#     if request.method == "GET":
#         return jsonify({'response': products})
#     elif request.method == "POST":
#         rqst_json = request.json
#         name = rqst_json['name']
#         rollnum = rqst_json['rollnum']
#         return jsonify({'response':"Hi "+name, 'rollnum':rollnum})
#     elif request.method == "PUT":
#         rqst_json = request.json
#         name = rqst_json['name']
#         rollnum = rqst_json['rollnum']
#         return jsonify({'response':name, 'rollnum':rollnum})
#     elif request.method == "DELETE":
#         for product in products:
#             if product['name'] == "product1":
#                 products.remove(product)
#         return jsonify({'response':products})



class learn(MethodView):
    def __init__(self):
        self.products = [{"name": "product1", "price": 100}, {"name": "product2", "price": 200}, {"name": "product3", "price": 300}]

    def get(self):
        return jsonify({'response': self.products})

    def post(self):
        rqst_json = request.json
        name = rqst_json['name']
        rollnum = rqst_json['rollnum']
        return jsonify({'response': "Hi " + name, 'rollnum': rollnum})

    def put(self):
        rqst_json = request.json
        name = rqst_json['name']
        rollnum = rqst_json['rollnum']
        return jsonify({'response': name, 'rollnum': rollnum})

    def delete(self):
        for product in self.products:
            if product['name'] == "product1":
                self.products.remove(product)
        return jsonify({'response': self.products})


product_view = learn.as_view('product_api')
app.add_url_rule('/demo', view_func=product_view, methods=['GET', 'POST', 'PUT', 'DELETE'])


# product_api = learn()
# @app.route("/demo", methods=["GET", "POST", "PUT", "DELETE"])
# def demo():
#     if request.method == "GET":
#         return product_api.get()
#     elif request.method == "POST":
#         return product_api.post()
#     elif request.method == "PUT":
#         return product_api.put()
#     elif request.method == "DELETE":
#         return product_api.delete()


if __name__ == "__main__":
    app.run(debug=True)


