import pandas as pd
from datetime import datetime

# Load combined CSV
df = pd.read_csv('data/combined_bike_data.csv')

# Convert to datetime
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])
df = df[(df['started_at'] >= '2021-10-01') & (df['started_at'] <= '2022-03-31')]

# Drop any rows with null start/end times or invalid dates
df.dropna(subset=['started_at', 'ended_at'], inplace=True)

# Calculate duration in minutes
df['duration_min'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

# Optional: remove negative or zero durations
df = df[df['duration_min'] > 0]

# Extract date parts
df['date'] = df['started_at'].dt.date
df['month'] = df['started_at'].dt.strftime('%Y-%m')
df['day_of_week'] = df['started_at'].dt.day_name()
df['hour'] = df['started_at'].dt.hour

# Select relevant columns only
processed_df = df[[
    'ride_id',
    'rideable_type',
    'member_casual',
    'started_at',
    'ended_at',
    'duration_min',
    'month',
    'day_of_week',
    'hour',
    'start_station_name',
    'end_station_name'
]]

# Save cleaned file
processed_df.to_csv(
    'data/cleaned_bike_data.csv',
    index=False,
    encoding='utf-8',
    lineterminator='\n'
)


print("✅ Preprocessing complete. Saved to: data/cleaned_bike_data.csv")
