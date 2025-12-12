class Subject:
    def __init__(self, id, title):
        self._id = id
        self._title = title

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title