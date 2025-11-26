import pytest
from project import list_all_pathologies
from project import get_pathology_by_name
from project import get_pathology_by_body_part

def test_list_all_pathologies():
    assert "Lumbar Spinal Stenosis" in list_all_pathologies()

# test patho by name 
 
def test_get_pathology_by_name():
    assert get_pathology_by_name("Spondylolysis / Spondylolisthesis")['name'] == "Spondylolysis / Spondylolisthesis"
  
def test_insensitive_get_pathology_by_name():
    assert get_pathology_by_name("carpal tunnel syndrome")['name'] == "Carpal Tunnel Syndrome"

# def test_get_pathology_by_body_part():
    # assert get_pathology_by_body_part("Upper limb: Carpal Tunnel Syndrome")['body_part']['name'] == "Upper limb: Carpal Tunnel Syndrome"
    # assert get_pathology_by_body_part("Upper limb:")['body_part']('Carpal Tunnel Syndrome')['name'] == "Upper limb: Carpal Tunnel Syndrome"
    # assert get_pathology_by_body_part("{pathology['back']}: {pathology['Lumbar Spinal Stenosis']}") == "Back: Lumbar Spinal Stenosis"