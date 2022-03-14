from flask import Flask, make_response, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
  resp = make_response(render_template('index.html'))
  # resp.set_cookie('path1cookie', value='1', path='/path1')
  # resp.set_cookie('setfromserver-not-secure', value='1')
  # resp.set_cookie('setfromserver-secure', value='1', secure=True)
  # resp.set_cookie('setfromserver-httponly', value='1', httponly=True)
  # resp.set_cookie('__Secure-foobar', value='1', secure=True)
  # resp.set_cookie('setfromserver-samesite-strict', value='1', samesite='Strict')
  return resp


@app.route('/path2')
def path2():
  print(request.cookies)
  resp = make_response(render_template('path1.html'))
  resp.set_cookie('path2cookie', value='2', path='/path2')
  return resp


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port='9000', debug=True)
