import pandas as pd

data = {
    "Name": ["Tejas", "Rahul", "Anu", "Kiran"],
    "Marks": [85, 55, 90, 45]
}

df = pd.DataFrame(data)

sorted_data = df.sort_values("Marks")

print("Sorted by marks:")
print(sorted_data)