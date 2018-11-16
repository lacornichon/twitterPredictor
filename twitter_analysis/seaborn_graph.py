import seaborn as sns
import matplotlib.pyplot as plt
from twitter_collect import storage
import pandas as pd

sns.set(style="darkgrid")

# Load an example dataset with long-form data


#ce programme prend 2 candidats et compare le nombres de retweets sur les derniers tweet qui citent ces candidats
def popular_words(queries):
    dataf=storage.dataframe_comparaison(queries)
    # Plot the responses for different events and regions
    sns.lineplot(x="created_at", y="retweet_count", hue="about", style="about", data=dataf)

#renvoie la positivité des tweet en fonction de leur popularité
def positive_words(queries):
    dataf=storage.dataframe_comparaison(queries)
    print(dataf)
    sns.lineplot(x="retweet_count", y="pos", hue="about", style="about", data=dataf)

plt.show()

positive_words(["Macron","Trump"])
