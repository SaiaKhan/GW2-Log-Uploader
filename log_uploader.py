import os
import datetime
import requests
import json
from PyQt5.QtCore import (pyqtSignal, QObject)
#import ast
import webhook

class log_uploader(QObject):
    uploaded_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        with open("options.json") as f:
            self.options = json.load(f)

        temp = []
        for wing_id in self.options["bosses"]:
            temp.append(list(self.options["bosses"][wing_id].keys()))
        #self.boss_ids = [id for wing in temp for id in wing]
        self.formatted_response = ""
        self.url = "https://dps.report/uploadContent"
        self.test = False

    def get_current_week_number(self):
        return datetime.datetime.now().isocalendar()[1]

    def format_date(self, date):
        if type(date) is float:
            return datetime.datetime.fromtimestamp(date).strftime("%d/%m/%Y %H:%M")
        return date

    #def upload_parts(self, parts):
        #""" Give this a list of parts, i.e. things from the bosslists section"""
        # To Do: refactor upload_parts so that the hook_url doesnt have to be passed 3 times
        #files = self.make_filelist(self.make_dirlist(parts))
        #self.upload_logs(files)


    def upload_logs(self, parts, hook_url):
        if self.test:
            self.parse_response([self.get_report_by_link()], self.options["hook_urls"]["Testserver"])
        else:
            filelist = self.make_filelist(self.make_dirlist(parts))
            result = []
            for file in filelist:
                with open(file, "rb") as f:
                    print("Starting upload for file: " + file)
                    r = requests.post(self.url, files={"file": f}, data={"json":1})
                    result.append(json.loads(r.content))
                    #print("finished upload for file!")
                    self.uploaded_signal.emit(1)
            self.parse_response(result, hook_url)
            # might want to save the result to file or just keep in memory

    def get_report_by_link(self, link="https://dps.report/Eiyx-20180525-224016_arkk"):
        base_url = "https://dps.report/getReport"
        r = requests.get(base_url, params={"permalink":link})
        return json.loads(r.content)

    def parse_response(self, responses, hook_url):
        formatted_response = """** %s ** \n""" % (datetime.datetime.now().strftime("%d/%m/%y %H:%M"))
        rc = webhook.cRaidclear(hook_url)
        #rc = webhook.cRaidclear(self.options["hook_urls"][])
        result = {}
        for r in responses:
            #print(r["metadata"]["evtc"]["bossId"])
            #result[self.boss_ids[int(r["metadata"]["evtc"]["bossId"])]] = r["permalink"]
            if "metadata" not in r.keys():
                result[self.convert_bossname(self.get_bossname_by_id(r["evtc"]["bossId"]))] = r["permalink"]
                formatted_response = formatted_response + self.get_bossname_by_id(r["evtc"]["bossId"]) + ": " + r["permalink"] + "\n"
            else:
                result[self.convert_bossname(self.get_bossname_by_id(r["metadata"]["evtc"]["bossId"]))] = r["permalink"]
                formatted_response = formatted_response + self.get_bossname_by_id(r["metadata"]["evtc"]["bossId"]) + ": " + r["permalink"] + "\n"
        self.formatted_response = formatted_response
        rc.set_bosses(result) # make sure this receives the abbreviated boss names
        rc.add_bossfields()
        rc.post_to_discord()


    def get_latest_file(self, **kwargs):
        if "dir" in kwargs.keys():
            dir = kwargs.get("dir")
        if "boss" in kwargs.keys():
            dir = os.path.join(self.log_folder, kwargs.get("boss"))
        #print("searching directory: " + glob.glob(dir+"*")[0])
        #print("checking folder: "+dir)
        max_ctime = 0
        max_file = "NOT FOUND"
        for dirname, subdirs, files in os.walk(dir):
            for fname in files:
                full_path = os.path.join(dirname, fname)
                ctime = os.path.getctime(full_path)
                if ctime > max_ctime:
                    max_ctime = ctime
                    #max_dir = dirname
                    max_file = fname
        if max_file == "NOT FOUND":
            return [max_file, 0]
        else:
            return [os.path.join(max_file), max_ctime]


    def make_dirlist(self, namelist):
        result = []
        if type(namelist) is str:
            print("You fucked up and need type conversion. SHAME")#names = ast.literal_eval(namelist)
        elif type(namelist) is list:
            names = namelist
        else:
            names = []
        for name in names:
            result.append(os.path.join(self.log_folder, name))
        return result


    def make_filelist(self, dirlist):
        result = []
        for dir in dirlist:
            result.append(os.path.join(dir, self.get_latest_file(dir=dir)[0]))
        return result

    def convert_bossname(self, bossname):
        alt_names = self.options["alternative_bossnames"]
        return alt_names.get(bossname, bossname)

    def get_wing_data(self):
        return self.options["bosses"]

    def get_bossname_by_id(self, id):
        id=str(id)
        #print("checking for id "+str(id)+" with type "+str(type(id)))
        for wing_id in self.options["bosses"]:
            for boss_id in self.options["bosses"][wing_id].keys():
                if id == boss_id:
                    #print("returning "+self.options["bosses"][wing_id][boss_id])
                    return self.options["bosses"][wing_id][boss_id]
        #return "Boss could not be found"

    #def upload_fractals(self):
        #files = self.make_filelist(self.make_dirlist(self.fractals))
        #self.upload_logs(files)


    #def upload_raids(self):
        #files = self.make_filelist(self.make_dirlist(self.raids))
        #self.upload_logs(files)

    def test_message(self):
        temp = webhook.cRaidclear(datetime.datetime.now().strftime("%d/%m/%Y"))
        temp.test_message()




    #def upload_test(self):
        #files = self.make_filelist(self.make_dirlist(["Xera"]))
        #self.upload_logs(files)
