import pytest
from ml_data_analysis import compute_average_mass, check_hemisphere, count_class

def test_compute_average_mass():
    assert(compute_average_mass([{'a':1}],'a') == 1)
    assert(compute_average_mass([{'a':1},{'a':2}],'a') == 1.5)
    assert(compute_average_mass([{'a':1},{'a':2},{'a':3}],'a') == 2)
    assert(compute_average_mass([{'a':1},{'a':2},{'a':3}],'a') != 3)
    assert isinstance(compute_average_mass([{'a':1},{'a':2}], 'a'), float)

def test_compute_average_mass_exceptions():
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([],'a')
    with pytest.raises(KeyError):
        compute_average_mass([{'a':1},{'b':1}], 'a')
    with pytest.raises(ValueError):
        compute_average_mass([{'a':1},{'a':'x'}], 'a')
    with pytest.raises(KeyError):
        compute_average_mass([{'a':1},{'a':2}], 'b')

def test_check_hemisphere():
    assert check_hemisphere(1,1) == 'Northern & Eastern'
    assert check_hemisphere(1,-1) == 'Northern & Western'
    assert check_hemisphere(-1,1) == 'Southern & Eastern'
    assert check_hemisphere(-1,-1) == 'Southern & Western'
    assert isinstance(check_hemisphere(90.,90.), str) == True

def test_check_hemisphere_exceptions():
    with pytest.raises(TypeError):
        check_hemisphere('notAFloat',10.)
    with pytest.raises(ValueError):
        check_hemisphere(1.23,0.0)

def test_count_class():
    assert(count_class([{'key1':'a', 'key2':'b'},{'key1':'a', 'key3':'c'}], 'key1') == {'a':2})
    assert(count_class([{'key1':'a', 'key2':'b'},{'key1':'a', 'key2':'c'}], 'key2') == {'b':1, 'c':1})
    assert(count_class([{'key1':'a'}], 'key1') == {'a':1})

def test_count_class_exceptions():
    with pytest.raises(KeyError):
        count_class([{'key1':'a', 'key2':'b'},{'key1':'a', 'key3':'c'}], 'badKey')
    with pytest.raises(TypeError):
        count_class([1,2,3])
    
