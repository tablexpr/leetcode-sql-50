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
    PARAMS_PROBLEM_180,
)
def test_problem_180(input_data, expected_data):
    table = pl.DataFrame(input_data)
    expected_table = pl.DataFrame(expected_data, schema={"ConsecutiveNums": pl.Int64})
    result = problem_180(table)
    assert_frame_equal(result, expected_table)
