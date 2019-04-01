import requests
from bs4 import BeautifulSoup
import re

def getfixstock(code,n):
    
    try:
         r = requests.get('https://tw.stock.yahoo.com/q/q?s='+str(code))
         soup = BeautifulSoup(r.text, 'html.parser')
         tables = soup.find_all('table')
         row = tables[5].find_all('td')[:-1]
         for item in row:
              row[row.index(item)] = item.text.strip()
         stock=re.sub("加到投資組合","",row[0])
         if row[1]=='':
             return "查無該股"
         elif n==0:
             return(stock+"各項資訊如下:\n"
                   '市價:'+row[2]+'\n'
                    '買價:'+row[3]+'\n'
                    '賣價:'+row[4]+'\n'
                    '成交量:'+row[6]+'\n'
                    '前日收盤價:'+row[7]+'\n'
                    '開盤:'+row[8]+'\n'
                    '最高:'+row[9]+'\n'
                    '買低:'+row[10]+'\n'
                     )
         elif n==1:
             return(stock+'市價:'+row[2])
         elif n==2:
             return(stock+'買價:'+row[3])
         elif n==3:
             return(stock+'賣價:'+row[4])
         elif n==4:
             return(stock+'成交量:'+row[6])
         elif n==5:
             return(stock+'前日收盤價:'+row[7])
         elif n==6:
             return(stock+'開盤:'+row[8])
         elif n==7:
             return(stock+'最高:'+row[9])
         elif n==8:
             return(stock+'最低:'+row[10])
        
       
        
             
    except Exception :
        return('查無該股')
        



if __name__ == "__main__":
    print("最後維護時間為於2018/12/4 12:05", getfixstock(2330,0))
   

