from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') # this is the home page route
def index():
  #code
  user_logged_in = True
  return render_template('basic.html',user_logged_in = user_logged_in)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81,debug=True)
