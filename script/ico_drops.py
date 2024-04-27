import pandas as pd
import pycountry

# Define a function to convert country codes to country names
def get_country_name(alpha_2):
    try:
        return pycountry.countries.get(alpha_2=alpha_2).name
    except:
        return None

# Load the CSV file with the correct delimiter
df = pd.read_csv('ICO drops - referring domains.csv', delimiter=';')

# Print the first few rows of the dataframe to confirm structure and column names
print(df.head())

# Print the column names to ensure the 'Country' column is present
print(df.columns)

# Strip any potential leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Apply the function to the 'Country' column with the correct case
df['Country'] = df['Country'].apply(get_country_name)

# Print the first few rows to verify the country names have been updated
print(df.head())

# Save the updated dataframe to a new CSV file
df.to_csv('Updated ICO drops - referring domains.csv', index=False)
