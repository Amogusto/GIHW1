import json
import vk

access_token = '***'
session = vk.Session(access_token = access_token, scope='Groups')
vk_api = vk.API(session)
response = api.groups.get(user_id=334155127)

with open('groups.json', 'w') as file:
    json.dump(response, file)
print(response)


