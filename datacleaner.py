import pandas as pd

# Load the CSV file (update the filename as needed)
filename = 'ecg.csv'
df = pd.read_csv(filename)

# Step 1: Remove rows where the first column is empty
df = df[df.iloc[:, 185].notna()]

# Step 2: Fill column 189 if empty and column 188 has value
# (Note: column indices in pandas are 0-based, so 188 => index 187, 189 => index 188)
col_188 = df.columns[187]
col_189 = df.columns[188]

# Apply logic row-wise
df.loc[df[col_188].notna() & df[col_189].isna(), col_189] = 1

# Save the modified CSV
df.to_csv('modified_' + filename, index=False)

print("CSV processing complete. Saved as:", 'labeled ' + filename)
