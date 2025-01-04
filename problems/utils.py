import inspect
import io
from textwrap import dedent

import pandas as pd

import problems.datafusion
import problems.pandas
import problems.polars
import problems.pyarrow


def gen_readme() -> str:
    data = """problem_id,title,difficulty,group
    1757,[Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products),Easy,Select
    584,[Find Customer Referee](https://leetcode.com/problems/find-customer-referee),Easy,Select
    595,[Big Countries](https://leetcode.com/problems/big-countries),Easy,Select
    1148,[Article Views I](https://leetcode.com/problems/article-views-i),Easy,Select
    1683,[Invalid Tweets](https://leetcode.com/problems/invalid-tweets),Easy,Select
    1378,[Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier),Easy,Basic Joins
    1068,[Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i),Easy,Basic Joins
    1581,[Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions),Easy,Basic Joins
    197,[Rising Temperature](https://leetcode.com/problems/rising-temperature),Easy,Basic Joins
    1661,[Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine),Easy,Basic Joins
    577,[Employee Bonus](https://leetcode.com/problems/employee-bonus),Easy,Basic Joins
    1280,[Students and Examinations](https://leetcode.com/problems/students-and-examinations),Easy,Basic Joins
    570,[Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports),Medium,Basic Joins
    1934,[Confirmation Rate](https://leetcode.com/problems/confirmation-rate),Medium,Basic Joins
    620,[Not Boring Movies](https://leetcode.com/problems/not-boring-movies),Easy,Basic Aggregate Functions
    1251,[Average Selling Price](https://leetcode.com/problems/average-selling-price),Easy,Basic Aggregate Functions
    1075,[Project Employees I](https://leetcode.com/problems/project-employees-i),Easy,Basic Aggregate Functions
    1633,[Percentage of Users Attended a Contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest),Easy,Basic Aggregate Functions
    1211,[Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage),Easy,Basic Aggregate Functions
    1193,[Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i),Medium,Basic Aggregate Functions
    1174,[Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii),Medium,Basic Aggregate Functions
    550,[Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv),Medium,Basic Aggregate Functions
    2356,[Number of Unique Subjects Taught by Each Teacher](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher),Easy,Sorting and Grouping
    1141,[User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i),Easy,Sorting and Grouping
    1070,[Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii),Medium,Sorting and Grouping
    596,[Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students),Easy,Sorting and Grouping
    1729,[Find Followers Count](https://leetcode.com/problems/find-followers-count),Easy,Sorting and Grouping
    619,[Biggest Single Number](https://leetcode.com/problems/biggest-single-number),Easy,Sorting and Grouping
    1045,[Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products),Medium,Sorting and Grouping
    1731,[The Number of Employees Which Report to Each Employee](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee),Easy,Advanced Select and Joins
    1789,[Primary Department for Each Employee](https://leetcode.com/problems/primary-department-for-each-employee),Easy,Advanced Select and Joins
    610,[Triangle Judgement](https://leetcode.com/problems/triangle-judgement),Easy,Advanced Select and Joins
    180,[Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers),Medium,Advanced Select and Joins
    1164,[Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date),Medium,Advanced Select and Joins
    1204,[Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus),Medium,Advanced Select and Joins
    1907,[Count Salary Categories](https://leetcode.com/problems/count-salary-categories),Medium,Advanced Select and Joins
    1978,[Employees Whose Manager Left the Company](https://leetcode.com/problems/employees-whose-manager-left-the-company),Easy,Subqueries
    626,[Exchange Seats](https://leetcode.com/problems/exchange-seats),Medium,Subqueries
    1341,[Movie Rating](https://leetcode.com/problems/movie-rating),Medium,Subqueries
    1321,[Restaurant Growth](https://leetcode.com/problems/restaurant-growth),Medium,Subqueries
    602,[Friend Requests II: Who Has the Most Friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends),Medium,Subqueries
    585,[Investments in 2016](https://leetcode.com/problems/investments-in-2016),Medium,Subqueries
    185,[Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries),Hard,Subqueries
    1667,[Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table),Easy,Advanced String Functions / Regex / Clause
    1527,[Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition),Easy,Advanced String Functions / Regex / Clause
    196,[Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails),Easy,Advanced String Functions / Regex / Clause
    176,[Second Highest Salary](https://leetcode.com/problems/second-highest-salary),Medium,Advanced String Functions / Regex / Clause
    1484,[Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date),Easy,Advanced String Functions / Regex / Clause
    1327,[List the Products Ordered in a Period](https://leetcode.com/problems/list-the-products-ordered-in-a-period),Easy,Advanced String Functions / Regex / Clause
    1517,[Find Users With Valid E-Mails](https://leetcode.com/problems/find-users-with-valid-e-mails),Easy,Advanced String Functions / Regex / Clause
    """
    df = pd.read_csv(io.StringIO(data))
    df["DataFusion"] = (
        df["problem_id"]
        .astype(str)
        .isin(
            [
                func[0].split("_")[-1]
                for func in inspect.getmembers(problems.datafusion, inspect.isfunction)
                if func[0].startswith("problem")
            ]
        )
    )
    df["pandas"] = (
        df["problem_id"]
        .astype(str)
        .isin(
            [
                func[0].split("_")[-1]
                for func in inspect.getmembers(problems.pandas, inspect.isfunction)
                if func[0].startswith("problem")
            ]
        )
    )
    df["Polars"] = (
        df["problem_id"]
        .astype(str)
        .isin(
            [
                func[0].split("_")[-1]
                for func in inspect.getmembers(problems.polars, inspect.isfunction)
                if func[0].startswith("problem")
            ]
        )
    )
    df["PyArrow"] = (
        df["problem_id"]
        .astype(str)
        .isin(
            [
                func[0].split("_")[-1]
                for func in inspect.getmembers(problems.pyarrow, inspect.isfunction)
                if func[0].startswith("problem")
            ]
        )
    )

    mapping = {True: "✅", False: "❌"}
    df[["DataFusion", "pandas", "Polars", "PyArrow"]] = df[
        ["DataFusion", "pandas", "Polars", "PyArrow"]
    ].map(mapping.get)

    s = io.BytesIO()
    s.write(
        dedent("""\
        # LeetCode SQL 50

        Fiddling around with [DataFusion](https://github.com/apache/datafusion), [pandas](https://github.com/pandas-dev/pandas), [Polars](https://github.com/pola-rs/polars), and [PyArrow](https://github.com/apache/arrow).

        """).encode()
    )

    for section in [
        "Select",
        "Basic Joins",
        "Basic Aggregate Functions",
        "Sorting and Grouping",
        "Advanced Select and Joins",
        "Subqueries",
        "Advanced String Functions / Regex / Clause",
    ]:
        s.write(f"## {section}\n".encode())
        s.write(
            df[df["group"] == section]
            .drop(columns=["group"])
            .to_markdown(index=False)
            .encode()
        )
        s.write("\n".encode())
    return s.getvalue()
