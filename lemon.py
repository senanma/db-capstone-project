#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector

    
con = mysql.connector.connect(user='root', password='****',
                                  host='127.0.0.1',
                                  database='LittleLemonDB')
cursor = con.cursor()
cursor.execute("USE LittleLemonDB")

creating_joins ="""
SELECT customerdetails.Names, 
customerdetails.Contacts, 
orders.TotalCost
FROM customerdetails
INNER JOIN orders ON customerdetails.customerID = orders.customerID
WHERE orders.TotalCost > 60;
"""

cursor.execute(creating_joins)
results =cursor.fetchall()
print(cursor.column_names)
print(results)

if con.is_connected():
    cursor.close()
    print("The cursor is closed.")
    con.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed.")

