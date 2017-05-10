import falcon
from wsgiref import simple_server
# from code.view import student as std
# import code.view.home as home
from View.student import StudentView, StudentDetailsView
from View.predmet import PredmetView, PredmetDetailsView
from View.prijava import PrijavaView
from Model.dbconn import Base, engine


def start():
    app = falcon.API()

    # Resources are represented by long-lived class instances
    # things will handle all requests to the '/things' URL path

    app.add_route('/student/', StudentView())
    app.add_route('/student/{sid}', StudentDetailsView())
    app.add_route('/predmet', PredmetView())
    app.add_route('/predmet/{pid}', PredmetDetailsView())
    app.add_route('/prijave', PrijavaView())

    httpd = simple_server.make_server('127.0.0.1', 8080, app)
    print('>>>Local server running on port 8080<<<')
    httpd.serve_forever()


def update_db():
    Base.metadata.create_all(engine)
