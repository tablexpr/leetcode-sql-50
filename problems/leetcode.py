from datetime import datetime, timedelta

import pyarrow as pa
import pyarrow.compute as pc


def problem_176(employee: pa.Table) -> pa.Table:
    result = pa.Table.from_arrays(
        [
            pc.sort_indices(
                pc.unique(employee["salary"]), sort_keys=[("salary", "descending")]
            ),
            pc.unique(employee["salary"]),
        ],
        names=["index", "SecondHighestSalary"],
    )
    result = result.filter(pc.equal(result["index"], pa.scalar(1))).drop("index")
    if result.num_rows == 0:
        return pa.Table.from_pydict({"SecondHighestSalary": [None]})
    return result


def problem_180(logs: pa.Table) -> pa.Table:
    if logs.num_rows == 0:
        return pa.Table.from_pydict(
            {"ConsecutiveNums": [None]},
            schema=pa.schema([pa.field("ConsecutiveNums", pa.int64())]),
        )
    table_lead_1 = logs.set_column(0, "id", pc.add(logs["id"], pa.scalar(1)))
    table_lead_2 = logs.set_column(0, "id", pc.add(logs["id"], pa.scalar(2)))
    joined = (
        logs.join(table_lead_1, keys=["id", "num"], join_type="inner")
        .join(table_lead_2, keys=["id", "num"], join_type="inner")
        .select(["num"])
    )
    return pa.Table.from_arrays([pc.unique(joined["num"])], names=["ConsecutiveNums"])


def problem_196(person: pa.Table) -> pa.Table:
    # There isn't really a way to modify a PyArrow table in place, so we have
    # to create a new table to return the desired results.
    return (
        person.group_by(["email"])
        .aggregate([("id", "min")])
        .rename_columns({"id_min": "id"})
        .select(["id", "email"])
    )


def problem_197(weather: pa.Table) -> pa.Table:
    lag_table = pa.table(
        {
            "recordDate": pc.add(weather["recordDate"], pa.scalar(timedelta(days=1))),
            "temperature": weather["temperature"],
        }
    )
    joined = weather.join(
        lag_table,
        keys="recordDate",
        join_type="inner",
        right_suffix="Lag",
    )

    joined = joined.filter(
        pc.greater(joined["temperature"], joined["temperatureLag"])
    ).select(["id"])

    return joined


