from flask import Flask,request,jsonify
import _plotly_utils
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    return  jsonify({
        'loactions':util.get_location_names()
    })
    responsible.headers.add('Access-Control-Allow-origin', ' +')

    return response




if __name__ =="__main__":
    print("Starting Python Flask server for the home price prediction...")
    app.run()