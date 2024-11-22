"""Solutions to LeetCode problems in PyArrow."""

from datetime import datetime, timedelta

import pyarrow as pa
import pyarrow.compute as pc


def problem_176(employee: pa.Table) -> pa.Table:
    """Find the second highest distinct salary from the Employee table.

    If there is no second highest salary, return null.

    Parameters
    ----------
    employee : pa.Table
        The table containing employee salary data.

    Returns
    -------
    pa.Table

    """
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
    """Find all numbers that appear at least three times consecutively.

    Return the result table in any order.

    Parameters
    ----------
    logs : pa.Table
        A table containing sequential ids and numbers.

    Returns
    -------
    pa.Table

    """
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
    """Delete duplicate emails, keeping one unique email with the smallest ID.

    Write a solution to delete all duplicate emails, keeping only one unique email
    with the smallest id.

    The final order of the Person table does not matter.

    Parameters
    ----------
    person : pa.Table
        A table containing email addresses.

    Returns
    -------
    pa.Table

    """
    # There isn't really a way to modify a PyArrow table in place, so we have
    # to create a new table to return the desired results.
    return (
        person.group_by(["email"])
        .aggregate([("id", "min")])
        .rename_columns({"id_min": "id"})
        .select(["id", "email"])
    )


def problem_197(weather: pa.Table) -> pa.Table:
    """Find IDs of dates with higher temperatures than the previous day.

    Write a solution to find all dates' id with higher temperatures compared to its
    previous dates (yesterday).

    Return the result table in any order.

    Parameters
    ----------
    weather : pa.Table
        A table contains information about the temperature on a certain day.

    Returns
    -------
    pa.Table

    """
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
    """Report the fraction of players who logged in the day after their first login.

    Write a solution to report the fraction of players that logged in again on the
    day after the day they first logged in, rounded to 2 decimal places. In other
    words, you need to count the number of players that logged in for at least two
    consecutive days starting from their first login date, then divide that number by
    the total number of players.

    Parameters
    ----------
    activity : pa.Table
        This table shows the activity of players of some games.

    Returns
    -------
    pa.Table

    """
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
    """Find managers with at least five direct reports.

    Return the result table in any order.

    Parameters
    ----------
    employee : pa.Table
        Table lists employee names, departments, and their manager's ID.

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
    """Report the name and bonus amount of each employee with a bonus less than 1000.

    Return the result table in any order.

    Parameters
    ----------
    employee : pa.Table
        Table shows employee names, IDs, salaries, and their manager's ID.
    bonus : pa.Table
        Table contains the id of an employee and their respective bonus.

    Returns
    -------
    pa.Table

    """
    return employee.join(bonus, keys="empId").select(["name", "bonus"])


def problem_584(customer: pa.Table) -> pa.Table:
    """Find names of customers not referred by the customer with ID = 2.

    Return the result table in any order.

    Parameters
    ----------
    customer : pa.Table
        Table shows customer IDs, names, and the ID of the customer who referred them.

    Returns
    -------
    pa.Table

    """
    return customer.filter(
        pc.or_kleene(
            pc.is_null(customer["referee_id"]),
            pc.not_equal(customer["referee_id"], pa.scalar(2)),
        )
    ).select(["name"])


def problem_585(insurance: pa.Table) -> pa.Table:
    """Report the sum of all total investment values in 2016 given conditions.

    Policyholder must have the same tiv_2015 value as one or more other policyholders,
    and are not located in the same city as any other policyholder.
    (i.e., the (lat, lon) attribute pairs must be unique).

    Round tiv_2016 to two decimal places.

    Parameters
    ----------
    insurance : pa.Table
        Table contains information about policy investments.

    Returns
    -------
    pa.Table

    """
    dropped_duplicates = (
        insurance.group_by(["lat", "lon"])
        .aggregate([("pid", "count")])
        .filter(pc.greater(pc.field("pid_count"), pa.scalar(1)))
        .join(insurance, keys=["lat", "lon"], join_type="inner")
        .drop("pid_count")
        .join(insurance, keys=["lat", "lon"], join_type="right anti")
    )
    grouped = (
        insurance.group_by("tiv_2015")
        .aggregate([("pid", "count")])
        .filter(pc.greater(pc.field("pid_count"), pa.scalar(1)))
    )
    joined = dropped_duplicates.join(grouped, keys=["tiv_2015"], join_type="inner")
    return pa.Table.from_arrays(
        [pa.array([pc.sum(joined["tiv_2016"])])], names=["tiv_2016"]
    )


def problem_595(world: pa.Table) -> pa.Table:
    """Find the name, population, and area of the big countries.

    A country is big if:
        it has an area of at least three million (i.e., 3000000 km2), or
        it has a population of at least twenty-five million (i.e., 25000000).

    Return the result table in any order.

    Parameters
    ----------
    world : pa.Table
        Table lists countries with their continent, area, population, and GDP details.

    Returns
    -------
    pa.Table

    """
    return world.filter(
        pc.or_(
            pc.greater_equal(world["area"], pa.scalar(3_000_000)),
            pc.greater_equal(world["population"], pa.scalar(25_000_000)),
        )
    ).select(["name", "population", "area"])


def problem_596(courses: pa.Table) -> pa.Table:
    """Find all the classes that have at least five students.

    Return the result table in any order.

    Parameters
    ----------
    courses : pa.Table
        Table indicates the name of a student and the class in which they are enrolled.

    Returns
    -------
    pa.Table

    """
    table_agg = courses.group_by("class").aggregate([("student", "count")])
    return table_agg.filter(
        pc.greater_equal(table_agg["student_count"], pa.scalar(5))
    ).select(["class"])


def problem_602(request_accepted: pa.Table) -> pa.Table:
    """Find who has the most number of friends, report who and how many.

    There can be no ties.

    Parameters
    ----------
    request_accepted : pa.Table
        Table shows the friend requests that have been accepted.

    Returns
    -------
    pa.Table

    """
    counted = pa.concat_arrays(
        [
            request_accepted["requester_id"].combine_chunks(),
            request_accepted["accepter_id"].combine_chunks(),
        ]
    ).value_counts()
    return (
        pa.Table.from_arrays([counted.field(0), counted.field(1)], names=["id", "num"])
        .sort_by([("num", "descending")])
        .take([0])
    )


def problem_610(triangle: pa.Table) -> pa.Table:
    """Report for every three line segments whether they can form a triangle.

    Return the result table in any order.

    Parameters
    ----------
    triangle : pa.Table
        Table contains the lengths of three line segments (x, y, z).

    Returns
    -------
    pa.Table

    """
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
    """Find the largest single number.

    A single number is a number that appeared only once in the MyNumbers table. If
    there is no single number, report null.

    Parameters
    ----------
    my_numbers : pa.Table
        Table containing numbers.

    Returns
    -------
    pa.Table

    """
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
    """Report movies with odd IDs and descriptions not equal to "boring".

    Return the result table ordered by rating in descending order.

    Parameters
    ----------
    cinema : pa.Table
        Table contains information about the name of a movie, genre, and its rating.

    Returns
    -------
    pa.Table

    """
    return cinema.filter(
        pc.and_(
            pc.equal(pc.bit_wise_and(cinema["id"], pa.scalar(1)), pa.scalar(1)),
            pc.not_equal(cinema["description"], pa.scalar("boring")),
        )
    ).sort_by([("id", "descending")])


def problem_626(seat: pa.Table) -> pa.Table:
    """Swap seat IDs of consecutive students; leave last ID unchanged if count is odd.

    Write a solution to swap the seat id of every two consecutive students. If the
    number of students is odd, the id of the last student is not swapped.

    Return the result table ordered by id in ascending order.

    Parameters
    ----------
    seat : pa.Table
        Table indicates the name and the ID of a student.

    Returns
    -------
    pa.Table

    """
    seat = seat.append_column(
        "exchange_id",
        pc.add(
            seat["id"],
            pc.subtract(seat["id"], pc.multiply(pc.divide(seat["id"], 2), 2)),
        ),
    )
    joined = (
        seat.join(
            seat,
            keys="exchange_id",
            join_type="inner",
            left_suffix="_x",
            right_suffix="_y",
        )
        .filter(pc.not_equal(pc.field("id_x"), pc.field("id_y")))
        .select(["id_x", "student_y"])
        .rename_columns({"id_x": "id", "student_y": "student"})
    )
    if joined.num_rows < seat.num_rows:
        return pa.concat_tables(
            [joined, seat.select(["id", "student"]).take([seat.num_rows - 1])]
        )
    return joined


def problem_1045(customer: pa.Table, product: pa.Table) -> pa.Table:
    """Report the customer ids that bought all the products in the Product table.

    Return the result table in any order.

    Parameters
    ----------
    customer : pa.Table
        Table of customer product purchases.
    product : pa.Table
        Defines unique products with product_key as the primary key.

    Returns
    -------
    pa.Table

    """
    grouped = customer.group_by("customer_id").aggregate(
        [("product_key", "count_distinct")]
    )
    return grouped.filter(
        pc.equal(grouped["product_key_count_distinct"], pa.scalar(product.num_rows))
    ).select(["customer_id"])


def problem_1068(sales: pa.Table, product: pa.Table) -> pa.Table:
    """Report the product_name, year, and price for each sale_id in the Sales table.

    Return the resulting table in any order.

    Parameters
    ----------
    sales : pa.Table
        This table shows a sale on the product product_id in a certain year.
    product : pa.Table
        This table indicates the product name of each product.

    Returns
    -------
    pa.Table

    """
    return sales.join(product, keys="product_id").select(
        ["product_name", "year", "price"]
    )


def problem_1070(sales: pa.Table, product: pa.Table) -> pa.Table:
    """Return details for the first year of every product sold.

    Select the product id, year, quantity, and price

    Return the resulting table in any order.

    Parameters
    ----------
    sales : pa.Table
        This table shows a sale on the product product_id in a certain year.

    product : pa.Table
        This table indicates the product name of each product.

    Returns
    -------
    pa.Table

    """
    min_product_year = sales.group_by("product_id").aggregate([("year", "min")])
    return (
        sales.join(
            min_product_year,
            keys=["product_id", "year"],
            right_keys=["product_id", "year_min"],
            join_type="inner",
        )
        .rename_columns({"year": "first_year"})
        .select(["product_id", "first_year", "quantity", "price"])
    )


def problem_1075(project: pa.Table, employee: pa.Table) -> pa.Table:
    """Report each project's average employee experience, rounded to 2 digits.

    Return the result table in any order.

    Parameters
    ----------
    project : pa.Table
        Table shows employees (employee_id) working on projects (project_id).
    employee : pa.Table
        This table contains information about one employee.

    Returns
    -------
    pa.Table

    """
    joined = (
        project.join(employee, keys="employee_id", join_type="inner")
        .group_by("project_id")
        .aggregate([("experience_years", "mean")])
    )
    return joined.set_column(
        1, "experience_years", pc.round(joined["experience_years_mean"], 2)
    )


def problem_1141(activity: pa.Table) -> pa.Table:
    """Find the daily active user count for a period of 30 days.

    The period ends on 2019-07-27 inclusively. A user was active on someday if they
    made at least one activity on that day.

    Return the result table in any order.

    Parameters
    ----------
    activity : pa.Table
        The table shows the user activities for a social media website.

    Returns
    -------
    pa.Table

    """
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
    """Find all the authors that viewed at least one of their own articles.

    Return the result table sorted by id in ascending order.

    Parameters
    ----------
    views : pa.Table
        Table logs viewers viewing articles by authors on specific dates.

    Returns
    -------
    pa.Table

    """
    return (
        views.filter(pc.equal(views["author_id"], views["viewer_id"]))
        .select(["author_id"])
        .rename_columns(["id"])
        .group_by("id")
        .aggregate([])
        .sort_by("id")
    )


def problem_1164(products: pa.Table) -> pa.Table:
    """Find the prices of all products on 2019-08-16.

    Assume the price of all products before any change is 10.

    Return the result table in any order.

    Parameters
    ----------
    products : pa.Table
        Table tracks product price changes with new prices and corresponding dates.

    Returns
    -------
    pa.Table

    """
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


def problem_1193(transactions: pa.Table) -> pa.Table:
    """Find monthly, country-wise transaction counts, totals, approved counts and sums.

    Find for each month and country, the number of transactions and their total amount,
    the number of approved transactions and their total amount.

    Return the result table in any order.

    Parameters
    ----------
    transactions : pa.Table
        The table has information about incoming transactions.

    Returns
    -------
    pa.Table

    """
    transactions = transactions.append_column(
        "month", pc.strftime(transactions["trans_date"], "%Y-%m")
    )
    transactions = transactions.append_column(
        "is_approved",
        pc.if_else(
            pc.equal(transactions["state"], "approved"), pa.scalar(1), pa.scalar(0)
        ),
    )
    transactions = transactions.append_column(
        "approved_amount",
        pc.if_else(
            pc.equal(
                pc.if_else(
                    pc.equal(transactions["state"], "approved"),
                    pa.scalar(1),
                    pa.scalar(0),
                ),
                pa.scalar(1),
            ),
            transactions["amount"],
            pa.scalar(0),
        ),
    )
    return (
        transactions.group_by(["month", "country"])
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


def problem_1204(queue: pa.Table) -> pa.Table:
    """Find the last person who can board the bus without exceeding the weight limit.

    There is a queue of people waiting to board a bus. However, the bus has a weight
    limit of 1000 kilograms, so there may be some people who cannot board.

    Note that only one person can board the bus at any given turn.

    Parameters
    ----------
    queue : pa.Table
        This table has the information about all people waiting for a bus.

    Returns
    -------
    pa.Table

    """
    queue = queue.sort_by("turn")
    queue = queue.append_column("weight_cumsum", pc.cumulative_sum(queue["weight"]))
    queue = queue.filter(pc.less_equal(queue["weight_cumsum"], pa.scalar(1000)))
    return queue.take([queue.num_rows - 1]).select(["person_name"])


def problem_1211(queries: pa.Table) -> pa.Table:
    """Find each query_name, the quality and poor_query_percentage.

    We define query quality as:
        The average of the ratio between query rating and its position.
    We also define poor query percentage as:
        The percentage of all queries with rating less than 3.

    Both quality and poor_query_percentage should be rounded to 2 decimal places.

    Return the result table in any order.

    Parameters
    ----------
    queries : pa.Table
        This table contains information collected from some queries on a database.

    Returns
    -------
    pa.Table

    """
    queries = queries.append_column(
        "quality", pc.divide(queries["rating"], queries["position"])
    ).append_column(
        "poor_query_percentage",
        pc.if_else(pc.less(queries["rating"], pa.scalar(3)), 100, 0),
    )

    queries_agg = queries.group_by("query_name").aggregate(
        [("quality", "mean"), ("poor_query_percentage", "mean")]
    )

    return queries_agg.set_column(
        1, "quality", pc.round(queries_agg["quality_mean"], 2)
    ).set_column(
        2,
        "poor_query_percentage",
        pc.round(queries_agg["poor_query_percentage_mean"], 2),
    )


def problem_1251(prices: pa.Table, units_sold: pa.Table) -> pa.Table:
    """Find the average selling price for each product.

    average_price should be rounded to 2 decimal places. If a product does not have any
    sold units, its average selling price is assumed to be 0.

    Return the result table in any order.

    Parameters
    ----------
    prices : pa.Table
        Table shows product prices by product_id for a date range.
    units_sold : pa.Table
        Table indicates the date, units, and product_id of each product sold.

    Returns
    -------
    pa.Table

    """
    joined = prices.join(units_sold, keys="product_id")
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
    """Find the number of times each student attended each exam.

    Return the result table ordered by student_id and subject_name.

    Parameters
    ----------
    students : pa.Table
        This table contains the ID and the name of one student in the school.
    subjects : pa.Table
        This table contains the name of one subject in the school.
    examinations : pa.Table
        This table indicates that a student attended the exam of subject_name.

    Returns
    -------
    pa.Table

    """
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
    """Find products that have at least 100 units ordered in February 2020.

    Return the result table in any order.

    Parameters
    ----------
    products : pa.Table
        The table containing product data.
    orders : pa.Table
        The table containing order data.

    Returns
    -------
    pa.Table

    """
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


def problem_1341(movies: pa.Table, users: pa.Table, movie_rating: pa.Table) -> pa.Table:
    """Find the top user by ratings and the highest-rated movie in February 2020.

    Identify the user who has rated the most movies. In case of a tie, return the
    lexicographically smaller user name.

    Identify the movie with the highest average rating in February 2020. In case of a
    tie, return the lexicographically smaller movie name.

    Parameters
    ----------
    movies : pa.Table
        The table containing movie data.
    users : pa.Table
        The table containing user data.
    movie_rating : pa.Table
        The table containing movie rating data.

    Returns
    -------
    pa.Table

    """
    user_most_ratings = (
        movie_rating.join(users, keys="user_id", join_type="inner")
        .group_by(["user_id", "name"])
        .aggregate([("movie_id", "count")])
        .sort_by([("movie_id_count", "descending"), ("name", "ascending")])
        .select(["name"])
        .take([0])["name"]
    )

    movie_highest_rating = (
        movie_rating.filter(
            pc.equal(
                pc.strftime(movie_rating["created_at"], "%Y-%m"), pa.scalar("2020-02")
            )
        )
        .join(movies, keys="movie_id", join_type="inner")
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
    """Find the unique ID of each user,.

    If a user does not have a unique ID replace just show null.

    Return the result table in any order.

    Parameters
    ----------
    employees : pa.Table
        This table contains the id and the name of an employee in a company.
    employee_uni : pa.Table
        Contains the id and the corresponding unique id of an employee in the company.

    Returns
    -------
    pa.Table

    """
    return employees.join(employee_uni, keys="id", join_type="left outer").select(
        ["unique_id", "name"]
    )


def problem_1527(patients: pa.Table) -> pa.Table:
    """Find the patients who have Type I Diabetes.

    Return the patient_id, patient_name, and conditions. Type I Diabetes always starts
    with DIAB1 prefix.

    Return the result table in any order.

    Parameters
    ----------
    patients : pa.Table
        A containing information of the patients in the hospital.

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


