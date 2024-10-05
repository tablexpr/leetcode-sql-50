from datetime import datetime, timedelta

import pyarrow as pa
import pyarrow.compute as pc


def problem_197(table: pa.Table) -> pa.Table:
    lag_table = pa.table(
        {
            "recordDate": pc.add(table["recordDate"], pa.scalar(timedelta(days=1))),
            "temperature": table["temperature"],
        }
    )
    joined = table.join(
        lag_table,
        keys="recordDate",
        join_type="inner",
        right_suffix="Lag",
    )

    joined = joined.filter(
        pc.greater(joined["temperature"], joined["temperatureLag"])
    ).select(["id"])

    return joined


def problem_584(table: pa.Table) -> pa.Table:
    return table.filter(
        pc.or_kleene(
            pc.is_null(table["referee_id"]),
            pc.not_equal(table["referee_id"], pa.scalar(2)),
        )
    ).select(["name"])


def problem_595(table: pa.Table) -> pa.Table:
    return table.filter(
        pc.or_(
            pc.greater_equal(table["area"], pa.scalar(3_000_000)),
            pc.greater_equal(table["population"], pa.scalar(25_000_000)),
        )
    ).select(["name", "population", "area"])


def problem_620(table: pa.Table) -> pa.Table:
    return table.filter(
        pc.and_(
            pc.equal(pc.bit_wise_and(table["id"], pa.scalar(1)), pa.scalar(1)),
            pc.not_equal(table["description"], pa.scalar("boring")),
        )
    ).sort_by([("id", "descending")])


def problem_1068(table_1: pa.Table, table_2: pa.Table) -> pa.Table:
    return table_1.join(table_2, keys="product_id").select(
        ["product_name", "year", "price"]
    )


def problem_1141(table: pa.Table) -> pa.Table:
    return (
        table.filter(
            pc.and_(
                pc.greater(
                    table["activity_date"],
                    pc.subtract(table["activity_date"], pa.scalar(timedelta(days=30))),
                ),
                pc.less_equal(table["activity_date"], pa.scalar(datetime(2019, 7, 27))),
            )
        )
        .group_by("activity_date")
        .aggregate([("user_id", "count_distinct")])
        .rename_columns(
            {"activity_date": "day", "user_id_count_distinct": "active_users"}
        )
    )


def problem_1148(table: pa.Table) -> pa.Table:
    return (
        table.filter(pc.equal(table["author_id"], table["viewer_id"]))
        .select(["author_id"])
        .rename_columns(["id"])
        .group_by("id")
        .aggregate([])
        .sort_by("id")
    )


def problem_1378(table: pa.Table, table_2: pa.Table) -> pa.Table:
    return table.join(table_2, keys="id", join_type="left outer").select(
        ["unique_id", "name"]
    )


def problem_1683(table: pa.Table) -> pa.Table:
    return table.filter(
        pc.greater(pc.utf8_length(table["content"]), pa.scalar(15))
    ).select(["tweet_id"])


def problem_1757(table: pa.Table) -> pa.Table:
    return table.filter(
        pc.and_(
            pc.equal(table["low_fats"], pa.scalar("Y")),
            pc.equal(table["recyclable"], pa.scalar("Y")),
        )
    ).select(["product_id"])


def problem_1978(table: pa.Table) -> pa.Table:
    return (
        table.filter(
            pc.and_(
                pc.less(table["salary"], pa.scalar(30_000)),
                pc.and_(
                    pc.invert(pc.is_in(table["manager_id"], table["employee_id"])),
                    pc.invert(pc.is_null(table["manager_id"])),
                ),
            )
        )
        .select(["employee_id"])
        .sort_by("employee_id")
    )
