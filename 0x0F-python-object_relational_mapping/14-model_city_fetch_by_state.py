#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

us = argv[1]
pw = argv[2]
db = argv[3]

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(us, pw, db), pool_pre_ping=True)

Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()

#all_state = session.query(State).join(City).all()
for state, city in session.query(State,City).filter(State.id == City.state_id).order_by(City.id).all():
    print("{}: ({}) {}".format(state.name, city.id, city.name))

#for state in all_state:
 #   print(state)

    #print("{}: {}".format(state.id, state.name))

session.close()
