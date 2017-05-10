from falcon import HTTP_200, HTTP_401
import json
from Model.tables import Prijava, Predmet, Student
from Model.dbconn import session


class PrijavaView:
    def on_get(self, req, resp):
        resp.status = HTTP_200  # This is the default status
        dump = {}
        for prijava in session.query(Prijava).all():
            dump[prijava.id] = {
                'student': {
                    'student_id': prijava.student_id,
                    'first_name': session.query(Student).filter_by(id=prijava.student_id).first().first_name,
                    'last_name': session.query(Student).filter_by(id=prijava.student_id).first().last_name
                },
                'course': {
                    'course_id': prijava.predmet_id,
                    'course_name': session.query(Predmet).filter_by(id=prijava.predmet_id).first().naziv,
                    'year': session.query(Predmet).filter_by(id=prijava.predmet_id).first().godina
                },
                'grade': prijava.ocena
            }

        resp.body = json.dumps(dump)

        # def on_post(self, req, resp):
        #     data = req.stream.read()
        #     data = json.loads(data.decode())
        #     novi = Student(first_name=data['first_name'], last_name=data['last_name'])
        #     session.add(novi)
        #     session.commit()
        #     resp.status = HTTP_200
