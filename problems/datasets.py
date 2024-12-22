"""Functions to load LeetCode problem datasets to pandas DataFrames."""

from typing import Tuple

import pandas as pd


def load_problem_176() -> pd.DataFrame:
    data = [[1, 100], [2, 200], [3, 300]]
    return pd.DataFrame(data, columns=["id", "salary"]).astype(
        {"id": "int64", "salary": "int64"}
    )


def load_problem_180() -> pd.DataFrame:
    data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
    return pd.DataFrame(data, columns=["id", "num"]).astype(
        {"id": "Int64", "num": "Int64"}
    )


def load_problem_185() -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = [
        [1, "Joe", 85000, 1],
        [2, "Henry", 80000, 2],
        [3, "Sam", 60000, 2],
        [4, "Max", 90000, 1],
        [5, "Janet", 69000, 1],
        [6, "Randy", 85000, 1],
        [7, "Will", 70000, 1],
    ]
    employee = pd.DataFrame(
        data, columns=["id", "name", "salary", "departmentId"]
    ).astype(
        {"id": "Int64", "name": "object", "salary": "Int64", "departmentId": "Int64"}
    )
    data = [[1, "IT"], [2, "Sales"]]
    department = pd.DataFrame(data, columns=["id", "name"]).astype(
        {"id": "Int64", "name": "object"}
    )
    return employee, department


def load_problem_196() -> pd.DataFrame:
    data = [[1, "john@example.com"], [2, "bob@example.com"], [3, "john@example.com"]]
    return pd.DataFrame(data, columns=["id", "email"]).astype(
        {"id": "int64", "email": "object"}
    )


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


def load_problem_550() -> pd.DataFrame:
    data = [
        [1, 2, "2016-03-01", 5],
        [1, 2, "2016-03-02", 6],
        [2, 3, "2017-06-25", 1],
        [3, 1, "2016-03-02", 0],
        [3, 4, "2018-07-03", 5],
    ]
    return pd.DataFrame(
        data, columns=["player_id", "device_id", "event_date", "games_played"]
    ).astype(
        {
            "player_id": "Int64",
            "device_id": "Int64",
            "event_date": "datetime64[ns]",
            "games_played": "Int64",
        }
    )


def load_problem_570() -> pd.DataFrame:
    data = [
        [101, "John", "A", None],
        [102, "Dan", "A", 101],
        [103, "James", "A", 101],
        [104, "Amy", "A", 101],
        [105, "Anne", "A", 101],
        [106, "Ron", "B", 101],
    ]
    return pd.DataFrame(data, columns=["id", "name", "department", "managerId"]).astype(
        {"id": "Int64", "name": "object", "department": "object", "managerId": "Int64"}
    )


def load_problem_577() -> Tuple[pd.DataFrame, pd.DataFrame]:
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


