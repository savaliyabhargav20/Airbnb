# 🏠 Airbnb Comparative Market Dashboard

An interactive data dashboard built with **Python and Streamlit** to explore and compare Airbnb short-term rental markets in **Chicago and New Orleans**. The dashboard helps users review listing counts, prices, reviews, availability, and room-type patterns using interactive charts and filters.

## 📌 Project Overview

This project uses Airbnb listing data to compare two city markets. Users can select cities, view key market metrics, explore room-type distribution, compare prices across room types, and review a summary of market trends.

## ✨ Features

- **City filter:** Select one or more cities from the sidebar.
- **Key metrics:** View total listings, average price, average reviews per listing, and average availability.
- **Room-type comparison:** Explore the number of listings by room type and city.
- **Price analysis:** Compare price ranges across room types and cities.
- **Market summary:** View a table of listing counts, average prices, reviews, and availability by city.
- **Data cleaning:** Load and clean the data before showing the dashboard.
- **Interactive charts:** Explore results using Plotly charts.

## 🛠️ Technologies Used

- **Python** — main programming language
- **Streamlit** — dashboard interface
- **Pandas** — data handling and analysis
- **NumPy** — numerical operations
- **Plotly** — interactive charts
- **Matplotlib and Seaborn** — data visualization libraries included in the project requirements

## 📂 Project Structure

```text
Airbnb/
├── app.py
├── requirements.txt
├── datasets/
├── pages/
└── src/
    └── data_loader.py
```

> The `datasets/`, `pages/`, and `src/` folders contain project data, dashboard pages, and supporting code. The exact files may vary as the project develops.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/savaliyabhargav20/Airbnb.git
cd Airbnb
```

### 2. Create a virtual environment (recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Check the dataset

Make sure the Airbnb dataset files required by `src/data_loader.py` are available in the expected location inside the `datasets/` folder.

### 5. Run the dashboard

```bash
streamlit run app.py
```

Streamlit will show a local URL in your terminal. Open that URL in your browser to use the dashboard.

## 📊 Dashboard Insights

The dashboard provides these main views:

| Metric / Chart | What it shows |
|---|---|
| Total Listings | Number of unique Airbnb listings in the selected cities |
| Average Price | Average listing price |
| Average Reviews per Listing | Average number of reviews for listings |
| Average Availability | Average available days in a 365-day period |
| Room Type Distribution | Listing distribution by room type and city |
| Price Distribution | Price variation by room type and city |
| Market Summary | City-level comparison of listings, prices, reviews, and availability |

## 🧹 Data Processing

The dashboard loads its data through the `load_and_clean_data()` function in `src/data_loader.py`. The data is cached with Streamlit to reduce repeated loading during a session.

## 💡 Possible Future Improvements

- Add more cities for comparison.
- Add filters for price, room type, and availability.
- Add maps to show listing locations.
- Add trend charts for reviews and availability.
- Deploy the dashboard online so others can access it.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes.
4. Open a pull request describing what you changed.

## 👤 Author

**Bhargav Savaliya**

- GitHub: [@savaliyabhargav20](https://github.com/savaliyabhargav20)
- Project: [Airbnb Comparative Market Dashboard](https://github.com/savaliyabhargav20/Airbnb)
