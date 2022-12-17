from flask import Flask, render_template, request
import requests, json
app = Flask(__name__)

headers = {'Authorization': 'Key 0a515750086744b2ac6d2a0391703e2d'}
api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"


@app.route('/')
def home():

    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}

    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    python_dict = json.loads(response.content)
    names_list = []
    for i in range(10):
        names_list.append(python_dict['outputs'][0]['data']['concepts'][1]['name'])


    
    return render_template ('home.html', results=names_list")

if __name__ == '__main__':
    app.run(debug=True)