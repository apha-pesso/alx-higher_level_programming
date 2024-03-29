#!/usr/bin/python3
"""Fetch all states using sqlalchemy"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    us = argv[1]
    pw = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(us, pw, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    all_state = session.query(State).all()

    for state in all_state:
        print("{}: {}".format(state.id, state.name))

    session.close()
