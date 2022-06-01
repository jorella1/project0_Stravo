from service.pace_calculator import *

import pytest


testdata1 = [
    (10, "00:00:10"), 
    (11, "00:00:11"), 
    (4000, "01:06:40"), 
    (9999, "02:46:39"),
    (100000, "03:46:40"),
    (0, "00:00:00")
    ]

@pytest.mark.parametrize("seconds, expected", testdata1)
def test_secs_to_time(seconds, expected):
    assert secs_to_time(seconds) == expected

testdata2 = [
    (1,1,1,["Mile: 0 Time: 00:00:00", "Mile: 1 Time: 00:01:01"]),
    (0 ,0,0,["Mile: 0 Time: 00:00:00"])
]
#tricky one to test because I'm not typing out the entire list of paces
@pytest.mark.parametrize("distance, paceM, paceS, expected", testdata2)
def test_Pacer(distance, paceM, paceS, expected):
    testpacer = Pacer()
    results = testpacer.paceCalc(distance, paceM, paceS)
    assert results == expected

testdata3 = [
    (13,1,1,"Mile: 5 Time: 00:05:05"),
    (29 ,0,0,"Mile: 5 Time: 00:00:00"),
    (100 ,9,13,"Mile: 5 Time: 00:46:05")
]

@pytest.mark.parametrize("distance, paceM, paceS, expected", testdata3)
def test_Pacer_specific(distance, paceM, paceS, expected):
    testpacer = Pacer()
    results = testpacer.paceCalc(distance, paceM, paceS)
    assert results[5] == expected