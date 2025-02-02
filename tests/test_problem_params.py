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


PARAMS_PROBLEM_602 = [
    pytest.param(
        {"requester_id": [1, 1, 2, 3], "accepter_id": [2, 3, 3, 4]},
        {"id": [3], "num": [3]},
        id="balanced",
    ),
    pytest.param(
        {"requester_id": [1, 1, 1, 1], "accepter_id": [2, 3, 4, 5]},
        {"id": [1], "num": [4]},
        id="three_ids_1_requester",
    ),
    pytest.param(
        {"requester_id": [2, 3, 4, 5], "accepter_id": [1, 1, 1, 1]},
        {"id": [1], "num": [4]},
        id="three_ids_1_accepter",
    ),
]


PARAMS_PROBLEM_610 = [
    pytest.param(
        {"x": [3], "y": [4], "z": [5]},
        {"x": [3], "y": [4], "z": [5], "triangle": ["Yes"]},
        id="valid_triangle",
    ),
    pytest.param(
        {"x": [5], "y": [5], "z": [5]},
        {"x": [5], "y": [5], "z": [5], "triangle": ["Yes"]},
        id="equilateral_triangle",
    ),
    pytest.param(
        {"x": [2], "y": [2], "z": [3]},
        {"x": [2], "y": [2], "z": [3], "triangle": ["Yes"]},
        id="isosceles_triangle",
    ),
    pytest.param(
        {"x": [1], "y": [1], "z": [2]},
        {"x": [1], "y": [1], "z": [2], "triangle": ["No"]},
        id="degenerate_triangle",
    ),
    pytest.param(
        {"x": [0], "y": [0], "z": [0]},
        {"x": [0], "y": [0], "z": [0], "triangle": ["No"]},
        id="zero_length_sides",
    ),
    pytest.param(
        {"x": [1], "y": [2], "z": [3]},
        {"x": [1], "y": [2], "z": [3], "triangle": ["No"]},
        id="non_triangle",
    ),
]


PARAMS_PROBLEM_619 = [
    pytest.param(
        {
            "num": [1, 2, 3, 4],
        },
        {"num": [4]},
        id="all_single_numbers",
    ),
    pytest.param(
        {
            "num": [1, 2, 2, 3, 3, 4],
        },
        {
            "num": [4],
        },
        id="mixed_single_and_duplicate_numbers",
    ),
    pytest.param(
        {
            "num": [2, 2, 3, 3],
        },
        {
            "num": [float("nan")],
        },
        id="all_duplicates",
    ),
]

PARAMS_PROBLEM_620 = [
    pytest.param(
        {
            "id": [1, 2, 3, 4],
            "description": ["interesting", "boring", "exciting", "boring"],
        },
        {"id": [3, 1], "description": ["exciting", "interesting"]},
        id="happy_path_mixed_ids_and_descriptions",
    ),
    pytest.param(
        {"id": [1, 3], "description": ["boring", "boring"]},
        {"id": [], "description": []},
        id="edge_case_all_boring",
    ),
    pytest.param(
        {"id": [2, 4], "description": ["interesting", "exciting"]},
        {"id": [], "description": []},
        id="edge_case_no_odd_ids",
    ),
    pytest.param(
        {"id": [1], "description": ["interesting"]},
        {"id": [1], "description": ["interesting"]},
        id="edge_case_single_row_matching",
    ),
    pytest.param(
        {"id": [2], "description": ["boring"]},
        {"id": [], "description": []},
        id="edge_case_single_row_not_matching",
    ),
]

PARAMS_PROBLEM_626 = [
    pytest.param(
        {
            "id": [1, 2, 3, 4, 5],
            "student": ["Abbot", "Doris", "Emerson", "Green", "Jeames"],
        },
        {
            "id": [1, 2, 3, 4, 5],
            "student": ["Doris", "Abbot", "Green", "Emerson", "Jeames"],
        },
        id="swap_students_odd_row_count",
    ),
    pytest.param(
        {
            "id": [1, 2],
            "student": ["Abbot", "Doris"],
        },
        {
            "id": [1, 2],
            "student": ["Doris", "Abbot"],
        },
        id="swap_students_even_row_count",
    ),
]

