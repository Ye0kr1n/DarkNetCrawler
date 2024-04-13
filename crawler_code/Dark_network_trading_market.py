# -*- coding: utf-8 -*-
# @Time    : 2023/3/31 19:37
# @Author  : Ye0kr1n
# @File    : Dark_network_trading_market.py
# @IDE: PyCharm
# @Email   : None
from typing import List, Any
from bs4 import BeautifulSoup
import requests, Config, pymysql, db_connect, datetime,logging
Dark_network_trading_market=[]
website_info = {}
proxies = Config.TorProxyConfig
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='/source/DarkNetCrawler/logs/Dark_network_trading_market_py.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
#try:
#    db_connect.delete_darknet_crawler_data("xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion")

#except:
#    print("历史数据清空失败")
#    logging.warning("")

html = requests.get("http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/index.php",
                        proxies=proxies).text
soup = BeautifulSoup(html, 'html.parser')
link_elements = soup.find_all('a', {'class': 'link_text_class'})
link_lists: List[Any] = []
for link_element in link_elements:
    link_element_text = link_element.text.replace('♅', '').replace('♛', '').replace('\n', '').replace('\r\n','').replace('        ', '').replace('♆', '')
    link_url = link_element['href']
    # print(f"Text: {link_element_text}, URL: http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion{link_url}")
    # print(f"spider link:http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion{link_url}")
    link_lists.append("http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion" + link_url)
    website_info['http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion' + link_url] = {
        'url': 'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion' + link_url,
        'domain': 'xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion',
        'title': link_element_text
        }
    ad_elements = soup.find_all('a', {'class': 'link_index_ad'})
for ad_element in ad_elements:
    ad_element_text = ad_element.text.replace('♅', '').replace('♆', '').replace('\r\n', '').replace('\n', '').replace('        ', '')
    ad_link_url = ad_element['href']
        # print(f"Text:{ad_element_text}, URL:http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion{ad_link_url}")
        # print(f"spider link:http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion{ad_link_url}")
    link_lists.append("http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion" + ad_link_url)
    website_info['http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion' + ad_link_url] = {
        'url': 'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion' + ad_link_url,
        'domain': 'xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion',
        'title': ad_element_text
        }
    print(f"[Dark_network_trading_market.py]{datetime.datetime.now()}link_list:\r\n{link_lists}")
    print(f"[Dark_network_trading_market.py]{datetime.datetime.now()}website_info:\r\n{website_info}")
cnx = pymysql.connect(
    host=Config.db_config['host'],
    user=Config.db_config['user'],
    password=Config.db_config['password'],
    database=Config.db_config['database']
)
for i in link_lists:
    infos=""
    try:
        html_body = requests.get(i, proxies=proxies).text
        soup = BeautifulSoup(html_body, 'html.parser')
        content = soup.t.get_text(separator=' ', strip=True)
         # print(f"Link:{i}  Content:{content}")
        website_info[i]['content'] = content
        soup_xml = BeautifulSoup(html_body, 'lxml')
        div_element = soup_xml.find('div', class_='div_goods_post_inner')
        div_text = div_element.text.strip()
        time_text = div_text.split("时间: ")[1]
        website_info[i]['time'] = time_text
        print( f"\r\n[Dark_network_trading_market.py] spider darknet info:\r\ntitle:{website_info[i]['title']}\r\ntime:{website_info[i]['time']}\r\nDomain:{website_info[i]['domain']}\r\nURL:{website_info[i]['url']}\r\ncontent:{website_info[i]['content']}")
        infos=db_connect.select_darknet_crawler_content_data(cnx,website_info[i]['content'])
        #print(infos)
        try:
            if len(infos[0][0]) > 1:                                                                                           #去重操作
                print(f"{website_info[i]['title']} 已存在")
            else:
                db_connect.insert_darknet_crawler_data(cnx, website_info[i]['domain'], website_info[i]['url'],
                                                       website_info[i]['time'], website_info[i]['title'],
                                                       website_info[i]['content'], datetime.datetime.now())
        except IndexError as e:
            db_connect.insert_darknet_crawler_data(cnx, website_info[i]['domain'], website_info[i]['url'],
                                                   website_info[i]['time'], website_info[i]['title'],
                                                   website_info[i]['content'], datetime.datetime.now())
        # insert_darknet_crawler_data(cnx, Domain, URL, ReleaseTime, Title, Content, add_time)
    except Exception as e:
        print(f"Error occurred while processing {i}: {e}")
cnx.close()

