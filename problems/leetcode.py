from datetime import datetime, timedelta

import pyarrow as pa
import pyarrow.compute as pc


def problem_176(table: pa.Table) -> pa.Table:
    result = pa.Table.from_arrays(
        [
            pc.sort_indices(
                pc.unique(table["salary"]), sort_keys=[("salary", "descending")]
            ),
            pc.unique(table["salary"]),
        ],
        names=["index", "SecondHighestSalary"],
    )
    result = result.filter(pc.equal(result["index"], pa.scalar(1))).drop("index")
    if result.num_rows == 0:
        return pa.Table.from_pydict({"SecondHighestSalary": [None]})
    return result


def problem_180(table: pa.Table) -> pa.Table:
    if table.num_rows == 0:
        return pa.Table.from_pydict(
            {"ConsecutiveNums": [None]},
            schema=pa.schema([pa.field("ConsecutiveNums", pa.int64())]),
        )
    table_lead_1 = table.set_column(0, "id", pc.add(table["id"], pa.scalar(1)))
    table_lead_2 = table.set_column(0, "id", pc.add(table["id"], pa.scalar(2)))
    joined = (
        table.join(table_lead_1, keys=["id", "num"], join_type="inner")
        .join(table_lead_2, keys=["id", "num"], join_type="inner")
        .select(["num"])
    )
    return pa.Table.from_arrays([pc.unique(joined["num"])], names=["ConsecutiveNums"])


def problem_196(table: pa.Table) -> pa.Table:
    # There isn't really a way to modify a PyArrow table in place, so we have
    # to create a new table to return the desired results.
    return (
        table.group_by(["email"])
        .aggregate([("id", "min")])
        .rename_columns({"id_min": "id"})
        .select(["id", "email"])
    )


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


def problem_550(table: pa.Table) -> pa.Table:
    grouped = table.group_by("player_id").aggregate([("event_date", "min")])
    grouped.append_column(
        "next_date", pc.add(grouped["event_date_min"], pa.scalar(timedelta(days=1)))
    ).join(
        table, keys=["player_id", "next_date"], right_keys=["player_id", "event_date"]
    )
    joined = grouped.append_column(
        "next_date", pc.add(grouped["event_date_min"], pa.scalar(timedelta(days=1)))
    ).join(
        table, keys=["player_id", "next_date"], right_keys=["player_id", "event_date"]
    )
    return pa.Table.from_arrays(
        [
            pa.array(
                [
                    pc.round(
                        pc.divide(
                            pc.cast(
                                pc.count(joined["games_played"], mode="only_valid"),
                                pa.float64(),
                            ),
                            pc.cast(
                                pc.count(joined["games_played"], mode="all"),
                                pa.float64(),
                            ),
                        ),
                        2,
                    )
                ]
            )
        ],
        names=["fraction"],
    )


def problem_570(table: pa.Table) -> pa.Table:
    grouped = table.group_by("managerId").aggregate([("id", "count")])
    grouped = grouped.filter(pc.greater_equal(grouped["id_count"], pa.scalar(5)))
    return table.join(
        grouped, keys="id", right_keys="managerId", join_type="inner"
    ).select(["name"])


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


def problem_596(table: pa.Table) -> pa.Table:
    table_agg = table.group_by("class").aggregate([("student", "count")])
    return table_agg.filter(
        pc.greater_equal(table_agg["student_count"], pa.scalar(5))
    ).select(["class"])


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


def problem_619(table: pa.Table) -> pa.Table:
    grouped = table.group_by("num").aggregate([("num", "count")])
    grouped = grouped.filter(pc.equal(grouped["num_count"], pa.scalar(1)))
    if grouped.num_rows == 0:
        return pa.Table.from_pydict({"num": [None]})
    else:
        return (
            grouped.group_by([])
            .aggregate([("num", "max")])
            .rename_columns({"num_max": "num"})
        )


def problem_620(table: pa.Table) -> pa.Table:
    return table.filter(
        pc.and_(
            pc.equal(pc.bit_wise_and(table["id"], pa.scalar(1)), pa.scalar(1)),
            pc.not_equal(table["description"], pa.scalar("boring")),
        )
    ).sort_by([("id", "descending")])


def problem_1045(table_1: pa.Table, table_2: pa.Table) -> pa.Table:
    grouped = table_1.group_by("customer_id").aggregate(
        [("product_key", "count_distinct")]
    )
    return grouped.filter(
        pc.equal(grouped["product_key_count_distinct"], pa.scalar(table_2.num_rows))
    ).select(["customer_id"])


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


