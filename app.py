import streamlit as st
import plotly.express as px

from src.data_loader import load_and_clean_data

st.set_page_config(
    page_title="Airbnb Analytics: Chicago vs New Orleans",
    page_icon="🏠",
    layout="wide",
)

st.title("🏠 Airbnb Comparative Market Dashboard")
st.caption("Chicago vs. New Orleans short-term rental market analysis")

# Load cached data
@st.cache_data

def get_dashboard_data():
    return load_and_clean_data()


df = get_dashboard_data()

st.sidebar.header("Filter Options")
selected_cities = st.sidebar.multiselect(
    "Select Cities",
    options=sorted(df["city"].unique()),
    default=sorted(df["city"].unique()),
)

filtered_df = df[df["city"].isin(selected_cities)].copy()

if filtered_df.empty:
    st.warning("No cities selected. Pick at least one city to show market insights.")
    st.stop()

# Top Metric Tiles
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Listings", f"{filtered_df['id'].nunique():,}")
col2.metric("Average Price", f"${filtered_df['price'].mean():.2f}")
col3.metric("Avg Reviews / Listing", f"{filtered_df['number_of_reviews'].mean():.1f}")
col4.metric("Avg Availability (365d)", f"{filtered_df['availability_365'].mean():.0f} days")

st.divider()

# Interactive Summary Charts
c1, c2 = st.columns(2)

with c1:
    st.subheader("Room Type Distribution")
    room_fig = px.histogram(
        filtered_df,
        x="room_type",
        color="city",
        barmode="group",
        title="Room Type Breakdown by City",
        labels={"room_type": "Room Type"},
    )
    st.plotly_chart(room_fig, use_container_width=True)

with c2:
    st.subheader("Price Distribution (Up to 95th Percentile)")
    p95 = filtered_df["price"].quantile(0.95)
    box_fig = px.box(
        filtered_df[filtered_df["price"] <= p95],
        x="room_type",
        y="price",
        color="city",
        title="Price Variation by Room Type",
    )
    st.plotly_chart(box_fig, use_container_width=True)

st.subheader("Quick Market Takeaways")
summary = filtered_df.groupby("city").agg(
    avg_price=("price", "mean"),
    avg_reviews=("number_of_reviews", "mean"),
    avg_availability=("availability_365", "mean"),
    listing_count=("id", "count"),
).reset_index()

st.dataframe(summary, use_container_width=True, hide_index=True)

st.info(
    "👈 Use the top-left sidebar or the section pages to explore detailed deep-dive analysis for property, pricing, and host trends."
)