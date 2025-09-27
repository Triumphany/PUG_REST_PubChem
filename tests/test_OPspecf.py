import requests
import pytest
from utils import config
from utils.logger import get_log

class Test_OPspecf:
    logger = get_log("Test_OPspecf")

    def test_check_compoundOP(self):
        operations = [
            "record", "property/MolecularWeight", "synonyms", "sids",
            "cids", "aids", "assaysummary", "classification",
            "description", "conformers"
        ]
        for op in operations:
            self.logger.info(f"Checking compound API operation: {op}")
            try:
                response = requests.get(f"{config.BASE_URL}/compound/cid/2244/{op}/JSON")
                assert response.status_code == 200
                self.logger.info(f"Compound API operation {op} : PASSED")
            except AssertionError:
                self.logger.error(f"Compound API operation {op} : FAILED - Status {response.status_code}")
                raise

    def test_check_substanceOP(self):
        operations = [
            "record", "synonyms", "sids", "cids",
            "aids", "assaysummary", "classification", "description"
        ]
        for op in operations:
            self.logger.info(f"Checking substance API operation: {op}")
            try:
                response = requests.get(f"{config.BASE_URL}/substance/sid/12345/{op}/JSON")
                assert response.status_code == 200
                self.logger.info(f"Substance API operation {op} : PASSED")
            except AssertionError:
                self.logger.error(f"Substance API operation {op} : FAILED - Status {response.status_code}")
                raise

    def test_check_assayOP(self):
        operations = [
            "record", "concise", "aids", "sids",
            "cids", "description", "summary", "classification"
        ]
        for op in operations:
            self.logger.info(f"Checking assay API operation: {op}")
            try:
                response = requests.get(f"{config.BASE_URL}/assay/aid/743122/{op}/JSON")
                assert response.status_code == 200
                self.logger.info(f"Assay API operation {op} : PASSED")
            except AssertionError:
                self.logger.error(f"Assay API operation {op} : FAILED - Status {response.status_code}")
                raise

    def test_check_gene(self):
        operations = ["summary", "aids", "concise", "pwaccs"]
        for op in operations:
            self.logger.info(f"Checking gene API operation: {op}")
            try:
                response = requests.get(f"{config.BASE_URL}/gene/geneid/7157/{op}/JSON")
                assert response.status_code == 200
                self.logger.info(f"Gene API operation {op} : PASSED")
            except AssertionError:
                self.logger.error(f"Gene API operation {op} : FAILED - Status {response.status_code}")
                raise

    def test_check_protein(self):
        operations = ["summary", "aids", "concise", "pwaccs"]
        for op in operations:
            self.logger.info(f"Checking protein API operation: {op}")
            try:
                response = requests.get(f"{config.BASE_URL}/protein/accession/P53_HUMAN/{op}/JSON")
                assert response.status_code == 200
                self.logger.info(f"Protein API operation {op} : PASSED")
            except AssertionError:
                self.logger.error(f"Protein API operation {op} : FAILED - Status {response.status_code}")
                raise

    def test_check_pathway(self):
        operations = ["summary", "cids", "geneids", "accessions"]
        for op in operations:
            self.logger.info(f"Checking pathway API operation: {op}")
            try:
                response = requests.get(f"{config.BASE_URL}/pathway/pwacc/hsa05200/{op}/JSON")
                assert response.status_code == 200
                self.logger.info(f"Pathway API operation {op} : PASSED")
            except AssertionError:
                self.logger.error(f"Pathway API operation {op} : FAILED - Status {response.status_code}")
                raise

    def test_check_taxonomy(self):
        operations = ["summary", "aids"]
        for op in operations:
            self.logger.info(f"Checking taxonomy API operation: {op}")
            try:
                response = requests.get(f"{config.BASE_URL}/taxonomy/taxid/9606/{op}/JSON")
                assert response.status_code == 200
                self.logger.info(f"Taxonomy API operation {op} : PASSED")
            except AssertionError:
                self.logger.error(f"Taxonomy API operation {op} : FAILED - Status {response.status_code}")
                raise

    def test_check_cell(self):
        operations = ["summary", "aids"]
        for op in operations:
            self.logger.info(f"Checking cell API operation: {op}")
            try:
                response = requests.get(f"{config.BASE_URL}/cell/cellacc/HeLa/{op}/JSON")
                assert response.status_code == 200
                self.logger.info(f"Cell API operation {op} : PASSED")
            except AssertionError:
                self.logger.error(f"Cell API operation {op} : FAILED - Status {response.status_code}")
                raise