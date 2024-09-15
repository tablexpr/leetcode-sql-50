# %% [markdown]
# # Quick analysis on the Diamonds dataset

# %% [markdown]
# Import the necessary libraries.

# %%
import io
import urllib

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.csv as csv

# %% [markdown]
# Download the CSV.

# %%
with urllib.request.urlopen(
    "https://github.com/tidyverse/ggplot2/raw/main/data-raw/diamonds.csv"
) as f:
    data = io.BytesIO(f.read())

# %% [markdown]
# We can use the `read_csv` function to read directly from BytesIO.

# %%
t = csv.read_csv(data)

# %% [markdown]
# Let's see how it looks.

# %%
t

# %% [markdown]
# We can return a list of the columns by using `column_names`.

# %%
t.column_names

# %% [markdown]
# Let's downcast the "price" column in the original dataset. We will want to ensure
# that the values are within the range of an int16. I happen to know in this case, we
# can safely downcast the values, but we will explore a method to determine this
# programatically soon.

# There is also a "safe" argument we can use, which is True by default. This will
# check for overflows or other unsafe conversions.

# %%
t = t.set_column(
    t.schema.get_field_index("price"),
    "price",
    pc.cast(t["price"], pa.int16()),
)

t

# %% [markdown]
# With `select`, we can return a Table with the specified columns.
#
# Here, we're just returning the first four columns as well as the price column.

# %%
t.select(["carat", "cut", "color", "clarity", "price"])

# %% [markdown]
# How about filtering?
#
# Let's look at cases where the carat is greater than or equal to 1.

# %%
t.filter(pc.greater_equal(t["carat"], pa.scalar(1)))

# %% [markdown]
# What about applying multiple filters?
#
# We'll extend the previous condition to also include "Ideal" cuts.

# %%
t.filter(
    pc.and_(
        pc.greater_equal(t["carat"], pa.scalar(1)),
        pc.equal(t["cut"], pa.scalar("Ideal")),
    )
)

# %% [markdown]
# Let's sort the table by price, descending.

# %%
t.sort_by([("price", "descending")])

# %% [markdown]
# Let's put all of that together now.

# %%
t.select(["carat", "cut", "color", "clarity", "price"]).filter(
    pc.and_(
        pc.greater_equal(t["carat"], pa.scalar(1)),
        pc.equal(t["cut"], pa.scalar("Ideal")),
    )
).sort_by([("price", "descending")])

# %% [markdown]
# If you're familiar with SQL, what we've done so far might look something
# like this:
# ```sql
# SELECT carat,
#        cut,
#        color,
#        clarity,
#        price
# FROM diamonds
# WHERE carat >= 1
#     AND cut = 'Ideal'
# ORDER BY price DESC;
# ```

# %% [markdown]
# Let's mix things up a bit now and start back over to determine the average
# price per cut.

# %%
t_agg = t.group_by("cut").aggregate([("price", "mean")])

t_agg

# %% [markdown]
# We can include a count as well.

# %%
t_agg = t.group_by("cut").aggregate([("price", "mean"), ("cut", "count")])

t_agg

# %% [markdown]
# Now let's take the previous result and round the
# price_mean value to two decimal places.

# %%
t_agg = t_agg.set_column(
    t_agg.schema.get_field_index("price_mean"),
    "price_mean",
    pc.round(t_agg["price_mean"], 2),
)

t_agg

# %% [markdown]
# Back to the SQL comparison, what we just wrote would look like this:
# ```sql
# SELECT cut,
#        ROUND(AVG(price), 2) AS price_mean,
#        COUNT(cut) AS cut_count
# FROM diamonds
# GROUP BY cut;
# ```
