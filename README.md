# Student Mental Health ETL Pipeline

## 📌 Project Description

This project analyzes student mental health data using a simple ETL pipeline.

The goal is to understand how the length of stay in a foreign country affects mental health for international students.

---

## ⚙️ Technologies Used

- Python
- Pandas
- PostgreSQL
- SQL
- Jupyter Notebook

---

## 🔄 ETL Process

### 1. Extract

- Load raw data from a CSV file

### 2. Transform

- Clean column names
- Select relevant columns
- Handle missing values
- Normalize text data
- Convert data types

### 3. Load

- Load cleaned data into PostgreSQL using SQLAlchemy

---

## 📊 Analysis

The project uses SQL to analyze:

- Number of international students by length of stay
- Average depression score (PHQ-9)
- Average social connectedness score (SCS)
- Average acculturative stress score (ASISS)

---

## 📁 Project Structure

```
project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── transform_data.py
│   └── load_data.py
│
├── sql/
│   └── analysis.sql
│
├── pipeline.py
├── README.md
```

---

## Key Insight

This project explores how mental health indicators change depending on how long international students stay in the host country.

---

## 🎯 Learning Goals

- Understand ETL process
- Practice data cleaning with pandas
- Load data into PostgreSQL
- Write SQL queries for analysis