def problem_1581(visits: pa.Table, transactions: pa.Table) -> pa.Table:
    """Find users who visited without transactions and count their visit frequency.

    Return the result table sorted in any order.

    Parameters
    ----------
    visits : pa.Table
        Table containing information about the customers who visited the mall.
    transactions : pa.Table
        Table containing information about the transactions made during the visit_id.

    Returns
    -------
    pa.Table

    """
    joined = visits.join(transactions, keys="visit_id", join_type="left outer")
    return (
        joined.filter(pc.is_null(joined["transaction_id"]))
        .group_by("customer_id")
        .aggregate([("visit_id", "count")])
        .rename_columns({"visit_id_count": "count_no_trans"})
    )


def problem_1633(users: pa.Table, register: pa.Table) -> pa.Table:
    """Find the percentage of the users registered in each contest.

    Return the result table ordered by percentage in descending order. In case of a
    tie, order it by contest_id in ascending order. The result should be rounded to two
    decimals.

    Parameters
    ----------
    users : pa.Table
        This table contains the name and the id of a user.
    register : pa.Table
        This table contains the id of a user and the contest they registered into.

    Returns
    -------
    pa.Table

    """
    register_agg = register.group_by("contest_id").aggregate([("user_id", "count")])
    total_users = pa.scalar(float(users.num_rows))
    return register_agg.set_column(
        1,
        "percentage",
        pc.round(
            pc.divide(register_agg["user_id_count"], total_users),
            2,
        ),
    ).sort_by([("percentage", "descending")])


