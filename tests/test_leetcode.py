from datetime import datetime

import pandas as pd
import pyarrow as pa
import pytest

from problems.leetcode import (
    problem_197,
    problem_584,
    problem_595,
    problem_1148,
    problem_1683,
    problem_1757,
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
            [
                [1, "Will", None],
                [2, "Jane", None],
                [4, "Bill", None],
                [5, "Zack", 1],
            ],
            ["Will", "Jane", "Bill", "Zack"],
            id="happy_path_all_valid",
        ),
        pytest.param([], [], id="edge_case_empty_table"),
        pytest.param(
            [
                [3, "Alex", 2],
                [6, "Mark", 2],
            ],
            [],
            id="edge_case_all_referee_id_2",
        ),
        pytest.param(
            [
                [1, "Will", None],
                [3, "Alex", 2],
                [5, "Zack", 1],
                [6, "Mark", 2],
            ],
            ["Will", "Zack"],
            id="mixed_case_some_valid",
        ),
    ],
)
def test_problem_584(input_data, expected_names):
    input_table = pa.Table.from_pandas(
        pd.DataFrame(input_data, columns=["id", "name", "referee_id"])
    )
    result_table = problem_584(input_table)
    result_names = result_table.column("name").to_pylist()
    assert result_names == expected_names


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        pytest.param(
            [
                ["Afghanistan", "Asia", 652_230, 25_500_100, 20343000000],
                ["Albania", "Europe", 28_748, 2_831_741, 12_960_000_000],
                ["Algeria", "Africa", 2_381_741, 37_100_000, 188_681_000_000],
                ["Andorra", "Europe", 468, 78_115, 3_712_000_000],
                ["Angola", "Africa", 1_246_700, 20_609_294, 100_990_000_000],
            ],
            [
                ["Afghanistan", 25_500_100, 652_230],
                ["Algeria", 37_100_000, 2_381_741],
            ],
            id="happy_path_various_countries",
        ),
        pytest.param([], [], id="edge_case_empty_table"),
        pytest.param(
            [
                ["CountryA", "ContinentA", 3_000_000, 30_000_000, 1_000_000_000],
                ["CountryB", "ContinentB", 4_000_000, 40_000_000, 2_000_000_000],
            ],
            [
                ["CountryA", 30_000_000, 3000_000],
                ["CountryB", 40_000_000, 4000_000],
            ],
            id="edge_case_all_countries_meeting_criteria",
        ),
    ],
)
def test_problem_595(input_data, expected_output):
    input_table = pa.Table.from_pandas(
        pd.DataFrame(
            input_data, columns=["name", "continent", "area", "population", "gdp"]
        )
    )
    result = problem_595(input_table)
    expected_table = pa.Table.from_pandas(
        pd.DataFrame(expected_output, columns=["name", "population", "area"])
    )
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            pa.table(
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
                schema=pa.schema(
                    [
                        pa.field("article_id", pa.int64()),
                        pa.field("author_id", pa.int64()),
                        pa.field("viewer_id", pa.int64()),
                        pa.field("view_date", pa.timestamp("ns")),
                    ]
                ),
            ),
            pa.table(
                {
                    "id": [3, 4, 7],
                }
            ),
            id="happy_path",
        ),
        pytest.param(
            pa.table(
                {
                    "article_id": [1, 2],
                    "author_id": [3, 7],
                    "viewer_id": [3, 7],
                    "view_date": [datetime(2019, 8, 1), datetime(2019, 8, 1)],
                },
                schema=pa.schema(
                    [
                        pa.field("article_id", pa.int64()),
                        pa.field("author_id", pa.int64()),
                        pa.field("viewer_id", pa.int64()),
                        pa.field("view_date", pa.timestamp("ns")),
                    ]
                ),
            ),
            pa.table(
                {
                    "id": [3, 7],
                }
            ),
            id="all_match",
        ),
    ],
)
def test_problem_1148(input_data, expected_data):
    result = problem_1148(input_data)
    assert result.equals(expected_data)


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
