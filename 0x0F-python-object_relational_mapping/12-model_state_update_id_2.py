#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sys import argv
from model_state import Base, State

us = argv[1]
pw = argv[2]
db = argv[3]

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(us, pw, db), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()
ali = session.query(State).filter(State.id == 2).update({"name": "New Mexico"})
session.commit()
"""
if all_state:
    print(all_state.id)
else:
    pass
"""
session.close()
