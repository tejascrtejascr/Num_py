import pandas as pd

data = {
    "Name": ["Tejas", "Rahul", "Anu", "Kiran"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 55, 90, 45]
}

df = pd.DataFrame(data)

passed = df[df["Marks"] >= 50]

print("Students who passed:")
print(passed)