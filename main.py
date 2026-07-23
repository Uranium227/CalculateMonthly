import pandas as pd
from ucimlrepo import fetch_ucirepo 

online_retail = fetch_ucirepo(id=352) 
df = online_retail.data.features

print(df)
