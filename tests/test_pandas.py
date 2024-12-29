from datetime import datetime

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from problems.pandas import (
    problem_176,
    problem_180,
    problem_197,
    problem_570,
    problem_577,
    problem_584,
    problem_595,
    problem_620,
    problem_1068,
    problem_1075,
    problem_1148,
    problem_1251,
    problem_1280,
    problem_1321,
    problem_1327,
    problem_1378,
    problem_1517,
    problem_1581,
    problem_1661,
    problem_1683,
    problem_1757,
    problem_1934,
)


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
    result = problem_176(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


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
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_180(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_197(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_197(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_570(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data).reset_index(drop=True)
    result = problem_570(table)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
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
    ],
)
def test_problem_577(input_data_1, input_data_2, expected_data):
    table_1 = pd.DataFrame(input_data_1)
    table_2 = pd.DataFrame(input_data_2)
    expected_table = pd.DataFrame(expected_data).reset_index(drop=True)
    result = problem_577(table_1, table_2)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_584(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_584(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_595(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_595(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "id": [1, 2, 3, 4],
                "description": ["interesting", "boring", "exciting", "boring"],
                "rating": [3, 1, 1, 1],
            },
            {
                "id": [1, 3],
                "description": ["interesting", "exciting"],
                "rating": [3, 1],
            },
            id="happy_path_mixed_ids_and_descriptions",
        ),
        pytest.param(
            {"id": [1, 3], "description": ["boring", "boring"], "rating": [1, 1]},
            {"id": [], "description": [], "rating": []},
            id="edge_case_all_boring",
        ),
        pytest.param(
            {
                "id": [2, 4],
                "description": ["interesting", "exciting"],
                "rating": [1, 1],
            },
            {"id": [], "description": [], "rating": []},
            id="edge_case_no_odd_ids",
        ),
        pytest.param(
            {"id": [1], "description": ["interesting"], "rating": [1]},
            {"id": [1], "description": ["interesting"], "rating": [1]},
            id="edge_case_single_row_matching",
        ),
        pytest.param(
            {"id": [2], "description": ["boring"], "rating": [1]},
            {"id": [], "description": [], "rating": []},
            id="edge_case_single_row_not_matching",
        ),
    ],
)
def test_problem_620(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_620(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
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
    ],
)
def test_problem_1068(input_data_1, input_data_2, expected_data):
    table_1 = pd.DataFrame(input_data_1)
    table_2 = pd.DataFrame(input_data_2)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1068(table_1, table_2).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
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
    ],
)
def test_problem_1075(input_data_1, input_data_2, expected_data):
    table_1 = pd.DataFrame(input_data_1)
    table_2 = pd.DataFrame(input_data_2)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1075(table_1, table_2).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_1148(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1148(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
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
    ],
)
def test_problem_1251(input_data_1, input_data_2, expected_data):
    table_1 = pd.DataFrame(input_data_1)
    table_2 = pd.DataFrame(input_data_2)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1251(table_1, table_2).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data_1, input_data_2, input_data_3, expected_data",
    [
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
    ],
)
def test_problem_1280(input_data_1, input_data_2, input_data_3, expected_data):
    table_1 = pd.DataFrame(input_data_1)
    table_2 = pd.DataFrame(input_data_2)
    table_3 = pd.DataFrame(input_data_3)
    expected_table = (
        pd.DataFrame(expected_data)
        .sort_values(["student_id", "subject_name"])
        .reset_index(drop=True)
    )
    result = (
        problem_1280(table_1, table_2, table_3)
        .sort_values(["student_id", "subject_name"])
        .reset_index(drop=True)
    )
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


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
    expected_table = pd.DataFrame(expected_data)
    result = problem_1321(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
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
    ],
)
def test_problem_1327(input_data_1, input_data_2, expected_data):
    table_1 = pd.DataFrame(input_data_1)
    table_2 = pd.DataFrame(input_data_2)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1327(table_1, table_2).reset_index(drop=True)

    assert_frame_equal(result, expected_table, check_dtype=False, check_index_type=True)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
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
    ],
)
def test_problem_1378(input_data_1, input_data_2, expected_data):
    table_1 = pd.DataFrame(input_data_1)
    table_2 = pd.DataFrame(input_data_2)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1378(table_1, table_2).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_1517(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1517(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
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
    ],
)
def test_problem_1581(input_data_1, input_data_2, expected_data):
    table_1 = pd.DataFrame(input_data_1)
    table_2 = pd.DataFrame(input_data_2)
    expected_table = (
        pd.DataFrame(expected_data).sort_values(by="customer_id").reset_index(drop=True)
    )
    result = problem_1581(table_1, table_2).sort_values(by="customer_id")

    assert_frame_equal(result, expected_table, check_dtype=False, check_index_type=True)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_1661(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1661(table)

    assert_frame_equal(result, expected_table, check_dtype=False, check_index_type=True)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        (
            {"tweet_id": [1, 2], "content": ["Short", "This is a long tweet"]},
            {"tweet_id": [2]},
        ),
        (
            {
                "tweet_id": [1, 2],
                "content": ["This is a long tweet", "Another long tweet"],
            },
            {"tweet_id": [1, 2]},
        ),
    ],
    ids=[
        "content_greater_than_15",
        "all_content_greater_than_15",
    ],
)
def test_problem_1683(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1683(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
    ids=["happy_path_mixed_values", "all_ys"],
)
def test_problem_1757(input_data, expected_data):
    table = pd.DataFrame(input_data)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1757(table).reset_index(drop=True)
    assert_frame_equal(
        result, expected_table, check_dtype=False, check_index_type=False
    )


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
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
    ],
)
def test_problem_1934(input_data_1, input_data_2, expected_data):
    table_1 = pd.DataFrame(input_data_1)
    table_2 = pd.DataFrame(input_data_2)
    expected_table = pd.DataFrame(expected_data)
    result = problem_1934(table_1, table_2).reset_index(drop=True)
    assert_frame_equal(result, expected_table, check_dtype=False, check_index_type=True)
