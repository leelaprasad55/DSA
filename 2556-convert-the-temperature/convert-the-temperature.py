class Solution:
    def convertTemperature(self,c: float) -> List[float]:
        l=[]
        l.append(c+273.15)
        l.append(c*1.80+32.00)
        return l
        