import streamlit as st
import pandas as pd
import psycopg2
import time
import random

connection = psycopg2.connect(
    host="localhost",
    database="redbus_database",
    user="postgres",
    password="1234"
)

query_states = "SELECT DISTINCT State FROM redbus_data"
df_state = pd.read_sql(query_states, connection)

max_price_query = "SELECT max(price) FROM redbus_data"
df_price = pd.read_sql(max_price_query, connection)

query_bustypes = "SELECT DISTINCT bus_type FROM redbus_data"
df_bustype = pd.read_sql(query_bustypes, connection)
st.sidebar.markdown(
    """
    <style>
    .stSlider > div {
        color: #4CAF50; /* Green color for the slider label */
    }
    .stNumberInput > div {
        color: #ff9800; /* Orange color for the number input */
    }
    </style>
    """, 
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .header-banner {
        background-color: #TT800;
        padding: 10px;
        text-align: center;
        color: white;
        font-size: 25px;
        font-weight: bold;
    }
    </style>
    <div class="header-banner">
        Welcome to Redbus Information
    </div>
    """, 
    unsafe_allow_html=True
)

st.image("C:/Users/raghul/Downloads/channels4_banner.jpg", use_column_width=True)
import streamlit as st


col1, col2 = st.sidebar.columns([1,2]) 

with col1:
    st.image("C:/Users/raghul/Downloads/unnamed.jpg", width=70)  

with col2:
    st.title("Filter Data")  

 





state = st.sidebar.selectbox("State:",df_state)



if state:
    route_query = f"SELECT DISTINCT Route FROM redbus_data WHERE State = '{state}'"
    df_route = pd.read_sql(route_query, connection)
    if not df_route.empty:
        route = st.sidebar.selectbox("Route:", df_route)
    else:
        st.sidebar.selectbox("Route:", ["No routes available"])

price = st.sidebar.number_input("Max Price", min_value=0.0, max_value=5000.0, value=100.0, step=100.0)

star = st.sidebar.slider("Star Rating", 1, 5, value=3, step=1)

bustype = st.sidebar.multiselect("Select Bus Type:", [''] + df_bustype['bus_type'].tolist())

all_q = "SELECT * FROM redbus_data"
all_clear = pd.read_sql(all_q, connection)

if st.button("Search"):
    filtered_query = "SELECT * FROM redbus_data WHERE 1=1"  

    if state:
        filtered_query += f" AND State = '{state}'"
    if route:
        filtered_query += f" AND route = '{route}'"  
    if price is not None:
        filtered_query += f" AND price <= {price}"
    if bustype:
        bustype_string = "', '".join(bustype)
        filtered_query += f" AND bus_type IN ('{bustype_string}')"
    if star is not None:
        filtered_query += f" AND star_rating <= {star}"

    try:
        df_filtered_data = pd.read_sql(filtered_query, connection)
        if df_filtered_data.empty:
            st.write("No data found with the selected filters.")
        else:
            st.dataframe(df_filtered_data[['route', 'bus_name', 'price', 'star_rating', 'departing_time', 'bus_type', 'duration_time', 'seats_available', 'reaching_time']])
    except Exception as e:
        st.write(f"An error occurred: {e}")

if st.sidebar.button("Show All Data"):
    with st.spinner('Wait for it...'):
        time.sleep(2)
        st.success("Done!")
        st.write("All Data:", all_clear)
        st.snow() 