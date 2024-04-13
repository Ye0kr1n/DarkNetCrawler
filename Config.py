# -*- coding: utf-8 -*-
# @Time    : 2023/3/31 19:51
# @Author  : Ye0kr1n
# @File    : Config.py
# @IDE: PyCharm
# @Email   : None
TorProxyConfig = {
    "http": "socks5h://127.0.0.1:9101",  # Tor代理地址
    "https": "socks5h://127.0.0.1:9101"  # Tor代理地址
}
db_config = {
    "host": "192.168.30.177",
    "user": "root",
    "password": "root",
    "database": "darknet_crawler_info",
    "charset": "utf8mb4"
}
Sys_Cofig = {
    "delete_data_time": "15",
    "crawler_file_mode": "crawler_code"
}
