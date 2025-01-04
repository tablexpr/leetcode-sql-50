"""Solutions to LeetCode problems in Polars."""

import polars as pl


def problem_176(employee: pl.DataFrame) -> pl.DataFrame:
    """Find the second highest distinct salary from the Employee table.

    If there is no second highest salary, return null.

    Parameters
    ----------
    employee : pl.DataFrame
        The table containing employee salary data.

    Returns
    -------
    pl.DataFrame

    Examples
    --------
    >>> import polars as pl
    >>> from problems.datasets import load_problem_176
    >>> from problems.polars import problem_176
    >>> employee = pl.DataFrame(load_problem_176())
    >>> problem_176(employee)
    ┌─────────────────────┐
    │ SecondHighestSalary │
    │ ---                 │
    │ i64                 │
    ╞═════════════════════╡
    │ 200                 │
    └─────────────────────┘

    """
    filtered = employee.select("salary").unique().sort("salary", descending=True)
    second_highest_salary = filtered[1, "salary"] if filtered.height > 1 else None
    return pl.DataFrame({"SecondHighestSalary": [second_highest_salary]})


def problem_180(logs: pl.DataFrame) -> pl.DataFrame:
    """Find all numbers that appear at least three times consecutively.

    Return the result table in any order.

    Parameters
    ----------
    logs : pl.DataFrame
        A table containing sequential ids and numbers.

    Returns
    -------
    pl.DataFrame

    Examples
    --------
    >>> import polars as pl
    >>> from problems.datasets import load_problem_180
    >>> from problems.polars import problem_180
    >>> logs = pl.DataFrame(load_problem_180())
    >>> problem_180(logs)
    ┌─────────────────┐
    │ ConsecutiveNums │
    │ ---             │
    │ i64             │
    ╞═════════════════╡
    │ 1               │
    └─────────────────┘

    """
    if logs.is_empty():
        return pl.DataFrame({"ConsecutiveNums": [None]}).cast(pl.Int64)

    logs_lead_1 = logs.with_columns((pl.col("id") + 1).alias("id"))
    logs_lead_2 = logs.with_columns((pl.col("id") + 2).alias("id"))

    return (
        logs.join(logs_lead_1, on=["id", "num"])
        .join(logs_lead_2, on=["id", "num"])
        .select("num")
        .unique()
        .rename({"num": "ConsecutiveNums"})
    )
