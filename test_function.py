import pytest

TC_1 = [10, 1, 3, 5, 101]
TC_2 = 101


# @pytest.mark.parametrize("input_params", [(TC_1), (TC_2)])
# def test_function(input_params):
#     for i in range(1, input_params):
#         assert i < 100 # Check is number greater than 100


@pytest.mark.parametrize("input_params", [i for i in TC_1])
def test_function(input_params):
    assert input_params < 100 # Check is number greater than 100