def problem_1661(activity: pa.Table) -> pa.Table:
    """Find the average time each machine takes to complete a process.

    There is a factory website that has several machines each running the same
    number of processes.

    The time to complete a process is the 'end' timestamp minus the 'start' timestamp.
    The average time is calculated by the total time to complete every process on the
    machine divided by the number of processes that were run.

    The resulting table should have the machine_id along with the average time as
    processing_time, which should be rounded to 3 decimal places.

    Return the result table in any order.

    Parameters
    ----------
    activity : pa.Table
        Table logs machine process activities with unique machine_id, process_id, type.

    Returns
    -------
    pa.Table

    """
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


def problem_1667(users: pa.Table) -> pa.Table:
    """Fix the names so that only the first character is uppercase.

    The remaining characters should be lowercase.

    Return the result table ordered by user_id.

    Parameters
    ----------
    users : pa.Table
        This table contains the ID and the name of the user.

    Returns
    -------
    pa.Table

    """
    return users.set_column(1, "name", pc.ascii_capitalize(users["name"])).sort_by(
        "user_id"
    )


def problem_1683(tweets: pa.Table) -> pa.Table:
    """Find the IDs of the invalid tweets.

    The tweet is invalid if the number of characters used in the content of the tweet
    is strictly greater than 15.

    Return the result table in any order.

    Parameters
    ----------
    tweets : pa.Table
        This table contains all the tweets in a social media app.

    Returns
    -------
    pa.Table

    """
    return tweets.filter(
        pc.greater(pc.utf8_length(tweets["content"]), pa.scalar(15))
    ).select(["tweet_id"])


