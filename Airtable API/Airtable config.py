#Install Pyp airtable

pip install airtable-python-wrapper

import os
from pprint import pprint
from airtable import Airtable

airtable = Airtable('appCeehu9RgHJAPYY','Table 1',api_key='key2oMENkcz6kdrIy')

#print(airtable.get_all(view='Name',sort='Notes'))
#print(airtable.get_all())


airtable.create('Table 1', {"Name":"Test import Python"})