PARAMS_PROBLEM_1045 = [
    pytest.param(
        {"customer_id": [1, 1, 2, 2], "product_key": [1, 2, 1, 2]},
        {"product_key": [1, 2]},
        {"customer_id": [1, 2]},
        id="happy_path_all_bought_all",
    ),
    pytest.param(
        {"customer_id": [1, 1, 2, 2], "product_key": [1, 2, 1, 3]},
        {"product_key": [1]},
        {"customer_id": []},
        id="happy_path_no_matching_distinct_count",
    ),
    pytest.param(
        {"customer_id": [], "product_key": []},
        {"product_key": [1]},
        {"customer_id": []},
        id="edge_case_empty_table_1",
    ),
    pytest.param(
        {"customer_id": [1, 1, 2, 2], "product_key": [1, 2, 1, 3]},
        {"product_key": []},
        {"customer_id": []},
        id="edge_case_empty_table_2",
    ),
    pytest.param(
        {"customer_id": [], "product_key": []},
        {"product_key": []},
        {"customer_id": []},
        id="edge_case_both_tables_empty",
    ),
]


PARAMS_PROBLEM_1068 = [
    pytest.param(
        {
            "product_id": [1, 2, 3],
            "product_name": ["Nokia", "Nokia", "Apple"],
            "year": [2008, 2009, 2011],
            "price": [5000, 5000, 9000],
        },
        {"product_id": [1, 2, 3]},
        {
            "product_name": ["Nokia", "Nokia", "Apple"],
            "year": [2008, 2009, 2011],
            "price": [5000, 5000, 9000],
        },
        id="happy_path",
    )
]


PARAMS_PROBLEM_1070 = [
    pytest.param(
        {
            "sale_id": [1, 2, 7],
            "product_id": [100, 100, 200],
            "year": [2008, 2009, 2011],
            "quantity": [10, 12, 15],
            "price": [5000, 5000, 9000],
        },
        {
            "product_id": [100, 200],
            "first_year": [2008, 2011],
            "quantity": [10, 15],
            "price": [5000, 9000],
        },
        id="basic_case_with_distinct_products",
    ),
    pytest.param(
        {
            "sale_id": [1, 2, 3, 4, 5],
            "product_id": [100, 100, 200, 200, 200],
            "year": [2008, 2009, 2011, 2012, 2013],
            "quantity": [10, 20, 15, 5, 10],
            "price": [5000, 5000, 9000, 9000, 9000],
        },
        {
            "product_id": [100, 200],
            "first_year": [2008, 2011],
            "quantity": [10, 15],
            "price": [5000, 9000],
        },
        id="duplicates_with_minimum_year_aggregation",
    ),
]


PARAMS_PROBLEM_1075 = [
    pytest.param(
        {
            "employee_id": [1, 2, 3],
            "project_id": [101, 102, 103],
            "experience_years": [5, 10, 15],
        },
        {"employee_id": [1, 2, 3], "department": ["HR", "IT", "Finance"]},
        {"project_id": [101, 102, 103], "average_years": [5.0, 10.0, 15.0]},
        id="happy_path",
    ),
    pytest.param(
        {
            "employee_id": [1, 2, 3],
            "project_id": [101, 101, 101],
            "experience_years": [33, 34, 34],
        },
        {"employee_id": [1, 2, 3], "department": ["HR", "IT", "IT"]},
        {"project_id": [101], "average_years": [33.67]},
        id="happy_path_rounding_2",
    ),
]

PARAMS_PROBLEMS_1141 = [
    pytest.param(
        {
            "user_id": [1, 1, 1, 2, 2, 2],
            "session_id": [1, 1, 1, 4, 4, 4],
            "activity_date": [
                datetime(2019, 7, 20, 0, 0),
                datetime(2019, 7, 20, 0, 0),
                datetime(2019, 7, 20, 0, 0),
                datetime(2019, 7, 21, 0, 0),
                datetime(2019, 7, 21, 0, 0),
                datetime(2019, 7, 21, 0, 0),
            ],
            "activity_type": [
                "open_session",
                "scroll_down",
                "end_session",
                "open_session",
                "send_message",
                "end_session",
            ],
        },
        {
            "day": [
                datetime(2019, 7, 20, 0, 0),
                datetime(2019, 7, 21, 0, 0),
            ],
            "active_users": [1, 1],
        },
        id="happy_path_1",
    )
]

