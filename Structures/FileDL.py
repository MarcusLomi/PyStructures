'''
Created on Jun 8, 2016

@author: Marcus
'''
from urllib import request
goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=5&e=8&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

'''First tell python to connect to the internet
'''
def download_stock_data(csv_url):
    response=request.urlopen(goog_url)
    csv=response.read()
    csv_str = str(csv)
    lines=csv_str.split("\\n")
    dest_url= r'goog.csv'
    fx=open(dest_url,"w")
   
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_stock_data(goog_url)
    