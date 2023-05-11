import os 
from ressource import Ressource

class UI:
    @staticmethod
    def clear():
        '''
        try:
            # pour windows
            os.system('cls')
        except:
            try:
                # pour mac et linux
                os.system('clear')
            except:
                pass
        print("\n---------Tour suivant---------\n")
        '''
        print("\n" * 100)



    @staticmethod
    def print_map(game):
        print("\nCARTE:")
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
        print("Resources: ", end="")
        resource_strings = [
            f"{resource_type.capitalize()}: {amount}" for resource_type, amount in game.resources.items()]
        print(", ".join(resource_strings))


    @staticmethod
    def print_invocation_message(unit):
        print(f"L'unité {unit} a été invoqué !! en ({unit.x}, {unit.y})")
