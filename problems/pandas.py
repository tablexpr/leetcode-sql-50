"""Solutions to LeetCode problems in pandas."""

from datetime import timedelta
from decimal import ROUND_HALF_UP, Decimal

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


def problem_185(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """Find the employees who are high earners in each of the departments.

    A company's executives are interested in seeing who earns the most money in each
    of the company's departments. A high earner in a department is an employee who has
    a salary in the top three unique salaries for that department.

    Return the result table in any order.

    Parameters
    ----------
    employee : pd.DataFrame
        Table containing employee salary data.
    department : pd.DataFrame
        Table containing department data.

    Returns
    -------
    pd.DataFrame

    """
    employee["rank"] = employee.groupby("departmentId")["salary"].rank(
        "dense", ascending=False
    )
    employee = employee.loc[employee["rank"] <= 3.0, ["departmentId", "name", "salary"]]
    return employee.merge(
        department, left_on="departmentId", right_on="id", how="inner"
    ).rename(
        columns={
            "name_x": "Employee",
            "name_y": "Department",
            "salary": "Salary",
        }
    )[["Department", "Employee", "Salary"]]


def problem_196(person: pd.DataFrame) -> pd.DataFrame:
    """Delete duplicate emails, keeping one unique email with the smallest ID.

    Write a solution to delete all duplicate emails, keeping only one unique email
    with the smallest id.

    The final order of the Person table does not matter.

    Parameters
    ----------
    person : pd.DataFrame
        A table containing email addresses.

    Returns
    -------
    pd.DataFrame

    """
    person = person.sort_values(["id", "email"], ascending=[True, True])
    return person.drop_duplicates(subset=["email"], keep="first")


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


def problem_550(activity: pd.DataFrame) -> pd.DataFrame:
    """Report the fraction of players who logged in the day after their first login.

    Write a solution to report the fraction of players that logged in again on the
    day after the day they first logged in, rounded to 2 decimal places. In other
    words, you need to count the number of players that logged in for at least two
    consecutive days starting from their first login date, then divide that number by
    the total number of players.

    Parameters
    ----------
    activity : pd.DataFrame
        This table shows the activity of players of some games.

    Returns
    -------
    pd.DataFrame

    """
    grouped = activity.groupby("player_id", as_index=False).aggregate(
        min_event_date=pd.NamedAgg("event_date", "min")
    )
    grouped["event_date"] = grouped["min_event_date"] + timedelta(days=1)
    joined = grouped.merge(activity, how="left", on=["player_id", "event_date"])
    joined.device_id.notna().sum() / len(joined.index)
    return pd.DataFrame(
        [joined.games_played.notna().sum() / len(joined.index)], columns=["fraction"]
    ).round(2)


def problem_620(cinema: pd.DataFrame) -> pd.DataFrame:
    """Report movies with odd IDs and descriptions not equal to "boring".

    Return the result table ordered by rating in descending order.

    Parameters
    ----------
    cinema : pd.DataFrame
        Table contains information about the name of a movie, genre, and its rating.

    Returns
    -------
    pd.DataFrame

    """
    mask = (cinema["id"] % 2 == 1) & (cinema["description"] != "boring")
    return cinema[mask].sort_values("description", ascending=False)


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


def problem_585(insurance: pd.DataFrame) -> pd.DataFrame:
    """Report the sum of all total investment values in 2016 given conditions.

    Policyholder must have the same tiv_2015 value as one or more other policyholders,
    and are not located in the same city as any other policyholder.
    (i.e., the (lat, lon) attribute pairs must be unique).

    Round tiv_2016 to two decimal places.

    Parameters
    ----------
    insurance : pd.DataFrame
        Table contains information about policy investments.

    Returns
    -------
    pd.DataFrame

    """
    dropped_duplicates = insurance.drop_duplicates(subset=["lat", "lon"], keep=False)
    grouped = insurance.groupby("tiv_2015", as_index=False).aggregate(
        count=pd.NamedAgg("pid", "count")
    )
    joined = dropped_duplicates.merge(grouped, on="tiv_2015")
    return pd.DataFrame(
        [joined.loc[joined["count"] > 1, "tiv_2016"].sum()], columns=["tiv_2016"]
    )


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


def problem_596(courses: pd.DataFrame) -> pd.DataFrame:
    """Find all the classes that have at least five students.

    Return the result table in any order.

    Parameters
    ----------
    courses : pd.DataFrame
        Table indicates the name of a student and the class in which they are enrolled.

    Returns
    -------
    pd.DataFrame

    """
    return (
        courses.groupby("class", as_index=False)
        .aggregate(count=pd.NamedAgg("student", "count"))
        .query("count >= 5")[["class"]]
    )


def problem_602(request_accepted: pd.DataFrame) -> pd.DataFrame:
    """Find who has the most number of friends, report who and how many.

    There can be no ties.

    Parameters
    ----------
    request_accepted : pd.DataFrame
        Table shows the friend requests that have been accepted.

    Returns
    -------
    pd.DataFrame

    """
    return (
        pd.concat([request_accepted.requester_id, request_accepted.accepter_id])
        .to_frame(name="id")
        .groupby("id", as_index=False)
        .aggregate(num=pd.NamedAgg("id", "count"))
        .sort_values("num", ascending=False)
        .head(1)
    )


def problem_610(triangle: pd.DataFrame) -> pd.DataFrame:
    """Report for every three line segments whether they can form a triangle.

    Return the result table in any order.

    Parameters
    ----------
    triangle : pd.DataFrame
        Table contains the lengths of three line segments (x, y, z).

    Returns
    -------
    pd.DataFrame

    """
    triangle["triangle"] = (
        (triangle["x"] + triangle["y"] > triangle["z"])
        & (triangle["x"] + triangle["z"] > triangle["y"])
        & (triangle["y"] + triangle["z"] > triangle["x"])
    )
    triangle["triangle"] = triangle["triangle"].map({True: "Yes", False: "No"})
    return triangle


def problem_619(my_numbers: pd.DataFrame) -> pd.DataFrame:
    """Find the largest single number.

    A single number is a number that appeared only once in the MyNumbers table. If
    there is no single number, report null.

    Parameters
    ----------
    my_numbers : pd.DataFrame
        Table containing numbers.

    Returns
    -------
    pd.DataFrame

    """
    return my_numbers.drop_duplicates(keep=False).max().to_frame(name="num")


def problem_626(seat: pd.DataFrame) -> pd.DataFrame:
    """Swap seat IDs of consecutive students; leave last ID unchanged if count is odd.

    Write a solution to swap the seat id of every two consecutive students. If the
    number of students is odd, the id of the last student is not swapped.

    Return the result table ordered by id in ascending order.

    Parameters
    ----------
    seat : pd.DataFrame
        Table indicates the name and the ID of a student.

    Returns
    -------
    pd.DataFrame

    """
    combined = seat.assign(exchange_id=seat.id % 2 + seat.id)
    joined = combined.merge(combined, how="inner", on="exchange_id")
    swapped = joined.loc[
        joined["id_x"] != joined["id_y"], ["id_x", "student_y"]
    ].rename(columns={"id_x": "id", "student_y": "student"})
    if len(seat.index) != len(swapped.index):
        return pd.concat([swapped, seat.tail(1)])
    return swapped


def problem_1045(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """Report the customer ids that bought all the products in the Product table.

    Return the result table in any order.

    Parameters
    ----------
    customer : pd.DataFrame
        Table of customer product purchases.
    product : pd.DataFrame
        Defines unique products with product_key as the primary key.

    Returns
    -------
    pd.DataFrame

    """
    grouped = (
        customer.drop_duplicates()
        .groupby("customer_id", as_index=False)
        .aggregate(products_purchased=pd.NamedAgg("product_key", "count"))
    )
    return grouped.loc[
        grouped["products_purchased"] == len(product.index), ["customer_id"]
    ]


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


def problem_1070(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """Return details for the first year of every product sold.

    Select the product id, year, quantity, and price

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

    Examples
    --------
    >>> import pandas as pd
    >>> from problems.pandas import problem_1070
    >>> from problems.datasets import load_problem_1070
    >>> data = load_problem_1070()
    >>> sales = data[0]
    >>> product = data[1]
    >>> problem_1070(sales, product)
      product_id  first_year  quantity  price
    0         100        2008        10   5000
    1         200        2011        15   9000

    """
    min_product_year = sales.groupby("product_id", as_index=False).aggregate(
        first_year=pd.NamedAgg("year", "min")
    )
    joined = sales.merge(
        min_product_year,
        left_on=["product_id", "year"],
        right_on=["product_id", "first_year"],
    )
    return joined[["product_id", "first_year", "quantity", "price"]]


def problem_1075(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    """Report each project's average employee experience, rounded to 2 digits.

    Return the result table in any order.

    Parameters
    ----------
    project : pd.DataFrame
        Table shows employees (employee_id) working on projects (project_id).
    employee : pd.DataFrame
        This table contains information about one employee.

    Returns
    -------
    pd.DataFrame

    Examples
    --------
    >>> import pandas as pd
    >>> from problems.pandas import problem_1075
    >>> from problems.datasets import load_problem_1075
    >>> project = load_problem_1075()[0]
    >>> employee = load_problem_1075()[1]
    >>> problem_1075(project, employee)
    project_id  average_years
    0           1            2.0
    1           2            2.5

    """
    joined = (
        project.merge(employee)
        .groupby("project_id")
        .aggregate(average_years=pd.NamedAgg(column="experience_years", aggfunc="mean"))
        .reset_index()
    )
    joined["average_years"] = joined["average_years"].round(2)
    return joined


def problem_1141(activity: pd.DataFrame) -> pd.DataFrame:
    """Find the daily active user count for a period of 30 days.

    The period ends on 2019-07-27 inclusively. A user was active on someday if they
    made at least one activity on that day.

    Return the result table in any order.

    Parameters
    ----------
    activity : pd.DataFrame
        The table shows the user activities for a social media website.

    Returns
    -------
    pd.DataFrame

    Examples
    --------
    >>> import pandas as pd
    >>> from problems.pandas import problem_1141
    >>> from problems.datasets import load_problem_1141
    >>> activity = load_problem_1141()
    >>> problem_1141(activity)
            day  active_users
    0 2019-07-20             2
    1 2019-07-21             2

    """
    return (
        activity[
            (
                activity["activity_date"]
                > pd.to_datetime("2019-07-27") - pd.DateOffset(days=30)
            )
            & (activity["activity_date"] <= pd.to_datetime("2019-07-27"))
        ]
        .groupby("activity_date")
        .user_id.nunique()
        .reset_index()
        .rename(columns={"activity_date": "day", "user_id": "active_users"})
    )


def problem_1164(products: pd.DataFrame) -> pd.DataFrame:
    """Find the prices of all products on 2019-08-16.

    Assume the price of all products before any change is 10.

    Return the result table in any order.

    Parameters
    ----------
    products : pd.DataFrame
        Table tracks product price changes with new prices and corresponding dates.

    Returns
    -------
    pd.DataFrame

    Examples
    --------
    >>> import pandas as pd
    >>> from problems.pandas import problem_1164
    >>> from problems.datasets import load_problem_1164
    >>> data = load_problem_1164()
    >>> products = data[0]
    >>> problem_1164(products)
        product_id  price
    0           2     50
    1           1     35
    5           3     10

    """
    products_filtered = products.loc[products["change_date"] <= "2019-08-16"]
    products_max_dates = products_filtered.groupby(["product_id"], as_index=False)[
        "change_date"
    ].max()
    joined = (
        products_filtered.merge(products_max_dates, on=["product_id", "change_date"])
        .drop(columns=["change_date"])
        .rename(columns={"new_price": "price"})
    )
    missing_products = products.assign(
        is_present=products["product_id"].isin(joined["product_id"])
    )
    missing_products = (
        missing_products.loc[~missing_products["is_present"], ["product_id"]]
        .assign(price=10)
        .drop_duplicates()
    )
    return pd.concat([joined, missing_products])


def problem_1174(delivery: pd.DataFrame) -> pd.DataFrame:
    """Find the percentage of immediate orders in the first orders of all customers.

    If the customer's preferred delivery date is the same as the order date, then the
    order is called immediate; otherwise, it is called scheduled. The first order of a
    customer is the order with the earliest order date that the customer made. It is
    guaranteed that a customer has precisely one first order.

    Round the result to 2 decimal places.

    Parameters
    ----------
    delivery : pd.DataFrame
        Table shows the order date, customer name, and preferred delivery date.

    Returns
    -------
    pd.DataFrame

    """
    delivery["is_immediate"] = (
        delivery["order_date"] == delivery["customer_pref_delivery_date"]
    ).astype(int)
    min_delivery = delivery.groupby("customer_id", as_index=False).aggregate(
        order_date=pd.NamedAgg("order_date", "min")
    )
    joined = delivery.merge(min_delivery)
    return pd.DataFrame(
        [(joined["is_immediate"].mean() * 100).round(2)],
        columns=["immediate_percentage"],
    )


def problem_1193(transactions: pd.DataFrame) -> pd.DataFrame:
    """Find monthly, country-wise transaction counts, totals, approved counts and sums.

    Find for each month and country, the number of transactions and their total amount,
    the number of approved transactions and their total amount.

    Return the result table in any order.

    Parameters
    ----------
    transactions : pd.DataFrame
        The table has information about incoming transactions.

    Returns
    -------
    pd.DataFrame

    """
    transactions["month"] = transactions["trans_date"].dt.strftime("%Y-%m")
    transactions["is_approved"] = transactions["state"] == "approved"
    transactions["approved_amount"] = transactions["is_approved"].case_when(
        [
            (transactions["is_approved"] == True, transactions["amount"]),  # noqa E712
            (transactions["is_approved"] == False, 0),  # noqa E712
        ]
    )

    return transactions.groupby(
        ["month", "country"], as_index=False, dropna=False
    ).aggregate(
        trans_count=pd.NamedAgg("id", "count"),
        approved_count=pd.NamedAgg("is_approved", "sum"),
        trans_total_amount=pd.NamedAgg("amount", "sum"),
        approved_total_amount=pd.NamedAgg("approved_amount", "sum"),
    )


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


def problem_1204(queue: pd.DataFrame) -> pd.DataFrame:
    """Find the last person who can board the bus without exceeding the weight limit.

    There is a queue of people waiting to board a bus. However, the bus has a weight
    limit of 1000 kilograms, so there may be some people who cannot board.

    Note that only one person can board the bus at any given turn.

    Parameters
    ----------
    queue : pd.DataFrame
        This table has the information about all people waiting for a bus.

    Returns
    -------
    pd.DataFrame

    """
    queue = queue.sort_values(by="turn")
    queue["weight_cumsum"] = queue["weight"].cumsum()
    return queue.loc[queue["weight_cumsum"] <= 1000, ["person_name"]].tail(1)


def problem_1211(queries: pd.DataFrame) -> pd.DataFrame:
    """Find each query_name, the quality and poor_query_percentage.

    We define query quality as:
        The average of the ratio between query rating and its position.
    We also define poor query percentage as:
        The percentage of all queries with rating less than 3.

    Both quality and poor_query_percentage should be rounded to 2 decimal places.

    Return the result table in any order.

    Parameters
    ----------
    queries : pd.DataFrame
        This table contains information collected from some queries on a database.

    Returns
    -------
    pd.DataFrame

    """
    queries["quality"] = queries["rating"] / queries["position"]
    queries["poor_query_percentage"] = (queries["rating"] < 3) * 100
    return (
        queries.groupby("query_name")[["quality", "poor_query_percentage"]]
        .mean()
        .map(
            lambda value: Decimal(value).quantize(
                Decimal("0.01"), rounding=ROUND_HALF_UP
            )
        )
        .reset_index()
    )


def problem_1251(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    """Find the average selling price for each product.

    average_price should be rounded to 2 decimal places. If a product does not have any
    sold units, its average selling price is assumed to be 0.

    Return the result table in any order.

    Parameters
    ----------
    prices : pd.DataFrame
        Table shows product prices by product_id for a date range.
    units_sold : pd.DataFrame
        Table indicates the date, units, and product_id of each product sold.

    Returns
    -------
    pd.DataFrame

    """
    joined = prices.merge(units_sold, how="left")
    joined = (
        joined.loc[
            (
                (joined["purchase_date"] >= joined["start_date"])
                & (joined["purchase_date"] <= joined["end_date"])
            )
            | (joined["purchase_date"].isna())
        ]
        .assign(total=joined["price"] * joined["units"])
        .fillna(0)
    )
    grouped = joined.groupby("product_id", as_index=False).aggregate(
        total_units=pd.NamedAgg("units", "sum"), total=pd.NamedAgg("total", "sum")
    )
    return grouped.assign(
        average_price=((grouped["total"] / grouped["total_units"]).round(2)).astype(
            float
        )
    )[["product_id", "average_price"]].fillna(0)


def problem_1280(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    """Find the number of times each student attended each exam.

    Return the result table ordered by student_id and subject_name.

    Parameters
    ----------
    students : pd.DataFrame
        This table contains the ID and the name of one student in the school.
    subjects : pd.DataFrame
        This table contains the name of one subject in the school.
    examinations : pd.DataFrame
        This table indicates that a student attended the exam of subject_name.

    Returns
    -------
    pd.DataFrame

    """
    examinations_agg = (
        examinations.groupby(["student_id", "subject_name"])
        .size()
        .reset_index(name="attended_exams")
    )
    joined = joined = (
        students.merge(subjects, how="cross")
        .merge(examinations_agg, how="left")
        .sort_values(["student_id", "subject_name"])
    )
    joined["attended_exams"] = joined["attended_exams"].fillna(0).astype(int)
    return joined


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


def problem_1327(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Find products that have at least 100 units ordered in February 2020.

    Return the result table in any order.

    Parameters
    ----------
    products : pd.DataFrame
        The table containing product data.
    orders : pd.DataFrame
        The table containing order data.

    Returns
    -------
    pd.DataFrame

    """
    orders_agg = (
        orders.loc[orders["order_date"].dt.strftime("%Y-%m") == "2020-02"]
        .groupby("product_id", as_index=False)
        .aggregate(unit=pd.NamedAgg("unit", "sum"))
    )
    joined = products.merge(orders_agg, on=["product_id"])
    return joined.loc[joined["unit"] >= 100][["product_name", "unit"]]


def problem_1341(
    movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame
) -> pd.DataFrame:
    """Find the top user by ratings and the highest-rated movie in February 2020.

    Identify the user who has rated the most movies. In case of a tie, return the
    lexicographically smaller user name.

    Identify the movie with the highest average rating in February 2020. In case of a
    tie, return the lexicographically smaller movie name.

    Parameters
    ----------
    movies : pd.DataFrame
        The table containing movie data.
    users : pd.DataFrame
        The table containing user data.
    movie_rating : pd.DataFrame
        The table containing movie rating data.

    Returns
    -------
    pd.DataFrame

    """
    user_most_ratings = (
        (
            movie_rating.merge(users)
            .groupby(["user_id", "name"], as_index=False)
            .aggregate(total_ratings=pd.NamedAgg("movie_id", "count"))
        )
        .sort_values(by=["total_ratings", "name"], ascending=[False, True])[["name"]]
        .head(1)
        .rename(columns={"name": "results"})
    )

    movie_highest_rating = (
        movie_rating.loc[movie_rating["created_at"].dt.strftime("%Y-%m") == "2020-02"]
        .merge(movies)
        .groupby(["movie_id", "title"], as_index=False)
        .aggregate(avg_rating=pd.NamedAgg("rating", "mean"))
        .sort_values(by=["avg_rating", "title"], ascending=[False, True])[["title"]]
        .head(1)
        .rename(columns={"title": "results"})
    )
    return pd.concat([user_most_ratings, movie_highest_rating])


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


def problem_570(employee: pd.DataFrame) -> pd.DataFrame:
    """Find managers with at least five direct reports.

    Return the result table in any order.

    Parameters
    ----------
    employee : pd.DataFrame
        Table lists employee names, departments, and their manager's ID.

    Returns
    -------
    pd.DataFrame

    """
    grouped = employee.groupby("managerId", as_index=False).aggregate(
        reports=pd.NamedAgg("id", "count")
    )
    grouped = grouped.loc[grouped["reports"] >= 5]
    return employee.merge(grouped, left_on="id", right_on="managerId")[["name"]]


def problem_1484(activities: pd.DataFrame) -> pd.DataFrame:
    """Find for each date the number of different products sold and their names.

    The sold products names for each date should be sorted lexicographically.

    Return the result table ordered by sell_date.

    Parameters
    ----------
    activities : pd.DataFrame
        The table containing the sales data.

    Returns
    -------
    pd.DataFrame

    """
    grouped = (
        activities.groupby(["sell_date", "product"]).size().reset_index(name="count")
    )
    return (
        grouped.groupby("sell_date")
        .agg(
            num_sold=("product", "size"),
            products=("product", lambda x: ",".join(sorted(x))),
        )
        .reset_index()
    ).sort_values(by="sell_date")


def problem_1517(users: pd.DataFrame) -> pd.DataFrame:
    """Find the users who have valid emails.

    A valid e-mail has a prefix name and a domain where:

    The prefix name is a string that may contain letters (upper or lower case), digits,
    underscore '_', period '.', and/or dash '-'. The prefix name must start with a
    letter.

    Return the result table in any order.

    Parameters
    ----------
    users : pd.DataFrame
        Table containing user names and emails.

    Returns
    -------
    pd.DataFrame

    """
    return users.loc[
        users["mail"].str.match(r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$")
    ]


def problem_1527(patients: pd.DataFrame) -> pd.DataFrame:
    """Find the patients who have Type I Diabetes.

    Return the patient_id, patient_name, and conditions. Type I Diabetes always starts
    with DIAB1 prefix.

    Return the result table in any order.

    Parameters
    ----------
    patients : pd.DataFrame
        A containing information of the patients in the hospital.

    Returns
    -------
    pd.DataFrame

    """
    return patients.loc[
        patients.conditions.str.split().apply(
            lambda x: any(i.startswith("DIAB1") for i in x)
        )
    ]


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


def problem_1633(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    """Find the percentage of the users registered in each contest.

    Return the result table ordered by percentage in descending order. In case of a
    tie, order it by contest_id in ascending order. The result should be rounded to two
    decimals.

    Parameters
    ----------
    users : pd.DataFrame
        This table contains the name and the id of a user.
    register : pd.DataFrame
        This table contains the id of a user and the contest they registered into.

    Returns
    -------
    pd.DataFrame

    """
    register_agg = register.groupby("contest_id", as_index=False).aggregate(
        user_count=pd.NamedAgg("user_id", "count")
    )
    register_agg["percentage"] = (
        (register_agg["user_count"] / len(users.index)) * 100
    ).apply(
        lambda value: Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    )
    register_agg.drop(columns=["user_count"], inplace=True)
    return register_agg.sort_values(
        ["percentage", "contest_id"], ascending=[False, True]
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


def problem_1667(users: pd.DataFrame) -> pd.DataFrame:
    """Fix the names so that only the first character is uppercase.

    The remaining characters should be lowercase.

    Return the result table ordered by user_id.

    Parameters
    ----------
    users : pd.DataFrame
        This table contains the ID and the name of the user.

    Returns
    -------
    pd.DataFrame

    """
    users["name"] = users.name.str.capitalize()
    return users.sort_values("user_id")


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


def problem_1729(followers: pd.DataFrame) -> pd.DataFrame:
    """Return the number of followers for each user.

    Return the result table ordered by user_id in ascending order.

    Parameters
    ----------
    followers : pd.DataFrame
        Table records user-follower relationships in a social media app.

    Returns
    -------
    pd.DataFrame

    """
    return (
        followers.groupby("user_id", as_index=False)
        .aggregate(followers_count=pd.NamedAgg("follower_id", "count"))
        .sort_values("user_id")
    )


def problem_1731(employees: pd.DataFrame) -> pd.DataFrame:
    """Report manager IDs, names, count of direct reports, and mean age of reports.

    For this problem, we will consider a manager an employee who has at least 1 other
    employee reporting to them.

    Write a solution to report the ids and the names of all managers, the number of
    employees who report directly to them, and the average age of the reports rounded
    to the nearest integer.

    Return the result table ordered by employee_id.

    Parameters
    ----------
    employees : pd.DataFrame
        Table contains information about employees and managers.

    Returns
    -------
    pd.DataFrame

    """
    joined = (
        employees.merge(employees, left_on="employee_id", right_on="reports_to")
        .groupby(["employee_id_x", "name_x"])
        .aggregate({"employee_id_x": "count", "age_y": "mean"})
        .rename(columns={"employee_id_x": "count"})
        .reset_index()
        .rename(
            columns={
                "employee_id_x": "employee_id",
                "name_x": "name",
                "count": "reports_count",
                "age_y": "average_age",
            }
        )
    )
    joined["average_age"] = joined["average_age"].apply(
        lambda x: float(Decimal(x).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    )
    return joined


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


def problem_1789(employee: pd.DataFrame) -> pd.DataFrame:
    """Report all the employees with their primary department.

    Employees can belong to multiple departments. When the employee joins other
    departments, they need to decide which department is their primary department. Note
    that when an employee belongs to only one department, their primary column is 'N'.

    For employees who belong to one department, report their only department.

    Return the result table in any order.

    Parameters
    ----------
    employee : pd.DataFrame
        A table containing employee and department data.

    Returns
    -------
    pd.DataFrame

    """
    counted = employee.groupby("employee_id", as_index=False).aggregate(
        count=pd.NamedAgg("employee_id", "count")
    )
    joined = employee.merge(counted, on="employee_id", how="inner")
    return joined.loc[(joined["primary_flag"] == "Y") | (joined["count"] == 1)][
        ["employee_id", "department_id"]
    ]


def problem_1907(accounts: pd.DataFrame) -> pd.DataFrame:
    """Calculate the number of bank accounts for each salary category.

    The salary categories are:

    - "Low Salary": All the salaries strictly less than $20000.
    - "Average Salary": All the salaries in the inclusive range [$20000, $50000].
    - "High Salary": All the salaries strictly greater than $50000.

    The result table must contain all three categories. If there are no accounts in a category, return 0.

    Return the result table in any order.

    Parameters
    ----------
    accounts : pd.DataFrame
        A table containing the account data.

    Returns
    -------
    pd.DataFrame

    """
    accounts["category"] = accounts["income"].case_when(
        [
            (accounts["income"] < 20_000, "Low Salary"),
            (
                (accounts["income"] >= 20_000) & (accounts["income"] <= 50_000),
                "Average Salary",
            ),
            (accounts["income"] > 50_000, "High Salary"),
        ]
    )
    return (
        pd.DataFrame(
            ["Low Salary", "Average Salary", "High Salary"], columns=["category"]
        )
        .merge(
            accounts.groupby("category", as_index=False).aggregate(
                accounts_count=pd.NamedAgg("account_id", "count")
            ),
            how="left",
        )
        .fillna(0)
    )


def problem_1934(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    """Find the confirmation rate of each user.

    The confirmation rate of a user is the number of 'confirmed' messages divided by
    the total number of requested confirmation messages. The confirmation rate of a
    user that did not request any confirmation messages is 0. Round the confirmation
    rate to two decimal places.

    Return the result table in any order.

    Parameters
    ----------
    signups : pd.DataFrame
        A table containing the user signups.
    confirmations : pd.DataFrame
        A table containing the user confirmation messages.

    Returns
    -------
    pd.DataFrame

    """
    joined = signups.merge(confirmations, on="user_id", how="left")
    joined["is_confirmed"] = joined["action"] == "confirmed"
    grouped = joined.groupby("user_id", as_index=False).aggregate(
        confirmed=pd.NamedAgg("is_confirmed", "sum"),
        total=pd.NamedAgg("is_confirmed", "count"),
    )
    return grouped.assign(
        confirmation_rate=(grouped["confirmed"] / grouped["total"]).round(2)
    )[["user_id", "confirmation_rate"]]


def problem_1978(employees: pd.DataFrame) -> pd.DataFrame:
    """Find employees whose salary is less than $30000 and whose manager left.

    When a manager leaves the company, their information is deleted from the Employees
    table, but the reports still have their manager_id set to the manager that left.

    Return the result table ordered by employee_id.

    Parameters
    ----------
    employees : pd.DataFrame
        The table containing employee data.

    Returns
    -------
    pd.DataFrame

    """
    return employees[
        (employees["salary"] < 30_000)
        & (~employees["manager_id"].isnull())
        & (~employees["manager_id"].isin(employees["employee_id"]))
    ][["employee_id"]].sort_values("employee_id")


def problem_2356(teacher: pd.DataFrame) -> pd.DataFrame:
    """Calculate the number of unique subjects each teacher teaches in the university.

    Return the result table in any order.

    Parameters
    ----------
    teacher : pd.DataFrame
        Table links teachers, subjects, and departments with unique subject-dept pairs.

    Returns
    -------
    pd.DataFrame

    """
    return teacher.groupby("teacher_id", as_index=False).aggregate(
        cnt=pd.NamedAgg("subject_id", "nunique")
    )
