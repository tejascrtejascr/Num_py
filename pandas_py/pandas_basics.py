import pandas as pd

data = {
    "Name": ["Tejas", "Rahul", "Anu"],
    "Age": [20, 21, 19],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)

print(df)