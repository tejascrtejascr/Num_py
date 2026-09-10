import pandas as pd

data = {
    "Name": ["Tejas", "Rahul", "Anu", "Kiran"],
    "Marks": [85, 55, 90, 45]
}

df = pd.DataFrame(data)

print("Total marks:", df["Marks"].sum())
print("Average marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())