import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


df = pd.read_csv("happiness.csv")


# First look at the data
#print(df.head())
#print(df.shape)
#print(df.columns.tolist())
#print(df.isnull().sum())


# Which 10 countries are the happiest?
# Which 10 countries are the least happy?
# What does the happiness score distribution look like? (histogram)

# Which 10 countries are the happiest?
#print(df.sort_values("Score", ascending=False).head(10))

# Which 10 countries are the least happy?
#print(df.sort_values("Score", ascending=True).head(10))

# What does the happiness score distribution look like? (histogram)
#plt.figure()
#plt.hist(df["Score"], bins=20)
#plt.xlabel("Happiness Score")
#plt.ylabel("Frequency")
#plt.tight_layout()
#plt.title("Distribution of Happiness Scores")
#plt.savefig("Happiness_Distribution.png")
#plt.close()


# Top 10 happiest countries bar chart
plt.figure()
top_10 = df.sort_values("Score", ascending=False).head(10)
plt.barh(top_10["Country or region"], top_10["Score"], color='skyblue')
plt.xlabel("Happiness Score")
plt.title("Top 10 Happiest Countries 2019")
plt.tight_layout()
plt.savefig("Top10_Happiest_Countries.png")
plt.close()


# Scatter plot — GDP vs Happiness Score
plt.figure()
plt.scatter(df["GDP per capita"], df["Score"], alpha=0.6, color='green')
plt.xlabel("GDP per Capita")
plt.ylabel("Happiness Score")
plt.title("GDP per Capita vs Happiness Score")
plt.tight_layout()
plt.savefig("GDP_vs_Happiness.png")
plt.close()


print("All charts saved!")



