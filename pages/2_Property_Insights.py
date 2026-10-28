import streamlit as st
import plotly.express as px

from src.data_loader import load_and_clean_data

st.set_page_config(page_title="Property Insights", page_icon="🏘️", layout="wide")

st.title("🏘️ Property Insights")

df = load_and_clean_data()
selected_cities = st.sidebar.multiselect(
    "Select Cities",
    options=sorted(df["city"].unique()),
    default=sorted(df["city"].unique()),
)
filtered_df = df[df["city"].isin(selected_cities)].copy()

if filtered_df.empty:
    st.warning("Select at least one city to continue.")
    st.stop()

room_type = st.selectbox("Room type", ["All", *sorted(filtered_df["room_type"].dropna().unique())])
if room_type != "All":
    filtered_df = filtered_df[filtered_df["room_type"] == room_type]

left, right = st.columns(2)
with left:
    st.subheader("Average price by room type")
    room_prices = filtered_df.groupby(["city", "room_type"], as_index=False)["price"].mean()
    fig = px.bar(room_prices, x="room_type", y="price", color="city", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Listing count by neighborhood")
    hood_counts = filtered_df.groupby(["city", "neighbourhood"], as_index=False)["id"].count().sort_values("id", ascending=False).head(15)
    fig = px.bar(hood_counts, x="neighbourhood", y="id", color="city", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Price vs. availability")
scatter = px.scatter(
    filtered_df,
    x="availability_365",
    y="price",
    color="city",
    hover_data=["neighbourhood", "room_type"],
    trendline="ols",
    title="Property pricing relative to annual availability",
)
st.plotly_chart(scatter, use_container_width=True)
