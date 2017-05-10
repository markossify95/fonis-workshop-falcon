from falcon import HTTP_200, HTTP_401
import json
from Model.tables import Predmet
from Model.dbconn import session


class PredmetView:
    def on_get(self, req, resp):
        resp.status = HTTP_200  # This is the default status
        dump = {}
        i = 0
        for p in session.query(Predmet).all():
            dump[i] = {
                'year': p.godina,
                'course_name': p.naziv,
                'id': p.id
            }
            i += 1

        resp.body = json.dumps(dump)

    def on_post(self, req, resp):
        data = req.stream.read()
        data = json.loads(data.decode())
        novi = Predmet(godina=data['year'], naziv=data['course_name'])
        session.add(novi)
        session.commit()
        resp.status = HTTP_200


class PredmetDetailsView:
    def on_get(self, req, resp, pid):
        predmet = session.query(Predmet).filter_by(id=pid).first()  # Student.vratiStudenta(sid)
        if predmet:
            resp.status = HTTP_200
            resp.body = json.dumps({'year': predmet.godina, 'course_name': predmet.naziv})
        else:
            resp.status = HTTP_401

