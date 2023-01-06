from repository.repository import Repostiory


class Service:
    def __init__(self, repository: Repostiory) -> None:
        self.repository = repository
