import requests
import pytest
import sys, os
from utils.logger import get_log
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import config

class Test_outputs:
    logger = get_log("Test_outputs")

    def test_check_JSON(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/MolecularWeight/JSON"
        self.logger.info(f"Requesting URL: {url}")
        try:
            response = requests.get(url)
            assert response.status_code == 200
            self.logger.info("JSON response : PASSED")
        except AssertionError:
            self.logger.error(f"JSON response : FAILED - Status {response.status_code}")
            raise

    def test_check_XML(self):
        url = f"{config.BASE_URL}/compound/cid/2244/property/MolecularWeight/XML"
        self.logger.info(f"Requesting URL: {url}")
        try:
            response = requests.get(url)
            assert response.status_code == 200
            self.logger.info("XML response : PASSED")
        except AssertionError:
            self.logger.error(f"XML response : FAILED - Status {response.status_code}")
            raise

    def test_check_SDF(self):
        url = f"{config.BASE_URL}/compound/cid/2244/record/SDF"
        self.logger.info(f"Requesting URL: {url}")
        try:
            response = requests.get(url)
            assert response.status_code == 200
            self.logger.info("SDF response : PASSED")
        except AssertionError:
            self.logger.error(f"SDF response : FAILED - Status {response.status_code}")
            raise

    def test_check_TXT(self):
        url = f"{config.BASE_URL}/compound/cid/2244/synonyms/TXT"
        self.logger.info(f"Requesting URL: {url}")
        try:
            response = requests.get(url)
            assert response.status_code == 200
            self.logger.info("TXT response : PASSED")
        except AssertionError:
            self.logger.error(f"TXT response : FAILED - Status {response.status_code}")
            raise

    def test_check_CSV(self):  # negative test
        url = f"{config.BASE_URL}/compound/cid/2244/synonyms/CSV"
        self.logger.info(f"Requesting URL: {url} (expecting failure)")
        try:
            response = requests.get(url)
            assert response.status_code != 200
            self.logger.info("CSV response : PASSED (negative test)")
        except AssertionError:
            self.logger.error(f"CSV response : FAILED - Status {response.status_code}")
            raise

    def test_check_PNG(self):
        url = f"{config.BASE_URL}/compound/cid/2244/PNG"
        self.logger.info(f"Requesting URL: {url}")
        try:
            response = requests.get(url)
            assert response.status_code == 200
            self.logger.info("PNG response : PASSED")
        except AssertionError:
            self.logger.error(f"PNG response : FAILED - Status {response.status_code}")
            raise