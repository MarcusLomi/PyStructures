'''
Created on Jun 8, 2016

@author: Marcus
'''
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '42c1770d2a8d4312b5c849a46a53d78a',
}

params = urllib.parse.urlencode({
    # Request parameters
    'seasonId': '{string}',
})

try:
    conn = http.client.HTTPSConnection('www.haloapi.com')
    conn.request("GET", "/stats/h5/servicerecords/arena?players=MOmonii&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

string_dat=str(data)
data_dict=dict(data)
string_dat=string_dat.split("{")
fw=open('haloStat.txt',"w")
for line in string_dat:
    fw.write(line+"\n")
fw.close()