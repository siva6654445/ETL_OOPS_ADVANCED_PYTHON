class de:


    def __init__(self,_v1,_v2,_v3):
        self._v1 = _v1
        self._v2 = _v2
        self._v3 = _v3

    def fx1(self):
        print(f"Hellow world,{self._v1}")

    def fx2(self):
        print(f"helw mnsd , {self._v2}")


o1 = de('a','b','c')
o1.fx2()