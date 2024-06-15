from colorama import Fore, Style
from Core.user_input import user_input
from dotenv import load_dotenv
import fade
import os
load_dotenv()

with open("Texts/welcome.txt", "r") as f:
    text_default = f.read()
    f.close()

with open("Texts/options.txt", "r") as f:
    choose_text = f.read()
    f.close()

snusbase_auth = os.getenv("SNUSBASE_AUTH_TOKEN")
snusbase_api = os.getenv("SNUSBASE_API")
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)

    text_choose_fade = fade.purpleblue(choose_text)
    print(text_choose_fade)

    print(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez votre choix (1-8) :")
    choice = input("> ")

    match choice:
        case "1":
            user_input("Entrez une adresse Email : ", "email")

        case "2":
            user_input("Entrez un Nom d'utilisateur : ", "username")

        case "3":
            user_input("Entrez une adresse IP : ", "lastip")

        case "4":
            user_input(text="Veuillez entrer une adresse IP : ", type="whois", api_url="https://beta.snusbase.com/v1")

        case "5":
            user_input(text="Veuillez entrer un mot de passe : ", type="password")

        case "6":
            user_input(text="Veuillez entrer un mot de passe hashé : ", type="hash")

        case "7":
            user_input("Entrez n'importe quelle valeur : ", "combo", "https://beta.snusbase.com/v2")

        case "8":
            user_input("Entrez un Nom & Prénom : ", "name")

        case "exit":
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        case "quitter":
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        case _:
            print("Choix invalide. Veuillez réessayer.")
            input("Appuyez sur une touche pour continuer...")
