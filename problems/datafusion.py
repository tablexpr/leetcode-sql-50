"""Solutions to LeetCode problems in DataFusion."""

from textwrap import dedent

import datafusion
import datafusion.functions as F
import pyarrow as pa


def problem_176(employee: pa.Table) -> datafusion.dataframe.DataFrame:
    """Find the second highest distinct salary from the Employee table.

    If there is no second highest salary, return null.

    Parameters
    ----------
    employee : pa.Table
        The table containing employee salary data.

    Returns
    -------
    datafusion.dataframe.DataFrame

    """
    ctx = datafusion.SessionContext()
    t = (
        ctx.from_arrow(employee)
        .select(
            F.col("salary").alias("SecondHighestSalary"),
            F.rank(order_by=[F.col("salary")]).alias("rank"),
        )
        .filter(F.col("rank") == 2)
        .distinct()
        .select(F.col("SecondHighestSalary"))
    )
    if t.count() == 0:
        return ctx.from_arrow(pa.table({"SecondHighestSalary": [None]}))
    return t


def problem_180(logs: pa.Table) -> datafusion.dataframe.DataFrame:
    """Find all numbers that appear at least three times consecutively.

    Return the result table in any order.

    Parameters
    ----------
    logs : pa.Table
        A table containing sequential ids and numbers.

    Returns
    -------
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import datafusion.functions as F
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_180
    >>> from problems.datasets import load_problem_180
    >>> ctx = datafusion.SessionContext()
    >>> logs = pa.table(load_problem_180())
    >>> problem_180(logs)
    DataFrame()
    +-----------------+
    | ConsecutiveNums |
    +-----------------+
    | 1               |
    +-----------------+

    """
    ctx = datafusion.SessionContext()
    logs = ctx.from_arrow(logs)
    logs = logs.select(
        F.col("num"),
        F.lag(F.col("num"), order_by=[F.col("id")]).alias("num_lag_1"),
        F.lag(F.col("num"), 2, order_by=[F.col("id")]).alias("num_lag_2"),
    )
    filtered = (
        logs.filter(
            (F.col("num") == F.col("num_lag_1")) & (F.col("num") == F.col("num_lag_2"))
        )
        .select("num")
        .with_column_renamed("num", "ConsecutiveNums")
    )
    ctx.from_arrow(filtered.to_arrow_table(), "filtered")
    result = ctx.sql("""SELECT DISTINCT "ConsecutiveNums" FROM filtered""")
    if result.to_arrow_table().num_rows == 0:
        return ctx.from_arrow(
            pa.table(
                {"ConsecutiveNums": [pa.scalar(None, type=pa.int64())]},
                schema=pa.schema({"ConsecutiveNums": pa.int64()}),
            )
        )
    return result


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
    ctx = datafusion.SessionContext()
    activity = ctx.from_arrow(activity)
    # TODO: Why do I need to cache for this to work without an Internal error?
    distinct_players = activity.select("player_id").distinct().cache().count()
    expr = F.lag(
        F.col("event_date"),
        partition_by=[F.col("player_id")],
        order_by=[F.col("event_date")],
    ).alias("event_date_lag")
    ctx.from_arrow(
        activity.select("event_date", expr).to_arrow_table(), name="event_date_lags"
    )


def problem_584(customer: pa.Table) -> datafusion.dataframe.DataFrame:
    """Find names of customers not referred by the customer with ID = 2.

    Return the result table in any order.

    Parameters
    ----------
    customer : pa.Table
        Table shows customer IDs, names, and the ID of the customer who referred them.

    Returns
    -------
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_584
    >>> from problems.datasets import load_problem_584
    >>> ctx = datafusion.SessionContext()
    >>> customer = pa.table(load_problem_584())
    >>> problem_584(customer)
    DataFrame()
    +------+
    | name |
    +------+
    | Will |
    | Jane |
    | Bill |
    | Zack |
    +------+

    """
    ctx = datafusion.SessionContext()
    customer = ctx.from_arrow(customer)
    return customer.filter(
        (F.col("referee_id") != 2) | (F.col("referee_id").is_null())
    ).select("name")


