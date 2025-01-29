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
    PARAMS_PROBLEM_1148,
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
    PARAMS_PROBLEM_1484,
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
    PARAMS_PROBLEM_1517,
)
def test_problem_1517(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1517(table)
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1683,
)
def test_problem_1683(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1683(table)
    assert result.to_arrow_table().equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1757,
    ids=["happy_path_mixed_values", "all_ys"],
)
def test_problem_1757(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1757(table)
    assert result.to_arrow_table().equals(expected_table)
