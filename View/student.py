from falcon import HTTP_200, HTTP_401
import json
from Model.tables import Student, Predmet, Prijava
from Model.dbconn import session


class StudentView:
    def on_get(self, req, resp):
        resp.status = HTTP_200  # This is the default status
        dump = {}
        for std in session.query(Student).all():
            dump[std.id] = {
                'first_name': std.first_name,
                'last_name': std.last_name,
            }

        resp.body = json.dumps(dump)

    def on_post(self, req, resp):
        data = req.stream.read()
        data = json.loads(data.decode())
        novi = Student(first_name=data['first_name'], last_name=data['last_name'])
        session.add(novi)
        session.commit()
        resp.status = HTTP_200


class StudentDetailsView:
    def on_get(self, req, resp, sid):
        student = session.query(Student).filter_by(id=sid).first()  # Student.vratiStudenta(sid)
        if student:
            resp.status = HTTP_200
            # resp.body = json.dumps({'id': student.id, 'first_name': student.first_name,
            # 'last_name': student.last_name})
            dump = {
                'student': {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name}
            }
            for p in student.predmeti:
                # ocena = session.query(Prijava).filter_by(student_id=student.id, predmet_id=p.id). \
                #     first().ocena
                prijava = session.query(Prijava).filter_by(student_id=student.id, predmet_id=p.id).order_by(
                    Prijava.id.desc()).first()
                dump[p.id] = {
                    'course_name': p.naziv,
                    'year': p.godina,
                    'grade': prijava.ocena
                }
            resp.body = json.dumps(dump)
        else:
            resp.status = HTTP_401
