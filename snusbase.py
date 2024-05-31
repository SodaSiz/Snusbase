import os
import json
import traceback
import datetime
import requests
import fade
from dotenv import load_dotenv
from pathlib import Path
from colorama import Fore, Style

load_dotenv()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_directory(category):
    directory = f"./resource/{category}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def save_error_log(error):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    log_directory = create_directory("logs")
    log_file = os.path.join(log_directory, f"error_{timestamp}.log")
    with open(log_file, "w") as file:
        file.write(str(error))

def handle_error():
    error = traceback.format_exc()
    print(Style.RESET_ALL + "Une erreur s'est produite. Veuillez consulter les logs pour plus de détails.")
    save_error_log(error)

snusbase_auth = os.getenv("SNUSBASE_AUTH_TOKEN")
snusbase_api = os.getenv("SNUSBASE_API")

#API-COMBO:
def api_combo():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    class network_discord:
        def __init__(self):
            pass

        def search(self, term):
            f = requests.get(f"https://beta.snusbase.com/v2/combo/{term}")
            if f.status_code == 200:
                out = f.json()["result"]
                l = []
                for item in out:
                    for item2 in out[item]:
                        l.append(item2)
                        
                formatted_results = json.dumps(l, indent=2)  # Pretty print the results
                print("")
                print(formatted_results)
            else:
                print("La requête a échoué.")
    
    if __name__ == '__main__':

        term = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez n'importe quelle valeur : ")

        if term == "exit":
            exit()

        elif term == "menu":
            default_menu()

        else:
            search = network_discord()
            search.search(term)
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-IP WHOIS:
def api_ip_whois():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def api_whois(snusbase_auth, ip):
        url = f"https://beta.snusbase.com/v1/whois/{ip}"
        headers = {
            "authorization": snusbase_auth
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            print("")
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print("La requête a échoué.")

    if __name__ == "__main__":
        ip = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez l'adresse IP : ")

        api_whois(snusbase_auth, ip)
        input("\nAppuyez sur Entrée pour continuer...")
        default_menu()

#-----------------------------------------------------------------

#API-EMAIL:
def api_email():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un adresse Email : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["email"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)

            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-USERNAME:
def api_username():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un nom d'utilisateur : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["username"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)

            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-IP:
def api_ip():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un adresse IP : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["lastip"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-HASH:
def api_hash():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un mot de passe Hash : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["hash"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-PASSWORD:
def api_password():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un mot de passe : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["password"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-NAME:
def api_name():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez un Prenom & Nom avec un espace : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["name"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#DEFAULT TEXT:
text_default =r'''
   _____                 _                    
  / ____|               | |                   
 | (___  _ __  _   _ ___| |__   __ _ ___  ___ 
  \___ \| '_ \| | | / __| '_ \ / _` / __|/ _ \
  ____) | | | | |_| \__ \ |_) | (_| \__ \  __/
 |_____/|_| |_|\__,_|___/_.__/ \__,_|___/\___|
 By Siz (M1stral, Alan)
'''

#CHECK IF OUTPUT DIRECTORY EXIST
if not os.path.isdir("output"):
    os.mkdir("output")

#MENU:
def default_menu():
    try:
        clear_screen()
        text_default_fade = fade.greenblue(text_default)
        print(text_default_fade)

        choose_text = '''
(1) - Rechercher avec un Email.             /  (5) - Rechercher via un mot de passe.
(2) - Rechercher avec un Nom d'utilisateur. /  (6) - Rechercher avec un mot de passe hashé.
(3) - Rechercher via une Adresse IP.        /  (7) - Rechercher avec Combo.
(4) - Geo une Adresse IP.                   /  (8) - Rechercher avec Nom & Prénom.

(exit) for leave the app !'''
        
        text_choose_fade = fade.purpleblue(choose_text)
        print(text_choose_fade)

        print(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez votre choix (1-8) :")
        choice = input("> ")
        
        match choice:
            case "1":
                api_email()

            case "2":
                api_username()

            case "3":
                api_ip()
            
            case "4":
                api_ip_whois()

            case "5":
                api_password()
            
            case "6":
                api_hash()
            
            case "7":
                api_combo()
            
            case "8":
                api_name()
            
            case "exit":
                clear_screen()
                exit()
 
            case _:
                print("Choix invalide. Veuillez réessayer.")
                input("Appuyez sur une touche pour continuer...")
                default_menu()
            

    except Exception as e:
        handle_error()


if __name__ == "__main__":
    default_menu()
