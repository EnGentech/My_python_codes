from main import engine, session, User

del_session = session(bind=engine)

delme = del_session.query(User).filter(User.name == "Mfet").first()

del_session.delete(delme)
del_session.commit()