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
                ["Afghanistan", "Asia", 652230, 25500100, 20343000000],
                ["Albania", "Europe", 28748, 2831741, 12960000000],
                ["Algeria", "Africa", 2381741, 37100000, 188681000000],
                ["Andorra", "Europe", 468, 78115, 3712000000],
                ["Angola", "Africa", 1246700, 20609294, 100990000000],
            ],
            [
                ["Afghanistan", 25500100, 652230],
                ["Algeria", 37100000, 2381741],
            ],
            id="happy_path_various_countries",
        ),
        pytest.param([], [], id="edge_case_empty_table"),
        pytest.param(
            [
                ["CountryA", "ContinentA", 3000000, 30000000, 1000000000],
                ["CountryB", "ContinentB", 4000000, 40000000, 2000000000],
            ],
            [
                ["CountryA", 30000000, 3000000],
                ["CountryB", 40000000, 4000000],
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
            [
                {
                    "article_id": 1,
                    "author_id": 3,
                    "viewer_id": 3,
                    "view_date": "2019-08-01",
                },
                {
                    "article_id": 2,
                    "author_id": 7,
                    "viewer_id": 7,
                    "view_date": "2019-08-01",
                },
                {
                    "article_id": 3,
                    "author_id": 4,
                    "viewer_id": 4,
                    "view_date": "2019-07-21",
                },
            ],
            [{"id": 3}, {"id": 4}, {"id": 7}],
            id="happy_path",
        ),
        pytest.param(
            [
                {
                    "article_id": 1,
                    "author_id": 3,
                    "viewer_id": 3,
                    "view_date": "2019-08-01",
                },
                {
                    "article_id": 2,
                    "author_id": 7,
                    "viewer_id": 7,
                    "view_date": "2019-08-01",
                },
            ],
            [{"id": 3}, {"id": 7}],
            id="all_match",
        ),
    ],
)
def test_problem_1148(input_data, expected_data):
    input_table = pa.Table.from_pylist(input_data)
    result = problem_1148(input_table)
    expected_table = pa.Table.from_pylist(expected_data)
    assert result.equals(expected_table)


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
