"""Functions to load LeetCode problem datasets to pandas DataFrames."""

import pandas as pd


def load_problem_197() -> pd.DataFrame:
    data = [
        [1, "2015-01-01", 10],
        [2, "2015-01-02", 25],
        [3, "2015-01-03", 20],
        [4, "2015-01-04", 30],
    ]
    return pd.DataFrame(data, columns=["id", "recordDate", "temperature"]).astype(
        {"id": "Int64", "recordDate": "datetime64[ns]", "temperature": "Int64"}
    )


def load_problem_577() -> tuple:
    data = [
        [3, "Brad", None, 4000],
        [1, "John", 3, 1000],
        [2, "Dan", 3, 2000],
        [4, "Thomas", 3, 4000],
    ]
    employee = pd.DataFrame(
        data, columns=["empId", "name", "supervisor", "salary"]
    ).astype(
        {"empId": "Int64", "name": "object", "supervisor": "Int64", "salary": "Int64"}
    )
    data = [[2, 500], [4, 2000]]
    bonus = pd.DataFrame(data, columns=["empId", "bonus"]).astype(
        {"empId": "Int64", "bonus": "Int64"}
    )
    return employee, bonus


def load_problem_584() -> pd.DataFrame:
    data = [
        [1, "Will", None],
        [2, "Jane", None],
        [3, "Alex", 2],
        [4, "Bill", None],
        [5, "Zack", 1],
        [6, "Mark", 2],
    ]
    return pd.DataFrame(data, columns=["id", "name", "referee_id"]).astype(
        {"id": "Int64", "name": "object", "referee_id": "Int64"}
    )


def load_problem_595() -> pd.DataFrame:
    data = [
        ["Afghanistan", "Asia", 652230, 25500100, 20343000000],
        ["Albania", "Europe", 28748, 2831741, 12960000000],
        ["Algeria", "Africa", 2381741, 37100000, 188681000000],
        ["Andorra", "Europe", 468, 78115, 3712000000],
        ["Angola", "Africa", 1246700, 20609294, 100990000000],
    ]
    return pd.DataFrame(
        data, columns=["name", "continent", "area", "population", "gdp"]
    ).astype(
        {
            "name": "object",
            "continent": "object",
            "area": "Int64",
            "population": "Int64",
            "gdp": "Int64",
        }
    )


def load_problem_1148() -> pd.DataFrame:
    data = [
        [1, 3, 5, "2019-08-01"],
        [1, 3, 6, "2019-08-02"],
        [2, 7, 7, "2019-08-01"],
        [2, 7, 6, "2019-08-02"],
        [4, 7, 1, "2019-07-22"],
        [3, 4, 4, "2019-07-21"],
        [3, 4, 4, "2019-07-21"],
    ]
    return pd.DataFrame(
        data, columns=["article_id", "author_id", "viewer_id", "view_date"]
    ).astype(
        {
            "article_id": "Int64",
            "author_id": "Int64",
            "viewer_id": "Int64",
            "view_date": "datetime64[ns]",
        }
    )


def load_problem_1378() -> tuple():
    data = [[1, "Alice"], [7, "Bob"], [11, "Meir"], [90, "Winston"], [3, "Jonathan"]]
    employees = pd.DataFrame(data, columns=["id", "name"]).astype(
        {"id": "int64", "name": "object"}
    )
    data = [[3, 1], [11, 2], [90, 3]]
    employee_uni = pd.DataFrame(data, columns=["id", "unique_id"]).astype(
        {"id": "int64", "unique_id": "int64"}
    )
    return employees, employee_uni


def load_problem_1484() -> pd.DataFrame:
    data = [
        ["2020-05-30", "Headphone"],
        ["2020-06-01", "Pencil"],
        ["2020-06-02", "Mask"],
        ["2020-05-30", "Basketball"],
        ["2020-06-01", "Bible"],
        ["2020-06-02", "Mask"],
        ["2020-05-30", "T-Shirt"],
    ]
    return pd.DataFrame(data, columns=["sell_date", "product"]).astype(
        {"sell_date": "datetime64[ns]", "product": "object"}
    )


def load_problem_1517() -> pd.DataFrame:
    data = [
        [1, "Winston", "winston@leetcode.com"],
        [2, "Jonathan", "jonathanisgreat"],
        [3, "Annabelle", "bella-@leetcode.com"],
        [4, "Sally", "sally.come@leetcode.com"],
        [5, "Marwan", "quarz#2020@leetcode.com"],
        [6, "David", "david69@gmail.com"],
        [7, "Shapiro", ".shapo@leetcode.com"],
    ]
    return pd.DataFrame(data, columns=["user_id", "name", "mail"]).astype(
        {"user_id": "int64", "name": "object", "mail": "object"}
    )


def load_problem_1683() -> pd.DataFrame:
    data = [[1, "Let us Code"], [2, "More than fifteen chars are here!"]]
    return pd.DataFrame(data, columns=["tweet_id", "content"]).astype(
        {"tweet_id": "Int64", "content": "object"}
    )


def load_problem_1757() -> pd.DataFrame:
    data = [
        ["0", "Y", "N"],
        ["1", "Y", "Y"],
        ["2", "N", "Y"],
        ["3", "Y", "Y"],
        ["4", "N", "N"],
    ]
    return pd.DataFrame(data, columns=["product_id", "low_fats", "recyclable"]).astype(
        {"product_id": "int64", "low_fats": "category", "recyclable": "category"}
    )
