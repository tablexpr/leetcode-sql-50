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
import pyarrow.parquet as pq

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
# How about the schema of the table?

# %%
t.schema

# %% [markdown]
# Let's downcast the "price" column in the original dataset. We will want to ensure
# that the values are within the range of an int16. I happen to know in this case, we
# can safely downcast the values, but we will explore a method to determine this
# programmatically soon.

# There is also a "safe" argument we can use, which is True by default. This will
# check for overflows or other unsafe conversions.

# We will capture the size of the original table (in KB) before we downcast the column
# so that we can compare the sizes afterward.

# %%

original_size = t.get_total_buffer_size() >> 10

t = t.set_column(
    t.schema.get_field_index("price"),
    "price",
    pc.cast(t["price"], pa.int16()),
)

t

# %% [markdown]
# If we know the schema ahead of time, we can specify the column types.
# This disables type inference on the defined columns.
# Since we have already consumed the BytesIO object, we will need to seek back to the
# beginning to reset the pointer.

# %%
data.seek(0)
t = csv.read_csv(
    data, convert_options=csv.ConvertOptions(column_types={"price": pa.int16()})
)

# %% [markdown]
# If we inspect the schema this time, we'll see that the "price" column is now an
# int16.

# %%
t.schema

# %% [markdown]
# I mentioned earlier that we could programmatically determine if we can downcast
# the values in the "price" column. We can use the `compute` module to do this.

# %%
pc.min_max(t["price"])

# %% [markdown]
# We also have quite a few columns that are of type float64 (double). We can downcast
# these to float32 (float). We could use the same method as before, but let's explore
# another way to do this.

# %%
schema = pa.schema(
    [
        pa.field("carat", pa.float32()),
        pa.field("cut", pa.string()),
        pa.field("color", pa.string()),
        pa.field("clarity", pa.string()),
        pa.field("depth", pa.float32()),
        pa.field("table", pa.float32()),
        pa.field("price", pa.int16()),
        pa.field("x", pa.float32()),
        pa.field("y", pa.float32()),
        pa.field("z", pa.float32()),
    ]
)

t = t.cast(schema)

# %% [markdown]
# Now we can can compare the sizes of the original table and the new table.

# %%
new_size = t.get_total_buffer_size() >> 10

original_size, new_size

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

# %% [markdown]
# Let's close out by writing the initial dataset to a Parquet buffer to demonstrate how
# easy it is to write and read Parquet files.

# %%
parquet_data = io.BytesIO()
pq.write_table(t, parquet_data)

# %% [markdown]
# When working with Parquet files, we have the luxury to only read specific columns.
# Before, we needed to read all of the columns from the CSV, but now we can read only
# the columns we need.

# %%
pq.read_table(parquet_data, columns=["carat", "cut", "color", "clarity", "price"])

# %% [markdown]
# We have a few more ways to read Parquet files. We won't cover them all here, but
# we will take a look at using ParquetFile.

# %%
pf = pq.ParquetFile(parquet_data)

# %% [markdown]
# We can use several of the class attributes to the metadata of the file, the Arrow
# schema, count the row groups, and use the `read` method to read the file into a
# PyArrow Table.

# %%
print(pf.metadata)
print(pf.schema_arrow)
print(pf.num_row_groups)
pf.read()
