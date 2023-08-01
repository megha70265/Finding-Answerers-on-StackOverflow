from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

# from flask import Flask,request,jsonify,render_template
# import numpy as np
# import pickle

# app = Flask(__name__)

# @app.route('/predict', methods=["POST"])
# def predict():
#     # if request.method=="POST":
#     #     number1=request.form.get("number1")
#     #     number2=request.form.get("number2")
#     #     number3=request.form.get("number3")
#     #     number4=request.form.get("number4")
#     #      #json_ = request.json
#     #     query_df = pd.DataFrame({number1,number2,number3,number4})
#     #     query = pd.get_dummies(query_df)

#     #     classifier = joblib.load('classifier.pkl')
#     #     prediction = classifier.predict(query)
#     #     #return jsonify({'prediction': list(prediction)})
#     #     #return prediction

#     return render_template("templates\index.html")
    

# if __name__ == '__main__':
#      app.run()