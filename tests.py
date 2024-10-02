import coffeedb as db
from random import randint
from datetime import datetime

cluster = db.Cluster('data')
testdb = cluster['testdb']

marca = testdb['marca']
producto = testdb['producto']

# marca.create_index('numerorandom')

# for i in range(1, 345):
#     try:
#         marca.insert({'nombre': 'Adidas', 'estatus': 'A', 'numerorandom': randint(1, 10000)})
#     except Exception as e:
#         print(str(e))

start = datetime.now()
# result = marca.select_by_id(1000)
result = marca.select({'_uuid_': 'acabd8c2adc543a0a8e0f41c74905839'})
end = datetime.now()
print(result)
print(len(result))
print(end - start)