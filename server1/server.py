from livereload import Server

from main import app


if __name__ == '__main__':
  app.debug = True
  server = Server(app.wsgi_app)
  server.watch('templates/*.html')
  server.serve(port=8000, host='0.0.0.0')