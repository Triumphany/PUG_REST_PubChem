import requests
import pytest
from utils.logger import get_log

class Test_element_from_periodic_table():
    logger = get_log("Test_element_from_periodic_table")

    def test_data_all_elements(self):
        for element in range(1,119):
            self.logger.info(f"Atomic Number {element} : STARTED")
            response = requests.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/element/{element}/JSON")
            assert response.status_code == 200
            self.logger.info(f"Atomic Number {element} : CHECKED")
        