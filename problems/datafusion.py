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
    pa.Table

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


def problem_620(cinema: pa.Table) -> datafusion.dataframe.DataFrame:
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
    ctx = datafusion.SessionContext()
    cinema = ctx.from_arrow(cinema)
    return cinema.filter(F.col("description") != "boring", F.col("id") % 2 == 1).sort(
        F.col("id").sort(ascending=False)
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
    pa.Table

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
    return ctx.sql(query).to_arrow_table()


def problem_1378(employees: pa.Table, employee_uni: pa.Table) -> pa.Table:
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
    pa.Table

    """
    ctx = datafusion.SessionContext()
    employees = ctx.from_arrow(employees, name="employees")
    employee_uni = ctx.from_arrow(employee_uni, name="employee_uni")
    return (
        employees.join(employee_uni, join_keys=(["id"], ["id"]), how="left")
        .select("unique_id", "name")
        .to_arrow_table()
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
