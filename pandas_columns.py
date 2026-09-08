import pandas as pd

data = {
    "Name": ["Tejas", "Rahul", "Anu"],
    "Age": [20, 21, 19],
    "Marks": [85, 75, 90]
}

df = pd.DataFrame(data)

print("Names:")
print(df["Name"])

print("Marks:")
print(df["Marks"])