def problem_1164(table: pa.Table) -> pa.Table:
    table_lte = table.filter(pc.less_equal(table["change_date"], datetime(2019, 8, 16)))
    products_max_dates = table_lte.group_by("product_id").aggregate(
        [("change_date", "max")]
    )
    joined = (
        table_lte.join(
            products_max_dates,
            keys=["product_id", "change_date"],
            right_keys=["product_id", "change_date_max"],
            join_type="inner",
        )
        .drop("change_date")
        .rename_columns({"new_price": "price"})
    )
    table_gt = table.filter(pc.greater(table["change_date"], datetime(2019, 8, 16)))
    missing_products = table_gt.filter(
        pc.invert(pc.is_in(table_gt["product_id"], joined["product_id"]))
    )
    missing_products = missing_products.drop_columns(
        ["new_price", "change_date"]
    ).append_column("price", pa.array([10] * missing_products.num_rows))
    if missing_products.num_rows == 0:
        return joined
    return pa.concat_tables([joined, missing_products])


def problem_1193(table: pa.Table) -> pa.Table:
    table = table.append_column("month", pc.strftime(table["trans_date"], "%Y-%m"))
    table = table.append_column(
        "is_approved",
        pc.if_else(pc.equal(table["state"], "approved"), pa.scalar(1), pa.scalar(0)),
    )
    table = table.append_column(
        "approved_amount",
        pc.if_else(
            pc.equal(table["is_approved"], pa.scalar(1)), table["amount"], pa.scalar(0)
        ),
    )
    return (
        table.group_by(["month", "country"])
        .aggregate(
            [
                ("id", "count"),
                ("is_approved", "sum"),
                ("amount", "sum"),
                ("approved_amount", "sum"),
            ]
        )
        .rename_columns(
            {
                "id_count": "trans_count",
                "is_approved_sum": "approved_count",
                "amount_sum": "trans_total_amount",
                "approved_amount_sum": "approved_total_amount",
            }
        )
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


def problem_1327(table_1: pa.Table, table_2: pa.Table) -> pa.Table:
    table_2 = table_2.append_column(
        "year_month", pc.strftime(table_2["order_date"], "%Y-%m")
    )
    table_2_agg = (
        table_2.filter(pc.equal(table_2["year_month"], pa.scalar("2020-02")))
        .group_by(["product_id"])
        .aggregate([("unit", "sum")])
    )
    joined = table_1.join(table_2_agg, keys=["product_id"])
    return (
        joined.filter(pc.greater_equal(joined["unit_sum"], pa.scalar(100)))
        .select(["product_name", "unit_sum"])
        .rename_columns({"unit_sum": "unit"})
    )


def problem_1378(table: pa.Table, table_2: pa.Table) -> pa.Table:
    return table.join(table_2, keys="id", join_type="left outer").select(
        ["unique_id", "name"]
    )


def problem_1527(table: pa.Table) -> pa.Table:
    return table.filter(
        pc.or_(
            pc.starts_with(table["conditions"], "DIAB1"),
            pc.match_like(table["conditions"], "% DIAB1%"),
        )
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


def problem_1667(table: pa.Table) -> pa.Table:
    return table.set_column(1, "name", pc.ascii_capitalize(table["name"])).sort_by(
        "user_id"
    )


def problem_1683(table: pa.Table) -> pa.Table:
    return table.filter(
        pc.greater(pc.utf8_length(table["content"]), pa.scalar(15))
    ).select(["tweet_id"])


def problem_1729(table: pa.Table) -> pa.Table:
    return (
        table.group_by("user_id")
        .aggregate([("follower_id", "count")])
        .rename_columns({"follower_id_count": "followers_count"})
        .sort_by("user_id")
    )


def problem_1757(table: pa.Table) -> pa.Table:
    return table.filter(
        pc.and_(
            pc.equal(table["low_fats"], pa.scalar("Y")),
            pc.equal(table["recyclable"], pa.scalar("Y")),
        )
    ).select(["product_id"])


def problem_1789(table: pa.Table) -> pa.Table:
    joined = table.join(
        table.group_by("employee_id").aggregate([("employee_id", "count")]),
        keys="employee_id",
    )
    return joined.filter(
        pc.or_(
            pc.equal(joined["primary_flag"], pa.scalar("Y")),
            pc.equal(joined["employee_id_count"], pa.scalar(1)),
        )
    ).select(["employee_id", "department_id"])


def problem_1934(table_1: pa.Table, table_2: pa.Table) -> pa.Table:
    joined = table_1.join(table_2, keys=["user_id"], join_type="left outer").select(
        ["user_id", "action"]
    )
    grouped = (
        joined.append_column(
            "is_confirmed",
            pc.fill_null(
                pc.if_else(
                    pc.equal(joined["action"], pa.scalar("confirmed")),
                    pa.scalar(1.0),
                    pa.scalar(0.0),
                ),
                pa.scalar(0.0),
            ),
        )
        .group_by("user_id")
        .aggregate([("is_confirmed", "sum"), ("is_confirmed", "count")])
    )
    return grouped.append_column(
        "confirmation_rate",
        pc.round(
            pc.divide(grouped["is_confirmed_sum"], grouped["is_confirmed_count"]), 2
        ),
    ).select(["user_id", "confirmation_rate"])


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


def problem_2356(table: pa.Table) -> pa.Table:
    return (
        table.group_by("teacher_id")
        .aggregate([("subject_id", "count_distinct")])
        .rename_columns({"subject_id_count_distinct": "cnt"})
    )
