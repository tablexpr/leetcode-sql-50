# %% [markdown]
# https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50
# %%
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc

# %% [markdown]
# Setup the views pandas DataFrame.

# %%
data = [
    [1, 3, 5, "2019-08-01"],
    [1, 3, 6, "2019-08-02"],
    [2, 7, 7, "2019-08-01"],
    [2, 7, 6, "2019-08-02"],
    [4, 7, 1, "2019-07-22"],
    [3, 4, 4, "2019-07-21"],
    [3, 4, 4, "2019-07-21"],
]
views = pd.DataFrame(
    data, columns=["article_id", "author_id", "viewer_id", "view_date"]
).astype(
    {
        "article_id": "Int64",
        "author_id": "Int64",
        "viewer_id": "Int64",
        "view_date": "datetime64[ns]",
    }
)

# %%
table = pa.Table.from_pandas(views)

# %%
(
    table.filter(pc.equal(table["author_id"], table["viewer_id"]))
    .select(["author_id"])
    .rename_columns(["id"])
    .group_by("id")
    .aggregate([])
    .sort_by("id")
)
