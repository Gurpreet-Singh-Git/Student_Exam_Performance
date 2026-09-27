import pandas as pd

#scaler and encoder import
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

#visualisation
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"../data/used_cars.csv")

s_scaler = StandardScaler()
df["model_year"] = s_scaler.fit_transform(df[["model_year"]])


oh_encoder = OneHotEncoder(sparse_output=False)
df["brand"] = oh_encoder.fit_transform(df[["brand"]])

# print(len(df["model"].unique().tolist()))

df["milage"] = (df["milage"].str.replace("mi.", "").str.replace(",", ""))
df["milage"] = pd.to_numeric(df["milage"])


mean = df["milage"].mean()
median = df["milage"].median()
std = df["milage"].std()
print(f"mean: {mean}\nstd: {std}\nmedian: {median}")

lower = mean - (1 * std)
upper = mean + (1 * std)
print(f"lower: {lower}\nupper: {upper}")

sns.stripplot(x=df["milage"], jitter=0.01)

plt.axvline(lower, linestyle="--", label="Mean - 3std")
plt.axvline(upper, linestyle="--", label="Mean + 3std")
plt.axvline(mean, linestyle="--", label="Mean")
plt.axvline(median, linestyle="--", label="Median")


plt.xlabel("Milage")
plt.title("Milage Distribution / Outliers")
plt.legend()
plt.show()

#try skew()