def problem_1729(followers: pa.Table) -> pa.Table:
    """Return the number of followers for each user.

    Return the result table ordered by user_id in ascending order.

    Parameters
    ----------
    followers : pa.Table
        Table records user-follower relationships in a social media app.

    Returns
    -------
    pa.Table

    """
    return (
        followers.group_by("user_id")
        .aggregate([("follower_id", "count")])
        .rename_columns({"follower_id_count": "followers_count"})
        .sort_by("user_id")
    )


def problem_1731(employees: pa.Table) -> pa.Table:
    """Report manager IDs, names, count of direct reports, and mean age of reports.

    For this problem, we will consider a manager an employee who has at least 1 other
    employee reporting to them.

    Write a solution to report the ids and the names of all managers, the number of
    employees who report directly to them, and the average age of the reports rounded
    to the nearest integer.

    Return the result table ordered by employee_id.

    Parameters
    ----------
    employees : pa.Table
        Table contains information about employees and managers.

    Returns
    -------
    pa.Table

    """
    joined = (
        employees.join(
            employees,
            keys="employee_id",
            right_keys="reports_to",
            join_type="inner",
            right_suffix="_reports",
        )
        .group_by(["employee_id", "name"])
        .aggregate([("employee_id", "count"), ("age_reports", "mean")])
        .rename_columns(
            {
                "employee_id": "employee_id",
                "name": "name",
                "employee_id_count": "reports_count",
                "age_reports_mean": "average_age",
            }
        )
    )
    return joined.set_column(3, "average_age", pc.round(joined["average_age"], 2))


