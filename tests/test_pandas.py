from datetime import datetime

import pandas as pd
import pytest

from problems.pandas import problem_176, problem_1321


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


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "customer_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3],
                "name": [
                    "Jhon",
                    "Daniel",
                    "Jade",
                    "Khaled",
                    "Winston",
                    "Elvis",
                    "Anna",
                    "Maria",
                    "Jaze",
                    "Jhon",
                    "Jade",
                ],
                "visited_on": [
                    datetime(2019, 1, 1),
                    datetime(2019, 1, 2),
                    datetime(2019, 1, 3),
                    datetime(2019, 1, 4),
                    datetime(2019, 1, 5),
                    datetime(2019, 1, 6),
                    datetime(2019, 1, 7),
                    datetime(2019, 1, 8),
                    datetime(2019, 1, 9),
                    datetime(2019, 1, 10),
                    datetime(2019, 1, 10),
                ],
                "amount": [100, 110, 120, 130, 110, 140, 150, 80, 110, 130, 150],
            },
            {
                "visited_on": [
                    datetime(2019, 1, 7),
                    datetime(2019, 1, 8),
                    datetime(2019, 1, 9),
                    datetime(2019, 1, 10),
                ],
                "amount": [860, 840, 840, 1000],
                "average_amount": [122.86, 120, 120, 142.86],
            },
            id="happy_path",
        ),
        pytest.param(
            {
                "customer_id": [1, 2, 3, 1, 4, 5, 6, 1, 7, 8, 9],
                "name": [
                    "Jhon",
                    "Daniel",
                    "Jade",
                    "Jhon",
                    "Khaled",
                    "Winston",
                    "Elvis",
                    "Jhon",
                    "Anna",
                    "Maria",
                    "Jaze",
                ],
                "visited_on": [
                    datetime(2019, 1, 1),
                    datetime(2019, 1, 2),
                    datetime(2019, 1, 3),
                    datetime(2019, 1, 1),
                    datetime(2019, 1, 4),
                    datetime(2019, 1, 5),
                    datetime(2019, 1, 6),
                    datetime(2019, 1, 1),
                    datetime(2019, 1, 7),
                    datetime(2019, 1, 8),
                    datetime(2019, 1, 9),
                ],
                "amount": [100, 110, 120, 50, 130, 110, 140, 40, 150, 80, 110],
            },
            {
                "visited_on": [
                    datetime(2019, 1, 7),
                    datetime(2019, 1, 8),
                    datetime(2019, 1, 9),
                ],
                "amount": [950, 840, 840],
                "average_amount": [135.71, 120, 120],
            },
            id="duplicated_days",
        ),
    ],
)
def test_problem_1321(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data).reset_index(drop=True)
    result = (
        problem_1321(table)
        .reset_index(drop=True)
        .astype(expected_table.dtypes.to_dict())
    )
    assert list(result.index) == list(
        expected_table.index
    ), f"Index mismatch: {result.index} vs {expected_table.index}"
    for col in expected_table.columns:
        assert result[col].equals(expected_table[col]), f"Mismatch in column '{col}'"

    assert result.equals(expected_table)
