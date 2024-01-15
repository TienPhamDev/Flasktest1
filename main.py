from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') # this is the home page route
def index():
  #code
  return render_template('basic.html')


@app.route('/puppy/<name>')
def puppy(name):
  return render_template('puppy.html', name=name)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81,debug=True)
