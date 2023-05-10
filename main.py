from game import Game
from unit import Lumberjack, Miner, Peasant
from building import ProductionBuilding, ToolCreationBuilding

def main():
    starting_resources = {"wood": 100, "gold": 100, "stone": 100, "food": 100}
    game = Game(10, 10, starting_resources)

    while not game.is_game_over():
        # Affichez les options de jeu
        print("\nOptions:")
        print("1 - Construire un bâtiment")
        print("2 - Jouer un tour")
        print("3 - Quitter")
        choice = input("Choisissez une option: ")

        if choice == "1":
            print("\nBâtiments disponibles:")
            print("1 - Bâtiment de production de bûcherons")
            print("2 - Bâtiment de production de mineurs")
            print("3 - Bâtiment de production de paysans")
            print("4 - Bâtiment de création d'outils pour les bûcherons")
            print("5 - Bâtiment de création d'outils pour les mineurs")
            print("6 - Bâtiment de création d'outils pour les paysans")
            building_choice = input("Choisissez un bâtiment à construire: ")

            if building_choice == "1":
                building = ProductionBuilding(game, {"wood": 10, "gold": 10, "stone": 10, "food": 10}, Lumberjack)
            elif building_choice == "2":
                building = ProductionBuilding(game, {"wood": 10, "gold": 10, "stone": 10, "food": 10}, Miner)
            elif building_choice == "3":
                building = ProductionBuilding(game, {"wood": 10, "gold": 10, "stone": 10, "food": 10}, Peasant)
            elif building_choice == "4":
                building = ToolCreationBuilding(game, {"wood": 10, "gold": 10, "stone": 10, "food": 10}, Lumberjack)
            elif building_choice == "5":
                building = ToolCreationBuilding(game, {"wood": 10, "gold": 10, "stone": 10, "food": 10}, Miner)
            elif building_choice == "6":
                building = ToolCreationBuilding(game, {"wood": 10, "gold": 10, "stone": 10, "food": 10}, Peasant)
            else:
                print("Choix non valide.")
                continue

            if building.build():
                game.buildings.append(building)
                print("Bâtiment construit.")
            else:
                print("Pas assez de ressources pour construire ce bâtiment.")

        elif choice == "2":
            game.play_turn()
        elif choice == "3":
            break
        else:
            print("Choix non valide.")

    print("Fin du jeu.")

if __name__ == "__main__":
    main()
