import requests
import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import config


class Test_propertyNAME_txt:

    def test_getMolecularWeight_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/MolecularWeight/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getMolecularFormula_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/MolecularFormula/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getCanonicalSMILES_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/CanonicalSMILES/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getIsomericSMILES_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/IsomericSMILES/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getInChI_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/InChI/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getInChIKey_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/InChIKey/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getIUPACName_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/IUPACName/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getXLogP_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/XLogP/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getTPSA_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/TPSA/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getExactMass_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/ExactMass/txt")
        assert response.status_code == 200
        print(response.text.strip())

    def test_getCharge_cid(self):
        response = requests.get(f"{config.BASE_URL}/compound/name/water/property/Charge/txt")
        assert response.status_code == 200
        print(response.text.strip())
