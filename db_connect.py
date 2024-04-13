# -*- coding: utf-8 -*-
# @Time    : 2023/3/31 21:30
# @Author  : Ye0kr1n
# @File    : db_connect.py
# @IDE: PyCharm
# @Email   : None
import pymysql
import Config,datetime
# 连接数据库

cnx = pymysql.connect(
    host=Config.db_config['host'],
    user=Config.db_config['user'],
    password=Config.db_config['password'],
    database=Config.db_config['database']
)

# 创建游标对象
#cursor = cnx.cursor()

# 插入数据
def insert_darknet_crawler_data(cnx,Domain,URL,ReleaseTime,Title,Content,add_time):
    cursor = cnx.cursor()
    insert_query = "INSERT INTO crawler_info (domain,url,release_time,title,content,add_time) VALUES (%s,%s,%s,%s,%s,%s)"
    insert_values = (Domain,URL,ReleaseTime,Title,Content,add_time)
    cursor.execute(insert_query, insert_values)
    cnx.commit()
    cursor.close()
    #cnx.close()
# 查询数据
def select_darknet_crawler_content_data(cnx,values):
    cursor = cnx.cursor()
    select_query = "SELECT * FROM crawler_info WHERE content=%s"
    select_values = values
    cursor.execute(select_query,select_values)
    rows = cursor.fetchall()
#    for row in rows:
 #       print(row)
    #cnx.close()

    return [rows]
# 更新数据
def update_darknet_crawler_data():
    cursor = cnx.cursor()
    update_query = "UPDATE crawler_info SET column1 = %s WHERE column2 = %s"
    update_values = ("new_value1", "value2")
    cursor.execute(update_query, update_values)
    cnx.commit()
    cursor.close()
    cnx.close()


# 删除15天前的数据
def clear_darknet_15_crawler_data():
    current_date = datetime.date.today()
    date_n_days_ago = current_date - datetime.timedelta(days=Config.Sys_Cofig['delete_data_time'])
    cursor = cnx.cursor()
    delete_query = "DELETE FROM crawler_info WHERE add_time < %s"
    cursor.execute(delete_query, (date_n_days_ago,))
    cnx.commit()
    cursor.close()
    cnx.close()

def delete_darknet_crawler_data(sits):
    sites=sits
    cursor = cnx.cursor()
    delete_query = "DELETE FROM crawler_info WHERE domain = %s"
    cursor.execute(delete_query, (sites,))
    cnx.commit()
    cursor.close()
    cnx.close()
# 关闭游标和连接
