import os
import datetime
import requests
import json


class log_uploader(object):
    def __init__(self):
        self.log_folder = os.path.join(os.path.expanduser("~"), "Documents",
                                     "Guild Wars 2", "addons", "arcdps",
                                     "arcdps.cbtlogs", "")
        self.options = {"include_fails": True,
                        "file_extentions": ["zip"]}
        with open("data\\bosses.json") as f:
            self.options["bosses"] = json.load(f)

        self.url = "https://dps.report/uploadContent"
        self.filelist = []
        self.filelist = [os.path.join(os.getcwd(), "test_logs", "testlog.zip"),
                         os.path.join(self.log_folder, "Xera", "20180212-210515.evtc.zip")]

    def get_current_week_number(self):
        return datetime.datetime.now().isocalendar()[1]


    def upload_logs(self):
        result = []
        for file in self.filelist:
            with open(file, "rb") as f:
                r = requests.post(self.url, files={"file": f}, data={"json":1})
                result.append(json.loads(r.content))
        print(result)

    def get_latest_file(self, dir):
        max_ctime = 0
        for dirname, subdirs, files in os.walk(dir):
            for fname in files:
                full_path = os.path.join(dirname, fname)
                ctime = os.path.getctime(full_path)
                if ctime > max_ctime:
                    max_ctime = ctime
                    #max_dir = dirname
                    max_file = fname
        return os.path.join(max_file)#max_dir, max_file)
