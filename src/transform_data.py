import pandas as pd


def transform_data(input_path, output_path):
    # Read the students csv
    df = pd.read_csv(input_path)

    # Drop missing values and duplicates
    df = df.dropna(how="all")
    df = df.drop_duplicates()

    # Clean columns names
    df.columns = df.columns.str.strip().str.lower()

    # Select only relevant columns
    columns_to_keep = [
        "inter_dom",
        "region",
        "gender",
        "academic",
        "age",
        "stay",
        "japanese_cate",
        "english_cate",
        "todep",
        "tosc",
        "toas",
    ]
    df = df[columns_to_keep]

    # Rename columns for clarity
    df = df.rename(
        columns={
            "stay": "years_country",
            "inter_dom": "student_type",
            "todep": "depression_score",
            "tosc": "social_connectedness_score",
            "toas": "acculturative_stress_score",
            "academic": "academic_level",
            "english_cate": "english_level",
            "japanese_cate": "japanese_level",
        }
    )

    # Normalized data
    text_cols = ["student_type", "academic_level", "english_level", "japanese_level"]

    for col in text_cols:
        df[col] = df[col].str.strip().str.title()

    df["academic_level"] = df["academic_level"].replace(
        {"Grad": "Graduated", "Under": "Undergraduate"}
    )

    df["student_type"] = df["student_type"].replace(
        {"Inter": "International", "Dom": "Domestic"}
    )

    # Type conversion for clarity
    df["years_country"] = pd.to_numeric(df["years_country"], errors="coerce")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    df = df.dropna(subset=["years_country", "age"])

    # Saving the new csv
    df.to_csv(output_path, index=False)
    print("Cleaned dataset saved")
    return df


df = transform_data(
    "../data/raw/students.csv",
    "../data/processed/students.csv",
)