def problem_1757(products: pa.Table) -> pa.Table:
    """Find the ids of products that are both low fat and recyclable.

    Return the result table in any order.

    Parameters
    ----------
    products : pa.Table
        Table stores products with low_fats and recyclable, keyed by product_id.

    Returns
    -------
    pa.Table

    """
    return products.filter(
        pc.and_(
            pc.equal(products["low_fats"], pa.scalar("Y")),
            pc.equal(products["recyclable"], pa.scalar("Y")),
        )
    ).select(["product_id"])


def problem_1789(employee: pa.Table) -> pa.Table:
    """Report all the employees with their primary department.

    Employees can belong to multiple departments. When the employee joins other
    departments, they need to decide which department is their primary department. Note
    that when an employee belongs to only one department, their primary column is 'N'.

    For employees who belong to one department, report their only department.

    Return the result table in any order.

    Parameters
    ----------
    employee : pa.Table
        A table containing employee and department data.

    Returns
    -------
    pa.Table

    """
    joined = employee.join(
        employee.group_by("employee_id").aggregate([("employee_id", "count")]),
        keys="employee_id",
    )
    return joined.filter(
        pc.or_(
            pc.equal(joined["primary_flag"], pa.scalar("Y")),
            pc.equal(joined["employee_id_count"], pa.scalar(1)),
        )
    ).select(["employee_id", "department_id"])


