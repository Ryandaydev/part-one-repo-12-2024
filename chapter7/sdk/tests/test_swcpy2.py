import pytest
from dotenv import load_dotenv

#load_dotenv()


"""Unit tests for PYSWC SDK

    Tests the functionality of the SDK to interact
    with the SWC API.

Typical usage example:

    pytest test_pyswc.py

"""



def test_environment_variable():
    import os

    # Retrieve the environment variable
    swc_base_url = os.getenv('SWC_API_BASE_URL')

    # Print the value of the environment variable
    print(f"SWC_API_BASE_URL: {swc_base_url}")
    # Check if the environment variable is set correctly
    assert(swc_base_url == 'http://0.0.0.0:8000')


