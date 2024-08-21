#!/usr/bin/python3


import pickle
from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
   with open('pickled.pk', 'rb') as f:
      results = pickle.load(f)
   print(results)

   return render_template('sports.html',
   sport_dict=results)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8012, debug=True)
