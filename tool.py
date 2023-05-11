class Tool:
    def __init__(self, level=1):
        self.level = level

    def upgrade(self):
        self.level += 1


    def __str__(self):
        return f"{self.__class__.__name__} (niveau {self.level})"
