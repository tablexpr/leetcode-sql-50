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
