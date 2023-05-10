from map import Map
from unit import Worker, Lumberjack, Miner, Peasant
from building import ProductionBuilding, ToolCreationBuilding
from ui import UI
from ressource import Ressource

class Game:
    def __init__(self, width, height, starting_resources):
        self.map = Map(width, height)
        self.units = []
        self.buildings = []
        self.resources = starting_resources
        self.turn = 1

    def play_turn(self):
        print("Tour " + str(self.turn) + ":" + "\n")
        self.spawn_units_from_buildings()
        self.move_and_work_units()
        self.feed_units()
        self.update_building_production()

        UI.clear()
        UI.print_map(self)
        UI.print_resources(self)

        self.turn += 1

    def move_and_work_units(self):
        for unit in self.units:
            if unit.can_work():
                unit.work()
            else:
                unit.move_to_closest_resource()

    def feed_units(self):
        units_to_remove = []
        for unit in self.units:
            if self.resources["food"] >= unit.get_food_cost():
                self.resources["food"] -= unit.get_food_cost()
                print(f"l'unité {unit} a mangé {unit.get_food_cost()} nourriture")
            else:
                unit.starve()
                if unit.should_be_removed():
                    units_to_remove.append(unit)

        for unit in units_to_remove:
            self.units.remove(unit)
            self.map.remove_entity(unit)

    def spawn_units_from_buildings(self):
        for building in self.buildings:
            if isinstance(building, ProductionBuilding) and building.can_build():
                building.build()

    def update_building_production(self):
        for building in self.buildings:
            if isinstance(building, ToolCreationBuilding) and building.can_build():
                building.build()

    def create_building(self, building_class):
        building = building_class(self)
        if building.build():
            self.buildings.append(building)

    def destroy_building(self, building):
        if building in self.buildings:
            self.buildings.remove(building)

    def create_unit(self, unit_class):
        x, y = self.map.get_random_empty_position()
        unit = unit_class(self, x, y)
        if unit.can_be_created():
            self.map.place_entity(unit, x, y)
            self.units.append(unit)

    def destroy_unit(self, unit):
        if unit in self.units:
            self.units.remove(unit)
            self.map.remove_entity(unit)

    def is_game_over(self):
        #print("all starving: " + str(all(unit.starvation_turns >= 5 for unit in self.units)))
        #print("all resources collected: " + str(self.map.all_resources_collected()))
        #print("barre de nourriture : " + str(self.resources["food"]))
        return (all(unit.starvation_turns >= 5 for unit in self.units) or self.map.all_resources_collected()) and self.turn > 5
