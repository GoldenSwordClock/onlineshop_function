#from DBconnect import *
from writeHeader import *
import json
#import MySQLdb
import base64
from urllib import parse

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
        response = writeHeader()
        response['body'] = self.bodydata
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
        print("handler a get request:\n",self.bodydata )

def handler(event, context):
    myApp = App()
    myApp.analysis(event)
    myApp.handler()
    response = myApp.getresponse()
    return response;

if __name__ == "__main__":
    event = {'requestContext': {'requestId': 'd19afa0b3f82c2552f3e6c787d01576b', 'apiId': '01a9a109570c47e0ba3f4b06aed29d90', 'stage': 'RELEASE'}, 'queryStringParameters': {}, 'path': '/test', 'httpMethod': 'POST', 'isBase64Encoded': 'True', 'headers': {'host': 'a08fcdddeeee4c02a38700f35091372c.apig.cn-south-1.huaweicloudapis.com', 'content-type': 'application/x-www-form-urlencoded', 'x-real-ip': '202.113.189.186', 'connection': 'keep-alive', 'sec-ch-ua-mobile': '?0', 'sec-fetch-site': 'cross-site', 'sec-fetch-dest': 'empty', 'referer': 'http://localhost:8080/', 'sec-ch-ua': '\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"', 'origin': 'http://localhost:8080', 'x-forwarded-host': 'a08fcdddeeee4c02a38700f35091372c.apig.cn-south-1.huaweicloudapis.com', 'accept': 'application/json, text/plain, */*', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https', 'content-length': '35', 'accept-encoding': 'gzip, deflate, br', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 'x-forwarded-for': '202.113.189.186', 'x-request-id': 'd19afa0b3f82c2552f3e6c787d01576b', 'accept-language': 'zh-CN,zh;q=0.9', 'sec-fetch-mode': 'cors'}, 'body': 'bmFtZT1qaWFuamlhbiZhZ2U9MjEmc2V4PSVFNSVBNSVCMyY=', 'pathParameters': {}}
    print( "\nresult=\n",handler(event,"") )
