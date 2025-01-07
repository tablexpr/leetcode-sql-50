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

PARAMS_PROBLEM_570 = [
    pytest.param(
        {
            "id": [101, 102, 103, 104, 105, 106],
            "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
            "managerId": [None, 101, 101, 101, 101, 101],
        },
        {"name": ["John"]},
        id="happy_path_one_with_five",
    ),
    pytest.param(
        {
            "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],
            "name": [
                "John",
                "Dan",
                "James",
                "Amy",
                "Anne",
                "Ron",
                "Alex",
                "Bob",
                "Charles",
                "David",
                "Edward",
            ],
            "managerId": [None, 101, 101, 101, 101, 101, 110, 110, 110, 110, 110],
        },
        {"name": ["John", "David"]},
        id="happy_path_two_with_five",
    ),
    pytest.param(
        {
            "id": [101, 102, 103, 104, 105, 106],
            "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
            "managerId": [None, 101, 101, 101, 101, 102],
        },
        {"name": []},
        id="none_with_five",
    ),
]


PARAMS_PROBLEM_577 = [
    pytest.param(
        {
            "empId": [3, 1, 2, 4],
            "name": ["Brad", "John", "Dan", "Thomas"],
            "supervisor": [None, 3, 3, 3],
            "salary": [4000, 1000, 2000, 4000],
        },
        {"empId": [2, 4], "bonus": [500, 2000]},
        {"name": ["Brad", "John", "Dan"], "bonus": [None, None, 500]},
        id="happy_path_basic",
    ),
    pytest.param(
        {
            "empId": [1, 2],
            "name": ["John", "Dan"],
            "supervisor": [None, 1],
            "salary": [3000, 2000],
        },
        {"empId": [1, 2], "bonus": [500, 1000]},
        {"name": ["John"], "bonus": [500]},
        id="bonus_filtering_with_matching_empIds",
    ),
]


PARAMS_PROBLEM_584 = [
    pytest.param(
        {
            "id": [1, 2, 4, 5],
            "name": ["Will", "Jane", "Bill", "Zack"],
            "referee_id": [None, None, None, 1],
        },
        {"name": ["Will", "Jane", "Bill", "Zack"]},
        id="happy_path_all_valid",
    ),
    pytest.param(
        {
            "id": [3, 6],
            "name": ["Alex", "Mark"],
            "referee_id": [2, 2],
        },
        {"name": []},
        id="edge_case_all_referee_id_2",
    ),
    pytest.param(
        {
            "id": [1, 3, 5, 6],
            "name": ["Will", "Alex", "Zack", "Mark"],
            "referee_id": [None, 2, 1, 2],
        },
        {"name": ["Will", "Zack"]},
        id="mixed_case_some_valid",
    ),
]
