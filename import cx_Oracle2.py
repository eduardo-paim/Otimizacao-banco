import cx_Oracle

# Connect to the Oracle database
conn = cx_Oracle.connect('username/password@database_name:1521/service_name')

# Create a cursor
cur = conn.cursor()

# Define the query
query = """
SELECT * FROM table_name A JOIN table_name B ON A.column_name = B.column_name
"""

# Execute the query
cur.execute(query)

# Fetch the results
results = cur.fetchall()

# Close the cursor
cur.close()

# Disconnect from the database
conn.close()

# Print the results
for row in results:
    print(row)
