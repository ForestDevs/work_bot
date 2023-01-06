from repository.user.repository import UserRepository
from models.user import User
from services.service import Service


class UserService(Service):

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository
        super().__init__(self.repository)

    def add(self, first_name, user_name, language_code):
        user = User()
        user.first_name = first_name
        user.user_name = user_name
        user.language_code = language_code
        self.repository.insert(user)
