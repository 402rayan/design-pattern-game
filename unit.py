import random
from map import Map
from tool import Tool

class Unit:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.tool = None

    def move(self, dx, dy):
        new_x, new_y = self.x + dx, self.y + dy
        if self.game.map.is_inside(new_x, new_y):
            self.game.map.move_entity(self, new_x, new_y)

    def work(self):
        raise NotImplementedError("Les unités doivent implémenter la méthode work().")

class Worker(Unit):
    def __init__(self, game, x, y, resource_type, tool_level=1):
        super().__init__(game, x, y)
        self.resource_type = resource_type
        self.tool = Tool(tool_level)
        self.experience = 0

    def work(self):
        resource = self.game.map.grid[self.y][self.x]
        if resource and resource.type == self.resource_type:
            amount_collected = min(self.tool.level, resource.amount)
            resource.amount -= amount_collected
            self.game.resources[self.resource_type] += amount_collected
            self.experience += amount_collected
            if resource.amount <= 0:
                self.game.map.grid[self.y][self.x] = None

class Lumberjack(Worker):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, "wood")

class Miner(Worker):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, random.choice(["gold", "stone"]))

class Peasant(Worker):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, "food")
