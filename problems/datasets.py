"""Functions to load LeetCode problem datasets to pandas DataFrames."""

import pandas as pd


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
