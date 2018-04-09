class stats():
    def __init__(self):
        self.stats = {"helmet_3": [63, 45, 45],
                      "shoulders_3": [47, 34, 34],
                      "chest_3 ": [141, 101, 101],
                      "gloves_3": [47, 34, 34],
                      "legs_3": [94, 67, 67],
                      "boots_3 ": [47, 34, 34],
                      "amulet_3 ": [157, 108, 108],
                      "ring_3": [126, 85, 85],
                      "earring_3": [110, 74, 74],
                      "backpiece_3": [63, 40, 40],
                      "2h_weap_3": [251, 179, 179],
                      "1h_weap_3": [125, 90, 90]}

        def get_stats(self, category):
            temp = self.stats.get(category)
