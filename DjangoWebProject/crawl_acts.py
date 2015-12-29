import json

import httplib2

from app.models import Act


def crawler(max_pages=1):
    for page in range(1, max_pages):
        print("PAGE " + str(page))
        h = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
        resp, content = h.request("https://api-v3.mojepanstwo.pl/dane/sejm_druki?_type=objects&page=" + str(page),
                                  "GET")

        all_acts = json.loads(content.decode('ascii'))
        for act in all_acts['Dataobject']:
            id_act = act['data']['sejm_druki.numer']
            title_act = act['data']['sejm_druki.tytul']
            url_act = act['mp_url']
            text = "  ID: " + str(id_act)
            if not Act.objects.filter(act_id=id_act).exists():
                a = Act(act_id=id_act, title=title_act, url=url_act)
                a.save()
                text += " + CREATED"
            else:
                text += " - EXISTS"
            print(text)
