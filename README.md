
# PUG REST PubChem API Testing

## Overview

This repository demonstrates API testing using the PubChem PUG REST API.
It covers fetching compound information, validating responses, and implementing automated test cases with proper reporting.

The project is designed as a learning exercise for building robust API testing workflows in Python.

## Features

* Query chemical compounds by name or CID
* Validate response fields such as molecular formula, weight, smiles and IUPAC name
* Centralized logging for test execution
* Automated test execution with pytest

## Technology Stack

* Python 3.x
* pytest (testing framework)
* requests (HTTP client)
* HTML reports 



## Folder Structure

Install my-project with npm

```bash
 PUG_REST_PubChem/
  │── utils/
  │   ├── config.py
  │── reports/
  │   ├── html/         # HTML reports
  │── tests/
  │── requirements.txt
  │── README.md

```
## Installation

Clone the repository and install dependencies:

```bash
  git clone https://github.com/Triumphany/PUG_REST_PubChem.git
  cd PUG_REST_PubChem
  pip install -r requirements.txt
```

## Running Tests

Execute the test suite with:

```bash
  pytest -v
  pytest -v tests/test_name.py --html=reports/html/name.html
```
* -v runs pytest in verbose mode
* HTML reports are stored in reports/html

