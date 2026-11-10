import pandas as pd 
series = pd.Series([1, 2, 3], index=["katalis", "remde", "imanuel"])
print(series)

dataframe = pd.DataFrame(
    {
        "nama": ["udin", "lisa", "raden"],
        "umur": [15, 24, 65],
        "prodi": ["sistem informasi", "manajemen", "akuntansi"]
    }
)
print(dataframe)