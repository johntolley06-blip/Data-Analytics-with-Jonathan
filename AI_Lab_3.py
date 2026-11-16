
import pandas as pd

# Load the workout dataset
file_path = "workout_history (1).csv"

df = pd.read_csv(file_path)

# Convert dates, supporting multiple date formats
df["Workout Date"] = pd.to_datetime(
    df["Workout Date"],
    format="mixed",
    errors="coerce"
)

# Explore the dataset
print("===== WORKOUT DATASET EXPLORATION =====")

print("\nNumber of Rows:", len(df))
print("Number of Columns:", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nWorkout Types:")
print(df["Activity Type"].value_counts())

print("\nEarliest Workout Date:")
print(df["Workout Date"].min())

print("\nLatest Workout Date:")
print(df["Workout Date"].max())

print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# Filter 2026 records
workouts_2026 = df[
    df["Workout Date"].dt.year == 2026
].copy()

print("\n===== 2026 WORKOUTS =====")
print("Total 2026 Records:", len(workouts_2026))
print(workouts_2026["Activity Type"].value_counts())