def problem_1907(accounts: pa.Table) -> pa.Table:
    """Calculate the number of bank accounts for each salary category.

    The salary categories are:

    - "Low Salary": All the salaries strictly less than $20000.
    - "Average Salary": All the salaries in the inclusive range [$20000, $50000].
    - "High Salary": All the salaries strictly greater than $50000.

    The result table must contain all three categories. If there are no accounts in a category, return 0.

    Return the result table in any order.

    Parameters
    ----------
    accounts : pa.Table
        A table containing the account data.

    Returns
    -------
    pa.Table

    """
    categories = pa.Table.from_pydict(
        {"category": ["Low Salary", "Average Salary", "High Salary"]}
    )

    is_low_salary = pc.less(accounts["income"], pa.scalar(20_000))
    is_average_salary = pc.and_(
        pc.greater_equal(accounts["income"], pa.scalar(20_000)),
        pc.less_equal(accounts["income"], pa.scalar(50_000)),
    )
    is_high_salary = pc.greater(accounts["income"], pa.scalar(50_000))

    cond = pa.StructArray.from_arrays(
        [
            is_low_salary.combine_chunks(),
            is_average_salary.combine_chunks(),
            is_high_salary.combine_chunks(),
        ],
        names=["Low Salary", "Average Salary", "High Salary"],
    )

    accounts = accounts.append_column(
        "category", pc.case_when(cond, "Low Salary", "Average Salary", "High Salary")
    )
    grouped = (
        accounts.group_by("category")
        .aggregate([("account_id", "count")])
        .rename_columns({"account_id_count": "accounts_count"})
    )
    joined = categories.join(grouped, keys="category", join_type="left outer")
    return joined.set_column(
        1, "accounts_count", pc.fill_null(joined["accounts_count"], pa.scalar(0))
    )


