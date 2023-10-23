from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_response', methods=['GET'])
def get_location_names():
    response = jsonify({
        'received': "true"  })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print("response sent")   
    return response



@app.route('/predict_quality', methods=['POST'])
def predict_home_quality():
    print("hello request received")
    ph = float(request.form['ph'])
    hardness = float(request.form['hardness'])
    solids = float(request.form['solids'])
    chloramines = float(request.form['chloramines'])
    sulfate = float(request.form['sulfate'])
    conductivity = float(request.form['conductivity'])
    organic_carbon = float(request.form['organic_carbon'])
    trihalomethanes = float(request.form['trihalomethanes'])
    turbidity = float(request.form['turbidity'])

    print("hello request received")
    # print(month)
    
    ans = util.get_estimated_quality(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity)
    ans = int(ans)
    response = jsonify({
       'estimated_quality': ans
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response






if __name__ == "__main__":
    print("Starting Python Flask Server For quality quality Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True,port=5000)