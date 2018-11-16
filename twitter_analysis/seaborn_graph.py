import seaborn as sns
import matplotlib.pyplot as plt
from twitter_collect import storage
import pandas as pd

sns.set(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal", hue="region", style="event", data=fmri)

query="Macron"

data=storage.dataframe(query)
retweet_c = pd.Series(data=data['retweet_count'].values, index=data['created_at'])
retweet_c.plot(figsize=(16,4), label="Retweets", legend=True)

query="Michel"

data=storage.dataframe(query)
retweet_c = pd.Series(data=data['retweet_count'].values, index=data['created_at'])
retweet_c.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()
