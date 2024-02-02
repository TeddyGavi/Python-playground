import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

trending = pytrend.today_searches(pn="CA")
# df = pd.DataFrame(trending)
#
# # print(results.to_string())
#
# # df = pd.DataFrame(trending.split(""))
# #
# # df["Query"] = df["Query"].str.extract(r"q=(*.?)&")
# # df["date"] = df["date"].str.extract(r"date=(*.?)&")
# #
# print(df)
#
# df["exploreLink"] = df["exploreLink"].str.extract(r"q=(.*?)&")
# print(df)
#
# print(df.head(20))  # Display DataFrame
# Replace '+' with space in each query
trending = [query.replace("+", " ") for query in trending]

# Create DataFrame with 'exploreLink' column
df = pd.Series(trending)
print(df.values, df.shape)
