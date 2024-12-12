import pandas as pd
import pytest

from problems.pandas import problem_176


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {"salary": [100, 200, 300]},
            {"SecondHighestSalary": [200]},
            id="distinct_salaries",
        ),
        pytest.param(
            {"salary": [100, 200, 200, 300]},
            {"SecondHighestSalary": [200]},
            id="multiple_second_highest",
        ),
        pytest.param(
            {"salary": [100]}, {"SecondHighestSalary": [None]}, id="single_salary"
        ),
        pytest.param(
            {"salary": [100, 100, 100]},
            {"SecondHighestSalary": [None]},
            id="all_salaries_same",
        ),
        pytest.param({"salary": []}, {"SecondHighestSalary": [None]}, id="empty_table"),
    ],
)
def test_problem_176(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_176(table)
    assert result.equals(expected_table)
