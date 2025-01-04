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
