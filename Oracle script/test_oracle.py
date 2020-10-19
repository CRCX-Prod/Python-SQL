import cx_Oracle

#__________________________________________________
#To be simplified
#____________________________________________
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

postConn = cx_Oracle.connect("charles","crich2020","192.168.1.62/ITOWER2")

postQuery = """SELECT * FROM ITOWERDATA.TXN_SITE_DOWN_TICKETS WHERE ROWNUM < 3"""

postColumns = getColumns(postConn,postQuery)
postData = getData(postConn,postQuery)

print(postData)


#Only column name
#postQuery = """SELECT column_name FROM all_tab_cols WHERE table_name = 'TXN_SITE_DOWN_TICKETS'"""