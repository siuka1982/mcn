# import http.client
import re
from lxml import etree
import requests


class BloadListCravler:
    headers = {
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7",
        # 'cookie': "main[UTMPUSERID]=guest; main[UTMPKEY]=31163785; main[UTMPNUM]=90483; Hm_lvt_bbac0322e6ee13093f98d5c4b5a10912=1560833564; Hm_lpvt_bbac0322e6ee13093f98d5c4b5a10912=1560840819",
        'referer': "https://www.newsmth.net/nForum/",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'cache-control': "no-cache"
    } 
    domain = 'http://www.newsmth.net'
    base_url=domain +'nForum/section/{}?ajax'
        
    def get_content(self, page_num):
        url=self.base_url.format(page_num)
        response=requests.get(url,headers=self.headers)
        return response.text
        
        

        
    def get_board_list(self,content):
        tree=etree.HTML(content)
        rows=tree.XPath("//table[@class='board-list corner']/tbody/tr")
        # rows=tree.XPath("//*[@id="body"]/div[2]/table/tbody/tr")
        print(rows[0])
    
if __name__ == "__main__":
    blc=BloadListCravler()
    c=blc.get_content(1)
    blc.get_board_list(c)
            

