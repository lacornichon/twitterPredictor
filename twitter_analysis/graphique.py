import numpy as np
from twitter_collect import storage
import pandas as pd

query="candidat"

data=storage.dataframe(query)
retweet_c = pd.Series(data=data['retweet_count'].values, index=data['created_at'])
retweet_c.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()
