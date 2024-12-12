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
