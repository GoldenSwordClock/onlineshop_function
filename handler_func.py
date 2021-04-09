import json
import MySQLdb

database = {'ip':'119.3.215.190','port':3306,'user':'root','password':'mypassword','base':'onlineshop' }

def getHomeHotData():   #获取推荐数据，我是返回一个json数组，建议对销量排序，返回前五
    print('handler_func.py: ','getHomeHotData')
    
    conn = MySQLdb.connect( database['ip'],database['user'],database['password'],database['base'],charset='utf8')
    cur = conn.cursor()
    cur.execute( "select * from goods;" )
    fetch = cur.fetchall()
    result = []
    for item in fetch:
        result.append( {'id':item[0],'name':item[1],'price':item[2],'url':item[3]} )
    print(result)
    return json.dumps(result)

def getHomeRecommendData():
    print('handler_func.py: ','getHomeRecommendData')#获取推荐数据,这时候会传一个page过来,也就是取第几页的数据，我是直接从一个Json文件里面拿数据，每页返回18个数据。
    return ""

