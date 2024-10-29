import streamlit as st
import pandas as pd
import sqlite3
from mapaction_logging.status_codes import StatusCode

def get_log_data():
    """
    Fetches log data from the database and returns a Pandas DataFrame.
    """
    conn = sqlite3.connect('mapaction_logging.db')
    df = pd.read_sql_query("SELECT * FROM logs", conn)
    conn.close()
    return df

def filter_data(df, selected_status_codes, selected_countries):
    """
    Filters the DataFrame based on selected status codes and countries.
    """
    if selected_status_codes:
        df = df[df['status_code'].isin([code.value for code in selected_status_codes])]
    if selected_countries:
        df = df[df['country'].isin(selected_countries)]
    return df

def main():
    st.title("MapAction Logging Dashboard")

    # Fetch log data
    df = get_log_data()

    # Sidebar filters
    st.sidebar.header("Filters")
    selected_status_codes = st.sidebar.multiselect(
        "Status Codes", list(StatusCode), default=list(StatusCode)
    )
    selected_countries = st.sidebar.multiselect(
        "Countries", df['country'].unique(), default=df['country'].unique()
    )

    # Filter data
    filtered_df = filter_data(df.copy(), selected_status_codes, selected_countries)

    # Display data
    st.dataframe(filtered_df)

if __name__ == "__main__":
    main()