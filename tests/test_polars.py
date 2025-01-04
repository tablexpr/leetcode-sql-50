import polars as pl
import pytest
from polars.testing import assert_frame_equal

from problems.polars import *
from tests.test_problem_params import *


@pytest.mark.parametrize("input_data, expected_data", PARAMS_PROBLEM_176)
def test_problem_176(input_data, expected_data):
    table = pl.DataFrame(input_data)
    expected_table = pl.DataFrame(expected_data)
    result = problem_176(table)
    assert_frame_equal(result, expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "id": [1, 2, 3, 4, 5, 6, 7, 8],
                "num": [1, 2, 3, 1, 1, 1, 4, 5],
            },
            {
                "ConsecutiveNums": [1],
            },
            id="one_consecutive_number_three_times",
        ),
        pytest.param(
            {
                "id": [1, 2, 3, 4, 5, 6, 7, 8],
                "num": [1, 2, 3, 1, 1, 1, 1, 5],
            },
            {
                "ConsecutiveNums": [1],
            },
            id="one_consecutive_number_four_times",
        ),
        pytest.param(
            {
                "id": [1, 2, 3, 4, 5],
                "num": [1, 2, 3, 4, 5],
            },
            {
                "ConsecutiveNums": [],
            },
            id="no_consecutive_numbers",
        ),
        pytest.param(
            {
                "id": [],
                "num": [],
            },
            {
                "ConsecutiveNums": [None],
            },
            id="empty_table",
        ),
    ],
)
def test_problem_180(input_data, expected_data):
    table = pl.DataFrame(input_data)
    expected_table = pl.DataFrame(expected_data, schema={"ConsecutiveNums": pl.Int64})
    result = problem_180(table)
    assert_frame_equal(result, expected_table)
