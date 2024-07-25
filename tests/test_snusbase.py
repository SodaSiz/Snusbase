import responses
import subprocess
import sys
import os
from unittest.mock import mock_open

# Charger les variables d'environnement
from dotenv import load_dotenv
load_dotenv()

@responses.activate
def test_snusbase_email_search(mocker):
    responses.add(
        responses.POST,
        'https://beta.snusbase.com/v1/data/search',
        json={'status': 'success', 'data': 'example data'},
        status=200
    )

    # Mocking open function to read welcome and options text
    mocker.patch('builtins.open', mock_open(read_data="Welcome to Snusbase\nChoose an option:"))
    mocker.patch('os.system')  # To prevent clearing the screen during test

    # Création d'un fichier temporaire pour les entrées utilisateur
    user_input = "1\ncorentin.destouches44.cd@gmail.com\nexit\n"
    input_file_path = "tests/temp_input.txt"
    with open(input_file_path, 'w') as f:
        f.write(user_input)

    # Rediriger stdin à partir du fichier temporaire
    with open(input_file_path, 'r') as f:
        result = subprocess.run([sys.executable, 'snusbase.py'], stdin=f, capture_output=True, text=True)

    # Supprimer le fichier temporaire après le test
    os.remove(input_file_path)

    assert result.returncode == 0
    assert "Recherche réussie" in result.stdout
    assert "'status': 'success'" in result.stdout
