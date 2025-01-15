from datetime import datetime

import pyarrow as pa
import pytest

from problems.datafusion import *
from tests.test_problem_params import *


@pytest.mark.parametrize("input_data, expected_data", PARAMS_PROBLEM_176)
def test_problem_176(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_176(table)
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_180,
)
def test_problem_180(input_data, expected_data):
    table = pa.Table.from_pydict(
        input_data,
        schema=pa.schema([pa.field("id", pa.int64()), pa.field("num", pa.int64())]),
    )
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("ConsecutiveNums", pa.int64())])
    )
    result = problem_180(table)
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_584,
)
def test_problem_584(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("name", pa.string())])
    )
    result = problem_584(input_table)
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_595,
)
def test_problem_595(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_595(input_table)
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_620,
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
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1068,
)
def test_problem_1068(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(
        expected_data,
    )
    result = problem_1068(table_1, table_2)
    assert result.to_arrow_table().equals(expected_table)


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
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data,
    )
    result = problem_1148(table)
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1321,
)
def test_problem_1321(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1321(table)
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1378,
)
def test_problem_1378(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1378(table_1, table_2)
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
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
    ],
)
def test_problem_1484(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1484(table)
    assert (
        result.to_arrow_table()
        .cast(
            pa.schema(
                [
                    pa.field("sell_date", pa.timestamp("us")),
                    pa.field("num_sold", pa.int64()),
                    pa.field("products", pa.utf8()),
                ]
            )
        )
        .equals(expected_table)
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
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1517(table)
    assert result.to_arrow_table().equals(expected_table)


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
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1683(table)
    assert result.to_arrow_table().equals(expected_table)


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
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1757(table)
    assert result.to_arrow_table().equals(expected_table)
