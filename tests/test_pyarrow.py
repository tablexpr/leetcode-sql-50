from datetime import datetime

import pyarrow as pa
import pytest

from problems.pyarrow import *
from tests.test_problem_params import *


@pytest.mark.parametrize("input_data, expected_data", PARAMS_PROBLEM_176)
def test_problem_176(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_176(table)
    assert result.equals(expected_table)


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
    result = problem_180(table).cast(
        pa.schema([pa.field("ConsecutiveNums", pa.int64())])
    )
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_185,
)
def test_problem_185(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_185(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_196,
)
def test_problem_196(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_196(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_197,
)
def test_problem_197(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("id", pa.int64())])
    )
    result = problem_197(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_550,
)
def test_problem_550(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_550(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_570,
)
def test_problem_570(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("name", pa.string())])
    )
    result = problem_570(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_577,
)
def test_problem_577(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data).sort_by(
        [("name", "ascending")]
    )
    result = problem_577(table_1, table_2).sort_by([("name", "ascending")])
    assert result.equals(expected_table)


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
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_585,
)
def test_problem_585(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("tiv_2016", pa.float64())])
    )
    result = problem_585(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_595,
)
def test_problem_595(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_595(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_596,
)
def test_problem_596(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("class", pa.string())])
    )
    result = problem_596(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_602,
)
def test_problem_602(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_602(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_610,
)
def test_problem_610(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_610(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_619,
)
def test_problem_619(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_619(table)
    result.to_pydict() == expected_table.to_pydict()


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
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_626,
)
def test_problem_626(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_626(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1045,
)
def test_problem_1045(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(
        input_data_1,
        schema=pa.schema(
            [pa.field("customer_id", pa.int64()), pa.field("product_key", pa.int64())]
        ),
    )
    table_2 = pa.Table.from_pydict(
        input_data_2, schema=pa.schema([pa.field("product_key", pa.int64())])
    )
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("customer_id", pa.int64())])
    )
    result = problem_1045(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1068,
)
def test_problem_1068(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1068(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1070,
)
def test_problem_1070(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1070(input_table, None)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1075,
)
def test_problem_1075(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1075(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEMS_1141,
)
def test_problem_1141(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result_table = problem_1141(input_table)
    assert result_table.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1148,
)
def test_problem_1148(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1148(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1164,
)
def test_problem_1164(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1164(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "delivery_id": [1, 2, 3, 4, 5, 6, 7],
                "customer_id": [1, 2, 1, 3, 3, 2, 4],
                "order_date": [
                    datetime(2019, 8, 1),
                    datetime(2019, 8, 2),
                    datetime(2019, 8, 11),
                    datetime(2019, 8, 24),
                    datetime(2019, 8, 21),
                    datetime(2019, 8, 11),
                    datetime(2019, 8, 9),
                ],
                "customer_pref_delivery_date": [
                    datetime(2019, 8, 2),
                    datetime(2019, 8, 2),
                    datetime(2019, 8, 12),
                    datetime(2019, 8, 24),
                    datetime(2019, 8, 22),
                    datetime(2019, 8, 13),
                    datetime(2019, 8, 9),
                ],
            },
            {"immediate_percentage": [50.0]},
            id="happy_path",
        ),
        pytest.param(
            {
                "delivery_id": [1, 2, 3],
                "customer_id": [1, 1, 2],
                "order_date": [
                    datetime(2020, 1, 1),
                    datetime(2020, 1, 2),
                    datetime(2020, 1, 3),
                ],
                "customer_pref_delivery_date": [
                    datetime(2020, 1, 1),
                    datetime(2020, 1, 2),
                    datetime(2020, 1, 3),
                ],
            },
            {"immediate_percentage": [100.0]},
            id="all_immediate",
        ),
    ],
)
def test_problem_1174(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1174(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1193,
)
def test_problem_1193(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1193(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1204,
)
def test_problem_1204(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1204(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1211,
)
def test_problem_1211(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1211(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1251,
)
def test_problem_1251(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1251(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, input_data_3, expected_data",
    PARAMS_PROBLEM_1280,
)
def test_problem_1280(input_data_1, input_data_2, input_data_3, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    table_3 = pa.Table.from_pydict(input_data_3)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1280(table_1, table_2, table_3)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1327,
)
def test_problem_1327(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(
        expected_data,
        schema=pa.schema(
            [pa.field("product_name", pa.string()), pa.field("unit", pa.int64())]
        ),
    )
    result = problem_1327(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, input_data_3, expected_data",
    PARAMS_PROBLEM_1341,
)
def test_problem_1341(input_data_1, input_data_2, input_data_3, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    table_3 = pa.Table.from_pydict(input_data_3)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1341(table_1, table_2, table_3)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1378,
)
def test_problem_1378(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1378(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1517,
)
def test_problem_1517(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1517(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1527,
)
def test_problem_1527(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1527(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1581,
)
def test_problem_1581(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    result = problem_1581(table_1, table_2)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {"contest_id": [1, 2], "user_id": [1, 2]},
            {"contest_id": [1, 1, 2], "user_id": [1, 2, 3]},
            {
                "contest_id": [1, 2],
                "percentage": [1.0, 0.5],
            },
            id="happy-path-1",
        ),
        pytest.param(
            {"contest_id": [1, 2, 3], "user_id": [1, 2, 3]},
            {"contest_id": [1, 2, 2, 3, 3, 3], "user_id": [1, 2, 3, 4, 5, 6]},
            {
                "contest_id": [3, 2, 1],
                "percentage": [1.0, 0.67, 0.33],
            },
            id="happy-path-2",
        ),
        pytest.param(
            {"contest_id": [1], "user_id": [1]},
            {"contest_id": [1], "user_id": [1]},
            {"contest_id": [1], "percentage": [1.0]},
            id="edge-single-row-table-2",
        ),
    ],
)
def test_problem_1633(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1633(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1661,
)
def test_problem_1661(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1661(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {"user_id": [1, 2], "name": ["alice", "bob"]},
            {"user_id": [1, 2], "name": ["Alice", "Bob"]},
            id="happy_path_simple",
        ),
        pytest.param(
            {"user_id": [2, 1], "name": ["bob", "alice"]},
            {"user_id": [1, 2], "name": ["Alice", "Bob"]},
            id="happy_path_unsorted_user_id",
        ),
        pytest.param(
            {"user_id": [3, 4], "name": ["tyler", "MaRy KaThRyN"]},
            {"user_id": [3, 4], "name": ["Tyler", "Mary kathryn"]},
            id="edge_case_two_part_name_table",
        ),
        pytest.param(
            {"user_id": [1], "name": [""]},
            {"user_id": [1], "name": [""]},
            id="edge_case_empty_name",
        ),
        pytest.param(
            {"user_id": [1], "name": ["ALICE"]},
            {"user_id": [1], "name": ["Alice"]},
            id="edge_case_all_caps",
        ),
        pytest.param(
            {"user_id": [1, 2], "name": [None, "bob"]},
            {"user_id": [1, 2], "name": [None, "Bob"]},
            id="error_case_none_name",
        ),
    ],
)
def test_problem_1667(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1667(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1683,
)
def test_problem_1683(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    result = problem_1683(table)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1729,
)
def test_problem_1729(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    result = problem_1729(table)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "employee_id": [9, 6, 4, 2],
                "name": ["Hercy", "Alice", "Bob", "Winston"],
                "reports_to": [None, 9, 9, None],
                "age": [43, 41, 36, 37],
            },
            {
                "employee_id": [9],
                "name": ["Hercy"],
                "reports_count": [2],
                "average_age": [38.5],
            },
            id="one_manager",
        ),
        pytest.param(
            {
                "employee_id": [1, 2, 3, 4, 5, 6, 7, 8],
                "name": [
                    "Michael",
                    "Alice",
                    "Bob",
                    "Charlie",
                    "David",
                    "Eve",
                    "Frank",
                    "Grace",
                ],
                "reports_to": [None, 1, 1, 2, 2, 3, None, None],
                "age": [45, 38, 42, 34, 40, 37, 50, 48],
            },
            {
                "employee_id": [1, 2, 3],
                "name": ["Michael", "Alice", "Bob"],
                "reports_count": [2, 2, 1],
                "average_age": [40.0, 37.0, 37.0],
            },
            id="three_managers",
        ),
    ],
)
def test_problem_1731(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    result = problem_1731(table)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1757,
    ids=["happy_path_mixed_values", "all_ys"],
)
def test_problem_1757(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    result = problem_1757(table)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1789,
)
def test_problem_1789(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1789(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1907,
)
def test_problem_1907(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1907(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    PARAMS_PROBLEM_1934,
)
def test_problem_1934(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(
        input_data_1,
        schema=pa.schema(
            [
                pa.field("user_id", pa.int64()),
            ]
        ),
    )
    table_2 = pa.Table.from_pydict(
        input_data_2,
        schema=pa.schema(
            [
                pa.field("user_id", pa.int64()),
                pa.field("action", pa.string()),
            ]
        ),
    )
    expected_table = pa.Table.from_pydict(
        expected_data,
        schema=pa.schema(
            [
                pa.field("user_id", pa.int64()),
                pa.field("confirmation_rate", pa.float64()),
            ]
        ),
    )
    result = problem_1934(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_1978,
)
def test_problem_1978(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("employee_id", pa.int64())])
    )
    result = problem_1978(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    PARAMS_PROBLEM_2356,
)
def test_problem_2356(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_2356(table)
    assert result.equals(expected_table)
