from flask import Flask, send_file, send_from_directory, request, jsonify, render_template, abort
from Aiwisfin_azure.getData.weather import getWeather
from Aiwisfin_azure.getData.runAIML import runAIML
from Aiwisfin_azure.getData.stock2 import getfixstock
from Aiwisfin_azure.getData.oilPrice import getOilPrice
from Aiwisfin_azure.getData.golden import getGolden
from Aiwisfin_azure.getData.Currency import getCurrency,exchangeBuy
from Aiwisfin_azure.getData.data import getSite,getStock,getStocNum
from Aiwisfin_azure.getData.law import get_Civil, get_constitution,get_criminal,get_Sexual
import re
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from Aiwisfin_azure.getData.wiki import wiki_search
from Aiwisfin_azure import app

import sqlite3 as lite




line_bot_api = LineBotApi('qdLjteAVKJ6iSgHoK9tNFbtt70EZZiDL46zzeYe/oOtYcKVAnpCYdxE0rDJ9qkX2LaXoaJUwI60jdNmPuEE+icH2a3w/vZIoploibUU/e1PVRVP3++KRP5CNknJyuRe0kv8Fy67V3a9ConpTCn9CNwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('47966f59dc72d9968a9f5c1723a42a7c')
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/en")
def index_eng():
    return render_template('1E.html')
@app.route("/chat")
def chat():
    return render_template('index.html')
@app.route("/chat_en")
def chat_eng():
    return render_template('index_en.html')
@app.route("/portfolio")
def portfolio():
    return render_template('2C_1.html')
@app.route("/portfolio_en")
def portfolio_eng():
    return render_template('2E_1.html')

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/statics/<path:path>')
def send_statics(path):
    return send_from_directory('statics', path)

@app.route('/_add_numbers')
def add_numbers():
    query = request.args.get('query')
    query = query.upper()
    query = re.sub('臺','台',query)
    reply = '很抱歉，無法替您解決此問題，建議點選上方Facebook圖示直接與我們聯絡'
    if query !="熱門查詢":
        con = lite.connect('mydatabase.sqlite')
        cur = con.cursor()
        sql1 = cur.execute('select * from HotValue where input=?',[query]).fetchone()
        if sql1 != None:
            cur.execute('update HotValue set hot=? where input=?',(sql1[1]+1,query))
        else:
            cur.execute('insert into HotValue(input,hot)values(?,?)',(query,1))
        con.commit()
        con.close()
    
    try:
        if(re.search('氣溫',query)!=None):
            regex = re.compile(getSite())
            query = regex.search(query)
            reply=getWeather(query.group(1),0)
        elif(re.search('公告',query)!=None):
            reply="1.目前所有服務修復完畢正常運作中<br>\
                   2.Facebook機器人功能受限於官方相關新規定而無法對外正式發佈，敬請見諒"
        elif(re.search('熱門查詢',query)!=None):
             con = lite.connect('mydatabase.sqlite')
             cur = con.cursor()
             sql1 = cur.execute('select input from HotValue order by hot desc limit 10').fetchall()
             result = re.sub(",\)","<br>",str(sql1))
             result = re.sub(","," ",result)
             result = re.sub("\["," ",result)
             result = re.sub("\]"," ",result)
             result = re.sub("\'"," ",result)
             result = re.sub("\("," ",result)
             result = re.sub("\)"," ",result)
             reply = "熱門查詢排行榜:<br>"+result
             
             con.close()
            
        elif(re.match('學說話管理員',query)!=None):
            con = lite.connect('mydatabase.sqlite')
            cur = con.cursor()
            ret = cur.fetchall()            
            cur.execute('select * from qa ')
            con.close()
            reply= re.sub(',','<br>',str(ret))
        elif(re.search('學說話',query)!=None and query!="公告"):
            try:
                con = lite.connect('mydatabase.sqlite')
                cur = con.cursor()
                sqlinset = 'insert into qa(question,answer)values(?,?)'
                query = query.split(";")
                ret=query
                cur.execute(sqlinset,ret[1:])
                con.commit()
                con.close()
                reply="學會了! 問題:"+query[1]+" 回答:"+query[2]
            except Exception as e:
                
                 reply='請以;分隔問答(EX:學說話;你好嗎;我很好)'
       
        elif(re.search('(我姓|我叫|我是)',query)!=None):

            reply=query[2]+'先生(女士)您好!歡迎使用Aiwsifin智慧客服，請問需要哪些幫助呢?'
        elif(re.search('(先生|小姐)',query)!=None):
            reply=query[0]+'先生(女士)您好!歡迎使用Aiwsifin智慧客服，請問需要哪些幫助呢?'
        elif(re.search('投資組合',query)!=None):
            reply='請直接點選上方的「投資組合」選項，完成問卷後即可得知您專屬的投資組合建議'
        elif(re.search('ETF',query)!=None):
            reply ='是一種在證券交易所交易，提供投資人參與指數表現的指數基金。'
        elif(re.search('證明',query)!=None):
            reply='<img src="https://cdn.discordapp.com/attachments/461176037397626880/489404601863503912/unknown.png" alt="https://cdn.discordapp.com/attachments/461176037397626880/489404601863503912/unknown.png" title="圖表">由圖表可顯示我們預測的價格與實際的價格相當接近'
        elif(re.search('辦信用卡',query)!=None):
            reply ='年滿二十歲，請提供身分證影本、收入財力證明，至本行各分行辦理。'
        elif(re.search('查帳單金額',query)!=None):
            reply ='網路銀行：登入網路銀行→信用卡→帳單總覽→可查詢近3個月的帳單明細。<br>\
                    行動銀行：登入行動銀行→帳務服務→信用卡→帳單總覽→可查詢近3個月的帳單明細。<br>\
                    電話語音：撥打語音專線(02)2182-1313→按快速碼”144”→依語音指示輸入正卡人信用卡卡號及身分證字號→可查詢最近一期帳單金額。<br>\
                    客服中心：致電客服中心(02)2182-1313→1信用卡服務→0→輸入身分證字號→轉接專人查詢'
        elif(re.search('繳款方式',query)!=None):
            reply ='年自動轉帳<br>四大便利商店繳款<br>網路銀行繳款<br>電話銀行繳款<br>臨櫃繳款<br>郵局繳款<br>WebATM繳款<br>匯款<br>e-bill全國繳費網<br>支票繳款<br>信用卡線上繳款'
        elif(re.search('開卡',query)!=None):
            reply ='網路開卡：至本行官網信用卡開卡專區進行開卡。<br>致電客服中心(02)2182-1313→1信用卡服務→0→輸入身分證字號→轉接專人開卡。'
        elif(re.search('款項疑問',query)!=None):
            reply ='收單機構係彙總您的刷卡簽帳單後向本行請款的機構，若您對某筆消費明細有疑問時，請務必於當期規定繳款截止日起前，通知本行代為向收單機構申請複查，逾期本行則無法再為您提出申請，亦不得以任何理由請求退款。因簽帳單皆留存於收單機構，調閱簽帳單需較長的作業時間，國內調單時程約需二個星期至一個月，國外調單時程約需一至一個半月。如您於期限內提出申請調單，經確認係為您本人消費，本行則代收調閱簽帳單手續費，國內每筆50元，國外每筆為100元。'
        elif(re.search('民法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_Civil(query.group())
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
        elif(re.search('刑法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_criminal(query.group())
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
        elif(re.search('憲法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_constitution(query.group())
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
           
        elif(re.search('天氣',query)!=None):
            try:
                regex = re.compile(getSite())
                query = regex.search(query)
                reply=getWeather(query.group(1),2)
            except Exception as e:
                reply="請搭配地點查詢(範例:台北天氣)"
        elif(re.search("大盤",query)!=None):
            if(re.search('(成交|漲跌|漲幅|金額)',query)!=None):
                    select ={'成交':0,'漲跌':1,'漲幅':2,'金額':3,} 
                    regex = re.compile('(成交|漲跌|漲幅|金額)')
                    query = regex.search(query)
                    reply = getTse(select[query.group()])
            else:
                reply= getTse(4)

        elif(re.search(getStock(),query)!=None):
            stock = getStocNum()
            regex = re.compile(getStock())
            stockname = regex.search(query)
            if (re.search('(市|買|賣|成交|收|開|高|低)',query)!=None):
                regex = re.compile('(市|買|賣|成交|收|開|高|低)')
                select ={'市':1,'買':2,'賣':3,'成交':4,'收':5,'開':6,'高':7,'低':8} 
                stockCode =regex.search(query)
                reply =  getfixstock(stock[stockname.group(0)],select[stockCode.group(0)])
            else:
                reply = getfixstock(stock[stockname.group(0)],0)
        
        elif(re.search('(美金|日圓|日元|人民幣|英鎊|歐元|匯率)',query)!=None):
            if(re.search('(買)',query)!=None):
                regex = re.compile('\d+')
                money = regex.search(query)
                regex = re.compile('(美金|日圓|日元|人民幣|英鎊|歐元)')
                c = regex.search(query)
                reply = exchangeBuy(c.group(),float(money.group()))
            else:
              
                regex = re.compile('(美金|日圓|日元|人民幣|英鎊|歐元)')
                if(regex.search(query)!=None):
                        query = regex.search(query)
                        reply = getCurrency(query.group(1))
                else:
                        reply="請確認幣別是否在目前提供的查詢之中(美金、日圓、人民幣、英鎊、歐元)"
           
        elif(re.search('\d',query)!=None):
            regex = re.compile('\d+')
            stocknum=regex.search(query)
            if (re.search('(市|買|賣|成交|收|開|高|低)',query)!=None):
                regex = re.compile('(市|買|賣|成交|收|開|高|低)')
                select ={'市':1,'買':2,'賣':3,'成交':4,'收':5,'開':6,'高':7,'低':8,'漲跌':9} 
                stockCode =regex.search(query)
                reply =  getfixstock(stocknum.group(),select[stockCode.group(0)])
            else:
                reply = getfixstock(stocknum.group(),0)
        elif(re.search('油價',query)!=None):
            reply = getOilPrice()
    
        elif(re.search('黃金',query)!=None):
            reply = getGolden()
       
            
        else:
            con = lite.connect('mydatabase.sqlite')
            cur = con.cursor()
            cur.execute('select * from qa where question =? order by Random()',[query])
            ret = cur.fetchone()
            
            if ret != None:
               reply=ret[1]
            else:
                query = query.upper()
                response = runAIML(query)
                if response != '':
                    reply = response
                else:
                    if wiki_search(query)!=None:
                        reply = wiki_search(query)
                    else:
                        raise Exception
            con.close()
            
            
        
    except Exception as e:
        print(e)
        pass
    return jsonify(result=reply)
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply = "很抱歉，無法替您解決此問題，建議至Facebook粉絲專業直接與我們聯絡"
    query = event.message.text
    query = query.upper()
    query = re.sub('臺','台',query)
    if query !="熱門查詢":
        con = lite.connect('mydatabase.sqlite')
        cur = con.cursor()
        sql1 = cur.execute('select * from HotValue where input=?',[query]).fetchone()
        if sql1 != None:
            cur.execute('update HotValue set hot=? where input=?',(sql1[1]+1,query))
        else:
            cur.execute('insert into HotValue(input,hot)values(?,?)',(query,1))
        con.commit()
        con.close()
    
    if(re.search('氣溫',query)!=None):
        regex = re.compile('(台北|新北|台中|高雄|台南|桃園|基隆|新竹|雲林|南投|嘉義|苗栗|彰化|花蓮|台東|澎湖|宜蘭)')
        query = regex.search(query)
        reply=getWeather(query.group(1),0)
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))
    elif(re.search('天氣',query)!=None):
        try:
            regex = re.compile('(台北|新北|台中|高雄|台南|桃園|基隆|新竹|雲林|南投|嘉義|苗栗|彰化|花蓮|台東|澎湖|宜蘭)')
            query = regex.search(query)
            reply=getWeather(query.group(1),2)
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply))
        except Exception as e:
            reply="請搭配地點做查詢"
    
    elif(re.search('民法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_Civil(query.group())
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    elif(re.search('刑法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_criminal(query.group())
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    elif(re.search('憲法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_constitution(query.group())
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    elif(re.search('性侵',query)!=None):
        reply = TemplateSendMessage(
            alt_text='性侵害相關條文',
            template=ButtonsTemplate(
                title='常見觸犯條文',
                text='點擊查看詳細條文內容',
                thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                actions=[
                    MessageTemplateAction(
                        label='刑法:第 227 條',
                        text='刑法:第 227 條 （未成年人性侵害）'
                    ),
                    MessageTemplateAction(
                        label='刑法:第 228 條',
                        text='刑法:第 228 條 （利用權勢性交或猥褻罪）'
                    ),
                    MessageTemplateAction(
                        label='刑法:第 332 條',
                        text='刑法:第 332 條 （強盜結合強制性交罪）'
                    ),
                    MessageTemplateAction(
                        label='刑法:第 348 條',
                        text='刑法:第 348 條 （擄人勒贖結合強制性交罪）'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, reply)
    elif(re.search("大盤",query)!=None):
        if(re.search('(成交|漲跌|漲幅|金額)',query)!=None):
            select ={'成交':0,'漲跌':1,'漲幅':2,'金額':3,} 
            regex = re.compile('(成交|漲跌|漲幅|金額)')
            query = regex.search(query)
            reply = getTse(select[query.group()])
        else:
            reply= getTse(4)
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))
    elif(re.search(getStock(),query)!=None):
        stock = getStocNum()
        regex = re.compile(getStock())
        stockname = regex.search(query)
        if (re.search('(市|買|賣|成交|收|開|高|低)',query)!=None):
            regex = re.compile('(市|買|賣|成交|收|開|高|低)')
            select ={'市':1,'買':2,'賣':3,'成交':4,'收':5,'開':6,'高':7,'低':8} 
            stockCode =regex.search(query)
            reply =  getfixstock(stock[stockname.group(0)],select[stockCode.group(0)])
        else:
            reply = getfixstock(stock[stockname.group(0)],0)
      
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))
   
    elif(re.search('油價',query)!=None):
        reply = getOilPrice()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    
    elif(re.search('黃金',query)!=None):
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=getGolden()))
    elif(re.search('(美金|日圓|日元|人民幣|英鎊|歐元)',query)!=None):
        if(re.search('(買)',query)!=None):
            regex = re.compile('\d+')
            money = regex.search(query)
            regex = re.compile('(美金|日圓|日元|人民幣|英鎊|歐元)')
            c = regex.search(query)
            reply = exchangeBuy(c.group(),float(money.group()))
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
        else:
                regex = re.compile('(美金|日圓|日元|人民幣|英鎊|歐元)')
                query = regex.search(query)
                reply = getCurrency(query.group(1))
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    elif(re.search('\d',query)!=None):
        regex = re.compile('\d+')
        stocknum=regex.search(query)
        if (re.search('(市|買|賣|成交|收|開|高|低)',query)!=None):
            regex = re.compile('(市|買|賣|成交|收|開|高|低)')
            select ={'市':1,'買':2,'賣':3,'成交':4,'收':5,'開':6,'高':7,'低':8} 
            stockCode =regex.search(query)
            reply =  getfixstock(stocknum.group(),select[stockCode.group(0)])
        else:
            reply = getfixstock(stocknum.group(),0)
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))
    else:
        query = query.upper()
        response = runAIML(query)
        if response != '':
            reply = response
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
        else:
            if wiki_search(query)!=None:
                reply = wiki_search(query)
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))

         
          
if __name__ == "__main__":
    app.run(
        port=5555)