PARAMS_PROBLEM_1148 = [
    pytest.param(
        {
            "article_id": [1, 2, 3],
            "author_id": [3, 7, 4],
            "viewer_id": [3, 7, 4],
            "view_date": [
                datetime(2019, 8, 1),
                datetime(2019, 8, 1),
                datetime(2019, 7, 21),
            ],
        },
        {
            "id": [3, 4, 7],
        },
        id="happy_path",
    ),
    pytest.param(
        {
            "article_id": [1, 2],
            "author_id": [3, 7],
            "viewer_id": [3, 7],
            "view_date": [datetime(2019, 8, 1), datetime(2019, 8, 1)],
        },
        {
            "id": [3, 7],
        },
        id="all_match",
    ),
]

PARAMS_PROBLEM_1164 = [
    pytest.param(
        {
            "product_id": [1, 1, 2],
            "change_date": [
                datetime(2019, 8, 15),
                datetime(2019, 8, 16),
                datetime(2019, 8, 17),
            ],
            "new_price": [100, 110, 120],
        },
        {"product_id": [1, 2], "price": [110, 10]},
        id="happy-path",
    ),
    pytest.param(
        {
            "product_id": [1, 2],
            "change_date": [
                datetime(2019, 8, 17),
                datetime(2019, 8, 18),
            ],
            "new_price": [100, 110],
        },
        {"product_id": [1, 2], "price": [10, 10]},
        id="no-products-before-cutoff",
    ),
    pytest.param(
        {
            "product_id": [1],
            "change_date": [
                datetime(2019, 8, 18),
            ],
            "new_price": [20],
        },
        {"product_id": [1], "price": [10]},
        id="single-product-after-cutoff",
    ),
    pytest.param(
        {
            "product_id": [1, 2],
            "new_price": [100, 100],
            "change_date": [
                datetime(2019, 8, 1),
                datetime(2019, 8, 2),
            ],
        },
        {"product_id": [1, 2], "price": [100, 100]},
        id="all-products-before-cutoff",
    ),
]

PARAMS_PROBLEM_1193 = [
    pytest.param(
        {
            "trans_date": [
                datetime(2023, 1, 1),
                datetime(2023, 1, 15),
                datetime(2023, 2, 1),
            ],
            "state": ["approved", "pending", "approved"],
            "amount": [100, 200, 300],
            "country": ["US", "US", "CA"],
            "id": [1, 2, 3],
        },
        {
            "month": ["2023-01", "2023-02"],
            "country": ["US", "CA"],
            "trans_count": [2, 1],
            "approved_count": [1, 1],
            "trans_total_amount": [300, 300],
            "approved_total_amount": [100, 300],
        },
        id="happy_path_1",
    ),
    pytest.param(
        {
            "trans_date": [datetime(2023, 3, 1)],
            "state": ["approved"],
            "amount": [500],
            "country": [None],
            "id": [4],
        },
        {
            "month": ["2023-03"],
            "country": [None],
            "trans_count": [1],
            "approved_count": [1],
            "trans_total_amount": [500],
            "approved_total_amount": [500],
        },
        id="happy_path_null_country",
    ),
    pytest.param(
        {
            "trans_date": [datetime(2023, 4, 1), datetime(2023, 4, 2)],
            "state": ["pending", "rejected"],
            "amount": [150, 250],
            "country": ["FR", "FR"],
            "id": [5, 6],
        },
        {
            "month": ["2023-04"],
            "country": ["FR"],
            "trans_count": [2],
            "approved_count": [0],
            "trans_total_amount": [400],
            "approved_total_amount": [0],
        },
        id="edge_case_all_unapproved",
    ),
]

PARAMS_PROBLEM_1204 = [
    pytest.param(
        {
            "turn": [1, 2, 3, 4, 5],
            "person_name": ["Abe", "Bob", "Chloe", "Dylan", "Eve"],
            "weight": [200, 200, 200, 200, 200],
        },
        {"person_name": ["Eve"]},
        id="happy_path",
    ),
    pytest.param(
        {
            "turn": [1, 5, 4, 3, 2],
            "person_name": ["Abe", "Bob", "Chloe", "Dylan", "Eve"],
            "weight": [200, 200, 300, 300, 200],
        },
        {"person_name": ["Chloe"]},
        id="out_of_order",
    ),
    pytest.param(
        {
            "turn": [1, 2],
            "person_name": ["Abe", "Bob"],
            "weight": [900, 200],
        },
        {"person_name": ["Abe"]},
        id="not_equal_1k",
    ),
]


