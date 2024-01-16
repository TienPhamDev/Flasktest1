from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') # this is the home page route
def index():
  #code
  return render_template('base.html')

@app.route('/home.html')
def home():
  return render_template('home.html')

@app.route('/puppy/<name>')
def puppy(name):
  return render_template('puppy.html', name=name)

if __name__ == '__main__':
  app.run(debug=True)
