import os
import requests

location = os.path.join(os.getcwd(), "test_logs", "testlog.zip")
print("starting upload")
log = "https://dps.report/uploadContent?json=1"
test = "https://httpbin.org/post"
with open(location, "rb") as f:
    r = requests.post(log, files={"file": f}, data={"json":1})
print("finished upload")
print(r.text)
print(type(r.text))
#print(os.path.split(os.path.split(location)[0]))
