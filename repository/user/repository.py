from sqlalchemy import insert
from repository.repository import Repostiory
from models.user import User


class UserRepository(Repostiory):

    def insert(self, user: User):
        ins = insert(user)
        r = self.connection.execute(ins)
        print(r)
