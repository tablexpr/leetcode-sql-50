from datetime import datetime

import pyarrow as pa
import pytest

from problems.leetcode import (
    problem_197,
    problem_577,
    problem_584,
    problem_595,
    problem_610,
    problem_620,
    problem_1068,
    problem_1075,
    problem_1141,
    problem_1148,
    problem_1161,
    problem_1211,
    problem_1280,
    problem_1378,
    problem_1581,
    problem_1683,
    problem_1757,
    problem_1978,
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
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("id", pa.int64())])
    )
    result = problem_197(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {"empId": [1, 2], "name": ["Alice", "Bob"]},
            {"empId": [1, 2], "bonus": [1000, 1500]},
            {"name": ["Alice", "Bob"], "bonus": [1000, 1500]},
            id="happy_path_basic",
        )
    ],
)
def test_problem_577(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_577(table_1, table_2)
    assert result.equals(expected_table)


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
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("name", pa.string())])
    )
    result = problem_584(input_table)
    assert result.equals(expected_table)


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
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_595(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_610(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_610(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_620(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data,
        schema=pa.schema(
            [pa.field("id", pa.int64()), pa.field("description", pa.string())]
        ),
    )
    result = problem_620(table)
    assert result.equals(expected_table)


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
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1068(table_1, table_2)
    assert result.equals(expected_table)


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
            {"project_id": [101, 102, 103], "experience_years": [5.0, 10.0, 15.0]},
            id="happy_path",
        ),
        pytest.param(
            {
                "employee_id": [1, 2, 3],
                "project_id": [101, 101, 101],
                "experience_years": [33, 34, 34],
            },
            {"employee_id": [1, 2, 3], "department": ["HR", "IT", "IT"]},
            {"project_id": [101], "experience_years": [33.67]},
            id="happy_path_rounding_2",
        ),
    ],
)
def test_problem_1075(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1075(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_1141(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result_table = problem_1141(input_table)
    assert result_table.equals(expected_table)


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
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1148(input_table)
    assert result.equals(expected_table)


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
def test_problem_1161(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1161(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_1211(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1211(table)
    assert result.equals(expected_table)


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
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    table_3 = pa.Table.from_pydict(input_data_3)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1280(table_1, table_2, table_3)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "table_data, table_2_data, expected_data",
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
def test_problem_1378(table_data, table_2_data, expected_data):
    table = pa.Table.from_pydict(table_data)
    table_2 = pa.Table.from_pydict(table_2_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1378(table, table_2)
    assert result.equals(expected_table)


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
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    result = problem_1581(table_1, table_2)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


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
    table = pa.Table.from_pydict(input_data)
    result = problem_1683(table)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


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
        )
    ],
    ids=[
        "happy_path_mixed_values",
    ],
)
def test_problem_1757(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    result = problem_1757(table)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_1978(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("employee_id", pa.int64())])
    )
    result = problem_1978(table)
    assert result.equals(expected_table)
