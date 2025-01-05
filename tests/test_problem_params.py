from datetime import datetime

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

PARAMS_PROBLEM_185 = [
    pytest.param(
        {
            "id": [1, 2, 3, 4, 5, 6, 7],
            "name": ["Joe", "Henry", "Sam", "Max", "Janet", "Randy", "Will"],
            "salary": [85000, 80000, 60000, 90000, 69000, 85000, 70000],
            "departmentId": [1, 2, 2, 1, 1, 1, 1],
        },
        {"id": [1, 2], "name": ["IT", "Sales"]},
        {
            "Department": ["IT", "Sales", "Sales", "IT", "IT", "IT"],
            "Employee": ["Joe", "Henry", "Sam", "Max", "Randy", "Will"],
            "Salary": [85000, 80000, 60000, 90000, 85000, 70000],
        },
        id="happy_path_basic",
    ),
    pytest.param(
        {
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
            "salary": [60000, 75000, 80000],
            "departmentId": [1, 2, 1],
        },
        {"id": [1, 2], "name": ["HR", "Finance"]},
        {
            "Department": ["HR", "Finance", "HR"],
            "Employee": ["Alice", "Bob", "Charlie"],
            "Salary": [60000, 75000, 80000],
        },
        id="single_employee_multiple_departments",
    ),
    pytest.param(
        {
            "id": [1, 2, 3, 4],
            "name": ["Alice", "Alice", "Bob", "Charlie"],
            "salary": [70000, 80000, 75000, 90000],
            "departmentId": [1, 1, 2, 2],
        },
        {"id": [1, 2], "name": ["IT", "Sales"]},
        {
            "Department": ["IT", "IT", "Sales", "Sales"],
            "Employee": ["Alice", "Alice", "Bob", "Charlie"],
            "Salary": [70000, 80000, 75000, 90000],
        },
        id="duplicate_employees_different_salaries",
    ),
]


PARAMS_PROBLEM_196 = [
    pytest.param(
        {
            "id": [1, 2, 3],
            "email": ["a@example.com", "b@example.com", "c@example.com"],
        },
        {
            "id": [1, 2, 3],
            "email": ["a@example.com", "b@example.com", "c@example.com"],
        },
        id="unique_emails",
    ),
    pytest.param(
        {
            "id": [1, 2, 3, 4],
            "email": [
                "a@example.com",
                "b@example.com",
                "a@example.com",
                "b@example.com",
            ],
        },
        {"id": [1, 2], "email": ["a@example.com", "b@example.com"]},
        id="duplicate_emails",
    ),
    pytest.param(
        {"id": [1], "email": ["a@example.com"]},
        {"id": [1], "email": ["a@example.com"]},
        id="single_row",
    ),
]


PARAMS_PROBLEM_197 = [
    pytest.param(
        {
            "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 2)],
            "temperature": [20, 25],
            "id": [1, 2],
        },
        {"id": [2]},
        id="happy_path_basic",
    ),
    pytest.param(
        {
            "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 2)],
            "temperature": [25, 25],
            "id": [1, 2],
        },
        {"id": []},
        id="no_temperature_increase",
    ),
    pytest.param(
        {
            "recordDate": [datetime(2023, 1, 1)],
            "temperature": [20],
            "id": [1],
        },
        {"id": []},
        id="single_record",
    ),
    pytest.param(
        {
            "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 2)],
            "temperature": [25, 20],
            "id": [1, 2],
        },
        {"id": []},
        id="temperature_decrease",
    ),
    pytest.param(
        {
            "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 3)],
            "temperature": [20, 25],
            "id": [1, 2],
        },
        {"id": []},
        id="skip_a_day",
    ),
]


PARAMS_PROBLEM_550 = [
    pytest.param(
        {
            "player_id": [1, 1, 2, 3, 3],
            "device_id": [2, 2, 3, 1, 4],
            "event_date": [
                datetime(2016, 3, 1),
                datetime(2016, 3, 2),
                datetime(2017, 6, 25),
                datetime(2016, 3, 2),
                datetime(2018, 7, 3),
            ],
            "games_played": [5, 6, 1, 0, 5],
        },
        {"fraction": [0.33]},
        id="happy_path_basic",
    ),
    pytest.param(
        {
            "player_id": [1, 1, 1, 2, 2],
            "device_id": [2, 2, 3, 1, 4],
            "event_date": [
                datetime(2023, 1, 1),
                datetime(2023, 1, 2),
                datetime(2023, 1, 3),
                datetime(2023, 1, 1),
                datetime(2023, 1, 2),
            ],
            "games_played": [1, 2, 3, 4, 5],
        },
        {"fraction": [1.0]},
        id="happy_path_multiple_dates",
    ),
    pytest.param(
        {
            "player_id": [1],
            "device_id": [1],
            "event_date": [datetime(2023, 1, 1)],
            "games_played": [1],
        },
        {"fraction": [0.0]},
        id="edge_case_single_entry",
    ),
]
