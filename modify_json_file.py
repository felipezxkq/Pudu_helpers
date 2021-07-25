import json
from json import encoder

products = []
attributes_list = ["code", "product_name", "brands", "quantity", "categories", "origins", "traces", "serving_size", "additives_n", "ingredients_from_palm_oil_n", "image_url", "image_small_url", "image_front_url"
, "image_ingredients_url", "image_ingredients_small_url", "fat_100g", "omega-9-fat_100g", "carbohydrates_100g", "sugars_100g", "fiber_100g", 
"proteins_100g", "salt_100g", "sodium_100g", "alcohol_100g", "ingredients_text", "nutriscore_score", "nutriscore_grade", "nova_group", "energy-kcal_100g", "energy_100g"]

def get_parameter(parameter, json_object):
    json_object_parameter = json_object.get(parameter)
    if json_object_parameter:
        print(json_object_parameter)
        return json_object_parameter
    else:
        return None


with open('productos_chile.json', encoding="utf8") as json_file:
    data = json.load(json_file)
    for p in data['products']:
        products.append({
            'product_name' : get_parameter('product_name', p),
            'code' : get_parameter('code', p),
            'brands' : get_parameter('brands', p),

        })

with open('productos_chile_modificado.json', 'w', encoding='utf8') as outfile:
    json.dump(obj=products, fp=outfile, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)





        

