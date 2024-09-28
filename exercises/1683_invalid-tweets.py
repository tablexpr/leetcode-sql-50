# %% [markdown]
# https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50
# %%
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc

# %% [markdown]
# Setup the tweets pandas DataFrame.

# %%
data = [[1, "Let us Code"], [2, "More than fifteen chars are here!"]]
tweets = pd.DataFrame(data, columns=["tweet_id", "content"]).astype(
    {"tweet_id": "Int64", "content": "object"}
)

# %%
table = pa.Table.from_pandas(tweets)

# %%
table.filter(pc.greater(pc.utf8_length(table["content"]), pa.scalar(15))).select(
    ["tweet_id"]
)
