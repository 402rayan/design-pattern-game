import os 
from ressource import Ressource

class UI:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_map(game):
        for row in game.map.grid:
            for cell in row:
                if cell is None:
                    print(".", end=" ")
                elif isinstance(cell, Ressource):
                    print(cell.type[0].upper(), end=" ")
                else:
                    print(cell.__class__.__name__[0].upper(), end=" ")
            print()

    @staticmethod
    def print_resources(game):
        print("Resources:")
        for resource_type, amount in game.resources.items():
            print(f"{resource_type.capitalize()}: {amount}")

    @staticmethod
    def print_invocation_message(unit_name):
        print(f"J'invoque un {unit_name} !")