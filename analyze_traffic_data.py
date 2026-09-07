import pandas as pd

# Read the new CSV
file_name = "shenyang_traffic_data.csv"
df = pd.read_csv(file_name)

# Basic data check
print("Data check")
print("Number of records:", len(df))
print("Number of columns:", len(df.columns))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate records:", df.duplicated().sum())

print("\nData source:")
print(df["data_source"].value_counts())

# Average results for each road
road_summary = (
    df.groupby("road")[
        ["travel_time_min", "average_speed_kmh"]
    ]
    .mean()
    .round(2)
)

print("\nAverage results by road:")
print(road_summary)

# Set the correct period order
period_order = [
    "Morning Peak",
    "Noon Off-Peak",
    "Evening Peak",
    "Night Off-Peak"
]

# Average results for each period
period_summary = (
    df.groupby("period")[
        ["travel_time_min", "average_speed_kmh"]
    ]
    .mean()
    .reindex(period_order)
    .round(2)
)

print("\nAverage results by period:")
print(period_summary)