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


def problem_584(customer: pd.DataFrame) -> pd.DataFrame:
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
    mask = customer[(customer["referee_id"].isnull()) | (customer["referee_id"] != 2)]
    return mask[["name"]]


def problem_595(world: pd.DataFrame) -> pd.DataFrame:
    """Find the name, population, and area of the big countries.

    A country is big if:
        it has an area of at least three million (i.e., 3000000 km2), or
        it has a population of at least twenty-five million (i.e., 25000000).

    Return the result table in any order.

    Parameters
    ----------
    world : pd.DataFrame
        Table lists countries with their continent, area, population, and GDP details.

    Returns
    -------
    pd.DataFrame

    """
    columns = ["name", "population", "area"]
    big_mask = (world["area"] >= 3_000_000) | (world["population"] >= 25_000_000)
    world = world[big_mask]
    return world[columns]


def problem_1148(views: pd.DataFrame) -> pd.DataFrame:
    """Find all the authors that viewed at least one of their own articles.

    Return the result table sorted by id in ascending order.

    Parameters
    ----------
    views : pd.DataFrame
        Table logs viewers viewing articles by authors on specific dates.

    Returns
    -------
    pd.DataFrame

    """
    return (
        views[views["author_id"] == views["viewer_id"]][["author_id"]]
        .drop_duplicates()
        .sort_values("author_id")
        .rename(columns={"author_id": "id"})
    )


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


def problem_1757(products: pd.DataFrame) -> pd.DataFrame:
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
    return pd.DataFrame(
        products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")][
            "product_id"
        ]
    )
