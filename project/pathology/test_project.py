import pytest
from project import list_all_pathologies

def test_list_all_pathologies():
    assert "Lumbar Spinal Stenosis" in list_all_pathologies()

# test patho by slug 

