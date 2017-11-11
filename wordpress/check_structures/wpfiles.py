import queue
import threading
import os
import urllib.request
import urllib.error

threads = 10

wpurl = "http://172.17.0.1/blog"
localwp = "/var/www/html/blog"
filters = [".jpg",".gif",".png",".css",".js"]

os.chdir(localwp)

web_paths = queue.Queue()

for root,directory,files in os.walk("."):
    for file in files:
        remote_path = "%s/%s" % (root,file)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(file)[1] not in filters:
            web_paths.put(remote_path)
            
def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = "%s/%s" % (wpurl,path)
        
        request = urllib.request.Request(url)
        
        try:
            response = urllib.request.urlopen(request)
            content = response.read()
            
            print("[%d] => %s" % (response.code,path))
            
            response.close()
            
        except urllib.error.HTTPError as error:
            # print("File get error")
            pass
        
for i in range(threads):
    print("Running thread: %d" % i)
    t = threading.Thread(target=test_remote)
    t.start()