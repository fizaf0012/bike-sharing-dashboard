import os
import pandas as pd

# Step 1: Set your folder path where CSVs are stored
folder_path = './raw_bike_data'  # Rename this to your actual folder

# Step 2: List all CSV files
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Step 3: Read and combine all files
combined_df = pd.concat([pd.read_csv(os.path.join(folder_path, file)) for file in csv_files], ignore_index=True)

# Step 4: Basic cleaning (optional)
# Drop rows with missing start/end times
combined_df = combined_df.dropna(subset=['started_at', 'ended_at'])

# Save the result
output_path = './combined_bike_data.csv'
combined_df.to_csv(output_path, index=False)

print(f"\n✅ Combined {len(csv_files)} files into: {output_path}")
print(f"✅ Total records: {len(combined_df)}")
