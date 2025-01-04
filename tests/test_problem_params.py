import pytest

PARAMS_PROBLEM_176 = [
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
]


PARAMS_PROBLEM_180 = [
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
]
