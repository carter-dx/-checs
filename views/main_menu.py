from models.player import Player
from models.tournament_model import Tournament
from controllers.tournament_controller import save_players, load_players, save_tournaments, load_tournaments

class MainMenu:
    def __init__(self):
        self.players = load_players()
        self.tournaments = load_tournaments()

    def show_menu(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Ajouter un joueur")
            print("2. Créer un tournoi")
            print("3. Voir les joueurs")
            print("4. Voir les tournois")
            print("5. Quitter")

            choice = input("Choix : ")

            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.create_tournament()
            elif choice == "3":
                self.show_players()
            elif choice == "4":
                self.show_tournaments()
            elif choice == "5":
                save_players(self.players)
                save_tournaments(self.tournaments)
                print("Fin du programme. Données sauvegardées.")
                break
            else:
                print("Choix invalide.")

    def add_player(self):
        first_name = input("Prénom : ")
        last_name = input("Nom : ")
        birth_date = input("Date de naissance (YYYY-MM-DD) : ")
        sex = input("Sexe (M/F) : ")
        ranking = int(input("Classement : "))
        player = Player(first_name, last_name, birth_date, sex, ranking)
        self.players.append(player)
        print(f"Joueur {first_name} {last_name} ajouté.")

    def create_tournament(self):
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        date = input("Date (YYYY-MM-DD) : ")
        time_control = input("Contrôle du temps (Bullet/Blitz/Coup rapide) : ")
        tournament = Tournament(name, location, date, time_control=time_control)
        # Ajouter tous les joueurs actuels
        for player in self.players:
            tournament.add_player(player)
        self.tournaments.append(tournament)
        print(f"Tournoi {name} créé avec {len(tournament.players)} joueurs.")

    def show_players(self):
        if not self.players:
            print("Aucun joueur.")
        else:
            for p in self.players:
                print(p)

    def show_tournaments(self):
        if not self.tournaments:
            print("Aucun tournoi.")
        else:
            for t in self.tournaments:
                print(f"{t.name} - {t.date} - {t.location}")


if __name__ == "__main__":
    menu = MainMenu()
    menu.show_menu()
