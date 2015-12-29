import json

import httplib2

nActs = 0

for page in range(1, 46):
    h = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
    resp, content = h.request("https://api-v3.mojepanstwo.pl/dane/sejm_druki?_type=objects&page=" + str(page), "GET")
    # print(resp)
    # print(content)

    allActs = json.loads(content.decode('ascii'))
    for act in allActs['Dataobject']:
        nActs += 1
        print(act['data']['sejm_druki.tytul'])

print(nActs)
