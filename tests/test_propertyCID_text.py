import requests
import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import config


class TestPropertyAPI:

    def test_getMolecularWeight_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/MolecularWeight/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getMolecularFormula_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/MolecularFormula/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getCanonicalSMILES_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/CanonicalSMILES/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getIsomericSMILES_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/IsomericSMILES/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getInChI_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/InChI/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getInChIKey_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/InChIKey/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getIUPACName_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/IUPACName/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getXLogP_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/XLogP/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getTPSA_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/TPSA/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getExactMass_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/ExactMass/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getCharge_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/Charge/txt")
        assert response.status_code == 200
        print(response.text.strip())
