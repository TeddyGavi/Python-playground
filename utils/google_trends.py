import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

trending = pytrend.today_searches(pn="US")
results = pd.DataFrame(trending).head(20)
print(results.to_string())
