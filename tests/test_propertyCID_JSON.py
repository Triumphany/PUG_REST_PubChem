import requests
import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import config
from utils.logger import get_log

class Test_propertyCID_JSON:
    logger = get_log("Test_propertyCID_JSON")

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
        url = f"{config.BASE_URL}/compound/cid/2244/property/MolecularWeight/JSON"
        self._log_request(url, "MolecularWeight")

    def test_getMolecularFormula_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/MolecularFormula/JSON"
        self._log_request(url, "MolecularFormula")

    def test_getCanonicalSMILES_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/CanonicalSMILES/JSON"
        self._log_request(url, "CanonicalSMILES")

    def test_getIsomericSMILES_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/IsomericSMILES/JSON"
        self._log_request(url, "IsomericSMILES")

    def test_getInChI_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/InChI/JSON"
        self._log_request(url, "InChI")

    def test_getInChIKey_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/InChIKey/JSON"
        self._log_request(url, "InChIKey")

    def test_getIUPACName_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/IUPACName/JSON"
        self._log_request(url, "IUPACName")

    def test_getXLogP_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/XLogP/JSON"
        self._log_request(url, "XLogP")

    def test_getTPSA_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/TPSA/JSON"
        self._log_request(url, "TPSA")

    def test_getExactMass_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/ExactMass/JSON"
        self._log_request(url, "ExactMass")

    def test_getCharge_cid(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/Charge/JSON"
        self._log_request(url, "Charge")