def problem_550(activity: pa.Table) -> pa.Table:
    grouped = activity.group_by("player_id").aggregate([("event_date", "min")])
    grouped.append_column(
        "next_date", pc.add(grouped["event_date_min"], pa.scalar(timedelta(days=1)))
    ).join(
        activity,
        keys=["player_id", "next_date"],
        right_keys=["player_id", "event_date"],
    )
    joined = grouped.append_column(
        "next_date", pc.add(grouped["event_date_min"], pa.scalar(timedelta(days=1)))
    ).join(
        activity,
        keys=["player_id", "next_date"],
        right_keys=["player_id", "event_date"],
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


def problem_570(employee: pa.Table) -> pa.Table:
    """Write a solution to find managers with at least five direct reports.

    Return the result table in any order.

    Parameters
    ----------
    employee : pa.Table

    Returns
    -------
    pa.Table

    """
    grouped = employee.group_by("managerId").aggregate([("id", "count")])
    grouped = grouped.filter(pc.greater_equal(grouped["id_count"], pa.scalar(5)))
    return employee.join(
        grouped, keys="id", right_keys="managerId", join_type="inner"
    ).select(["name"])


def problem_577(employee: pa.Table, bonus: pa.Table) -> pa.Table:
    return employee.join(bonus, keys="empId").select(["name", "bonus"])


def problem_584(customer: pa.Table) -> pa.Table:
    return customer.filter(
        pc.or_kleene(
            pc.is_null(customer["referee_id"]),
            pc.not_equal(customer["referee_id"], pa.scalar(2)),
        )
    ).select(["name"])


def problem_595(world: pa.Table) -> pa.Table:
    return world.filter(
        pc.or_(
            pc.greater_equal(world["area"], pa.scalar(3_000_000)),
            pc.greater_equal(world["population"], pa.scalar(25_000_000)),
        )
    ).select(["name", "population", "area"])


def problem_596(courses: pa.Table) -> pa.Table:
    table_agg = courses.group_by("class").aggregate([("student", "count")])
    return table_agg.filter(
        pc.greater_equal(table_agg["student_count"], pa.scalar(5))
    ).select(["class"])


def problem_610(triangle: pa.Table) -> pa.Table:
    return triangle.append_column(
        "triangle",
        pc.if_else(
            pc.and_(
                pc.and_(
                    pc.greater(pc.add(triangle["x"], triangle["y"]), triangle["z"]),
                    pc.greater(pc.add(triangle["x"], triangle["z"]), triangle["y"]),
                ),
                pc.greater(pc.add(triangle["y"], triangle["z"]), triangle["x"]),
            ),
            "Yes",
            "No",
        ),
    )


def problem_619(my_numbers: pa.Table) -> pa.Table:
    grouped = my_numbers.group_by("num").aggregate([("num", "count")])
    grouped = grouped.filter(pc.equal(grouped["num_count"], pa.scalar(1)))
    if grouped.num_rows == 0:
        return pa.Table.from_pydict({"num": [None]})
    else:
        return (
            grouped.group_by([])
            .aggregate([("num", "max")])
            .rename_columns({"num_max": "num"})
        )


def problem_620(cinema: pa.Table) -> pa.Table:
    return cinema.filter(
        pc.and_(
            pc.equal(pc.bit_wise_and(cinema["id"], pa.scalar(1)), pa.scalar(1)),
            pc.not_equal(cinema["description"], pa.scalar("boring")),
        )
    ).sort_by([("id", "descending")])


def problem_1045(customer: pa.Table, product: pa.Table) -> pa.Table:
    grouped = customer.group_by("customer_id").aggregate(
        [("product_key", "count_distinct")]
    )
    return grouped.filter(
        pc.equal(grouped["product_key_count_distinct"], pa.scalar(product.num_rows))
    ).select(["customer_id"])


def problem_1068(sales: pa.Table, product: pa.Table) -> pa.Table:
    return sales.join(product, keys="product_id").select(
        ["product_name", "year", "price"]
    )


def problem_1075(project: pa.Table, employee: pa.Table) -> pa.Table:
    joined = (
        project.join(employee, keys="employee_id", join_type="inner")
        .group_by("project_id")
        .aggregate([("experience_years", "mean")])
    )
    return joined.set_column(
        1, "experience_years", pc.round(joined["experience_years_mean"], 2)
    )


def problem_1141(activity: pa.Table) -> pa.Table:
    return (
        activity.filter(
            pc.and_(
                pc.greater(
                    activity["activity_date"],
                    pc.subtract(
                        activity["activity_date"], pa.scalar(timedelta(days=30))
                    ),
                ),
                pc.less_equal(
                    activity["activity_date"], pa.scalar(datetime(2019, 7, 27))
                ),
            )
        )
        .group_by("activity_date")
        .aggregate([("user_id", "count_distinct")])
        .rename_columns(
            {"activity_date": "day", "user_id_count_distinct": "active_users"}
        )
    )


def problem_1148(views: pa.Table) -> pa.Table:
    return (
        views.filter(pc.equal(views["author_id"], views["viewer_id"]))
        .select(["author_id"])
        .rename_columns(["id"])
        .group_by("id")
        .aggregate([])
        .sort_by("id")
    )


def problem_1164(products: pa.Table) -> pa.Table:
    table_lte = products.filter(
        pc.less_equal(products["change_date"], datetime(2019, 8, 16))
    )
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
    table_gt = products.filter(
        pc.greater(products["change_date"], datetime(2019, 8, 16))
    )
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


def problem_1204(table: pa.Table) -> pa.Table:
    table = table.sort_by("turn")
    table = table.append_column("weight_cumsum", pc.cumulative_sum(table["weight"]))
    table = table.filter(pc.less_equal(table["weight_cumsum"], pa.scalar(1000)))
    return table.take([table.num_rows - 1]).select(["person_name"])


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


def problem_1251(table_1: pa.Table, table_2: pa.Table) -> pa.Table:
    joined = table_1.join(table_2, keys="product_id")
    joined = joined.filter(
        pc.or_kleene(
            pc.and_(
                pc.greater_equal(joined["purchase_date"], joined["start_date"]),
                pc.less_equal(joined["purchase_date"], joined["end_date"]),
            ),
            pc.is_null(joined["purchase_date"]),
        )
    )
    joined = joined.append_column(
        "total", pc.multiply(joined["price"], joined["units"])
    )
    grouped = joined.group_by("product_id").aggregate(
        [("units", "sum"), ("total", "sum")]
    )
    return grouped.append_column(
        "average_price",
        pc.round(
            pc.fill_null(
                pc.divide(
                    pc.cast(grouped["total_sum"], pa.float64()), grouped["units_sum"]
                ),
                0,
            ),
            2,
        ),
    ).select(["product_id", "average_price"])


def problem_1280(
    students: pa.Table, subjects: pa.Table, examinations: pa.Table
) -> pa.Table:
    students = students.append_column("key", pa.array([1] * len(students)))
    subjects = subjects.append_column("key", pa.array([1] * len(subjects)))
    examinations_agg = (
        examinations.group_by(["student_id", "subject_name"])
        .aggregate([("student_id", "count")])
        .rename_columns({"student_id_count": "attended_exams"})
    )
    joined = (
        students.join(subjects, keys="key")
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


def problem_1327(products: pa.Table, orders: pa.Table) -> pa.Table:
    orders_agg = (
        orders.filter(
            pc.equal(pc.strftime(pc.field("order_date"), "%Y-%m"), pa.scalar("2020-02"))
        )
        .group_by(["product_id"])
        .aggregate([("unit", "sum")])
    )
    joined = products.join(orders_agg, keys=["product_id"])
    return (
        joined.filter(pc.greater_equal(joined["unit_sum"], pa.scalar(100)))
        .select(["product_name", "unit_sum"])
        .rename_columns({"unit_sum": "unit"})
    )


def problem_1341(table_1: pa.Table, table_2: pa.Table, table_3: pa.Table) -> pa.Table:
    user_most_ratings = (
        table_3.join(table_2, keys="user_id", join_type="inner")
        .group_by(["user_id", "name"])
        .aggregate([("movie_id", "count")])
        .sort_by([("movie_id_count", "descending"), ("name", "ascending")])
        .select(["name"])
        .take([0])["name"]
    )

    movie_highest_rating = (
        table_3.filter(
            pc.equal(pc.strftime(table_3["created_at"], "%Y-%m"), pa.scalar("2020-02"))
        )
        .join(table_1, keys="movie_id", join_type="inner")
        .group_by(["movie_id", "title"])
        .aggregate([("rating", "mean")])
        .sort_by([("rating_mean", "descending"), ("title", "ascending")])
        .select(["title"])
        .take([0])["title"]
    )

    return pa.Table.from_arrays(
        [
            pa.concat_arrays(
                [
                    user_most_ratings.combine_chunks(),
                    movie_highest_rating.combine_chunks(),
                ]
            )
        ],
        names=["results"],
    )


def problem_1378(employees: pa.Table, employee_uni: pa.Table) -> pa.Table:
    """Write a solution to show the unique ID of each user, If a user does not have a
    unique ID replace just show null.

    Return the result table in any order.

    Parameters
    ----------
    employees : pa.Table
    employee_uni : pa.Table

    Returns
    -------
    pa.Table

    """
    return employees.join(employee_uni, keys="id", join_type="left outer").select(
        ["unique_id", "name"]
    )


def problem_1527(patients: pa.Table) -> pa.Table:
    """Write a solution to find the patient_id, patient_name, and conditions of the
    patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

    Return the result table in any order.

    Parameters
    ----------
    patients : pa.Table

    Returns
    -------
    pa.Table

    """
    return patients.filter(
        pc.or_(
            pc.starts_with(patients["conditions"], "DIAB1"),
            pc.match_like(patients["conditions"], "% DIAB1%"),
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


def problem_1661(activity: pa.Table) -> pa.Table:
    table_starts = activity.filter(
        pc.equal(activity["activity_type"], pa.scalar("start"))
    ).drop("activity_type")
    table_ends = activity.filter(
        pc.equal(activity["activity_type"], pa.scalar("end"))
    ).drop("activity_type")
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


def problem_1757(products: pa.Table) -> pa.Table:
    return products.filter(
        pc.and_(
            pc.equal(products["low_fats"], pa.scalar("Y")),
            pc.equal(products["recyclable"], pa.scalar("Y")),
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


def problem_1907(table: pa.Table) -> pa.Table:
    categories = pa.Table.from_pydict(
        {"category": ["Low Salary", "Average Salary", "High Salary"]}
    )

    is_low_salary = pc.less(table["income"], pa.scalar(20_000))
    is_average_salary = pc.and_(
        pc.greater_equal(table["income"], pa.scalar(20_000)),
        pc.less_equal(table["income"], pa.scalar(50_000)),
    )
    is_high_salary = pc.greater(table["income"], pa.scalar(50_000))

    cond = pa.StructArray.from_arrays(
        [
            is_low_salary.combine_chunks(),
            is_average_salary.combine_chunks(),
            is_high_salary.combine_chunks(),
        ],
        names=["Low Salary", "Average Salary", "High Salary"],
    )

    table = table.append_column(
        "category", pc.case_when(cond, "Low Salary", "Average Salary", "High Salary")
    )
    grouped = (
        table.group_by("category")
        .aggregate([("account_id", "count")])
        .rename_columns({"account_id_count": "accounts_count"})
    )
    joined = categories.join(grouped, keys="category", join_type="left outer")
    return joined.set_column(
        1, "accounts_count", pc.fill_null(joined["accounts_count"], pa.scalar(0))
    )


def problem_1934(signups: pa.Table, confirmations: pa.Table) -> pa.Table:
    joined = signups.join(
        confirmations, keys=["user_id"], join_type="left outer"
    ).select(["user_id", "action"])
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
