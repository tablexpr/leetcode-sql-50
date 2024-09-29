# %% [markdown]
# https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50
# %%
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
from datetime import timedelta

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
previous_day = pc.add(table["recordDate"], pa.scalar(timedelta(days=-1)))
lag_table = table.set_column(1, "previousDayDate", previous_day)

# TODO: We don't need id in the lag table, we can drop it.

# %%
joined = table.join(
    lag_table,
    keys="recordDate",
    right_keys="previousDayDate",
    join_type="inner",
    right_suffix="lag",
)

# %%
# TODO: Finish this problem.
