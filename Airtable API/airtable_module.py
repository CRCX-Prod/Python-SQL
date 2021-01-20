import os
from pprint import pprint
from airtable import Airtable


def queryAirtable (base,table,view):

    airtable = Airtable(base,table,api_key='key2oMENkcz6kdrIy')
    query = airtable.get_all(view=view,maxRecords=20)
    #query = airtable.get_all(view=view,maxRecords=20)

    return query

def getColumns (query):

    #Process list
    column_step1 = list(query[0].values())
    column_step2 = column_step1[1]
    columns_result = list(column_step2)

    return columns_result


def getData (query):

    
    #Process list
    for x in range(len(query)):

        data_step1 = list(query[x].values())
        data_step2 = data_step1[1]
        dataItem = tuple(data_step2.values())

        #print(dataItem)
        if x==0:
            dataList =(dataItem,)  #For first item
            continue
        dataList = dataList+(dataItem,)
        #dataList = dataList+(dataItem,)

    #dataList = dataList,dataItem
    return dataList


"""
base = 'appIZ8SjK4PI6fDWc'
table = 'Sites'
view = 'Python test'

query = queryAirtable(base,table,view)
test = getColumns (query)
test = getData(query)

print(test)
"""