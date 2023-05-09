import random

class Map:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

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

    def is_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
    
    def all_resources_collected(self):
        for row in self.grid:
            for cell in row:
                if cell and cell.resource and cell.resource.amount > 0:
                    return False
        return True