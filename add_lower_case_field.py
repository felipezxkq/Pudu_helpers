import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import timeit
# Use a service account
cred = credentials.Certificate('service-account.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create a reference to the cities collection
cities_ref = db.collection(u'Products').stream()

for doc in cities_ref:
    #print(f'{doc.id} => {doc.to_dict()}')
    doc_dict = doc.to_dict()
    prod_name = doc_dict.get('product_name')
    prod_name_lc = prod_name.lower()

    lower_case_name = doc_dict.get('product_name_lc')
    
    if lower_case_name is None:
        db.collection(u'Products').document(doc.id).update({"product_name_lc" : prod_name_lc})
        print("Updated "+prod_name+" to "+prod_name_lc)
