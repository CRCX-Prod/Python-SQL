#Install Pyp airtable

pip install airtable-python-wrapper

import os
from pprint import pprint
from airtable import Airtable

airtable = Airtable('appmDMFeyQhBLXMmO','Contact list',api_key='key2oMENkcz6kdrIy')

print(airtable.get_all(view='Name',sort='Reference'))
