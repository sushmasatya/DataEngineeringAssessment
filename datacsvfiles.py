import json
import pandas as pd

path = r"C:\Users\sushma\IdeaProjects\untitled4"
df = pd.DataFrame(json.load(open(f"{path}/customer_data.json", encoding="utf-8")))
df.to_csv(f"{path}/customer_data.csv", index=False, encoding="utf-8")
print(df["email"].str.len().max())