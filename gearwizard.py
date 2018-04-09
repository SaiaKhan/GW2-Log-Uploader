class GearSetup():
    def __init__(self):
        self.power = 1000
        self.precision = 1000
        self.ferocity = 1000
        self.healing = 0
        self.vitality = 1000
        self.expertise = 0
        self.concentration = 0
        self.toughness = 1000

        self.effectivePower = 0

        self.convertablePower = 0
        self.convertablePrecision = 0
        self.convertableFerocity = 0
        self.convertableExpertise = 0
        self.convertableConcentration = 0
        self.convertableHealing = 0
        self.convertableToughness = 0

        self.food = None
        self.utility = None

    def getEffectivePower(self, power, precision, ferocity):
        return power*(((precision-895)/2100)*((ferocity/1500)+0.5)+1)
