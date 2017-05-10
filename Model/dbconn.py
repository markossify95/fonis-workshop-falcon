from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
engine = create_engine('mysql+pymysql://root:root@localhost/falcon',
                       connect_args=dict(host='localhost', port=3306), echo=True)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

Base = declarative_base()

# work with sess
# myobject = MyObject('foo', 'bar')
# session.add(myobject)
# session.commit()
