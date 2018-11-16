import seaborn as sns
import matplotlib.pyplot as plt
from twitter_collect import storage
import pandas as pd

sns.set(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
print(fmri)

#ce programme prend 2 candidats et compare le nombres de retweets sur les derniers tweet qui citent ces candidats

dataf=storage.dataframe_comparaison(["chocolatine","pain au chocolat"])
print(dataf)
# Plot the responses for different events and regions
sns.lineplot(x="created_at", y="retweet_count", hue="about", style="about", data=dataf)


plt.show()

