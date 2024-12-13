"""Solutions to LeetCode problems in pandas."""

import pandas as pd


def problem_176(employee: pd.DataFrame) -> pd.DataFrame:
    """Find the second highest distinct salary from the Employee table.

    If there is no second highest salary, return null.

    Parameters
    ----------
    employee : pd.DataFrame
        The table containing employee salary data.

    Returns
    -------
    pd.DataFrame

    """
    filtered = (
        employee[["salary"]]
        .drop_duplicates()
        .sort_values("salary", ascending=False)
        .reset_index(drop=True)
    )
    second_highest_salary = filtered.iloc[1]["salary"] if len(filtered) > 1 else None
    result = pd.DataFrame([second_highest_salary], columns=["SecondHighestSalary"])
    if result.empty:
        return pd.DataFrame([None], columns=["SecondHighestSalary"])
    return result


def problem_1321(customer: pd.DataFrame) -> pd.DataFrame:
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
    pd.DataFrame

    """
    grouped = customer.groupby(["visited_on"]).aggregate(
        amount=pd.NamedAgg("amount", "sum")
    )
    grouped = (
        grouped.assign(amount=grouped["amount"].rolling("7D").sum())
        .reset_index()
        .loc[6:]
    )
    return grouped.assign(average_amount=(grouped["amount"] / 7).round(2))
