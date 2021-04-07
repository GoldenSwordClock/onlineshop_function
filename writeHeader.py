def writeHeader(statusCode = 200, 
                headers={'Content-Type': 'application/json','Access-Control-Allow-Origin': '*'},
                body=''):
    result = {}
    result['statusCode'] = statusCode
    result['headers'] = headers
    result['isBase64Encoded'] = False
    result['body'] = body

    return result