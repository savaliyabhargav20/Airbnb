import streamlit as st
import plotly.express as px

from src.data_loader import load_and_clean_data

st.set_page_config(page_title="Host Analysis", page_icon="👥", layout="wide")

st.title("👥 Host Analysis")

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

left, right = st.columns(2)

with left:
    st.subheader("Host type mix")
    host_summary = filtered_df.groupby(["city", "host_type"], as_index=False)["id"].count()
    fig = px.bar(host_summary, x="host_type", y="id", color="city", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Average reviews by host type")
    review_by_host = filtered_df.groupby(["city", "host_type"], as_index=False)["number_of_reviews"].mean()
    fig = px.bar(review_by_host, x="host_type", y="number_of_reviews", color="city", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Top host listing count distribution")
listing_distribution = filtered_df.groupby(["city", "host_listing_count"], as_index=False)["id"].count().sort_values("host_listing_count")
fig = px.line(listing_distribution, x="host_listing_count", y="id", color="city", markers=True)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Host performance summary")
performance = filtered_df.groupby("city").agg(
    avg_host_listings=("host_listing_count", "mean"),
    avg_reviews_per_listing=("number_of_reviews", "mean"),
    share_with_reviews=("has_reviews", "mean"),
).reset_index()
st.dataframe(performance, use_container_width=True, hide_index=True)
