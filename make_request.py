import json
import requests

url = "http://127.0.0.1:9000/" # if docker and exposed to 9000
# url = "http://127.0.0.1:5000/" # if using flask

data = ["Amputation is the removal of a limb by trauma, medical illness, or surgery. As a surgical measure, it is used to control pain or a disease process in the affected limb, such as malignancy or gangrene. In some cases, it is carried out on individuals as a preventive surgery for such problems. A special case is that of congenital amputation, a congenital disorder, where fetal limbs have been cut off by constrictive bands. In some countries, amputation is currently used to punish people who commit crimes.[1][2][3][4] Amputation has also been used as a tactic in war and acts of terrorism; it may also occur as a war injury. In some cultures and religions, minor amputations or mutilations are considered a ritual accomplishment.[5][6][7] When done by a person, the person executing the amputation is an amputator.[8][9] In the US, the majority of new amputations occur due to complications of the vascular system (the blood vessels), especially from diabetes. Between 1988 and 1996, there were an average of 133,735 hospital discharges for amputation per year in the US.[10] In 2005, just in the US, there were 1.6 million amputees.[11] In 2013, the US had 2.1 million amputees. Approximately 185,000 amputations occur in the United States each year. In 2009, hospital costs associated with amputation totaled more than $8.3 billion.[12] There will be an estimated 3.6 million people in the US living with limb loss by 2025.[11]"]

jdata = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

# request and print return
r = requests.post(url, data=jdata, headers=headers)
print(r, r.text)

