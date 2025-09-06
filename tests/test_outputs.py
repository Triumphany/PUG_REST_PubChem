import requests
import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import config


class TestPropertyAPI:
    def test_check_JSON(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/MolecularWeight/JSON")
        assert response.status_code == 200

    def test_check_XML(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/MolecularWeight/XML")
        assert response.status_code == 200

    def test_check_SDF(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/record/SDF")
        assert response.status_code == 200

    def test_check_TXT(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/synonyms/TXT")
        assert response.status_code == 200

    def test_check_CSV(self):    #negative request
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/synonyms/CSV")
        assert response.status_code != 200

    def test_check_PNG(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/PNG")
        assert response.status_code == 200



    
