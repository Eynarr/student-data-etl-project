import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


def load_data_postgres(df):
    # Load data form the .env
    load_dotenv()

    # Create the connection
    engine = create_engine(
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

    # Send it to PostgreSQL
    df.to_sql("students", engine, if_exists="replace", index=False)

    print("Data loaded in the Database")
