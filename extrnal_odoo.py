import xmlrpc.client
url = "http://localhost:8069"
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(f" {common.version()}")

db = "Cabinet"
username = "admin"
password = "admin"
uid = common.authenticate(db, username, password, {})
print(f"Uid {uid}")