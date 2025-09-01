import requests
import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import config


class TestPropertyAPI:

    def test_getMolecularWeight_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/MolecularWeight/JSON")
        assert response.status_code == 200

    def test_getMolecularFormula_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/MolecularFormula/JSON")
        assert response.status_code == 200

    def test_getCanonicalSMILES_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/CanonicalSMILES/JSON")
        assert response.status_code == 200

    def test_getIsomericSMILES_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/IsomericSMILES/JSON")
        assert response.status_code == 200

    def test_getInChI_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/InChI/JSON")
        assert response.status_code == 200

    def test_getInChIKey_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/InChIKey/JSON")
        assert response.status_code == 200

    def test_getIUPACName_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/IUPACName/JSON")
        assert response.status_code == 200

    def test_getXLogP_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/XLogP/JSON")
        assert response.status_code == 200

    def test_getTPSA_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/TPSA/JSON")
        assert response.status_code == 200

    def test_getExactMass_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/ExactMass/JSON")
        assert response.status_code == 200

    def test_getCharge_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/Charge/JSON")
        assert response.status_code == 200
