# %% [markdown]
# https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50
# %%
from datetime import timedelta

import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc

# %% [markdown]
# Setup the weather pandas DataFrame.

# %%
data = [
    [1, "2015-01-01", 10],
    [2, "2015-01-02", 25],
    [3, "2015-01-03", 20],
    [4, "2015-01-04", 30],
]
weather = pd.DataFrame(data, columns=["id", "recordDate", "temperature"]).astype(
    {"id": "Int64", "recordDate": "datetime64[ns]", "temperature": "Int64"}
)

# %%
table = pa.Table.from_pandas(weather)

# %%
lag_table = pa.table(
    {
        "recordDate": pc.add(table["recordDate"], pa.scalar(timedelta(days=1))),
        "temperature": table["temperature"],
    }
)

# %%
joined = table.join(
    lag_table,
    keys="recordDate",
    join_type="inner",
    right_suffix="Lag",
)

# %%
joined.filter(pc.greater(joined["temperature"], joined["temperatureLag"])).select(
    ["id"]
)
