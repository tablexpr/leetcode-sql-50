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


def problem_577(table_1: pa.Table, table_2: pa.Table) -> pa.Table:
    return table_1.join(table_2, keys="empId").select(["name", "bonus"])


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


def problem_610(table: pa.Table) -> pa.Table:
    return table.append_column(
        "triangle",
        pc.if_else(
            pc.and_(
                pc.and_(
                    pc.greater(pc.add(table["x"], table["y"]), table["z"]),
                    pc.greater(pc.add(table["x"], table["z"]), table["y"]),
                ),
                pc.greater(pc.add(table["y"], table["z"]), table["x"]),
            ),
            "Yes",
            "No",
        ),
    )


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


def problem_1075(table_1: pa.Table, table_2: pa.Table) -> pa.Table:
    joined = (
        table_1.join(table_2, keys="employee_id", join_type="inner")
        .group_by("project_id")
        .aggregate([("experience_years", "mean")])
    )
    return joined.set_column(
        1, "experience_years", pc.round(joined["experience_years_mean"], 2)
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


def problem_1161(table: pa.Table) -> pa.Table:
    table_starts = table.filter(
        pc.equal(table["activity_type"], pa.scalar("start"))
    ).drop("activity_type")
    table_ends = table.filter(pc.equal(table["activity_type"], pa.scalar("end"))).drop(
        "activity_type"
    )
    joined = table_starts.join(
        table_ends,
        keys=["machine_id", "process_id"],
        left_suffix="_start",
        right_suffix="_end",
    )
    joined_agg = (
        joined.append_column(
            "processing_time",
            pc.subtract(joined["timestamp_end"], joined["timestamp_start"]),
        )
        .group_by("machine_id")
        .aggregate([("processing_time", "mean")])
    )
    return joined_agg.set_column(
        1, "processing_time", pc.round(joined_agg["processing_time_mean"], 3)
    )


def problem_1211(table: pa.Table) -> pa.Table:
    table = table.append_column(
        "quality", pc.divide(table["rating"], table["position"])
    ).append_column(
        "poor_query_percentage",
        pc.if_else(pc.less(table["rating"], pa.scalar(3)), 100, 0),
    )

    table_agg = table.group_by("query_name").aggregate(
        [("quality", "mean"), ("poor_query_percentage", "mean")]
    )

    return table_agg.set_column(
        1, "quality", pc.round(table_agg["quality_mean"], 2)
    ).set_column(
        2, "poor_query_percentage", pc.round(table_agg["poor_query_percentage_mean"], 2)
    )


def problem_1280(table_1: pa.Table, table_2: pa.Table, table_3: pa.Table) -> pa.Table:
    table_1 = table_1.append_column("key", pa.array([1] * len(table_1)))
    table_2 = table_2.append_column("key", pa.array([1] * len(table_2)))
    examinations_agg = (
        table_3.group_by(["student_id", "subject_name"])
        .aggregate([("student_id", "count")])
        .rename_columns({"student_id_count": "attended_exams"})
    )
    joined = (
        table_1.join(table_2, keys="key")
        .drop("key")
        .join(
            examinations_agg,
            keys=["student_id", "subject_name"],
            join_type="left outer",
        )
        .sort_by([("student_id", "ascending"), ("student_name", "ascending")])
    )
    return joined.set_column(
        3, "attended_exams", pc.coalesce(joined["attended_exams"], pa.scalar(0))
    )


def problem_1378(table: pa.Table, table_2: pa.Table) -> pa.Table:
    return table.join(table_2, keys="id", join_type="left outer").select(
        ["unique_id", "name"]
    )


def problem_1581(table_1: pa.Table, table_2: pa.Table) -> pa.Table:
    joined = table_1.join(table_2, keys="visit_id", join_type="left outer")
    return (
        joined.filter(pc.is_null(joined["transaction_id"]))
        .group_by("customer_id")
        .aggregate([("visit_id", "count")])
        .rename_columns({"visit_id_count": "count_no_trans"})
    )


def problem_1633(table_1: pa.Table, table_2: pa.Table) -> pa.Table:
    table_2_agg = table_2.group_by("contest_id").aggregate([("user_id", "count")])
    total_users = pa.scalar(float(table_1.num_rows))
    return table_2_agg.set_column(
        1,
        "percentage",
        pc.round(
            pc.divide(table_2_agg["user_id_count"], total_users),
            2,
        ),
    ).sort_by([("percentage", "descending")])


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
