import random
from map import Map
from tool import Tool
from ressource import Ressource
import logging

logging.basicConfig(filename='game.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log_movement(func):
    def wrapper(self, dx, dy):
        old_x, old_y = self.x, self.y
        func(self, dx, dy)
        new_x, new_y = self.x, self.y
        if (old_x, old_y) != (new_x, new_y):
            print(
                f"{self.__class__.__name__} moved from ({old_x}, {old_y}) to ({new_x}, {new_y})")
    return wrapper

class Unit:
    def __init__(self, game, x, y, speed, food_cost):
        self.game = game
        self.x = x
        self.y = y
        self.speed = speed
        self.food_cost = food_cost
        self.tool = Tool()
        self.starvation_turns = 0


    @log_movement
    def move(self, dx, dy):
        # Coût du mouvement en nourriture
        move_food_cost = 1

        # Vérifiez si l'unité a assez de nourriture pour se déplacer
        if self.game.resources['food'] < move_food_cost:
            logging.warning(
                f"{self.__class__.__name__} does not have enough food to move.")
            return

        new_x, new_y = self.x + dx, self.y + dy
        if self.game.map.is_inside(new_x, new_y):
            # Déduire le coût du mouvement de la nourriture totale
            self.game.resources['food'] -= move_food_cost
            self.game.map.move_entity(self, new_x, new_y)


    def work(self):
        raise NotImplementedError("Les unités doivent implémenter la méthode work().")


    def can_work(self):
        entity = self.game.map.grid[self.y][self.x]
        #print s'il peut work ou non 
        return isinstance(entity, Ressource) and entity.type == self.resource_type


    def move_to_closest_resource(self):
        min_distance = float('inf')
        closest_resource_position = None

        for y, row in enumerate(self.game.map.grid):
            for x, cell in enumerate(row):
                if isinstance(cell, Ressource) and cell.type == self.resource_type:
                    distance = abs(x - self.x) + abs(y - self.y)
                    if distance < min_distance:
                        min_distance = distance
                        closest_resource_position = (x, y)

        if closest_resource_position:
            dx, dy = closest_resource_position
            if dx > self.x:
                self.move(1, 0)
            elif dx < self.x:
                self.move(-1, 0)
            elif dy > self.y:
                self.move(0, 1)
            elif dy < self.y:
                self.move(0, -1)

    def get_food_cost(self):
        return self.food_cost

    def starve(self):
        self.starvation_turns += 1
        print(
            f"{self.__class__.__name__} is starving. Starvation turns: {self.starvation_turns}.")

    def should_be_removed(self):
        print(f"{self.__class__.__name__} died of starvation.")
        return self.starvation_turns >= 5
    

class Worker(Unit):
    def __init__(self, game, x, y, resource_type, speed, food_cost, tool_level=1):
        super().__init__(game, x, y, speed, food_cost)
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
            print(
                f"{self.__class__.__name__} collected {amount_collected} {self.resource_type}.")
            if resource.amount <= 0:
                print(
                    f"The resource at ({self.x}, {self.y}) has been depleted.")
                self.game.map.grid[self.y][self.x] = None

    def __str__(self):
        return f"{self.__class__.__name__} (outil : {self.tool})"

class Lumberjack(Worker):
    def __init__(self, game, x, y, speed=1, food_cost=1):
        super().__init__(game, x, y, "wood", speed, food_cost)

    def __str__(self):
        return super().__str__()

class Miner(Worker):
    def __init__(self, game, x, y, speed=1, food_cost=1):
        super().__init__(game, x, y, random.choice(["gold", "stone"]), speed, food_cost)

    def __str__(self):
        return super().__str__()

class Peasant(Worker):
    def __init__(self, game, x, y, speed=1, food_cost=1):
        super().__init__(game, x, y, "food", speed, food_cost)

    def __str__(self):
        return super().__str__()