# %% [markdown]
# https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50
# %%
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc

# %% [markdown]
# Setup the customer pandas DataFrame.

# %%
data = [
    [1, "Will", None],
    [2, "Jane", None],
    [3, "Alex", 2],
    [4, "Bill", None],
    [5, "Zack", 1],
    [6, "Mark", 2],
]
customer = pd.DataFrame(data, columns=["id", "name", "referee_id"]).astype(
    {"id": "Int64", "name": "object", "referee_id": "Int64"}
)

# %%
table = pa.Table.from_pandas(customer)

# %%
table.filter(
    pc.or_kleene(
        pc.is_null(table["referee_id"]), pc.not_equal(table["referee_id"], pa.scalar(2))
    )
).select(["name"])
