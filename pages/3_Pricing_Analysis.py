import streamlit as st
import plotly.express as px

from src.data_loader import load_and_clean_data

st.set_page_config(page_title="Pricing Analysis", page_icon="💰", layout="wide")

st.title("💰 Pricing Analysis")

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

p95 = filtered_df["price"].quantile(0.95)
trimmed = filtered_df[filtered_df["price"] <= p95]

c1, c2 = st.columns(2)

with c1:
    st.subheader("Price distribution by city")
    fig = px.histogram(
        trimmed,
        x="price",
        color="city",
        nbins=40,
        marginal="box",
        title="Distribution of Listing Prices",
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Median price by room type")
    metrics = trimmed.groupby(["city", "room_type"], as_index=False)["price"].median()
    fig = px.bar(metrics, x="room_type", y="price", color="city", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Price spread across room types")
box_fig = px.box(
    trimmed,
    x="room_type",
    y="price",
    color="city",
    title="Price Variation by Room Type",
)
st.plotly_chart(box_fig, use_container_width=True)

st.subheader("Price vs. reviews")
review_scatter = px.scatter(
    filtered_df,
    x="number_of_reviews",
    y="price",
    color="city",
    hover_data=["neighbourhood", "room_type"],
    title="Listing prices against review volume",
)
st.plotly_chart(review_scatter, use_container_width=True)
