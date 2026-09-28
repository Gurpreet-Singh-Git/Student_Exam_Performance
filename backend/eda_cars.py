import pandas as pd

# Scaler and encoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# ML models
from sklearn.linear_model import LinearRegression


# =========================
# DATA
# =========================

df = pd.read_csv(r"../data/used_cars.csv")

X = df.drop(columns=["price"])
y = df["price"]


# =========================
# BRAND - ONE HOT ENCODING
# =========================

oh_encoder = OneHotEncoder(
    sparse_output=False,
    handle_unknown="ignore"
)

brand_encoded = oh_encoder.fit_transform(X[["brand"]])


# =========================
# MODEL
# =========================

X = X.drop(columns=["model"])


# =========================
# MODEL YEAR
# =========================

s_scaler = StandardScaler()

X["model_year"] = s_scaler.fit_transform(
    X[["model_year"]]
)


# =========================
# MILAGE
# =========================

X["milage"] = (
    X["milage"]
    .str.replace("mi.", "", regex=False)
    .str.replace(",", "", regex=False)
)

X["milage"] = pd.to_numeric(X["milage"])


# =========================
# MILAGE EDA visualiazation
# =========================
"""
mean = X["milage"].mean()
median = X["milage"].median()
std = X["milage"].std()

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Std: {std}")


# Mean ± 3 Standard Deviations

lower = mean - (3 * std)
upper = mean + (3 * std)

print(f"Lower (Mean - 3std): {lower}")
print(f"Upper (Mean + 3std): {upper}")


sns.stripplot(
    x=X["milage"],
    jitter=0.01
)

plt.axvline(
    lower,
    linestyle="--",
    label="Mean - 3std"
)

plt.axvline(
    upper,
    linestyle="--",
    label="Mean + 3std"
)

plt.axvline(
    mean,
    linestyle="-",
    label="Mean"
)

plt.axvline(
    median,
    linestyle="--",
    label="Median"
)

plt.xlabel("Mileage")
plt.title("Mileage Distribution / Outliers")
plt.legend()
plt.show()
"""



# fuel_type
X["fuel_type"] = oh_encoder.fit_transform(X[["fuel_type"]])





print(X.head().to_string())







# =========================
# PRICE
# =========================

y = (
    y
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)
y = pd.to_numeric(y)
