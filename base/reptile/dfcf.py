#-*-coding:utf-8-*-  
''''' 
Created on 2017年3月17日 
@author: lavi 
'''  
import requests  
from bs4 import BeautifulSoup  
import bs4  
import re  
import traceback  
from setuptools.package_index import HREF  
def getHTMLText(url,code="utf-8"):  
    try:  
        r = requests.get(url,timeout=30)  
        r.raise_for_status  
        #r.encoding = r.apparent_encoding  
        r.encoding = code #编码识别优化  
        return r.text  
    except:  
        return ""  
''''' 
从东方财富网获取股票代码列表 
'''  
def getStockList(stock_list,stock_list_url):  
    html= getHTMLText(stock_list_url,"GB2312")  
    soup = BeautifulSoup(html,"html.parser")  
    a = soup.find_all("a")  
    for i in a:  
        try:  
            href = i.attrs["href"] #相当于i.get("href")   
            stock_list.append(re.findall(r's[zh]\d{6}',href)[0])  
        except:  
            continue  
''''' 
根据东方财富网获取的股票代码，从百度股票获取个股的信息 
百度股票上显示个股信息的url的前缀是相同的，后缀是股票代码 
'''  
def getStockinfo(stock_list,stock_info_url,output_file):  
    count = 0  
    for stockCode in stock_list:  
        html = getHTMLText(stock_info_url+stockCode+".html")  
        try:  
            if html == "":  
                continue  
            infoDict={}  
            soup = BeautifulSoup(html,"html.parser")  
            stockInfo = soup.find("div",attrs={'class':'stock-bets'})  
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]  
            infoDict.update({"股票名称":name.text.split()[0]})  #Python 字典(Dictionary) update() 函数把一个字典dict2的键/值对更新到一个新的字典dict里。  
              
            key_list = stockInfo.find_all("dt")  
            value_list = stockInfo.find_all("dd")  
            for i in range(len(key_list)):  
                key = key_list[i].text #也可以使用.string？  
                value = value_list[i].string  
                infoDict[key]=value  
            with open(output_file, "a", encoding="utf-8") as f:  
                f.write(str(infoDict)+"\n")  
                count = count+1  
                print("\r当前进度：{:.2f}%".format(count*100/len(stock_list)),end="")  
                #转义符\r,一行打印结束后将光标提到该行的头部，在这一行重新输出内容，覆盖原来的内容，实现不换行的进度条显示  
        except:  
            traceback.print_exc()  
            count = count+1  
            print("\r当前进度：{:.2f}%".format(count*100/len(stock_list)),end="")  
            continue          
def main():  
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"  
    stock_info_url = "https://gupiao.baidu.com/stock/"  
    output_file = "e://BaiduStock1.txt"  
    stock_list=[]  
    getStockList(stock_list,stock_list_url)  
    getStockinfo(stock_list,stock_info_url,output_file)  
      
main()  