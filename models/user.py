from models.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    user_name = Column(String(30))
    language_code = Column(String(5))

    def __repr__(self):
        return f"User(id={self.id!r}, first_name={self.first_name!r}, user_name={self.user_name!r} language_code={self.language_code!r})"