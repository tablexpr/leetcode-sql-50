from datetime import datetime

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from problems.pandas import (
    problem_176,
    problem_180,
    problem_197,
    problem_577,
    problem_584,
    problem_595,
    problem_1068,
    problem_1148,
    problem_1321,
    problem_1378,
    problem_1581,
    problem_1661,
    problem_1683,
    problem_1757,
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
    result = problem_176(table)
    assert result.equals(expected_table)


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
    if result.shape == (0, len(expected_table.columns)):
        assert result.shape == expected_table.shape
        assert result.columns.equals(expected_table.columns)
    else:
        assert result.equals(
            expected_table
        ), f"Expected table {expected_table}, but got {result}"


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
    if result.shape == (0, len(expected_table.columns)):
        assert result.shape == expected_table.shape
        assert result.columns.equals(expected_table.columns)
    else:
        assert result.equals(
            expected_table
        ), f"Expected table {expected_table}, but got {result}"


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
        )
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
    if result.shape == (0, len(expected_table.columns)):
        assert result.shape == expected_table.shape
        assert result.columns.equals(expected_table.columns)
    else:
        assert result.equals(
            expected_table
        ), f"Expected table {expected_table}, but got {result}"


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
    if result.shape == (0, len(expected_table.columns)):
        assert result.shape == expected_table.shape
        assert result.columns.equals(expected_table.columns)
    else:
        assert result.equals(
            expected_table
        ), f"Expected table {expected_table}, but got {result}"


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
    expected_table = pd.DataFrame(expected_data).reset_index(drop=True)
    result = (
        problem_1068(table_1, table_2)
        .reset_index(drop=True)
        .astype(expected_table.dtypes.to_dict())
    )
    assert list(result.index) == list(
        expected_table.index
    ), f"Index mismatch: {result.index} vs {expected_table.index}"
    for col in expected_table.columns:
        assert result[col].equals(expected_table[col]), f"Mismatch in column '{col}'"

    assert result.equals(expected_table)


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
    assert result.equals(expected_table)


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
    expected_table = pd.DataFrame(expected_data).reset_index(drop=True)
    result = (
        problem_1321(table)
        .reset_index(drop=True)
        .astype(expected_table.dtypes.to_dict())
    )
    assert list(result.index) == list(
        expected_table.index
    ), f"Index mismatch: {result.index} vs {expected_table.index}"
    for col in expected_table.columns:
        assert result[col].equals(expected_table[col]), f"Mismatch in column '{col}'"

    assert result.equals(expected_table)


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
    expected_table = pd.DataFrame(expected_data).reset_index(drop=True)
    result = (
        problem_1378(table_1, table_2)
        .reset_index(drop=True)
        .astype(expected_table.dtypes.to_dict())
    )
    assert list(result.index) == list(
        expected_table.index
    ), f"Index mismatch: {result.index} vs {expected_table.index}"
    for col in expected_table.columns:
        assert result[col].equals(expected_table[col]), f"Mismatch in column '{col}'"

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
    expected_table = (
        pd.DataFrame(
            expected_data
        )  # .sort_values(by="customer_id").reset_index(drop=True)
    )
    result = problem_1661(table)  # .sort_values(by="customer_id")

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
    assert result.equals(expected_table)
