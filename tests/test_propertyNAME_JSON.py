import requests
import pytest
import sys, os
from utils.logger import get_log
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import config

class Test_propertyNAME_JSON:
    logger = get_log("Test_propertyNAME_JSON")

    def _log_request(self, url, property_name):
        self.logger.info(f"Requesting {property_name}")
        try:
            response = requests.get(url)
            assert response.status_code == 200
            self.logger.info(f"{property_name} : PASSED")
        except AssertionError:
            self.logger.error(f"{property_name} : FAILED - Status {response.status_code}")
            raise

    def test_getMolecularWeight_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/MolecularWeight/JSON"
        self._log_request(url, "MolecularWeight")

    def test_getMolecularFormula_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/MolecularFormula/JSON"
        self._log_request(url, "MolecularFormula")

    def test_getCanonicalSMILES_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/CanonicalSMILES/JSON"
        self._log_request(url, "CanonicalSMILES")

    def test_getIsomericSMILES_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/IsomericSMILES/JSON"
        self._log_request(url, "IsomericSMILES")

    def test_getInChI_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/InChI/JSON"
        self._log_request(url, "InChI")

    def test_getInChIKey_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/InChIKey/JSON"
        self._log_request(url, "InChIKey")

    def test_getIUPACName_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/IUPACName/JSON"
        self._log_request(url, "IUPACName")

    def test_getXLogP_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/XLogP/JSON"
        self._log_request(url, "XLogP")

    def test_getTPSA_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/TPSA/JSON"
        self._log_request(url, "TPSA")

    def test_getExactMass_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/ExactMass/JSON"
        self._log_request(url, "ExactMass")

    def test_getCharge_cid(self):
        url = f"{config.BASE_URL}/compound/name/water/property/Charge/JSON"
        self._log_request(url, "Charge")
