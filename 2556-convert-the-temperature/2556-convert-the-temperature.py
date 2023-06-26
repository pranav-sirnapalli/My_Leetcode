class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        l = []
        kel = celsius + 273.15
        fahr = celsius * 1.80 + 32.00
        l.append(kel)
        l.append(fahr)
        return l