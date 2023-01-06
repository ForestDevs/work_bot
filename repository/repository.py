from utils.database.sqlalchemyConnect import connection


class Repostiory:

    def __init__(self) -> None:
        self.connection = connection
