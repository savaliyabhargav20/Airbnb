from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def load_and_clean_data():
    base_dir = Path(__file__).resolve().parents[1]
    chi_path = base_dir / "datasets" / "Chicago.csv"
    nola_path = base_dir / "datasets" / "New Orleans.csv"

    chi = pd.read_csv(chi_path)
    nola = pd.read_csv(nola_path)
    chi["city"] = "Chicago"
    nola["city"] = "New Orleans"
    df = pd.concat([chi, nola], ignore_index=True)

    # Clean price
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Clean text & reviews
    df["neighbourhood"] = df["neighbourhood"].astype(str).str.strip().str.title()
    df["reviews_per_month"] = df["reviews_per_month"].fillna(0)
    df["number_of_reviews"] = df["number_of_reviews"].fillna(0)

    # Host listing count
    if "calculated_host_listings_count" in df.columns:
        df["host_listing_count"] = df["calculated_host_listings_count"]
    else:
        host_counts = df.groupby("host_id")["id"].nunique().rename("host_listing_count")
        df = df.merge(host_counts, on="host_id", how="left")

    def host_type(x):
        if pd.isna(x):
            return "Unknown"
        if x == 1:
            return "Single-listing Host"
        if x <= 3:
            return "Small Host (2-3)"
        if x <= 10:
            return "Mid Host (4-10)"
        return "Multi-listing Host (>10)"

    df["host_type"] = df["host_listing_count"].apply(host_type)
    df["has_reviews"] = df["number_of_reviews"] > 0

    return df