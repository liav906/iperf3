import pandas as pd

# Sample data for jitter and bandwidth
jitter_values = [1.2, 1.5, 1.8, 2.0]
bandwidth_values = [5.5, 6.0, 6.5, 7.0]

# Create a DataFrame with jitter and bandwidth columns
data = {
    'Jitter': jitter_values,
    'Bandwidth': bandwidth_values
}

df = pd.DataFrame(data)

# Specify the Excel file name
excel_file = 'jitter_bandwidth_data.xlsx'

# Save the DataFrame to the Excel file
df.to_excel(excel_file, index=False)

print(f'Data has been saved to {excel_file}')
