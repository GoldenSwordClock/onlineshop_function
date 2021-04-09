#from DBconnect import *
from writeHeader import *
import json
#import MySQLdb
import base64
from urllib import parse
from handler_func import *

config = { 'database':{'ip':'localhost','port':3306 }  }

def unpack_instr( pack_instr ):
    pass

class App:
    
    def __init__(self):
        self.dbip = config['database']['ip']
        self.dbport = config['database']['port']

    def analysis(self, event):
        print("---Analysis Begin:")
        if type(event)==dict:
            self.httpMethod = event['httpMethod']
            self.body = event['body']
            self.queryStringParameters = event['queryStringParameters']
            self.bodydata = base64.decodebytes(self.body.encode('utf-8')).decode('utf-8')
            self.bodydata = parse.unquote(self.bodydata)
        else:
            print("Analysis ERROR: the message is not dict-type data.")
            exit(-1)

        print( "httpMethod", self.httpMethod, sep=': ' )
        print( "queryStringParameters: ",self.queryStringParameters )
        print( "bodydata: ",self.body )
        print( "---Analysis End" )

    def getresponse(self):
        response = writeHeader(body=self.responcebody)

        return response

    def handler(self):
        print("---Handler begin")
        if self.httpMethod=='POST':
            self.handler_POST()
        elif self.httpMethod=='GET':
            self.handler_GET()
        else:
            print( "Handler ERROR: not support %s request"%self.httpMethod)
        
        print("---Handler end")

    def handler_POST(self):
        print("handler a post request:\n",self.bodydata )

        
    def handler_GET(self):
        print("handler a get request:\n",self.queryStringParameters )
        reqtype = self.queryStringParameters['type']
        self.responcebody = ""
        if reqtype=='getHomeHotData':
            self.responcebody = getHomeHotData()
        elif reqtype=='getHomeRecommendData':
            self.responcebody = getHomeRecommendData()
        else:
            print( "Handler ERROR: ","unkonwn request type %s"%reqtype )
        

def handler(event, context):
    myApp = App()
    myApp.analysis(event)
    myApp.handler()
    response = myApp.getresponse()
    return response;

if __name__ == "__main__":
    event = {'requestContext': {'requestId': 'f5423a60ceb8ca5356156312b4a49c34', 'apiId': '01a9a109570c47e0ba3f4b06aed29d90', 'stage': 'RELEASE'}, 'queryStringParameters': {'type': 'getHomeHotData'}, 'path': '/test', 'httpMethod': 'GET', 'isBase64Encoded': 'True', 'headers': {'host': 'a08fcdddeeee4c02a38700f35091372c.apig.cn-south-1.huaweicloudapis.com', 'x-real-ip': '202.113.176.63', 'connection': 'keep-alive', 'x-forwarded-port': '443', 'x-forwarded-host': 'a08fcdddeeee4c02a38700f35091372c.apig.cn-south-1.huaweicloudapis.com', 'x-forwarded-for': '202.113.176.63', 'x-forwarded-proto': 'https', 'referer': 'http://localhost:8080/', 'accept-encoding': 'gzip, deflate, br', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36', 'x-request-id': 'f5423a60ceb8ca5356156312b4a49c34', 'accept-language': 'zh-CN,zh;q=0.9,es-ES;q=0.8,es;q=0.7', 'origin': 'http://localhost:8080', 'accept': 'application/json, text/plain, */*'}, 'body': '', 'pathParameters': {}}
    print( "\nresult=\n",handler(event,"") )
