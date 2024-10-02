from datetime import timedelta

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


def problem_1148(table: pa.Table) -> pa.Table:
    return (
        table.filter(pc.equal(table["author_id"], table["viewer_id"]))
        .select(["author_id"])
        .rename_columns(["id"])
        .group_by("id")
        .aggregate([])
        .sort_by("id")
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
