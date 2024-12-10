import psycopg2
import pandas as pd

# PostgreSQL connection details
host = 'localhost'        # e.g., localhost or an IP address
port = '5432'             # default PostgreSQL port
dbname = 'CHIP CHIP'    # the name of your PostgreSQL database
user = 'postgres'        # your database username
password = 'Samin2384' # your database password

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# SQL query to select the data you want
query = "SELECT * FROM product_variation_prices;"  # Replace with your query

# Fetch the data and load it into a pandas DataFrame
df = pd.read_sql(query, conn)

# Close the cursor and connection
cursor.close()
conn.close()

# Save the DataFrame to a CSV file
df.to_csv('./Data/product_variation_prices.csv', index=False)  # Replace with desired file name
print("Data saved to 'product_variation_prices.csv'")