def load_problem_585() -> pd.DataFrame:
    data = [
        [1, 10, 5, 10, 10],
        [2, 20, 20, 20, 20],
        [3, 10, 30, 20, 20],
        [4, 10, 40, 40, 40],
    ]
    return pd.DataFrame(
        data, columns=["pid", "tiv_2015", "tiv_2016", "lat", "lon"]
    ).astype(
        {
            "pid": "Int64",
            "tiv_2015": "Float64",
            "tiv_2016": "Float64",
            "lat": "Float64",
            "lon": "Float64",
        }
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


def load_problem_596() -> pd.DataFrame:
    data = [
        ["A", "Math"],
        ["B", "English"],
        ["C", "Math"],
        ["D", "Biology"],
        ["E", "Math"],
        ["F", "Computer"],
        ["G", "Math"],
        ["H", "Math"],
        ["I", "Math"],
    ]
    return pd.DataFrame(data, columns=["student", "class"]).astype(
        {"student": "object", "class": "object"}
    )


def load_problem_602() -> pd.DataFrame:
    data = [
        [1, 2, "2016/06/03"],
        [1, 3, "2016/06/08"],
        [2, 3, "2016/06/08"],
        [3, 4, "2016/06/09"],
    ]
    return pd.DataFrame(
        data, columns=["requester_id", "accepter_id", "accept_date"]
    ).astype(
        {
            "requester_id": "Int64",
            "accepter_id": "Int64",
            "accept_date": "datetime64[ns]",
        }
    )


def load_problem_610() -> pd.DataFrame:
    data = [[13, 15, 30], [10, 20, 15]]
    return pd.DataFrame(data, columns=["x", "y", "z"]).astype(
        {"x": "Int64", "y": "Int64", "z": "Int64"}
    )


def load_problem_619() -> pd.DataFrame:
    data = [[8], [8], [3], [3], [1], [4], [5], [6]]
    return pd.DataFrame(data, columns=["num"]).astype({"num": "Int64"})


def load_problem_620() -> pd.DataFrame:
    data = [
        [1, "War", "great 3D", 8.9],
        [2, "Science", "fiction", 8.5],
        [3, "irish", "boring", 6.2],
        [4, "Ice song", "Fantacy", 8.6],
        [5, "House card", "Interesting", 9.1],
    ]
    return pd.DataFrame(data, columns=["id", "movie", "description", "rating"]).astype(
        {"id": "Int64", "movie": "object", "description": "object", "rating": "Float64"}
    )


def load_problem_626() -> pd.DataFrame:
    data = [[1, "Abbot"], [2, "Doris"], [3, "Emerson"], [4, "Green"], [5, "Jeames"]]
    return pd.DataFrame(data, columns=["id", "student"]).astype(
        {"id": "Int64", "student": "object"}
    )


def load_problem_1045() -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
    customer = pd.DataFrame(data, columns=["customer_id", "product_key"]).astype(
        {"customer_id": "Int64", "product_key": "Int64"}
    )
    data = [[5], [6]]
    product = pd.DataFrame(data, columns=["product_key"]).astype(
        {"product_key": "Int64"}
    )
    return customer, product


def load_problem_1068() -> pd.DataFrame:
    data = [
        [1, 100, 2008, 10, 5000],
        [2, 100, 2009, 12, 5000],
        [7, 200, 2011, 15, 9000],
    ]
    sales = pd.DataFrame(
        data, columns=["sale_id", "product_id", "year", "quantity", "price"]
    ).astype(
        {
            "sale_id": "Int64",
            "product_id": "Int64",
            "year": "Int64",
            "quantity": "Int64",
            "price": "Int64",
        }
    )
    data = [[100, "Nokia"], [200, "Apple"], [300, "Samsung"]]
    product = pd.DataFrame(data, columns=["product_id", "product_name"]).astype(
        {"product_id": "Int64", "product_name": "object"}
    )
    return sales, product


def load_problem_1070() -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = [
        [1, 100, 2008, 10, 5000],
        [2, 100, 2009, 12, 5000],
        [7, 200, 2011, 15, 9000],
    ]
    sales = pd.DataFrame(
        data, columns=["sale_id", "product_id", "year", "quantity", "price"]
    ).astype(
        {
            "sale_id": "Int64",
            "product_id": "Int64",
            "year": "Int64",
            "quantity": "Int64",
            "price": "Int64",
        }
    )
    data = [[100, "Nokia"], [200, "Apple"], [300, "Samsung"]]
    product = pd.DataFrame(data, columns=["product_id", "product_name"]).astype(
        {"product_id": "Int64", "product_name": "object"}
    )
    return sales, product


def load_problem_1075() -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
    project = pd.DataFrame(data, columns=["project_id", "employee_id"]).astype(
        {"project_id": "Int64", "employee_id": "Int64"}
    )
    data = [[1, "Khaled", 3], [2, "Ali", 2], [3, "John", 1], [4, "Doe", 2]]
    employee = pd.DataFrame(
        data, columns=["employee_id", "name", "experience_years"]
    ).astype({"employee_id": "Int64", "name": "object", "experience_years": "Int64"})
    return project, employee


def load_problem_1141() -> pd.DataFrame:
    data = [
        [1, 1, "2019-07-20", "open_session"],
        [1, 1, "2019-07-20", "scroll_down"],
        [1, 1, "2019-07-20", "end_session"],
        [2, 4, "2019-07-20", "open_session"],
        [2, 4, "2019-07-21", "send_message"],
        [2, 4, "2019-07-21", "end_session"],
        [3, 2, "2019-07-21", "open_session"],
        [3, 2, "2019-07-21", "send_message"],
        [3, 2, "2019-07-21", "end_session"],
        [4, 3, "2019-06-25", "open_session"],
        [4, 3, "2019-06-25", "end_session"],
    ]
    return pd.DataFrame(
        data, columns=["user_id", "session_id", "activity_date", "activity_type"]
    ).astype(
        {
            "user_id": "Int64",
            "session_id": "Int64",
            "activity_date": "datetime64[ns]",
            "activity_type": "object",
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


def load_problem_1164() -> pd.DataFrame:
    data = [
        [1, 20, "2019-08-14"],
        [2, 50, "2019-08-14"],
        [1, 30, "2019-08-15"],
        [1, 35, "2019-08-16"],
        [2, 65, "2019-08-17"],
        [3, 20, "2019-08-18"],
    ]
    return pd.DataFrame(
        data, columns=["product_id", "new_price", "change_date"]
    ).astype(
        {"product_id": "Int64", "new_price": "Int64", "change_date": "datetime64[ns]"}
    )


def load_problem_1174() -> pd.DataFrame:
    data = [
        [1, 1, "2019-08-01", "2019-08-02"],
        [2, 2, "2019-08-02", "2019-08-02"],
        [3, 1, "2019-08-11", "2019-08-12"],
        [4, 3, "2019-08-24", "2019-08-24"],
        [5, 3, "2019-08-21", "2019-08-22"],
        [6, 2, "2019-08-11", "2019-08-13"],
        [7, 4, "2019-08-09", "2019-08-09"],
    ]
    return pd.DataFrame(
        data,
        columns=[
            "delivery_id",
            "customer_id",
            "order_date",
            "customer_pref_delivery_date",
        ],
    ).astype(
        {
            "delivery_id": "Int64",
            "customer_id": "Int64",
            "order_date": "datetime64[ns]",
            "customer_pref_delivery_date": "datetime64[ns]",
        }
    )


def load_problem_1193() -> pd.DataFrame:
    data = [
        [121, "US", "approved", 1000, "2018-12-18"],
        [122, "US", "declined", 2000, "2018-12-19"],
        [123, "US", "approved", 2000, "2019-01-01"],
        [124, "DE", "approved", 2000, "2019-01-07"],
    ]
    return pd.DataFrame(
        data, columns=["id", "country", "state", "amount", "trans_date"]
    ).astype(
        {
            "id": "Int64",
            "country": "object",
            "state": "object",
            "amount": "Int64",
            "trans_date": "datetime64[ns]",
        }
    )


def load_problem_1204() -> pd.DataFrame:
    data = [
        [5, "Alice", 250, 1],
        [4, "Bob", 175, 5],
        [3, "Alex", 350, 2],
        [6, "John Cena", 400, 3],
        [1, "Winston", 500, 6],
        [2, "Marie", 200, 4],
    ]
    return pd.DataFrame(
        data, columns=["person_id", "person_name", "weight", "turn"]
    ).astype(
        {
            "person_id": "Int64",
            "person_name": "object",
            "weight": "Int64",
            "turn": "Int64",
        }
    )


def load_problem_1211() -> pd.DataFrame:
    data = [
        ["Dog", "Golden Retriever", 1, 5],
        ["Dog", "German Shepherd", 2, 5],
        ["Dog", "Mule", 200, 1],
        ["Cat", "Shirazi", 5, 2],
        ["Cat", "Siamese", 3, 3],
        ["Cat", "Sphynx", 7, 4],
    ]
    return pd.DataFrame(
        data, columns=["query_name", "result", "position", "rating"]
    ).astype(
        {
            "query_name": "object",
            "result": "object",
            "position": "Int64",
            "rating": "Int64",
        }
    )


def load_problem_1251() -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = [
        [1, "2019-02-17", "2019-02-28", 5],
        [1, "2019-03-01", "2019-03-22", 20],
        [2, "2019-02-01", "2019-02-20", 15],
        [2, "2019-02-21", "2019-03-31", 30],
    ]
    prices = pd.DataFrame(
        data, columns=["product_id", "start_date", "end_date", "price"]
    ).astype(
        {
            "product_id": "Int64",
            "start_date": "datetime64[ns]",
            "end_date": "datetime64[ns]",
            "price": "Int64",
        }
    )
    data = [
        [1, "2019-02-25", 100],
        [1, "2019-03-01", 15],
        [2, "2019-02-10", 200],
        [2, "2019-03-22", 30],
    ]
    units_sold = pd.DataFrame(
        data, columns=["product_id", "purchase_date", "units"]
    ).astype(
        {"product_id": "Int64", "purchase_date": "datetime64[ns]", "units": "Int64"}
    )
    return prices, units_sold


def load_problem_1280() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    data = [[1, "Alice"], [2, "Bob"], [13, "John"], [6, "Alex"]]
    students = pd.DataFrame(data, columns=["student_id", "student_name"]).astype(
        {"student_id": "Int64", "student_name": "object"}
    )
    data = [["Math"], ["Physics"], ["Programming"]]
    subjects = pd.DataFrame(data, columns=["subject_name"]).astype(
        {"subject_name": "object"}
    )
    data = [
        [1, "Math"],
        [1, "Physics"],
        [1, "Programming"],
        [2, "Programming"],
        [1, "Physics"],
        [1, "Math"],
        [13, "Math"],
        [13, "Programming"],
        [13, "Physics"],
        [2, "Math"],
        [1, "Math"],
    ]
    examinations = pd.DataFrame(data, columns=["student_id", "subject_name"]).astype(
        {"student_id": "Int64", "subject_name": "object"}
    )
    return students, subjects, examinations


def load_problem_1321() -> pd.DataFrame:
    data = [
        [1, "Jhon", "2019-01-01", 100],
        [2, "Daniel", "2019-01-02", 110],
        [3, "Jade", "2019-01-03", 120],
        [4, "Khaled", "2019-01-04", 130],
        [5, "Winston", "2019-01-05", 110],
        [6, "Elvis", "2019-01-06", 140],
        [7, "Anna", "2019-01-07", 150],
        [8, "Maria", "2019-01-08", 80],
        [9, "Jaze", "2019-01-09", 110],
        [1, "Jhon", "2019-01-10", 130],
        [3, "Jade", "2019-01-10", 150],
    ]
    return pd.DataFrame(
        data, columns=["customer_id", "name", "visited_on", "amount"]
    ).astype(
        {
            "customer_id": "Int64",
            "name": "object",
            "visited_on": "datetime64[ns]",
            "amount": "Int64",
        }
    )


def load_problem_1327() -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = [
        [1, "Leetcode Solutions", "Book"],
        [2, "Jewels of Stringology", "Book"],
        [3, "HP", "Laptop"],
        [4, "Lenovo", "Laptop"],
        [5, "Leetcode Kit", "T-shirt"],
    ]
    products = pd.DataFrame(
        data, columns=["product_id", "product_name", "product_category"]
    ).astype(
        {"product_id": "Int64", "product_name": "object", "product_category": "object"}
    )
    data = [
        [1, "2020-02-05", 60],
        [1, "2020-02-10", 70],
        [2, "2020-01-18", 30],
        [2, "2020-02-11", 80],
        [3, "2020-02-17", 2],
        [3, "2020-02-24", 3],
        [4, "2020-03-01", 20],
        [4, "2020-03-04", 30],
        [4, "2020-03-04", 60],
        [5, "2020-02-25", 50],
        [5, "2020-02-27", 50],
        [5, "2020-03-01", 50],
    ]
    orders = pd.DataFrame(data, columns=["product_id", "order_date", "unit"]).astype(
        {"product_id": "Int64", "order_date": "datetime64[ns]", "unit": "Int64"}
    )
    return products, orders


def load_problem_1341() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    data = [[1, "Avengers"], [2, "Frozen 2"], [3, "Joker"]]
    movies = pd.DataFrame(data, columns=["movie_id", "title"]).astype(
        {"movie_id": "Int64", "title": "object"}
    )
    data = [[1, "Daniel"], [2, "Monica"], [3, "Maria"], [4, "James"]]
    users = pd.DataFrame(data, columns=["user_id", "name"]).astype(
        {"user_id": "Int64", "name": "object"}
    )
    data = [
        [1, 1, 3, "2020-01-12"],
        [1, 2, 4, "2020-02-11"],
        [1, 3, 2, "2020-02-12"],
        [1, 4, 1, "2020-01-01"],
        [2, 1, 5, "2020-02-17"],
        [2, 2, 2, "2020-02-01"],
        [2, 3, 2, "2020-03-01"],
        [3, 1, 3, "2020-02-22"],
        [3, 2, 4, "2020-02-25"],
    ]
    movie_rating = pd.DataFrame(
        data, columns=["movie_id", "user_id", "rating", "created_at"]
    ).astype(
        {
            "movie_id": "Int64",
            "user_id": "Int64",
            "rating": "Int64",
            "created_at": "datetime64[ns]",
        }
    )
    return movies, users, movie_rating


def load_problem_1378() -> Tuple[pd.DataFrame, pd.DataFrame]:
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


def load_problem_1527() -> pd.DataFrame:
    data = [
        [1, "Daniel", "YFEV COUGH"],
        [2, "Alice", ""],
        [3, "Bob", "DIAB100 MYOP"],
        [4, "George", "ACNE DIAB100"],
        [5, "Alain", "DIAB201"],
    ]
    return pd.DataFrame(
        data, columns=["patient_id", "patient_name", "conditions"]
    ).astype({"patient_id": "int64", "patient_name": "object", "conditions": "object"})


def load_problem_1581() -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]]
    visits = pd.DataFrame(data, columns=["visit_id", "customer_id"]).astype(
        {"visit_id": "Int64", "customer_id": "Int64"}
    )
    data = [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]
    transactions = pd.DataFrame(
        data, columns=["transaction_id", "visit_id", "amount"]
    ).astype({"transaction_id": "Int64", "visit_id": "Int64", "amount": "Int64"})
    return visits, transactions


def load_problem_1633() -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = [[6, "Alice"], [2, "Bob"], [7, "Alex"]]
    users = pd.DataFrame(data, columns=["user_id", "user_name"]).astype(
        {"user_id": "Int64", "user_name": "object"}
    )
    data = [
        [215, 6],
        [209, 2],
        [208, 2],
        [210, 6],
        [208, 6],
        [209, 7],
        [209, 6],
        [215, 7],
        [208, 7],
        [210, 2],
        [207, 2],
        [210, 7],
    ]
    register = pd.DataFrame(data, columns=["contest_id", "user_id"]).astype(
        {"contest_id": "Int64", "user_id": "Int64"}
    )
    return users, register


def load_problem_1661() -> pd.DataFrame:
    data = [
        [0, 0, "start", 0.712],
        [0, 0, "end", 1.52],
        [0, 1, "start", 3.14],
        [0, 1, "end", 4.12],
        [1, 0, "start", 0.55],
        [1, 0, "end", 1.55],
        [1, 1, "start", 0.43],
        [1, 1, "end", 1.42],
        [2, 0, "start", 4.1],
        [2, 0, "end", 4.512],
        [2, 1, "start", 2.5],
        [2, 1, "end", 5],
    ]
    return pd.DataFrame(
        data, columns=["machine_id", "process_id", "activity_type", "timestamp"]
    ).astype(
        {
            "machine_id": "Int64",
            "process_id": "Int64",
            "activity_type": "object",
            "timestamp": "Float64",
        }
    )


def load_problem_1667() -> pd.DataFrame:
    data = [[1, "aLice"], [2, "bOB"]]
    return pd.DataFrame(data, columns=["user_id", "name"]).astype(
        {"user_id": "Int64", "name": "object"}
    )


def load_problem_1683() -> pd.DataFrame:
    data = [[1, "Let us Code"], [2, "More than fifteen chars are here!"]]
    return pd.DataFrame(data, columns=["tweet_id", "content"]).astype(
        {"tweet_id": "Int64", "content": "object"}
    )


def load_problem_1729() -> pd.DataFrame:
    data = [["0", "1"], ["1", "0"], ["2", "0"], ["2", "1"]]
    return pd.DataFrame(data, columns=["user_id", "follower_id"]).astype(
        {"user_id": "Int64", "follower_id": "Int64"}
    )


def load_problem_1731() -> pd.DataFrame:
    data = [
        [9, "Hercy", None, 43],
        [6, "Alice", 9, 41],
        [4, "Bob", 9, 36],
        [2, "Winston", None, 37],
    ]
    return pd.DataFrame(
        data, columns=["employee_id", "name", "reports_to", "age"]
    ).astype(
        {
            "employee_id": "Int64",
            "name": "object",
            "reports_to": "Int64",
            "age": "Int64",
        }
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


def load_problem_1789() -> pd.DataFrame:
    data = [
        ["1", "1", "N"],
        ["2", "1", "Y"],
        ["2", "2", "N"],
        ["3", "3", "N"],
        ["4", "2", "N"],
        ["4", "3", "Y"],
        ["4", "4", "N"],
    ]
    return pd.DataFrame(
        data, columns=["employee_id", "department_id", "primary_flag"]
    ).astype(
        {"employee_id": "Int64", "department_id": "Int64", "primary_flag": "object"}
    )


def load_problem_1907() -> pd.DataFrame:
    data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
    return pd.DataFrame(data, columns=["account_id", "income"]).astype(
        {"account_id": "Int64", "income": "Int64"}
    )


def load_problem_1934() -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = [
        [3, "2020-03-21 10:16:13"],
        [7, "2020-01-04 13:57:59"],
        [2, "2020-07-29 23:09:44"],
        [6, "2020-12-09 10:39:37"],
    ]
    signups = pd.DataFrame(data, columns=["user_id", "time_stamp"]).astype(
        {"user_id": "Int64", "time_stamp": "datetime64[ns]"}
    )
    data = [
        [3, "2021-01-06 03:30:46", "timeout"],
        [3, "2021-07-14 14:00:00", "timeout"],
        [7, "2021-06-12 11:57:29", "confirmed"],
        [7, "2021-06-13 12:58:28", "confirmed"],
        [7, "2021-06-14 13:59:27", "confirmed"],
        [2, "2021-01-22 00:00:00", "confirmed"],
        [2, "2021-02-28 23:59:59", "timeout"],
    ]
    confirmations = pd.DataFrame(
        data, columns=["user_id", "time_stamp", "action"]
    ).astype({"user_id": "Int64", "time_stamp": "datetime64[ns]", "action": "object"})
    return signups, confirmations


def load_problem_1978() -> pd.DataFrame:
    data = [
        [3, "Mila", 9, 60301],
        [12, "Antonella", None, 31000],
        [13, "Emery", None, 67084],
        [1, "Kalel", 11, 21241],
        [9, "Mikaela", None, 50937],
        [11, "Joziah", 6, 28485],
    ]
    return pd.DataFrame(
        data, columns=["employee_id", "name", "manager_id", "salary"]
    ).astype(
        {
            "employee_id": "Int64",
            "name": "object",
            "manager_id": "Int64",
            "salary": "Int64",
        }
    )


def load_problem_2356() -> pd.DataFrame:
    data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
    return pd.DataFrame(data, columns=["teacher_id", "subject_id", "dept_id"]).astype(
        {"teacher_id": "Int64", "subject_id": "Int64", "dept_id": "Int64"}
    )