def problem_595(world: pa.Table) -> datafusion.dataframe.DataFrame:
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
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_595
    >>> from problems.datasets import load_problem_595
    >>> ctx = datafusion.SessionContext()
    >>> world = pa.table(load_problem_595())
    >>> problem_595(world)
    DataFrame()
    +-------------+------------+---------+
    | name        | population | area    |
    +-------------+------------+---------+
    | Afghanistan | 25500100   | 652230  |
    | Algeria     | 37100000   | 2381741 |
    +-------------+------------+---------+

    """
    ctx = datafusion.SessionContext()
    world = ctx.from_arrow(world)
    return world.filter(
        (F.col("area") >= 3_000_000) | (F.col("population") >= 25_000_000)
    ).select("name", "population", "area")


def problem_620(cinema: pa.Table) -> datafusion.dataframe.DataFrame:
    """Report movies with odd IDs and descriptions not equal to "boring".

    Return the result table ordered by rating in descending order.

    Parameters
    ----------
    cinema : pa.Table
        Table contains information about the name of a movie, genre, and its rating.

    Returns
    -------
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_620
    >>> from problems.datasets import load_problem_620
    >>> ctx = datafusion.SessionContext()
    >>> cinema = pa.table(load_problem_620())
    >>> problem_620(cinema)
    +----+------------+-------------+--------+
    | id | movie      | description | rating |
    +----+------------+-------------+--------+
    | 5  | House card | Interesting | 9.1    |
    | 1  | War        | great 3D    | 8.9    |
    +----+------------+-------------+--------+

    """
    ctx = datafusion.SessionContext()
    cinema = ctx.from_arrow(cinema)
    return cinema.filter(F.col("description") != "boring", F.col("id") % 2 == 1).sort(
        F.col("id").sort(ascending=False)
    )


def problem_1068(sales: pa.Table, product: pa.Table) -> datafusion.dataframe.DataFrame:
    """Report the product_name, year, and price for each sale_id in the Sales table.

    Return the resulting table in any order.

    Parameters
    ----------
    sales : pd.DataFrame
        This table shows a sale on the product product_id in a certain year.
    product : pd.DataFrame
        This table indicates the product name of each product.

    Returns
    -------
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_1068
    >>> from problems.datasets import load_problem_1068
    >>> ctx = datafusion.SessionContext()
    >>> data = load_problem_1068()
    >>> sales = data[0]
    >>> product = data[1]
    >>> problem_1068(sales, product)

    """
    ctx = datafusion.SessionContext()
    sales = ctx.from_arrow(sales)
    product = ctx.from_arrow(product)
    return sales.join(
        product, join_keys=(["product_id"], ["product_id"]), how="inner"
    ).select("product_name", "year", "price")


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
        1, "average_years", pc.round(joined["experience_years_mean"], 2)
    )


def problem_1148(views: pa.Table) -> datafusion.dataframe.DataFrame:
    """Find all the authors that viewed at least one of their own articles.

    Return the result table sorted by id in ascending order.

    Parameters
    ----------
    views : pa.Table
        Table logs viewers viewing articles by authors on specific dates.

    Returns
    -------
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_1148
    >>> from problems.datasets import load_problem_1148
    >>> ctx = datafusion.SessionContext()
    >>> views = pa.table(load_problem_1148())
    >>> problem_1148(views)
    DataFrame()
    +----+
    | id |
    +----+
    | 4  |
    | 7  |
    +----+

    """
    ctx = datafusion.SessionContext()
    views = ctx.from_arrow(views)
    return (
        views.filter(F.col("author_id") == F.col("viewer_id"))
        .select(F.col("author_id").alias("id"))
        .distinct()
        .sort(F.col("id").sort())
    )


def problem_1174(delivery: pa.Table) -> pa.Table:
    """Find the percentage of immediate orders in the first orders of all customers.

    If the customer's preferred delivery date is the same as the order date, then the
    order is called immediate; otherwise, it is called scheduled. The first order of a
    customer is the order with the earliest order date that the customer made. It is
    guaranteed that a customer has precisely one first order.

    Round the result to 2 decimal places.

    Parameters
    ----------
    delivery : pa.Table
        Table shows the order date, customer name, and preferred delivery date.

    Returns
    -------
    pa.Table

    """
    delivery = delivery.append_column(
        "is_immediate",
        (pc.equal(delivery["order_date"], delivery["customer_pref_delivery_date"])),
    )
    first_orders = delivery.group_by("customer_id").aggregate([("order_date", "min")])
    joined = delivery.join(
        first_orders,
        keys=["customer_id", "order_date"],
        right_keys=["customer_id", "order_date_min"],
        join_type="inner",
    )
    return pa.Table.from_arrays(
        [
            pa.array(
                [
                    pc.round(
                        pc.multiply(
                            pc.mean(pc.cast(joined["is_immediate"], pa.int16())),
                            pa.scalar(100.0),
                        ),
                        2,
                    )
                ]
            )
        ],
        names=["immediate_percentage"],
    )


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


def problem_1321(customer: pa.Table) -> datafusion.dataframe.DataFrame:
    """Compute the moving average of how much the customer paid in a seven days window.

    You are the restaurant owner and you want to analyze a possible expansion (there
    will be at least one customer every day). Seven day window refers to current day +
    6 days before. `average_amount` should be rounded to two decimal places.

    Return the result table ordered by visited_on in ascending order.

    Parameters
    ----------
    customer : pa.Table
        Table shows the amount paid by a customer on a certain day.

    Returns
    -------
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_1321
    >>> from problems.datasets import load_problem_1321
    >>> ctx = datafusion.SessionContext()
    >>> customer = pa.table(load_problem_1321())
    >>> problem_1321(customer)
    DataFrame()
    +---------------------+--------+----------------+
    | visited_on          | amount | average_amount |
    +---------------------+--------+----------------+
    | 2019-01-07T00:00:00 | 860    | 122.86         |
    | 2019-01-08T00:00:00 | 840    | 120.0          |
    | 2019-01-09T00:00:00 | 840    | 120.0          |
    | 2019-01-10T00:00:00 | 1000   | 142.86         |
    +---------------------+--------+----------------+

    """
    query = dedent(
        """
    SELECT visited_on,
        SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM
    (
        SELECT visited_on,
            SUM(amount) AS amount
        FROM Customer
        GROUP BY visited_on
    )
    OFFSET 6;
    """
    )
    ctx = datafusion.SessionContext()
    ctx.from_arrow(customer, name="customer")
    ctx.from_arrow(customer).aggregate(
        group_by=[F.col("visited_on")], aggs=[F.sum(F.col("amount")).alias("amount")]
    )
    return ctx.sql(query)


def problem_1378(
    employees: pa.Table, employee_uni: pa.Table
) -> datafusion.dataframe.DataFrame:
    """Find the unique ID of each user.

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
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_1378
    >>> from problems.datasets import load_problem_1378
    >>> ctx = datafusion.SessionContext()
    >>> data = load_problem_1378()
    >>> employees = data[0]
    >>> employee_uni = data[1]
    >>> problem_1378(employees, employee_uni)

    """
    ctx = datafusion.SessionContext()
    employees = ctx.from_arrow(employees, name="employees")
    employee_uni = ctx.from_arrow(employee_uni, name="employee_uni")
    return employees.join(employee_uni, join_keys=(["id"], ["id"]), how="left").select(
        "unique_id", "name"
    )


def problem_1484(activities: pa.Table) -> datafusion.dataframe.DataFrame:
    """Find for each date the number of different products sold and their names.

    The sold products names for each date should be sorted lexicographically.

    Return the result table ordered by sell_date.

    Parameters
    ----------
    activities : pa.Table
        The table containing the sales data.

    Returns
    -------
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_1484
    >>> from problems.datasets import load_problem_1484
    >>> ctx = datafusion.SessionContext()
    >>> activities = pa.table(load_problem_1484())
    >>> problem_1484(activities)
    DataFrame()
    +---------------------+----------+------------------------------+
    | sell_date           | num_sold | products                     |
    +---------------------+----------+------------------------------+
    | 2020-05-30T00:00:00 | 3        | Basketball,Headphone,T-Shirt |
    | 2020-06-01T00:00:00 | 2        | Bible,Pencil                 |
    | 2020-06-02T00:00:00 | 1        | Mask                         |
    +---------------------+----------+------------------------------+

    """
    ctx = datafusion.SessionContext()
    ctx.from_arrow(activities, name="activities")
    ctx.from_arrow(
        ctx.table("activities").distinct().to_arrow_table(),
        name="distinct_product_dates",
    )
    return (
        ctx.table("distinct_product_dates")
        .aggregate(
            group_by=[
                F.col("sell_date"),
            ],
            aggs=[
                F.count(F.col("product")).alias("num_sold"),
                F.array_agg(F.col("product")).alias("products"),
            ],
        )
        .sort(F.col("sell_date"))
        .with_column(
            "products",
            F.array_join(
                F.array_sort(F.col("products")), delimiter=datafusion.lit(",")
            ),
        )
    )


def problem_1517(users: pa.Table) -> datafusion.dataframe.DataFrame:
    """Find the users who have valid emails.

    A valid e-mail has a prefix name and a domain where:

    The prefix name is a string that may contain letters (upper or lower case), digits,
    underscore '_', period '.', and/or dash '-'. The prefix name must start with a
    letter.

    Return the result table in any order.

    Parameters
    ----------
    users : pa.Table
        Table containing user names and emails.

    Returns
    -------
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_1517
    >>> from problems.datasets import load_problem_1517
    >>> ctx = datafusion.SessionContext()
    >>> users = pa.table(load_problem_1517())
    >>> problem_1517(users)
    DataFrame()
    +---------+-----------+-------------------------+
    | user_id | name      | mail                    |
    +---------+-----------+-------------------------+
    | 1       | Winston   | winston@leetcode.com    |
    | 3       | Annabelle | bella-@leetcode.com     |
    | 4       | Sally     | sally.come@leetcode.com |
    +---------+-----------+-------------------------+

    """
    ctx = datafusion.SessionContext()
    users = ctx.from_arrow(users, "users")
    return ctx.sql("""
        SELECT *
        FROM users
        WHERE REGEXP_MATCH(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$') IS NOT NULL
    """)


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


def problem_1683(tweets: pa.Table) -> datafusion.dataframe.DataFrame:
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
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_1683
    >>> from problems.datasets import load_problem_1683
    >>> ctx = datafusion.SessionContext()
    >>> tweets = pa.table(load_problem_1683())
    >>> problem_1683(tweets)
    DataFrame()
    +----------+
    | tweet_id |
    +----------+
    | 2        |
    +----------+

    """
    ctx = datafusion.SessionContext()
    tweets = ctx.from_arrow(tweets)
    return tweets.filter(F.length(F.col("content")) > 15).select("tweet_id")


def problem_1757(products: pa.Table) -> datafusion.dataframe.DataFrame:
    """Find the ids of products that are both low fat and recyclable.

    Return the result table in any order.

    Parameters
    ----------
    products : pa.Table
        Table stores products with low_fats and recyclable, keyed by product_id.

    Returns
    -------
    datafusion.dataframe.DataFrame

    Examples
    --------
    >>> import datafusion
    >>> import pyarrow as pa
    >>> from problems.datafusion import problem_1757
    >>> from problems.datasets import load_problem_1757
    >>> ctx = datafusion.SessionContext()
    >>> products = ctx.from_arrow(products)
    >>> problem_1757(activities)
    DataFrame()
    +------------+
    | product_id |
    +------------+
    | 1          |
    | 3          |
    +------------+

    """
    ctx = datafusion.SessionContext()
    products = ctx.from_arrow(products)
    return products.filter(F.col("low_fats") == "Y", F.col("recyclable") == "Y").select(
        "product_id"
    )
