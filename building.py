class Building:
    def __init__(self, game, cost):
        self.game = game
        self.cost = cost

    def build(self):
        if self.can_build():
            for resource_type, amount in self.cost.items():
                self.game.resources[resource_type] -= amount
            self.build_effect()
            return True
        return False

    def can_build(self):
        for resource_type, amount in self.cost.items():
            if self.game.resources[resource_type] < amount:
                return False
        return True

    def build_effect(self):
        raise NotImplementedError("Les bâtiments doivent implémenter la méthode build_effect().")

class ProductionBuilding(Building):
    def __init__(self, game, cost, unit_class):
        super().__init__(game, cost)
        self.unit_class = unit_class

    def build_effect(self):
        x, y = self.game.map.get_random_empty_position()
        unit = self.unit_class(self.game, x, y)
        self.game.map.place_entity(unit, x, y)
        self.game.units.append(unit)

class ToolCreationBuilding(Building):
    def __init__(self, game, cost, worker_class):
        super().__init__(game, cost)
        self.worker_class = worker_class

    def build_effect(self):
        for unit in self.game.units:
            if isinstance(unit, self.worker_class):
                unit.tool.upgrade()
