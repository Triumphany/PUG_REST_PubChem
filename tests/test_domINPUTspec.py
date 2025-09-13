import requests
import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import config


class Test_domINPUTspec:
    def test_check_compound(self):
        response = requests.get(f"{config.BASE_URL}/compound/cid/2244/property/MolecularWeight/JSON")
        assert response.status_code == 200

    def test_check_substance(self):
        response = requests.get(f"{config.BASE_URL}/substance/sid/12345/record/JSON")
        assert response.status_code == 200

    def test_check_assay(self):
        response = requests.get(f"{config.BASE_URL}/assay/aid/743122/summary/JSON")
        assert response.status_code == 200

    def test_check_gene(self):
        response = requests.get(f"{config.BASE_URL}/gene/geneid/7157/summary/JSON")
        assert response.status_code == 200

    def test_check_protein(self):
        response = requests.get(f"{config.BASE_URL}/protein/accession/P53_HUMAN/summary/JSON")
        assert response.status_code == 200

    def test_check_pathway(self):
        response = requests.get(f"{config.BASE_URL}/pathway/pwacc/hsa05200/cids/JSON")
        assert response.status_code == 200

    def test_check_taxonomy(self):
        response = requests.get(f"{config.BASE_URL}/taxonomy/taxid/9606/summary/JSON")
        assert response.status_code == 200

    def test_check_cell(self):
        response = requests.get(f"{config.BASE_URL}/cell/cellacc/HeLa/summary/JSON")
        assert response.status_code == 200

    
