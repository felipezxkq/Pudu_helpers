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
    calories = doc_dict.get('product_name')
    if calories == None:
        db.collection(u'Products').document(doc.id).delete()
        print("Deleted")