PARAMS_PROBLEM_1211 = [
    pytest.param(
        {
            "query_name": ["query1", "query1", "query2"],
            "rating": [4, 5, 2],
            "position": [2, 1, 1],
        },
        {
            "query_name": ["query1", "query2"],
            "quality": [3.5, 2.0],
            "poor_query_percentage": [0.0, 100.0],
        },
        id="happy_path_1",
    ),
    pytest.param(
        {
            "query_name": ["query1", "query2", "query2"],
            "rating": [3, 1, 5],
            "position": [1, 1, 1],
        },
        {
            "query_name": ["query1", "query2"],
            "quality": [3.0, 3.0],
            "poor_query_percentage": [0.0, 50.0],
        },
        id="happy_path_2",
    ),
]


PARAMS_PROBLEM_1251 = [
    pytest.param(
        {
            "product_id": [1, 1, 2, 2],
            "start_date": [
                datetime(2019, 2, 7),
                datetime(2019, 3, 1),
                datetime(2019, 2, 1),
                datetime(2019, 2, 21),
            ],
            "end_date": [
                datetime(2019, 2, 28),
                datetime(2019, 3, 22),
                datetime(2019, 2, 20),
                datetime(2019, 3, 31),
            ],
            "price": [5, 20, 15, 30],
        },
        {
            "product_id": [1, 1, 2, 2],
            "purchase_date": [
                datetime(2019, 2, 25),
                datetime(2019, 3, 1),
                datetime(2019, 2, 10),
                datetime(2019, 3, 22),
            ],
            "units": [100, 15, 200, 30],
        },
        {"product_id": [1, 2], "average_price": [6.96, 16.96]},
        id="two_products_with_purchases",
    ),
    pytest.param(
        {
            "product_id": [1, 1, 2, 2, 3],
            "start_date": [
                datetime(2019, 2, 7),
                datetime(2019, 3, 1),
                datetime(2019, 2, 1),
                datetime(2019, 2, 21),
                datetime(2019, 2, 21),
            ],
            "end_date": [
                datetime(2019, 2, 28),
                datetime(2019, 3, 22),
                datetime(2019, 2, 20),
                datetime(2019, 3, 31),
                datetime(2019, 3, 31),
            ],
            "price": [5, 20, 15, 30, 30],
        },
        {
            "product_id": [1, 1, 2, 2],
            "purchase_date": [
                datetime(2019, 2, 25),
                datetime(2019, 3, 1),
                datetime(2019, 2, 10),
                datetime(2019, 3, 22),
            ],
            "units": [100, 15, 200, 30],
        },
        {"product_id": [1, 2, 3], "average_price": [6.96, 16.96, 0]},
        id="two_products_with_purchases_one_missing",
    ),
]


