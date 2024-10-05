from datetime import datetime

import pandas as pd
import pyarrow as pa
import pytest

from problems.leetcode import (
    problem_197,
    problem_584,
    problem_595,
    problem_620,
    problem_1141,
    problem_1148,
    problem_1378,
    problem_1683,
    problem_1757,
    problem_1978,
)


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 2)],
                "temperature": [20, 25],
                "id": [1, 2],
            },
            [2],
            id="happy_path_basic",
        ),
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 2)],
                "temperature": [25, 25],
                "id": [1, 2],
            },
            [],
            id="no_temperature_increase",
        ),
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1)],
                "temperature": [20],
                "id": [1],
            },
            [],
            id="single_record",
        ),
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 2)],
                "temperature": [25, 20],
                "id": [1, 2],
            },
            [],
            id="temperature_decrease",
        ),
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 3)],
                "temperature": [20, 25],
                "id": [1, 2],
            },
            [],
            id="skip_a_day",
        ),
    ],
)
def test_problem_197(input_data, expected_output):
    table = pa.table(input_data)
    result = problem_197(table)
    assert result["id"].to_pylist() == expected_output


@pytest.mark.parametrize(
    "input_data, expected_names",
    [
        pytest.param(
            {
                "id": [1, 2, 4, 5],
                "name": ["Will", "Jane", "Bill", "Zack"],
                "referee_id": [None, None, None, 1],
            },
            ["Will", "Jane", "Bill", "Zack"],
            id="happy_path_all_valid",
        ),
        pytest.param(
            {
                "id": [],
                "name": [],
                "referee_id": [],
            },
            [],
            id="edge_case_empty_table",
        ),
        pytest.param(
            {
                "id": [3, 6],
                "name": ["Alex", "Mark"],
                "referee_id": [2, 2],
            },
            [],
            id="edge_case_all_referee_id_2",
        ),
        pytest.param(
            {
                "id": [1, 3, 5, 6],
                "name": ["Will", "Alex", "Zack", "Mark"],
                "referee_id": [None, 2, 1, 2],
            },
            ["Will", "Zack"],
            id="mixed_case_some_valid",
        ),
    ],
)
def test_problem_584(input_data, expected_names):
    input_table = pa.table(input_data)
    result_table = problem_584(input_table)
    result_names = result_table.column("name").to_pylist()
    assert result_names == expected_names


@pytest.mark.parametrize(
    "input_data, expected_output",
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
                "name": [],
                "continent": [],
                "area": [],
                "population": [],
                "gdp": [],
            },
            {"name": [], "population": [], "area": []},
            id="edge_case_empty_table",
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
def test_problem_595(input_data, expected_output):
    input_schema = pa.schema(
        [
            pa.field("name", pa.string()),
            pa.field("continent", pa.string()),
            pa.field("area", pa.int64()),
            pa.field("population", pa.int64()),
            pa.field("gdp", pa.int64()),
        ]
    )
    input_table = pa.table(input_data, schema=input_schema)
    output_schema = pa.schema(
        [
            pa.field("name", pa.string()),
            pa.field("population", pa.int64()),
            pa.field("area", pa.int64()),
        ]
    )
    output_table = pa.table(expected_output, schema=output_schema)
    result = problem_595(input_table)
    assert result.equals(output_table)


