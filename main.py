from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

 
RESULT = {
	"probabilities": [
		{
			"id": "1111111",
			"probability": 0.75
		},
		{
			"id": "2222222",
			"probability": 0.03
		},
		{
			"id": "3333333",
			"probability": 0.013
		}
	]
}

class Predict(Resource):
    def get(self):
        return RESULT

    def post(self):
        return RESULT

api.add_resource(Predict, '/voice/predict', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=10002)
