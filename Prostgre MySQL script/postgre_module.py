import psycopg2

def getColumns (connection,query):
 
    cur = connection.cursor()
    cur.execute(query)
 
    query_columns = [desc[0] for desc in cur.description]
    return query_columns

def getData (connection,query):
 
    cur = connection.cursor()
    cur.execute(query)

    query_results = cur.fetchall()
    return query_results