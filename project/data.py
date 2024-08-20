import pandas as pd

df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
print(df)
df.set_index("col1", inplace=True, drop=False)
print(
    (
        df.assign(col3=lambda x: x.col1 + x.col2)
        .assign(col4=lambda x: -x.col3 + 1)
        .assign(col5=lambda x: x.col4 + x.col3)
    )
)


def fuc(a, b):
    c = a + b
    c = c
    
    return c


fuc(4, 1)
fuc1(4, 1)