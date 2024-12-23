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


def problem_180(logs: pd.DataFrame) -> pd.DataFrame:
    """Find all numbers that appear at least three times consecutively.

    Return the result table in any order.

    Parameters
    ----------
    logs : pd.DataFrame
        A table containing sequential ids and numbers.

    Returns
    -------
    pd.DataFrame

    """
    if logs.empty:
        return pd.DataFrame({"ConsecutiveNums": [None]})

    logs_lead_1 = logs.assign(id=logs["id"] + 1)
    logs_lead_2 = logs.assign(id=logs["id"] + 2)

    return (
        logs.merge(logs_lead_1, on=["id", "num"])
        .merge(logs_lead_2, on=["id", "num"])[["num"]]
        .drop_duplicates()
        .rename(columns={"num": "ConsecutiveNums"})
    )


def problem_197(weather: pd.DataFrame) -> pd.DataFrame:
    """Find IDs of dates with higher temperatures than the previous day.

    Write a solution to find all dates' id with higher temperatures compared to its
    previous dates (yesterday).

    Return the result table in any order.

    Parameters
    ----------
    weather : pd.DataFrame
        A table contains information about the temperature on a certain day.

    Returns
    -------
    pd.DataFrame

    """
    weather = weather.sort_values("recordDate")
    mask = (weather["temperature"] > weather["temperature"].shift(1)) & (
        weather["recordDate"].shift(1) == weather["recordDate"] - pd.Timedelta("1 day")
    )
    return weather[mask][["id"]]


def problem_577(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    """Report the name and bonus amount of each employee with a bonus less than 1000.

    Return the result table in any order.

    Parameters
    ----------
    employee : pd.DataFrame
        Table shows employee names, IDs, salaries, and their manager's ID.
    bonus : pd.DataFrame
        Table contains the id of an employee and their respective bonus.

    Returns
    -------
    pd.DataFrame

    Examples
    --------
    >>> import pandas as pd
    >>> from problems.pandas import problem_577
    >>> from problems.datasets import load_problem_577
    >>> data = load_problem_577()
    >>> employee = data[0]
    >>> bonus = data[1]
    >>> problem_577(employee, bonus)

    """
    joined = employee.merge(bonus, how="left")
    return joined.loc[
        (joined["bonus"] < 1000) | joined["bonus"].isnull(), ["name", "bonus"]
    ]


def problem_584(customer: pd.DataFrame) -> pd.DataFrame:
    """Find names of customers not referred by the customer with ID = 2.

    Return the result table in any order.

    Parameters
    ----------
    customer : pd.DataFrame
        Table shows customer IDs, names, and the ID of the customer who referred them.

    Returns
    -------
    pd.DataFrame

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


def problem_1068(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
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
    pd.DataFrame

    """
    return sales.merge(product, on="product_id")[["product_name", "year", "price"]]


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
    customer : pd.DataFrame
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


def problem_1378(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    """Find the unique ID of each user.

    If a user does not have a unique ID replace just show null.

    Return the result table in any order.

    Parameters
    ----------
    employees : pd.DataFrame
        This table contains the id and the name of an employee in a company.
    employee_uni : pd.DataFrame
        Contains the id and the corresponding unique id of an employee in the company.

    Returns
    -------
    pd.DataFrame

    """
    return employees.merge(employee_uni, how="left", on="id")[["unique_id", "name"]]


def problem_1581(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """Find users who visited without transactions and count their visit frequency.

    Return the result table sorted in any order.

    Parameters
    ----------
    visits : pd.DataFrame
        Table containing information about the customers who visited the mall.
    transactions : pd.DataFrame
        Table containing information about the transactions made during the visit_id.

    Returns
    -------
    pd.DataFrame

    """
    joined = visits.merge(transactions, how="left")
    return (
        joined.loc[joined["transaction_id"].isnull(), ["visit_id", "customer_id"]]
        .groupby("customer_id", as_index=False)
        .count()
        .rename(columns={"visit_id": "count_no_trans"})
    )


def problem_1661(activity: pd.DataFrame) -> pd.DataFrame:
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
    activity : pd.DataFrame
        Table logs machine process activities with unique machine_id, process_id, type.

    Returns
    -------
    pd.DataFrame

    """
    activity_starts = activity.loc[
        activity["activity_type"] == "start", ["machine_id", "process_id", "timestamp"]
    ]
    activity_ends = activity.loc[
        activity["activity_type"] == "end", ["machine_id", "process_id", "timestamp"]
    ]
    joined = activity_starts.merge(
        activity_ends,
        on=["machine_id", "process_id"],
        how="outer",
        suffixes=("_start", "_end"),
    )
    joined["processing_time"] = joined["timestamp_end"] - joined["timestamp_start"]
    result = (
        joined.groupby("machine_id", dropna=False)
        .agg(processing_time=("processing_time", "mean"))
        .reset_index()
    )
    result["processing_time"] = result["processing_time"].round(3)

    return result


def problem_1683(tweets: pd.DataFrame) -> pd.DataFrame:
    """Find the IDs of the invalid tweets.

    The tweet is invalid if the number of characters used in the content of the tweet
    is strictly greater than 15.

    Return the result table in any order.

    Parameters
    ----------
    tweets : pd.DataFrame
        This table contains all the tweets in a social media app.

    Returns
    -------
    pd.DataFrame

    """
    return tweets[tweets["content"].str.len() > 15][["tweet_id"]]


def problem_1757(products: pd.DataFrame) -> pd.DataFrame:
    """Find the ids of products that are both low fat and recyclable.

    Return the result table in any order.

    Parameters
    ----------
    products : pd.DataFrame
        Table stores products with low_fats and recyclable, keyed by product_id.

    Returns
    -------
    pd.DataFrame

    """
    return pd.DataFrame(
        products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")][
            "product_id"
        ]
    )
