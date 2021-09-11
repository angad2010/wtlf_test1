from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Search(Resource):
    def get(self):
       
        parser = reqparse.RequestParser()
        parser.add_argument('face')
        args = parser.parse_args()
        
        
        data = pd.read_csv('Export_Log_Clean.csv')
        
        query = args['face']
        
        
        
        if query is None:
            
            #
            data = data.to_dict('records')
            
            return {'Here is data for all WTLF Avatars' : data}, 200
            
        #Else
        result = data[data['Avatar Name'] == query]
            
        x= result.to_dict('records')
        
        return x, 200
           
                   
            
        
        


    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('Avatar Name', required=True)
    #     parser.add_argument('Head and Headwear', required=True)
    #     parser.add_argument('Eyewear', required=True)
    #     args = parser.parse_args()

    #     data = pd.read_csv(r"C:\Users\angad\OneDrive\Desktop\PF\sample\Rename\Export_Log_Clean.csv")

    #     new_data = pd.DataFrame({
    #         'Avatar Name'      : [args['Avatar Name']],
    #         'Head and Headwear' : [args['Head and Headwear']],
    #         'Eyewear' : [args['Eyewear']]
    #     })

    #     data = data.append(new_data, ignore_index = True)
    #     data.to_csv(r"C:\Users\angad\OneDrive\Desktop\PF\sample\Rename\Export_Log_Clean.csv", index=False)
    #     return {'data' : new_data.to_dict('records')}, 201

    # def delete(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('Avatar Name', required=True)
    #     args = parser.parse_args()

    #     data = pd.read_csv(r"C:\Users\angad\OneDrive\Desktop\PF\sample\Rename\Export_Log_Clean.csv")

    #     data = data[data['Avatar Name'] != args['Avatar Name']]

    #     data.to_csv(r"C:\Users\angad\OneDrive\Desktop\PF\sample\Rename\Export_Log_Clean.csv", index=False)
    #     return {'message' : 'Record deleted successfully.'}, 200


        

# Add URL endpoints
api.add_resource(Search, '/archive')


if __name__ == '__main__':
    app.run()