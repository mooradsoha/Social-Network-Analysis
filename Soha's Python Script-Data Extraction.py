import requests

headers = {
    "accept": "application/json, text/plain, /",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "Cookie": "visid_incap_662566=ZAKfrn2BRFKnVozHPKfn5RW0XWUAAAAAQUIPAAAAAABWjk5ZSG2RUqnBq/aieWkw; _ga=GA1.2.136790598.1698897787; _ga_7ZZWT14N79=GS1.1.1699562965.5.1.1699563597.0.0.0; _hjSessionUser_1674280=eyJpZCI6ImQyMTNhOTYzLTYwOGEtNTJkMi04ZjRjLTYzZjVhOTlmNTQ0MCIsImNyZWF0ZWQiOjE2OTg4OTc3OTEwOTUsImV4aXN0aW5nIjp0cnVlfQ==; _gac_UA-109253606-1=1.1699537256.Cj0KCQiAo7KqBhDhARIsAKhZ4uiic3PPKr3CczXHarPdf-Jp-HFkfwFpAcN3Mrz9ZdHBJACyKUmJOdQaAixbEALw_wcB; UN_Disclaimer=accepted; nlbi_662566_2350111=F8caEiRACluL95z3kRho8wAAAADEbDFjtruM5GEvpFz8RwLH; incap_ses_256_662566=o6SjB2alsyAhEB2esH+NA3xJZGUAAAAAe0R0IUlGPdUpS7cDEFa/8A=="
}
body = '{"take":150,"skip":0,"searchText":"","reportingCycle":{"years":[]},"hasProgress":false,"progressTracking":{"goals":false,"targets":false,"decisionMakingArrangement":false,"monitoringArrangements":false,"dedicatedStaff":false,"budget":false,"includeActionsUndertaken":false,"actionsUndertaken":{"keyAchivements":false,"increaseInAmbition":false,"supportToNDC":false,"nationalPrioritiesAlignment":false},"deliverablesAndOutputs":false,"includeChallengesAndOpportunities":false,"challengesAndOpportunities":{"keyChallenges":false,"keyOpportunities":false}},"sorting":0}'
r = requests.post("https://climateaction.unfccc.int/apiv2/initiative/list", headers=headers, data=body)
res = r.json()

initiatives = res["initiatives"]
print(len(initiatives))

for i in initiatives:
    id = i["id"]
    headers = {
    'Accept': 'application/json, text/plain, /',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'visid_incap_662566=ZAKfrn2BRFKnVozHPKfn5RW0XWUAAAAAQUIPAAAAAABWjk5ZSG2RUqnBq/aieWkw; _ga=GA1.2.136790598.1698897787; _ga_7ZZWT14N79=GS1.1.1699562965.5.1.1699563597.0.0.0; _hjSessionUser_1674280=eyJpZCI6ImQyMTNhOTYzLTYwOGEtNTJkMi04ZjRjLTYzZjVhOTlmNTQ0MCIsImNyZWF0ZWQiOjE2OTg4OTc3OTEwOTUsImV4aXN0aW5nIjp0cnVlfQ==; _gac_UA-109253606-1=1.1699537256.Cj0KCQiAo7KqBhDhARIsAKhZ4uiic3PPKr3CczXHarPdf-Jp-HFkfwFpAcN3Mrz9ZdHBJACyKUmJOdQaAixbEALw_wcB; UN_Disclaimer=accepted; nlbi_662566_2350111=F8caEiRACluL95z3kRho8wAAAADEbDFjtruM5GEvpFz8RwLH; incap_ses_256_662566=o6SjB2alsyAhEB2esH+NA3xJZGUAAAAAe0R0IUlGPdUpS7cDEFa/8A==',
    'Pragma': 'no-cache',
    'Referer': f'https://climateaction.unfccc.int/Initiatives?id={id}',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
    }
    body = '{"take":200,"skip":0,"progressTracking":{},"engagementType":{"includeInitiativeParticipations":true,"commitments":{"emissionReduction":{}}},"cooperativeInitiatives":{"cooperativeInitiativeIds":[' + str(id) + ']},"sorting":0,"actorsType":{"includeCountries":true}}'

    r = requests.post('https://climateaction.unfccc.int/apiv2/actor/list', headers=headers, data=body)
    res = r.json()
    stats = res["stats"]
    actors = res["actors"]
    totalCount = stats['totalCount']
    print(stats)
    countriesCount = stats['countriesStats']['count'] if stats['countriesStats'] else 0
    for actor in actors:
        print(actor)
        break

    
## stats
# {
#  'totalCount': 26, 
#  'worldRegionsCount': 6, 
#  'countriesCount': 26,
#  'countriesStats': {
#      'count': 26, 
#      'worldRegionsCount': 6
#     }, 
#  'citiesStats': {
#     'count': 0, 
#     'population': 0
#  }, 
#  'regionsStats': {
#     'count': 0, 
#     'population': 0
#  }, 
#  'organizationsStats': {
#     'count': 0, 
#     'countriesCount': 0
#  }, 
#  'investorsStats': {'count': 0, 'countriesCount': 0}, 
#  'companiesStats': {'count': 0, 'sectorsCount': 0}, 
#  'initiativesStats': None
# }
## actors
# {
#     'id': 109, 
#     'publicId': 'CIP-7', 
#     'initiativeName': 'Bonn Challenge', 
#     'statement': '', 
#     'climteFocus': 'Equally mitigation and adaptation/resilience', 
#     'description': 'The Bonn Challenge is a global goal to bring 150 million hectares of degraded and deforested landscapes into restoration by 2020 and 350 million hectares by 2030', 
#     'isNew': False, 
#     'addedDate': None
#  }, 