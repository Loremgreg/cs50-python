import pytest
from project import list_all_pathologies
from project import get_pathology_by_name

def test_list_all_pathologies():
    assert "Lumbar Spinal Stenosis" in list_all_pathologies()

# test patho by name 
 
def test_get_pathology_by_name():
    assert get_pathology_by_name("Spondylolysis / Spondylolisthesis")['name'] == "Spondylolysis / Spondylolisthesis"
  