PARAMS_PROBLEM_1280 = [
    pytest.param(
        {
            "student_id": [1, 2, 13, 6],
            "student_name": ["Alice", "Bob", "John", "Alex"],
        },
        {"subject_name": ["Math", "Physics", "Programming"]},
        {
            "student_id": [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
            "subject_name": [
                "Math",
                "Physics",
                "Programming",
                "Programming",
                "Physics",
                "Math",
                "Math",
                "Programming",
                "Physics",
                "Math",
                "Math",
            ],
        },
        {
            "student_id": [1, 1, 1, 2, 2, 2, 6, 6, 6, 13, 13, 13],
            "student_name": [
                "Alice",
                "Alice",
                "Alice",
                "Bob",
                "Bob",
                "Bob",
                "Alex",
                "Alex",
                "Alex",
                "John",
                "John",
                "John",
            ],
            "subject_name": [
                "Programming",
                "Physics",
                "Math",
                "Programming",
                "Math",
                "Physics",
                "Programming",
                "Physics",
                "Math",
                "Programming",
                "Physics",
                "Math",
            ],
            "attended_exams": [1, 2, 3, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        },
        id="happy_path",
    ),
    pytest.param(
        {
            "student_id": [1, 2, 13, 6],
            "student_name": ["Alice", "Bob", "John", None],
        },
        {"subject_name": ["Math", "Physics", "Programming"]},
        {
            "student_id": [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
            "subject_name": [
                "Math",
                "Physics",
                "Programming",
                "Programming",
                "Physics",
                "Math",
                "Math",
                "Programming",
                "Physics",
                "Math",
                "Math",
            ],
        },
        {
            "student_id": [1, 1, 1, 2, 2, 2, 6, 6, 6, 13, 13, 13],
            "student_name": [
                "Alice",
                "Alice",
                "Alice",
                "Bob",
                "Bob",
                "Bob",
                None,
                None,
                None,
                "John",
                "John",
                "John",
            ],
            "subject_name": [
                "Programming",
                "Physics",
                "Math",
                "Programming",
                "Math",
                "Physics",
                "Programming",
                "Physics",
                "Math",
                "Programming",
                "Physics",
                "Math",
            ],
            "attended_exams": [1, 2, 3, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        },
        id="happy_path_null_name",
    ),
]


PARAMS_PROBLEM_1321 = [
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
]


PARAMS_PROBLEM_1327 = [
    pytest.param(
        {"product_id": [1, 2], "product_name": ["Product A", "Product B"]},
        {
            "product_id": [1, 2],
            "order_date": [datetime(2020, 2, 15), datetime(2020, 2, 20)],
            "unit": [150, 50],
        },
        {"product_name": ["Product A"], "unit": [150]},
        id="happy_path_single_match",
    ),
    pytest.param(
        {"product_id": [1], "product_name": ["Product A"]},
        {"product_id": [1], "order_date": [datetime(2020, 3, 1)], "unit": [150]},
        {"product_name": [], "unit": []},
        id="no_matching_year_month",
    ),
    pytest.param(
        {"product_id": [1], "product_name": ["Product A"]},
        {"product_id": [1], "order_date": [datetime(2020, 2, 15)], "unit": [50]},
        {"product_name": [], "unit": []},
        id="no_products_with_unit_sum_gte_100",
    ),
]

PARAMS_PROBLEM_1378 = [
    pytest.param(
        {"id": [1, 2], "unique_id": [101, 102], "name": ["Alice", "Bob"]},
        {"id": [1, 2], "extra": ["x", "y"]},
        {"unique_id": [101, 102], "name": ["Alice", "Bob"]},
        id="happy_path_matching_ids",
    ),
    pytest.param(
        {"id": [1, 2], "unique_id": [101, 102], "name": ["Alice", "Bob"]},
        {"id": [3, 4], "extra": ["x", "y"]},
        {"unique_id": [101, 102], "name": ["Alice", "Bob"]},
        id="happy_path_non_matching_ids",
    ),
]


PARAMS_PROBLEM_1341 = [
    pytest.param(
        {"movie_id": [1, 2, 3], "title": ["Avengers", "Frozen 2", "Joker"]},
        {"user_id": [1, 2, 3, 4], "name": ["Daniel", "Monica", "Maria", "James"]},
        {
            "movie_id": [1, 1, 1, 1, 2, 2, 2, 3, 3],
            "user_id": [1, 2, 3, 4, 1, 2, 3, 1, 2],
            "rating": [3, 4, 2, 1, 5, 2, 2, 3, 4],
            "created_at": [
                datetime(2020, 1, 12),
                datetime(2020, 2, 11),
                datetime(2020, 2, 12),
                datetime(2020, 1, 1),
                datetime(2020, 2, 17),
                datetime(2020, 2, 1),
                datetime(2020, 3, 1),
                datetime(2020, 2, 22),
                datetime(2020, 2, 25),
            ],
        },
        {"results": ["Daniel", "Frozen 2"]},
        id="tied_length_name",
    ),
    pytest.param(
        {"movie_id": [1], "title": ["The Matrix"]},
        {"user_id": [1, 2, 3], "name": ["Neo", "Trinity", "Morpheus"]},
        {
            "movie_id": [1, 1, 1],
            "user_id": [1, 2, 3],
            "rating": [5, 5, 5],
            "created_at": [
                datetime(2020, 2, 1),
                datetime(2022, 1, 2),
                datetime(2022, 1, 3),
            ],
        },
        {"results": ["Morpheus", "The Matrix"]},
        id="single_movie_all_high_ratings",
    ),
]


PARAMS_PROBLEM_1484 = [
    pytest.param(
        {
            "sell_date": [
                datetime(2020, 5, 30),
                datetime(2020, 6, 1),
                datetime(2020, 6, 2),
                datetime(2020, 5, 30),
                datetime(2020, 6, 1),
                datetime(2020, 6, 2),
                datetime(2020, 5, 30),
            ],
            "product": [
                "Headphone",
                "Pencil",
                "Mask",
                "Basketball",
                "Bible",
                "Mask",
                "T-Shirt",
            ],
        },
        {
            "sell_date": [
                datetime(2020, 5, 30),
                datetime(2020, 6, 1),
                datetime(2020, 6, 2),
            ],
            "num_sold": [3, 2, 1],
            "products": [
                "Basketball,Headphone,T-Shirt",
                "Bible,Pencil",
                "Mask",
            ],
        },
        id="happy_path",
    ),
]

PARAMS_PROBLEM_1517 = [
    pytest.param(
        {
            "user_id": [1, 2, 3, 4, 5, 6, 7],
            "name": [
                "Winston",
                "Jonathan",
                "Annabelle",
                "Sally",
                "Marwan",
                "David",
                "Shapiro",
            ],
            "mail": [
                "winston@leetcode.com",
                "jonathanisgreat",
                "bella-@leetcode.com",
                "sally.come@leetcode.com",
                "quarz#2020@leetcode.com",
                "david69@gmail.com",
                ".shapo@leetcode.com",
            ],
        },
        {
            "user_id": [1, 3, 4],
            "name": [
                "Winston",
                "Annabelle",
                "Sally",
            ],
            "mail": [
                "winston@leetcode.com",
                "bella-@leetcode.com",
                "sally.come@leetcode.com",
            ],
        },
        id="happy_path",
    ),
    pytest.param(
        {
            "user_id": [360, 966, 901, 162, 181, 240, 221, 388, 211, 178],
            "name": [
                "Ezra",
                "Daniel",
                "Yehudah",
                "Daniel",
                "Aharon",
                "Gavriel",
                "Levi",
                "Eliyahu",
                "Michael",
                "Aharon",
            ],
            "mail": [
                "Ezra4VZabfK",
                "DanielEnEMjNoG6",
                "Yehudah*5m9@leetcode.com",
                "Daniel07L@leetcode.com",
                "AharonxuZA530S8Q",
                "GavrielLVC@leetcode.com",
                "Leviz6OzK@leetcode.com",
                "Eliyahu--wzsgX@leetcode.com",
                ".Michael@leetcode.com",
                "AharonnDFFSqcY",
            ],
        },
        {
            "user_id": [162, 240, 221, 388],
            "name": ["Daniel", "Gavriel", "Levi", "Eliyahu"],
            "mail": [
                "Daniel07L@leetcode.com",
                "GavrielLVC@leetcode.com",
                "Leviz6OzK@leetcode.com",
                "Eliyahu--wzsgX@leetcode.com",
            ],
        },
        id="happy_path_2",
    ),
]


PARAMS_PROBLEM_1581 = [
    pytest.param(
        {
            "visit_id": [1, 2, 5, 5, 5, 4, 6, 7, 8],
            "customer_id": [23, 9, 54, 54, 54, 30, 96, 54, 54],
        },
        {
            "visit_id": [1, 2, 5],
            "transaction_id": [12, 13, 9],
            "amount": [910, 970, 200],
        },
        {"customer_id": [30, 96, 54], "count_no_trans": [1, 1, 2]},
        id="happy_path",
    ),
    pytest.param(
        {"visit_id": [10, 11], "customer_id": [100, 101]},
        {"visit_id": [1, 2], "transaction_id": [12, 13], "amount": [910, 970]},
        {"customer_id": [100, 101], "count_no_trans": [1, 1]},
        id="no_matching_visit_id",
    ),
]

PARAMS_PROBLEM_1661 = [
    pytest.param(
        {
            "machine_id": [0, 0, 0, 0],
            "process_id": [0, 0, 1, 1],
            "activity_type": ["start", "end", "start", "end"],
            "timestamp": [0.712, 1.52, 3.14, 4.12],
        },
        {"machine_id": [0], "processing_time": [0.894]},
        id="happy_path_single_machine",
    ),
    pytest.param(
        {
            "machine_id": [0, 0, 1, 1, 2, 2],
            "process_id": [0, 0, 1, 1, 2, 2],
            "activity_type": ["start", "end", "start", "end", "start", "end"],
            "timestamp": [0.5, 1.5, 0.7, 1.2, 0.9, 2.0],
        },
        {"machine_id": [0, 1, 2], "processing_time": [1.0, 0.5, 1.1]},
        id="multiple_machines",
    ),
    pytest.param(
        {
            "machine_id": [0, 0, 1],
            "process_id": [0, 0, 1],
            "activity_type": ["start", "end", "start"],
            "timestamp": [0.5, 1.5, 0.7],
        },
        {"machine_id": [0, 1], "processing_time": [1.0, None]},
        id="incomplete_process",
    ),
]

PARAMS_PROBLEM_1683 = [
    pytest.param(
        {"tweet_id": [1, 2], "content": ["Short", "This is a long tweet"]},
        {"tweet_id": [2]},
        id="content_greater_than_15",
    ),
    pytest.param(
        {
            "tweet_id": [1, 2],
            "content": ["This is a long tweet", "Another long tweet"],
        },
        {"tweet_id": [1, 2]},
        id="all_content_greater_than_15",
    ),
]

PARAMS_PROBLEM_1729 = [
    pytest.param(
        {"user_id": [1, 1, 2, 2, 3], "follower_id": [10, 11, 12, 13, 14]},
        {"user_id": [1, 2, 3], "followers_count": [2, 2, 1]},
        id="multiple_users",
    ),
    pytest.param(
        {"user_id": [1], "follower_id": [10]},
        {"user_id": [1], "followers_count": [1]},
        id="single_user",
    ),
    pytest.param(
        {"user_id": [1, 1, 1], "follower_id": [10, 11, 12]},
        {"user_id": [1], "followers_count": [3]},
        id="single_user_multiple_followers",
    ),
]

PARAMS_PROBLEM_1757 = [
    (
        {
            "product_id": [0, 1, 2, 3, 4],
            "low_fats": ["Y", "Y", "N", "Y", "N"],
            "recyclable": ["N", "Y", "Y", "Y", "N"],
        },
        {"product_id": [1, 3]},
    ),
    (
        {
            "product_id": [0, 1, 2, 3, 4],
            "low_fats": ["Y", "Y", "Y", "Y", "Y"],
            "recyclable": ["Y", "Y", "Y", "Y", "Y"],
        },
        {"product_id": [0, 1, 2, 3, 4]},
    ),
]

PARAMS_PROBLEM_1789 = [
    pytest.param(
        {"employee_id": [1], "department_id": [101], "primary_flag": ["Y"]},
        {"employee_id": [1], "department_id": [101]},
        id="single_employee_primary_Y",
    ),
    pytest.param(
        {
            "employee_id": [1, 2, 2],
            "department_id": [101, 102, 103],
            "primary_flag": ["N", "Y", "N"],
        },
        {"employee_id": [1, 2], "department_id": [101, 102]},
        id="multiple_employees_one_primary_Y",
    ),
    pytest.param(
        {"employee_id": [1], "department_id": [101], "primary_flag": ["N"]},
        {"employee_id": [1], "department_id": [101]},
        id="single_employee_no_primary_Y",
    ),
    pytest.param(
        {
            "employee_id": [1, 1, 2, 2, 3, 3],
            "department_id": [101, 102, 101, 102, 101, 102],
            "primary_flag": ["Y", "N", "Y", "N", "Y", "N"],
        },
        {"employee_id": [1, 2, 3], "department_id": [101, 101, 101]},
        id="all_employees_multiple_departments",
    ),
]

PARAMS_PROBLEM_1907 = [
    pytest.param(
        {"account_id": [1, 2, 3], "income": [10000, 25000, 100000]},
        {
            "category": ["Low Salary", "Average Salary", "High Salary"],
            "accounts_count": [1, 1, 1],
        },
        id="all_three_salary_categories",
    ),
    pytest.param(
        {"account_id": [1, 2], "income": [10000, 25000]},
        {
            "category": ["Low Salary", "Average Salary", "High Salary"],
            "accounts_count": [1, 1, 0],
        },
        id="missing_one_salary_category",
    ),
]

PARAMS_PROBLEM_1934 = [
    pytest.param(
        {"user_id": [1]},
        {"user_id": [1], "action": ["confirmed"]},
        {"user_id": [1], "confirmation_rate": [1.0]},
        id="user_confirmed",
    ),
    pytest.param(
        {"user_id": [1]},
        {"user_id": [1, 1], "action": ["confirmed", "confirmed"]},
        {"user_id": [1], "confirmation_rate": [1.0]},
        id="same_user_twice_confirmed",
    ),
    pytest.param(
        {"user_id": [1]},
        {"user_id": [1], "action": ["pending"]},
        {"user_id": [1], "confirmation_rate": [0.0]},
        id="user_not_confirmed",
    ),
    pytest.param(
        {"user_id": []},
        {"user_id": [], "action": []},
        {"user_id": [], "confirmation_rate": []},
        id="empty_tables",
    ),
    pytest.param(
        {"user_id": [1]},
        {"user_id": [1, 1], "action": ["confirmed", "pending"]},
        {"user_id": [1], "confirmation_rate": [0.5]},
        id="mixed_actions",
    ),
]

PARAMS_PROBLEM_1978 = [
    pytest.param(
        {
            "employee_id": [3, 12, 13, 1, 9, 11, 14],
            "name": [
                "Mila",
                "Antonella",
                "Emery",
                "Kalel",
                "Mikaela",
                "Joziah",
                "Hayden",
            ],
            "manager_id": [9.0, None, None, 11.0, None, 6.0, None],
            "salary": [60301, 31000, 67084, 21241, 50937, 28485, 4123],
        },
        {"employee_id": [11]},
        id="basic_filtering",
    ),
    pytest.param(
        {
            "employee_id": [3, 12, 13, 1, 9, 11, 14],
            "name": [
                "Mila",
                "Antonella",
                "Emery",
                "Kalel",
                "Mikaela",
                "Joziah",
                "Hayden",
            ],
            "manager_id": [9.0, None, None, 11.0, None, 6.0, None],
            "salary": [60301, 31000, 67084, 31241, 50937, 38485, 41230],
        },
        {"employee_id": []},
        id="no_low_salary",
    ),
    pytest.param(
        {
            "employee_id": [3, 12, 13, 1, 9, 11, 14],
            "name": [
                "Mila",
                "Antonella",
                "Emery",
                "Kalel",
                "Mikaela",
                "Joziah",
                "Hayden",
            ],
            "manager_id": [3, 12, 13, 1, 9, 11, 14],
            "salary": [60301, 31000, 67084, 21241, 50937, 28485, 4123],
        },
        {"employee_id": []},
        id="all_managers_are_employees",
    ),
    pytest.param(
        {
            "employee_id": [3, 12, 13, 1, 9, 11, 14],
            "name": [
                "Mila",
                "Antonella",
                "Emery",
                "Kalel",
                "Mikaela",
                "Joziah",
                "Hayden",
            ],
            "manager_id": [None, None, None, None, None, None, None],
            "salary": [60301, 31000, 67084, 21241, 50937, 28485, 4123],
        },
        {"employee_id": []},
        id="all_manager_ids_null",
    ),
]

PARAMS_PROBLEM_2356 = [
    pytest.param(
        {"teacher_id": [1, 1, 2, 2], "subject_id": [101, 102, 101, 103]},
        {"teacher_id": [1, 2], "cnt": [2, 2]},
        id="multiple_teachers_distinct_subjects",
    ),
    pytest.param(
        {"teacher_id": [1], "subject_id": [101]},
        {"teacher_id": [1], "cnt": [1]},
        id="single_teacher_single_subject",
    ),
    pytest.param(
        {"teacher_id": [1], "subject_id": [101]},
        {"teacher_id": [1], "cnt": [1]},
        id="single_teacher_repeated_subjects",
    ),
]
