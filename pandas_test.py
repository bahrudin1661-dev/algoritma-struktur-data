import pandas as pd
# series : satu kolom
nilai = pd.Series([80, 60, 80], index=["andi", "lidya", "linda"])

# DataFrame : table utuh

df = pd.DataFrame({
    "nama": ["udin", "lisa", "linda"],
    "jurusan": ["SI", "TI", "IT"],
    "IPK": [2.4, 2.3, 2.1]
})
print(df)