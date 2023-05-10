import random
from ressource import Ressource

class Map:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.generate_resources()

    def generate_resources(self):
        resource_types = ["wood", "gold", "stone", "food"]
        num_resources = random.randint(10, 20)

        for _ in range(num_resources):
            x, y = self.get_random_empty_position()
            resource_type = random.choice(resource_types)
            resource_amount = random.randint(5, 20)
            resource = Ressource(resource_type, resource_amount)
            self.place_entity(resource, x, y)

    def get_random_empty_position(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.grid[y][x] is None:
                return x, y

    def place_entity(self, entity, x, y):
        self.grid[y][x] = entity

    def move_entity(self, entity, new_x, new_y):
        x, y = entity.x, entity.y
        self.grid[y][x] = None
        self.grid[new_y][new_x] = entity
        entity.x, entity.y = new_x, new_y

    def remove_entity(self, entity):
        x, y = entity.x, entity.y
        self.grid[y][x] = None
    
    
    def is_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
    
    def all_resources_collected(self):
        for row in self.grid:
            for cell in row:
                if isinstance(cell, Ressource) and cell.amount > 0:
                    return False
        return True
