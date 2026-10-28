import streamlit as st
import plotly.express as px

from src.data_loader import load_and_clean_data

st.set_page_config(page_title="Overview", page_icon="📊", layout="wide")

st.title("📊 Overview")

df = load_and_clean_data()

st.sidebar.header("Overview Filters")
selected_cities = st.sidebar.multiselect(
    "Select Cities",
    options=sorted(df["city"].unique()),
    default=sorted(df["city"].unique()),
)
filtered_df = df[df["city"].isin(selected_cities)].copy()

if filtered_df.empty:
    st.warning("Select at least one city to continue.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Listings", f"{filtered_df['id'].nunique():,}")
col2.metric("Avg Price", f"${filtered_df['price'].mean():.2f}")
col3.metric("Avg Reviews", f"{filtered_df['number_of_reviews'].mean():.1f}")
col4.metric("Avg Availability", f"{filtered_df['availability_365'].mean():.0f} days")

c1, c2 = st.columns(2)

with c1:
    st.subheader("City comparison: room types")
    fig = px.histogram(
        filtered_df,
        x="room_type",
        color="city",
        barmode="group",
        title="Room Type Mix by City",
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Average price by neighborhood")
    neighborhood_prices = (
        filtered_df.groupby(["city", "neighbourhood"], as_index=False)["price"].mean()
        .sort_values("price", ascending=False)
        .head(15)
    )
    fig = px.bar(
        neighborhood_prices,
        x="neighbourhood",
        y="price",
        color="city",
        title="Top Neighborhood Pricing",
        barmode="group",
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Summary table")
summary = filtered_df.groupby("city").agg(
    listings=("id", "count"),
    avg_price=("price", "mean"),
    avg_reviews=("number_of_reviews", "mean"),
    avg_availability=("availability_365", "mean"),
).reset_index()
st.dataframe(summary, use_container_width=True, hide_index=True)
