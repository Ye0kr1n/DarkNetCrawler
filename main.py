# -*- coding: utf-8 -*-
# @Time    : 2023/3/31 19:37
# @Author  : Ye0kr1n
# @File    : Dark_network_trading_market.py
# @IDE: PyCharm
# @Email   : None
import django
import Config, json,threading
module_list = {}
def run_crawler(crawler_info):
    print(crawler_info)
    if crawler_info['IsAlive'] == '1':
        print(f"run alive crawler plug: {crawler_info['Crawler_Files']}")
        with open('./crawler_code/' + crawler_info['Crawler_Files'], "r", encoding='utf-8') as file:
            plugs = file.read()
        print(exec(plugs))

if __name__ == '__main__':
    with open('./crawler_code/crawler.json', 'r', encoding='utf-8') as file:
        # 读取文件内容
        crawler_info = file.read()
    crawler_infos = json.loads(crawler_info)
    print(crawler_infos)
    threads = []
    for c in crawler_infos:
        if crawler_infos[c]['IsAlive'] == '1':
            t = threading.Thread(target=run_crawler, args=(crawler_infos[c],))
            t.start()
            threads.append(t)
    for t in threads:
        t.join()
#        if crawler_infos[c]['IsAlive'] == '1':
#            print(f"run crawler plug:{c}")
#            with open('./crawler_code/'+crawler_infos[c]['Crawler_Files'], "r", encoding='utf-8') as file:
#                plugs = file.read()
#            print(exec(plugs))

#        else:
#            continue
