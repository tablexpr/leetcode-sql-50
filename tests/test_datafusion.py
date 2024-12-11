from datetime import datetime

import pyarrow as pa
import pytest

from problems.datafusion import (
    problem_176,
    problem_620,
    problem_1321,
    problem_1484,
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
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_176(table)
    assert result.to_arrow_table().equals(expected_table)


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
    assert result.to_arrow_table().equals(expected_table)


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
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1321(table)
    assert result.equals(expected_table)


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
    result = problem_1484(table).to_pydict()
    assert result == expected_data
