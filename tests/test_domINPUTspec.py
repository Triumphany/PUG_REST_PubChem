import requests
import pytest
from utils import config
from utils.logger import get_log


class Test_domINPUTspec:
    logger = get_log("Test_domINPUTspec")

    def test_check_compound(self):
        self.logger.info("Checking compound API with CID 2244")
        try:
            response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/MolecularWeight/JSON")
            assert response.status_code == 200
            self.logger.info("Compound API (CID 2244) : PASSED")
        except AssertionError:
            self.logger.error(f"Compound API (CID 2244) : FAILED - Status {response.status_code}")
            raise

    def test_check_substance(self):
        self.logger.info("Checking substance API with SID 12345")
        try:
            response = requests.get(f"{config.BASE_URL}/substance/sid/12345/record/JSON")
            assert response.status_code == 200
            self.logger.info("Substance API (SID 12345) : PASSED")
        except AssertionError:
            self.logger.error(f"Substance API (SID 12345) : FAILED - Status {response.status_code}")
            raise

    def test_check_assay(self):
        self.logger.info("Checking assay API with AID 743122")
        try:
            response = requests.get(f"{config.BASE_URL}/assay/aid/743122/summary/JSON")
            assert response.status_code == 200
            self.logger.info("Assay API (AID 743122) : PASSED")
        except AssertionError:
            self.logger.error(f"Assay API (AID 743122) : FAILED - Status {response.status_code}")
            raise

    def test_check_gene(self):
        self.logger.info("Checking gene API with GeneID 7157")
        try:
            response = requests.get(f"{config.BASE_URL}/gene/geneid/7157/summary/JSON")
            assert response.status_code == 200
            self.logger.info("Gene API (GeneID 7157) : PASSED")
        except AssertionError:
            self.logger.error(f"Gene API (GeneID 7157) : FAILED - Status {response.status_code}")
            raise

    def test_check_protein(self):
        self.logger.info("Checking protein API with accession P53_HUMAN")
        try:
            response = requests.get(f"{config.BASE_URL}/protein/accession/P53_HUMAN/summary/JSON")
            assert response.status_code == 200
            self.logger.info("Protein API (P53_HUMAN) : PASSED")
        except AssertionError:
            self.logger.error(f"Protein API (P53_HUMAN) : FAILED - Status {response.status_code}")
            raise

    def test_check_pathway(self):
        self.logger.info("Checking pathway API with pwacc hsa05200")
        try:
            response = requests.get(f"{config.BASE_URL}/pathway/pwacc/hsa05200/cids/JSON")
            assert response.status_code == 200
            self.logger.info("Pathway API (hsa05200) : PASSED")
        except AssertionError:
            self.logger.error(f"Pathway API (hsa05200) : FAILED - Status {response.status_code}")
            raise

    def test_check_taxonomy(self):
        self.logger.info("Checking taxonomy API with TaxID 9606")
        try:
            response = requests.get(f"{config.BASE_URL}/taxonomy/taxid/9606/summary/JSON")
            assert response.status_code == 200
            self.logger.info("Taxonomy API (TaxID 9606) : PASSED")
        except AssertionError:
            self.logger.error(f"Taxonomy API (TaxID 9606) : FAILED - Status {response.status_code}")
            raise

    def test_check_cell(self):
        self.logger.info("Checking cell API with accession HeLa")
        try:
            response = requests.get(f"{config.BASE_URL}/cell/cellacc/HeLa/summary/JSON")
            assert response.status_code == 200
            self.logger.info("Cell API (HeLa) : PASSED")
        except AssertionError:
            self.logger.error(f"Cell API (HeLa) : FAILED - Status {response.status_code}")
            raise
    
