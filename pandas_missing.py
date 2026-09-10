import pandas as pd

data = {
    "Name": ["Tejas", "Rahul", "Anu", "Kiran"],
    "Marks": [85, None, 90, 75]
}

df = pd.DataFrame(data)

print("Original data:")
print(df)

print("\nMissing values:")
print(df.isnull())

df["Marks"] = df["Marks"].fillna(0)

print("\nAfter filling missing values:")
print(df)