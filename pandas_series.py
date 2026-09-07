import pandas as pd

marks = pd.Series([85, 78, 92, 88, 95])

print("Marks:")
print(marks)

print("First mark:", marks[0])
print("Average:", marks.mean())