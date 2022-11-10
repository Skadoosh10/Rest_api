from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd


app = Flask(__name__)
api = Api(app)

class Books(Resource):
    def get(self):
        data = pd.read_csv('books.csv')
        data = data.to_dict('records')
        
        return {'data' : data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Title')
        parser.add_argument('Author')
     
        args = parser.parse_args()

        data = pd.read_csv('books.csv')

        new_data = pd.DataFrame({
            'Title'      : [args['Title']],
            'Author'      : [args['Author']],
           
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('books.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201
    
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Title', required=True)
        parser.add_argument('Author', required=True)
    
        args = parser.parse_args()

        data = pd.read_csv('books.csv')

        data = data[data['Title'] != args['Title']]

        data.to_csv('books.csv', index=False)
        return {'message' : 'Record deleted successfully.'}, 200



api.add_resource(Books, "/books")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
    