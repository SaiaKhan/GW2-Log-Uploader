import os
import datetime
import requests
import json
import glob
import pyperclip
import configparser
import ast

class log_uploader(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("options.ini")
        self.log_folder = os.path.join(os.path.expanduser("~"), "Documents",
                                     "Guild Wars 2", "addons", "arcdps",
                                     "arcdps.cbtlogs")
        self.bossIds = self.config["bossids"]

        self.url = "https://dps.report/uploadContent"
        self.fractals = self.config["bosslists"]["fractals"]
        self.raids = self.config["bosslists"]["raids"]
        self.response = []


    def get_current_week_number(self):
        return datetime.datetime.now().isocalendar()[1]


    def upload_logs(self, filelist):
        result = []
        for file in filelist:
            with open(file, "rb") as f:
                print("Starting upload for file: " + file)
                r = requests.post(self.url, files={"file": f}, data={"json":1})
                result.append(json.loads(r.content))
                print("finished upload for file!")
        self.response = result
        self.parse_response(result)


    def get_latest_file(self, dir):
        #print("searching directory: " + glob.glob(dir+"*")[0])
        max_ctime = 0
        for dirname, subdirs, files in os.walk(dir):
            for fname in files:
                full_path = os.path.join(dirname, fname)
                ctime = os.path.getctime(full_path)
                if ctime > max_ctime:
                    max_ctime = ctime
                    #max_dir = dirname
                    max_file = fname
        return [os.path.join(max_file), max_ctime]#max_dir, max_file)


    def make_dirlist(self, namelist):
        result = []
        if type(namelist) is str:
            names = ast.literal_eval(namelist)
        elif type(namelist) is list:
            names = namelist
        else:
            names = []
        for name in names:
            result.append(glob.glob(os.path.join(self.log_folder, name+"*"))[0])
        return result


    def make_filelist(self, dirlist):
        result = []
        for dir in dirlist:
            result.append(os.path.join(dir, self.get_latest_file(dir)[0]))
        return result


    def upload_fractals(self):
        files = self.make_filelist(self.make_dirlist(self.fractals))
        self.upload_logs(files)


    def upload_raids(self):
        files = self.make_filelist(self.make_dirlist(self.raids))
        self.upload_logs(files)


    def parse_response(self, responses):
        result = """** %s ** \n""" % (datetime.datetime.now().strftime("%d/%m/%y %H:%M"))
        for r in responses:
            #print(r["metadata"]["evtc"]["bossId"])
            result = result + self.bossIds[str(r["metadata"]["evtc"]["bossId"])] + ": " + r["permalink"] + "\n"
        pyperclip.copy(result)


    def upload_test(self):
        files = self.make_filelist(self.make_dirlist(["Xera"]))
        self.upload_logs(files)

    def upload_parts(self, parts):
        """ Give this a list of parts, i.e. things from the bosslists section"""
        files = self.make_filelist(self.make_dirlist(parts))
        self.upload_logs(files)
