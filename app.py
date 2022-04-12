from flask import Flask, request, render_template
import pickle

vector = pickle.load(open("vectorizer.pkl",'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__)
  
@app.route('/')
def methods():
   return render_template ("interface.html")
 
@app.route('/prediction', methods=['GET','POST'])
def prediction():
   
   if request.method==("POST"):
      news =str(request.form['news'])

      print(news)
      prediction = model.prediction(vector.transform([news]))[0]
      print(prediction)

      return render_template(prediction_text ="News Headline is-> {}".format(prediction))
      
   else:
      request.methods=("GET")
      return render_template("prediction.html")



if __name__=='__main__':
   app.run(debug=True) 