import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import timeit
# Use a service account
cred = credentials.Certificate('service-account.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create a reference to the cities collection
cities_ref = db.collection(u'Products').stream()


data = {}
data['products'] = []
for doc in cities_ref:
    doc_dict = doc.to_dict()
    data['products'].append(doc_dict)


with open('products.json', 'w', encoding='utf8') as outfile:
    json.dump(obj=data, fp=outfile, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)