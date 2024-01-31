import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

trending = pytrend.today_searches(pn="US")
results = pd.DataFrame(trending).head(20)
print(results.to_string())

df = pd.DataFrame(trending.split(""))

df["Query"] = df["Query"].str.extract(r"q=(*.?)&")
df["date"] = df["date"].str.extract(r"date=(*.?)&")

print(df)
