from analyze_water import calc_turbidity
from analyze_water import calc_threshold_min_time
import pytest
import math

def test_calc_turbidity():
    assert calc_turbidity(0,0) == 0
    assert calc_turbidity(2,2) == 4
    assert calc_turbidity(-1,1) == -1
    assert calc_turbidity('a',4) == 'aaaa'
    assert calc_turbidity(1,2) == 2
    

def test_calc_threshold_min_time():
    assert calc_threshold_min_time(0) == 0
    assert calc_threshold_min_time(1) == 0
    assert math.floor(calc_threshold_min_time(20)) == 148
    assert math.floor(calc_threshold_min_time(40)) == 182     
    
def test_calc_threshold_min_time_exceptions():
    with pytest.raises(TypeError):
        calc_threshold_min_time([])
    with pytest.raises(TypeError):
        calc_threshold_min_time('a')
