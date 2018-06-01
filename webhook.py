from discord_hooks import Webhook
import datetime
import urllib3
import certifi
import re

class cRaidclear():
    def __init__(self, hook_url, date=datetime.datetime.now().strftime("%d/%m/%Y")):
        #TO DO: give this the iconmap dict as parameter, selected based on the discord server
        self.bosses = {}
        self.date = date
        self.sample_data = {'Spirit Vale': [{"Vale Guardian":"https://dps.report/4yAL-20180528-205407_vg"},{'Gorseval': 'https://dps.report/F2Qr-20180528-205930_gorse'}, {'Sabetha': 'https://dps.report/B7D9-20180528-210701_sab'}],
                       "Salvation Pass": [{"Slothasor": "https://dps.report/6VPv-20180528-211410_sloth"}, {"Matthias": "https://dps.report/yqQl-20180528-213034_matt"}],
                       "Stronghold of the Faithful": [{"Keep Construct": "https://dps.report/QL2H-20180528-195330_kc"}, {"Xera": "https://dps.report/7jiO-20180528-201011_xera"}],
                       'Bastion of the Penitent': [{'Cairn': 'https://dps.report/8VG1-20180528-190433_cairn'}, {'Mursaat Overseer': 'https://dps.report/qyxl-20180528-190925_mo'}, {"Samarog": "https://dps.report/hViY-20180528-192137_sam"}, {"Deimos": "https://dps.report/To3i-20180528-193358_dei"}],
                       "Hall of Chains": [{"Soulless Horror": "https://dps.report/QLOi-20180528-201723_sh"}, {"Dhuum": "https://dps.report/LaYe-20180528-204710_dhuum"}],
                       "99CM": [{"MAMA": "https://dps.report/5p9Z-20180531-192436_mama"}, {"Siax":"https://dps.report/FAUP-20180531-193010_siax"}, {"Ensolyss": "https://dps.report/nS05-20180531-193344_enso"}],
                       "100CM": [{"Skorvald": "https://dps.report/DsFD-20180531-191137_skor"}, {"Artsariiv": "https://dps.report/KdiW-20180531-191639_ariiv"}, {"Arkk": "https://dps.report/xWBI-20180531-192102_arkk"}]}
        self.placeholder_icon = "<:FeelsDeadMan:446396105077424138>"
        self.iconmap2 = {"Vale Guardian": "<:vale_guardian:449838205701718016>",
                        "Gorseval": "<:gorseval:449838206179868672>",
                        "Sabetha": "<:sabetha:449838205118971909>",
                        "Slothasor": "<:sloth:449838206045913098>",
                        "Matthias": "<:matthias:449838206054170645>",
                        "Keep Construct": "<:keep_construct:449838205731340290>",
                        "Xera": "<:xera:449838206100176896>",
                        "Cairn": "<:cairn:449838199523639307>",
                        "Mursaat Overseer": "<:mursaat_overseer:449838206310023168>",
                        "Samarog":"<:samarog:449838206205296650>",
                        "Deimos": "<:deimos:449838200295391232> ",
                        "Soulless Horror": "<:soulless_horror:449838201943621632>",
                        "Dhuum":"<:dhuum:449838200999903232>",
                        "Skorvald": "<:skorvald:451782654166171660>",
                        "Artsariiv": "<:artsariiv:451782652614148097>",
                        "Arkk": "<:arkk:451782648734547969>",
                        "MAMA": "<:mama:451782654325686272>",
                        "Siax": "<:siax:451782654530945024>",
                        "Ensolyss":"<:ensolyss:451782654430412800>"}

        self.iconmap = {"Vale Guardian": "<:vale_guardian:451069804426559509>",
                        "Gorseval": "<:gorseval:451069805475135488>",
                        "Sabetha": "<:sabetha:451069805101973507>",
                        "Slothasor": "<:sloth:451069804720422913>",
                        "Matthias": "<:matthias:451069804993052682>",
                        "Keep Construct": "<:keep_construct:451069805475266570>",
                        "Xera": "<:xera:451069805060161536>",
                        "Cairn": "<:cairn:451069797116149761>",
                        "Mursaat Overseer": "<:mursaat_overseer:451069804800114689>",
                        "Samarog":"<:samarog:451069805764804608>",
                        "Deimos": "<:deimos:451069798093422613>",
                        "Soulless Horror": "<:soulless_horror:451069800123334675>",
                        "Dhuum":"<:dhuum:451069799355645982>",
                        "Skorvald": "<:skorvald:451782733442711572>",
                        "Artsariiv": "<:artsariiv:451782727637663744>",
                        "Arkk": "<:arkk:451782725901221888>",
                        "MAMA": "<:mama:451782730133274635>",
                        "Siax": "<:siax:451782732264243201>",
                        "Ensolyss":"<:ensolyss:451782728954675230>"}

        self.hook_url = hook_url

        self.embed = Webhook(self.hook_url, color=0x483768)

        #self.embed.set_thumbnail("https://wiki.guildwars2.com/images/9/9d/Epidemic.png")
        self.embed.set_footer(text="Privacy policy updated :>", ts=False)

    def set_bosses(self, bosses):
        """bosses is a dict that containts the bosses + links """
        self.bosses = bosses

    def add_bossfields(self):
        """This adds all bosses to 1 field"""
        for key in self.bosses.keys():
            self.embed.add_field(name=self.iconmap.get(key, self.placeholder_icon)+key, value="[dps.report]("+self.bosses[key]+" \""+self.bosses[key]+"\")")

    def mask_link(self, url, mask):
        return "["+mask+"]("+url+" \""+url+"\")"

    def post_to_discord(self):
        self.embed.set_title(title="__***[Meta] Raid Run on "+self.date+"***__")
        self.embed.set_desc("total clear time (bosses only): ")
        #self.embed.set_author(name="Chrononono")
        self.embed.post()

    def setup_message_old(self, test = False):
        sample_data = self.sample_data
        if test:
            data = sample_data
        else:
            data = self.bosses
        for wing in data.keys():
            field_data = "\n"
            for boss_dict in data[wing]:
                field_data += self.make_boss_info(list(boss_dict.keys())[0], list(boss_dict.values())[0])
            self.embed.add_field(name="**" + wing + "**", value = field_data, inline=False)

    def setup_message(self, test = False):
        if test:
            data = self.sample_data
        for wing in data.keys():
            self.add_wing_field(wing)
            col_count = len(data[wing])
            for boss_dict in data[wing]:
                self.add_boss_field(list(boss_dict.keys())[0], list(boss_dict.values())[0], self.generate_link_mask(list(boss_dict.values())[0]))
            if col_count % 3 == 2:
                self.add_placeholder_field()

    def add_wing_field(self, wingname):
        self.embed.add_field(name=wingname, value="~~"+self.repeat_to_length(" ", 110)+"~~", inline=False)

    def add_boss_field(self, bossname, link, mask=""):
        if mask:
            link = self.mask_link(link, mask)
        self.embed.add_field(name=self.get_boss_icon_by_altname(bossname)+" "+bossname, value=link, inline=True)

    def add_placeholder_field(self):
        self.embed.add_field(name="­­​⁣⁣⁣ ", value="­­​⁣⁣⁣ ")

    def scrape_html(self, html_string):
        regex_str = r"\d+\sminute.?\s\d+[.]\d"
        matches = re.search(regex_str, html_string, re.MULTILINE)
        raw_str_time = matches.group()

        mins = re.search("\d+", raw_str_time).group()
        secs = re.search("\d+.\d", raw_str_time).group()
        time = float(mins)*60 + float(secs)
        time_formatted = re.search(":\d+:\d+", str(datetime.timedelta(seconds=float(secs), minutes=float(mins)))).group()
        time_formatted = time_formatted[1:]

        regex_str = r"\d+ Health"
        matches = re.search(regex_str, html_string, re.MULTILINE)
        raw_str_hp = matches.group()
        hp = int(raw_str_hp.split(" ")[0])
        dps = float(hp)/float(time)

        return [str(time_formatted), "{:4.1f}".format(dps/1000)+"k"]

    def generate_link_mask(self, link, seperator="  ‧  "):
        # grab html file and scrape it for the info no the boss
        http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
        r = http.request("GET", link)

        #get clear Time
        res = self.scrape_html(r.data.decode("utf-8"))
        return res[0] + seperator + res[1]

    def repeat_to_length(self, string_to_expand, length):
        return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

    def make_boss_info(self, boss, info, masked = True):
         result = self.get_boss_icon_by_altname(boss) + " " + boss + "\t" + self.mask_link(info, "dps.report") +"\n\n"
         return result

    def get_boss_icon_by_altname(self, altname):
        return self.iconmap.get(altname, self.placeholder_icon)
