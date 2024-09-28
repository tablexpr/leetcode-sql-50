# %% [markdown]
# https://leetcode.com/problems/big-countries/?envType=study-plan-v2&envId=top-sql-50
# %%
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc

# %% [markdown]
# Setup the world pandas DataFrame.

# %%
data = [
    ["Afghanistan", "Asia", 652230, 25500100, 20343000000],
    ["Albania", "Europe", 28748, 2831741, 12960000000],
    ["Algeria", "Africa", 2381741, 37100000, 188681000000],
    ["Andorra", "Europe", 468, 78115, 3712000000],
    ["Angola", "Africa", 1246700, 20609294, 100990000000],
]
world = pd.DataFrame(
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

# %%
table = pa.Table.from_pandas(world)

# %%
table.filter(
    pc.or_(
        pc.greater_equal(table["area"], pa.scalar(3_000_000)),
        pc.greater_equal(table["population"], pa.scalar(25_000_000)),
    )
).select(["name", "population", "area"])
