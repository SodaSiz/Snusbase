# Script Snusbase Python
![Snusbase Logo](https://snusbase.com/img/logo_vertical.png)

Un simple utilitaire en ligne de commande pour utiliser snusbase

## Instructions

- 1. Pour commencer, vous devez au préalable entrer remplir votre fichier .env dans ce format :

> SNUSBASE_AUTH_TOKEN="<Votre token d'authentification snusbase>"
> SNUSBASE_API="https://api-experimental.snusbase.com/"

> [!IMPORTANT] 
> N'oubliez surtout pas d'entrer votre token d'authentification !

- 2. Installer les librairies nécessaires au fonctionnement de snusbase
```sh
pip install -r requirements.txt
```

- 3. Lancer l'utilitaire Snusbase
```sh
python3 snusbase.py
```