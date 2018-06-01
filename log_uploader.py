import os
import datetime
import requests
import json
from PyQt5.QtCore import (pyqtSignal, QObject)
import webhook

class log_uploader(QObject):
    uploaded_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        with open("options.json") as f:
            self.options = json.load(f)
        #TO DO: get iconmaps from the options file aswell and select the right iconmap depending on the server selected
        temp = []
        for wing_id in self.options["bosses"]:
            temp.append(list(self.options["bosses"][wing_id].keys()))
        self.formatted_response = ""
        self.url = "https://dps.report/uploadContent"
        self.test = False

    def get_current_week_number(self):
        return datetime.datetime.now().isocalendar()[1]

    def format_date(self, date):
        if type(date) is float:
            return datetime.datetime.fromtimestamp(date).strftime("%d/%m/%Y %H:%M")
        return date

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
        result = {}
        for r in responses:
            #print(r["metadata"]["evtc"]["bossId"])
            #result[self.boss_ids[int(r["metadata"]["evtc"]["bossId"])]] = r["permalink"]
            if "metadata" not in r.keys():
                #result[self.convert_bossname(self.get_bossname_by_id(r["evtc"]["bossId"]))] = r["permalink"]
                result[r["evtc"]["bossId"]] = r["permalink"]
                formatted_response = formatted_response + self.get_bossname_by_id(r["evtc"]["bossId"]) + ": " + r["permalink"] + "\n"
            else:
                #result[self.convert_bossname(self.get_bossname_by_id(r["metadata"]["evtc"]["bossId"]))] = r["permalink"]
                result[r["metadata"]["evtc"]["bossId"]] = r["permalink"]
                formatted_response = formatted_response + self.get_bossname_by_id(r["metadata"]["evtc"]["bossId"]) + ": " + r["permalink"] + "\n"

        # This is the string for the clipboard
        self.formatted_response = formatted_response

        # This sets up and sends the message for the chosen discord channel
        #rc.set_bosses(result)
        if not self.test:
            rc.set_bosses(self.format_bosslist(result))
            rc.setup_message()
            rc.post_to_discord()
        else:
            rc.setup_message(test = True)
            rc.post_to_discord()


    def get_latest_file(self, **kwargs):
        if "dir" in kwargs.keys():
            dir = kwargs.get("dir")
        if "boss" in kwargs.keys():
            dir = os.path.join(self.log_folder, kwargs.get("boss"))
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
            print("You fucked up and need type conversion. SHAME")
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
        for wing_id in self.options["bosses"]:
            for boss_id in self.options["bosses"][wing_id].keys():
                if id == boss_id:
                    return self.options["bosses"][wing_id][boss_id]

    def test_message(self, url):
        msg = webhook.cRaidclear(url)
        testdata = {15429: "https://dps.report/F2Qr-20180528-205930_gorse",
                    17194: "https://dps.report/8VG1-20180528-190433_cairn",
                    17172: "https://dps.report/qyxl-20180528-190925_mo"}
        bosses = self.format_bosslist(testdata)
        msg.set_bosses(bosses)
        msg.setup_message_new()
        msg.post_to_discord()

    def format_bosslist(self, data):
        result = {}
        altname=  True
        for boss_id in data.keys():
            wingname = self.get_wingname_by_boss_id(boss_id)
            bossname = self.get_bossname_by_id(boss_id)
            if altname:
                bossname = self.convert_bossname(bossname)
            if wingname not in result.keys():
                result[wingname] = [{bossname: data[boss_id]}]
            else:
                result[wingname].append({bossname: data[boss_id]})

        return result

    def wing_id_to_name(self, id):
        id = str(id)
        return self.options["wings"].get(id, "Unknown wing name for id "+id)

    def get_wingname_by_boss_id(self, boss_id):
        for wing_id in self.options["bosses"].keys():
            #print("Checking wing with id "+wing_id)
            #print("Wing containts these bosses:")
            #print(self.options["bosses"][wing_id].keys() )
            if str(boss_id) in self.options["bosses"][wing_id].keys():
                #print("Found boss with id %s in wing with id %s" % (boss_id, wing_id))
                return self.wing_id_to_name(wing_id)
