import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\qaism\Downloads\MSDS-Orientation-Computer-Survey(in).csv")
data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')

def filter_outliers(df, col):
    Q1, Q3 = df[col].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    lb, ub = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    return df[(df[col] >= lb) & (df[col] <= ub)]

filtered_data = filter_outliers(data, 'Hard Drive Size (in GB)')
max_size = filtered_data['Hard Drive Size (in GB)'].max()
min_size = filtered_data['Hard Drive Size (in GB)'].min()

plt.figure(figsize=(12, 8))
plt.hist(filtered_data['Hard Drive Size (in GB)'], bins=10, color='purple', edgecolor='black')
plt.title('Distribution of Hard Drive Sizes', fontsize=15)
plt.xlabel('Hard Drive Size (in GB)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axvline(max_size, color='red', linestyle='dashed', linewidth=1)
plt.axvline(min_size, color='blue', linestyle='dashed', linewidth=1)
plt.text(max_size, plt.ylim()[1] * 0.9, f'Max: {max_size} GB', rotation=90, color='red', fontsize=10)
plt.text(min_size, plt.ylim()[1] * 0.9, f'Min: {min_size} GB', rotation=90, color='blue', fontsize=10)
plt.show()
