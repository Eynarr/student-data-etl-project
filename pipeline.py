from load_data import load_data_postgres
from transform_data import transform_data

df = transform_data("../data/raw/students.csv", "../data/processed/students.csv")

load_data_postgres(df)
