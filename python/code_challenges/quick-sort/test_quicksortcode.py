import pytest
from quicksortcode import quick_sort

def test_sample_array(sample_array):
    assert quick_sort(sample_array, 0, 5) == [4, 8, 15, 42, 23, 16]



@pytest.fixture
def sample_array():
    return [8,4,23,42,16,15]
