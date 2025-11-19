import os
import sys
import pytest

#to make sure it finds the project root
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()
