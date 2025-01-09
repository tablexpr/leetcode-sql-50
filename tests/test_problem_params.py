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

PARAMS_PROBLEM_585 = [
    pytest.param(
        {
            "pid": [1, 2, 3, 4],
            "tiv_2015": [10.0, 20.0, 10.0, 10.0],
            "tiv_2016": [5.0, 20.0, 30.0, 40.0],
            "lat": [10.0, 20.0, 20.0, 40.0],
            "lon": [10.0, 20.0, 20.0, 40.0],
        },
        {"tiv_2016": [45]},
        id="test_case_small_data_consistency",
    ),
    pytest.param(
        {
            "pid": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
            ],
            "tiv_2015": [
                224.17,
                224.17,
                824.61,
                424.32,
                424.32,
                625.05,
                424.32,
                624.46,
                425.49,
                624.46,
                624.46,
                225.93,
                824.61,
                824.61,
                826.37,
                824.61,
                824.61,
                626.81,
                224.76,
                224.76,
                427.25,
                224.76,
                424.9,
                227.69,
                424.9,
                424.9,
                828.13,
                625.05,
                625.05,
            ],
            "tiv_2016": [
                952.73,
                900.66,
                645.13,
                323.66,
                282.9,
                243.53,
                968.94,
                714.13,
                463.85,
                776.85,
                692.71,
                933.0,
                786.86,
                935.34,
                516.1,
                374.5,
                924.19,
                897.47,
                714.79,
                681.53,
                263.27,
                671.8,
                769.18,
                830.5,
                844.97,
                733.35,
                931.83,
                659.13,
                300.16,
            ],
            "lat": [
                32.4,
                52.4,
                72.4,
                12.4,
                12.4,
                52.5,
                72.5,
                12.5,
                32.5,
                12.4,
                72.5,
                12.5,
                32.6,
                52.6,
                12.4,
                12.6,
                32.6,
                52.6,
                72.6,
                12.4,
                32.7,
                52.7,
                72.7,
                12.7,
                12.4,
                52.7,
                72.8,
                12.8,
                32.8,
            ],
            "lon": [
                20.2,
                32.7,
                45.2,
                7.7,
                7.7,
                32.8,
                45.3,
                7.8,
                20.3,
                7.7,
                45.3,
                7.8,
                20.3,
                32.8,
                7.7,
                7.9,
                20.4,
                32.9,
                45.4,
                7.7,
                20.4,
                32.9,
                45.4,
                7.9,
                7.7,
                32.9,
                45.5,
                8.0,
                20.5,
            ],
        },
        {"tiv_2016": [8206.2]},
        id="test_case_large_data_variation",
    ),
]


PARAMS_PROBLEM_595 = [
    pytest.param(
        {
            "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
            "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
            "area": [652_230, 28_748, 2_381_741, 468, 1_246_700],
            "population": [25_500_100, 2_831_741, 37_100_000, 78_115, 20_609_294],
            "gdp": [
                20_343_000_000,
                12_960_000_000,
                188_681_000_000,
                3_712_000_000,
                100_990_000_000,
            ],
        },
        {
            "name": ["Afghanistan", "Algeria"],
            "population": [25_500_100, 37_100_000],
            "area": [652_230, 2_381_741],
        },
        id="happy_path_various_countries",
    ),
    pytest.param(
        {
            "name": ["CountryA", "CountryB"],
            "continent": ["ContinentA", "ContinentB"],
            "area": [3_000_000, 4_000_000],
            "population": [30_000_000, 40_000_000],
            "gdp": [1_000_000_000, 2_000_000_000],
        },
        {
            "name": ["CountryA", "CountryB"],
            "population": [30_000_000, 40_000_000],
            "area": [3_000_000, 4_000_000],
        },
        id="edge_case_all_countries_meeting_criteria",
    ),
]


PARAMS_PROBLEM_596 = [
    pytest.param(
        {
            "student": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
            ],
            "class": [
                "Math",
                "Math",
                "Biology",
                "Math",
                "Computer",
                "Math",
                "Math",
                "Math",
                "Computer",
                "Computer",
                "Computer",
                "Computer",
            ],
        },
        {"class": ["Math", "Computer"]},
        id="happy_path_multiple_classes",
    ),
    pytest.param(
        {
            "class": ["History", "History", "History", "History", "History"],
            "student": ["Alice", "Bob", "Charlie", "David", "Eve"],
        },
        {"class": ["History"]},
        id="edge_case_exactly_5_students",
    ),
    pytest.param(
        {
            "class": ["Art", "Art", "Art", "Art"],
            "student": ["Alice", "Bob", "Charlie", "David"],
        },
        {"class": []},
        id="edge_case_less_than_5_students",
    ),
]
