import streamlit as st
import sqlite3
import pandas as pd

# Streamlit config
st.set_page_config(page_title="IntelliSQL", layout="centered")
st.title("IntelliSQL – English to SQL")

# Simple rule-based SQL generator (NO Gemini for now)
def get_sql(question):
    q = question.lower()

    if "all students" in q:
        return "SELECT * FROM STUDENTS;"
    elif "marks" in q:
        return "SELECT NAME, MARKS FROM STUDENTS;"
    elif "class" in q:
        return "SELECT NAME, CLASS FROM STUDENTS;"
    else:
        return "SELECT * FROM STUDENTS;"

# Run SQL
def run_query(sql):
    conn = sqlite3.connect("data.db")
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

# UI
question = st.text_input("Ask a question about the students database:")

if st.button("Generate & Run"):
    if question:
        try:
            sql_query = get_sql(question)
            st.subheader("Generated SQL Query")
            st.code(sql_query)

            result_df = run_query(sql_query)
            st.subheader("Result")
            st.dataframe(result_df)
        except Exception as e:
            st.error(str(e))
    else:
        st.warning("Please enter a question")