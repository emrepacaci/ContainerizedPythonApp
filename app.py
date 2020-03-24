#!/bin pyhton3
import requests
import redis
import ast
import os
from bottle import get, post, run, request, route
from tabulate import tabulate

@get('/upload')
def fileUploadForm():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
          Select a txt file: <input type="file" name="upload" />
          <input type="submit" value="Start Analysis" />
        </form>
    '''

@route('/upload', method='POST')
def do_upload():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.txt'):
        return 'File extension:' + ext + ' not allowed.'

    raw = upload.file.read()
    hashes = raw.splitlines()
    result = {}
    result.setdefault('resource',[])
    result.setdefault('result',[])
    result.setdefault('total',[])
    result.setdefault('scan_date',[])
    for hash in hashes:
        response = getReport(hash.decode('utf-8)'))
        if response:
            result['resource'].append(response['resource'])
            result['result'].append(response['result'])
            result['total'].append(response["total"])
            result['scan_date'].append(response['scan_date'])
    headers=["hash_value (MD5 or Sha256)", "Fortinet detection name", "Number of engines detected", "Scan Dates"]
    return tabulate(result, headers, tablefmt="html")

def getReport(hash):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': '8c2f112539ef7cdb18172917e12afe7d2bab0b60bfffcade4c7ab14b0cb19ca4', 'resource': hash}
    isRedisAlive = True
    try:
        redis_db.ping()
    except:
        isRedisAlive = False
    if isRedisAlive:
        result = redis_db.get(hash)
    if isRedisAlive and result:
        print("cache hit:" + hash)
        result = ast.literal_eval(result.decode('utf-8)')) #convert bytes to json(dict)
    else:
        print("cache miss:" + hash)
        try:
            response = requests.get(url, params=params)
            if response.status_code != 200:
                print("bad response for " + hash +". status_code:", response.status_code)
                return 0
            else:
                response = response.json() 
        except: 
            return 0
        result = {}
        if response and response['response_code']==1:
            result['resource'] = str(hash)
            result['result'] = str(response['scans']['Fortinet']['result'])
            result['total'] = str(response['total'])
            result['scan_date'] = str(response['scan_date'])
            if isRedisAlive:
                redis_db.set(hash, str(result))
        else:
            return 0
    return result

redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

if __name__ == "__main__":
    run(host='0.0.0.0', port=80, debug=True)