def problem_1934(signups: pa.Table, confirmations: pa.Table) -> pa.Table:
    """Find the confirmation rate of each user.

    The confirmation rate of a user is the number of 'confirmed' messages divided by
    the total number of requested confirmation messages. The confirmation rate of a
    user that did not request any confirmation messages is 0. Round the confirmation
    rate to two decimal places.

    Return the result table in any order.

    Parameters
    ----------
    signups : pa.Table
        A table containing the user signups.
    confirmations : pa.Table
        A table containing the user confirmation messages.

    Returns
    -------
    pa.Table

    """
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


def problem_1978(employees: pa.Table) -> pa.Table:
    """Find employees whose salary is less than $30000 and whose manager left.

    When a manager leaves the company, their information is deleted from the Employees
    table, but the reports still have their manager_id set to the manager that left.

    Return the result table ordered by employee_id.

    Parameters
    ----------
    employees : pa.Table
        The table containing employee data.

    Returns
    -------
    pa.Table

    """
    return (
        employees.filter(
            pc.and_(
                pc.less(employees["salary"], pa.scalar(30_000)),
                pc.and_(
                    pc.invert(
                        pc.is_in(employees["manager_id"], employees["employee_id"])
                    ),
                    pc.invert(pc.is_null(employees["manager_id"])),
                ),
            )
        )
        .select(["employee_id"])
        .sort_by("employee_id")
    )


def problem_2356(teacher: pa.Table) -> pa.Table:
    """Calculate the number of unique subjects each teacher teaches in the university.

    Return the result table in any order.

    Parameters
    ----------
    teacher : pa.Table
        Table links teachers, subjects, and departments with unique subject-dept pairs.

    Returns
    -------
    pa.Table

    """
    return (
        teacher.group_by("teacher_id")
        .aggregate([("subject_id", "count_distinct")])
        .rename_columns({"subject_id_count_distinct": "cnt"})
    )
