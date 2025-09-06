import requests
import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import config


class TestPropertyAPI:
    def test_check_compoundOP(self):
        operation_specificationns = [
    "record",
    "property/MolecularWeight",
    "synonyms",
    "sids",
    "cids",
    "aids",
    "assaysummary",
    "classification",
    "description",
    "conformers"
]
        for operation in operation_specificationns:
            response = requests.get(f"{config.BASE_URL}/compound/cid/2244/{operation}/JSON")
            assert response.status_code == 200

    def test_check_substanceOP(self):
        operation_specificationns = [
    "record",
    "synonyms",
    "sids",
    "cids",
    "aids",
    "assaysummary",
    "classification",
    "description"
]
        for operation in operation_specificationns:
            response = requests.get(f"{config.BASE_URL}/substance/sid/12345/{operation}/JSON")
            assert response.status_code == 200

    def test_check_assayOP(self):
        operations = [
    "record",
    "concise",
    "aids",
    "sids",
    "cids",
    "description",
    "summary",
    "classification"
]
        for operation in operations:
            response = requests.get(f"{config.BASE_URL}/assay/aid/743122/{operation}/JSON")
            assert response.status_code == 200

    def test_check_gene(self):
        operations = [
    "summary",
    "aids",
    "concise",
    "pwaccs"
]
        for operation in operations:
            response = requests.get(f"{config.BASE_URL}/gene/geneid/7157/{operation}/JSON")
            assert response.status_code == 200

    def test_check_protein(self):
        operations = [
    "summary",
    "aids",
    "concise",
    "pwaccs"
]
        for operation in operations:
            response = requests.get(f"{config.BASE_URL}/protein/accession/P53_HUMAN/{operation}/JSON")
            assert response.status_code == 200

    def test_check_pathway(self):
        operations = [
    "summary",
    "cids",
    "geneids",
    "accessions"
]
        for operation in operations:
            response = requests.get(f"{config.BASE_URL}/pathway/pwacc/hsa05200/{operation}/JSON")
            assert response.status_code == 200

    def test_check_taxonomy(self):
        operations = [
    "summary",
    "aids"
]
        for operation in operations:
            response = requests.get(f"{config.BASE_URL}/taxonomy/taxid/9606/{operation}/JSON")
            assert response.status_code == 200

    def test_check_cell(self):
        operations = [
    "summary",
    "aids"
]
        for operation in operations:
            response = requests.get(f"{config.BASE_URL}/cell/cellacc/HeLa/{operation}/JSON")
            assert response.status_code == 200

    

    
