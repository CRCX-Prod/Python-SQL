import psycopg2

#________________________________________
#Array of columns from a Postgre query

def getColumns (connection,query):
 
    cur = connection.cursor()
    cur.execute(query)
 
    query_columns = [desc[0] for desc in cur.description]
    return query_columns

#__________________________________
#Array of data from a Postgre query

def getData (connection,query):
 
    cur = connection.cursor()
    cur.execute(query)

    query_results = cur.fetchall()
    return query_results