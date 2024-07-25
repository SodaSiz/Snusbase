import responses
import subprocess
import sys
from unittest.mock import mock_open

# Charger les variables d'environnement
from dotenv import load_dotenv
load_dotenv()

# Simuler la réponse de l'API Snusbase
@responses.activate
def test_snusbase_email_search(mocker):
    responses.add(
        responses.POST,
        'https://beta.snusbase.com/v1/data/search',
        json={'status': 'success', 'data': 'example data'},
        status=200
    )

    # Mocking input and open function
    mocker.patch('builtins.input', side_effect=['1', 'corentin.destouches44.cd@gmail.com', 'exit'])
    mocker.patch('os.system')  # To prevent clearing the screen during test

    result = subprocess.run([sys.executable, 'snusbase.py'], capture_output=True, text=True)

    assert result.returncode == 0
    assert "Recherche réussie" in result.stdout
    assert "'status': 'success'" in result.stdout
