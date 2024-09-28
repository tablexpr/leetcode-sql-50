# %% [markdown]
# https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50

# %%
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc

# %% [markdown]
# Setup the products pandas DataFrame.

# %%
data = [
    ["0", "Y", "N"],
    ["1", "Y", "Y"],
    ["2", "N", "Y"],
    ["3", "Y", "Y"],
    ["4", "N", "N"],
]
products = pd.DataFrame(data, columns=["product_id", "low_fats", "recyclable"]).astype(
    {"product_id": "int64", "low_fats": "category", "recyclable": "category"}
)

# %%
table = pa.Table.from_pandas(products)

# %%
table.filter(
    pc.and_(
        pc.equal(table["low_fats"], pa.scalar("Y")),
        pc.equal(table["recyclable"], pa.scalar("Y")),
    )
).select(["product_id"])
