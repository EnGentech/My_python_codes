from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (
create_engine,
Column,
Integer,
ForeignKey,
String,
)

#creating base class for inheritance
url = 'mysql+mysqldb://root:admin8634@localhost/relationship'
Base = declarative_base()

engine = create_engine(url, echo=True)

"""creating classes """

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    nickname = Column(String(10), nullable=False)
    #we reference the class Post while creating the relationship
    posts = relationship('Post', backref='author')

    def __repr__(self):
        return "<User =={}== ({})".format(self.id, self.name)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return "<Post =={}== {} : {}".format(self.id, self.title, self.content)

#Base.metadata.create_all(engine)