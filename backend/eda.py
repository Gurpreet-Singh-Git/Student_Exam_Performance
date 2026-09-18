import pandas as pd
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv(r"../data/student_exam_performance.csv").drop(columns="student_id")

ncol_dict = {}
ocol_dict = {}

for col in df.columns:

    if df[col].dtype == "object":
        ocol_dict[col] = df[col].unique()

    else:
        ncol_dict[col] = {
            "max": df[col].max(),
            "min": df[col].min(),
            "mean": df[col].mean(),
            "std": df[col].std()
        }


# Number of missing values
for col in df.columns:
    if df[col].dtype == "object":
        print(f"{col}, {df[col].dtype}")
        print(f"{df[col].unique()}")
        print(df[col].isna().sum(),f"\n\n")


# Apply direct mappings to all ordinal categorical columns
df['notes_quality'] = df['notes_quality'].map({"Poor": 0, "Average": 1, "Excellent": 2})
df['sleep_quality'] = df['sleep_quality'].map({"Poor": 0, "Fair": 1, "Good": 2, "Excellent": 3})
df['parent_education'] = df['parent_education'].map({"High School": 0, "Associate": 1, "Bachelor": 2, "Master": 3, "Doctorate": 4})
df['family_income'] = df['family_income'].map({"Low": 0, "Lower-Middle": 1, "Middle": 2, "Upper-Middle": 3, "High": 4})
df['class_participation'] = df['class_participation'].map({"Low": 0, "Medium": 1, "High": 2})
df['study_consistency'] = df['study_consistency'].map({"Low": 0, "Medium": 1, "High": 2})
df['study_environment'] = df['study_environment'].map({"Noisy": 0, "Moderate": 1, "Quiet": 2})
df['revision_frequency'] = df['revision_frequency'].map({"Rarely": 0, "Weekly": 1, "Daily": 2})
df['break_frequency'] = df['break_frequency'].map({"Rarely": 0, "Occasionally": 1, "Frequently": 2})
df['motivation_level'] = df['motivation_level'].map({"Low": 0, "Medium": 1, "High": 2})
df['exam_difficulty'] = df['exam_difficulty'].map({"Easy": 0, "Medium": 1, "Hard": 2})
df['educational_app_usage'] = df['educational_app_usage'].map({"Low": 0, "Moderate": 1, "High": 2})
df['performance_grade'] = df['performance_grade'].map({"F": 0, "D": 1, "C": 2, "B": 3, "A": 4})
df['performance_level'] = df['performance_level'].map({"Low": 0, "Medium": 1, "High": 2})
df['education_level'] = df['education_level'].map({"High School": 0, "Undergraduate": 1})
df['pass_status'] = df['pass_status'].map({"Fail": 0, "Pass": 1})

# Apply one-hot encoding for nominal categorical columns
onehot_cols = ['gender', 'school_type', 'urban_rural', 'study_method', "device_availability"]
onehot_encoder = OneHotEncoder(sparse_output=False)
onehot_encoded = onehot_encoder.fit_transform(df[onehot_cols])
df = df.drop(columns=onehot_cols)

df = pd.concat([
    df,
    pd.DataFrame(
        onehot_encoded,
        columns=onehot_encoder.get_feature_names_out(onehot_cols),
        index=df.index
    )
], axis=1)


# Seperate categorical and numerical columns
num_cols = df.select_dtypes(include="number").columns
cat_cols = df.select_dtypes(include="object").columns

pd.set_option("display.max_columns", None)

#print(df.head(10))




# imputer = KNNImputer(n_neighbors=10)