@pytest.mark.parametrize(
    "input_data, expected_ids",
    [
        pytest.param(
            [
                {"id": 1, "description": "interesting"},
                {"id": 2, "description": "boring"},
                {"id": 3, "description": "exciting"},
                {"id": 4, "description": "boring"},
            ],
            [3, 1],
            id="happy_path_mixed_ids_and_descriptions",
        ),
        pytest.param(
            [
                {"id": 1, "description": "boring"},
                {"id": 3, "description": "boring"},
            ],
            [],
            id="edge_case_all_boring",
        ),
        pytest.param(
            [
                {"id": 2, "description": "interesting"},
                {"id": 4, "description": "exciting"},
            ],
            [],
            id="edge_case_no_odd_ids",
        ),
        pytest.param(
            [
                {"id": 1, "description": "interesting"},
            ],
            [1],
            id="edge_case_single_row_matching",
        ),
        pytest.param(
            [
                {"id": 2, "description": "boring"},
            ],
            [],
            id="edge_case_single_row_not_matching",
        ),
    ],
)
def test_problem_620(input_data, expected_ids):
    table = pa.Table.from_pylist(input_data)
    result = problem_620(table)
    result_ids = result.column("id").to_pylist()
    assert result_ids == expected_ids


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            [
                {
                    "user_id": 1,
                    "session_id": 1,
                    "activity_date": datetime(2019, 7, 20),
                    "activity_type": "open_session",
                },
                {
                    "user_id": 1,
                    "session_id": 1,
                    "activity_date": datetime(2019, 7, 20),
                    "activity_type": "scroll_down",
                },
                {
                    "user_id": 1,
                    "session_id": 1,
                    "activity_date": datetime(2019, 7, 20),
                    "activity_type": "end_session",
                },
                {
                    "user_id": 2,
                    "session_id": 4,
                    "activity_date": datetime(2019, 7, 21),
                    "activity_type": "open_session",
                },
                {
                    "user_id": 2,
                    "session_id": 4,
                    "activity_date": datetime(2019, 7, 21),
                    "activity_type": "send_message",
                },
                {
                    "user_id": 2,
                    "session_id": 4,
                    "activity_date": datetime(2019, 7, 21),
                    "activity_type": "end_session",
                },
            ],
            [
                {"day": datetime(2019, 7, 20), "active_users": 1},
                {"day": datetime(2019, 7, 21), "active_users": 1},
            ],
            id="happy_path_1",
        )
    ],
)
def test_problem_1141(input_data, expected_data):
    input_table = pa.Table.from_pylist(input_data)
    expected_table = pa.Table.from_pylist(expected_data)
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
    input_schema = pa.schema(
        [
            pa.field("article_id", pa.int64()),
            pa.field("author_id", pa.int64()),
            pa.field("viewer_id", pa.int64()),
            pa.field("view_date", pa.timestamp("ns")),
        ]
    )
    input_table = pa.table(input_data, schema=input_schema)
    expected_schema = pa.schema([pa.field("id", pa.int64())])
    expected_table = pa.table(expected_data, schema=expected_schema)
    result = problem_1148(input_table)
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
    expected = pa.Table.from_pydict(expected_data)
    result = problem_1378(table, table_2)
    assert result.equals(expected)


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        (
            pa.table(
                {"tweet_id": [1, 2], "content": ["Short", "This is a long tweet"]}
            ),
            pa.table({"tweet_id": [2]}),
        ),
        (
            pa.table(
                {
                    "tweet_id": [1, 2],
                    "content": ["This is a long tweet", "Another long tweet"],
                }
            ),
            pa.table({"tweet_id": [1, 2]}),
        ),
    ],
    ids=[
        "content_greater_than_15",
        "all_content_greater_than_15",
    ],
)
def test_problem_1683(input_data, expected_output):
    result = problem_1683(input_data)
    assert result.equals(expected_output)


@pytest.mark.parametrize(
    "data, expected_ids",
    [
        (
            [
                ["0", "Y", "N"],
                ["1", "Y", "Y"],
                ["2", "N", "Y"],
                ["3", "Y", "Y"],
                ["4", "N", "N"],
            ],
            [1, 3],
        )
    ],
    ids=[
        "happy_path_mixed_values",
    ],
)
def test_problem_1757(data, expected_ids):
    table = pa.Table.from_pandas(
        pd.DataFrame(data, columns=["product_id", "low_fats", "recyclable"]).astype(
            {"product_id": "int64", "low_fats": "category", "recyclable": "category"}
        )
    )
    result = problem_1757(table)
    assert result.column("product_id").to_pylist() == expected_ids


@pytest.mark.parametrize(
    "data, expected_ids",
    [
        pytest.param(
            [
                [3, "Mila", 9, 60301],
                [12, "Antonella", None, 31000],
                [13, "Emery", None, 67084],
                [1, "Kalel", 11, 21241],
                [9, "Mikaela", None, 50937],
                [11, "Joziah", 6, 28485],
                [14, "Hayden", None, 4123],
            ],
            [11],
            id="basic_filtering",
        ),
        pytest.param(
            [
                [3, "Mila", 9, 60301],
                [12, "Antonella", None, 31000],
                [13, "Emery", None, 67084],
                [1, "Kalel", 11, 31241],
                [9, "Mikaela", None, 50937],
                [11, "Joziah", 6, 38485],
                [14, "Hayden", None, 41230],
            ],
            [],
            id="no_low_salary",
        ),
        pytest.param(
            [
                [3, "Mila", 3, 60301],
                [12, "Antonella", 12, 31000],
                [13, "Emery", 13, 67084],
                [1, "Kalel", 1, 21241],
                [9, "Mikaela", 9, 50937],
                [11, "Joziah", 11, 28485],
                [14, "Hayden", 14, 4123],
            ],
            [],
            id="all_managers_are_employees",
        ),
        pytest.param(
            [
                [3, "Mila", None, 60301],
                [12, "Antonella", None, 31000],
                [13, "Emery", None, 67084],
                [1, "Kalel", None, 21241],
                [9, "Mikaela", None, 50937],
                [11, "Joziah", None, 28485],
                [14, "Hayden", None, 4123],
            ],
            [],
            id="all_manager_ids_null",
        ),
    ],
)
def test_problem_1978(data, expected_ids):
    table = pa.Table.from_pandas(
        pd.DataFrame(data, columns=["employee_id", "name", "manager_id", "salary"])
    )
    result = problem_1978(table)
    assert result.column("employee_id").to_pylist() == expected_ids
