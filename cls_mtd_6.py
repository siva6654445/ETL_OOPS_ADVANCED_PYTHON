class cls:
    _v1 = 200


    @classmethod
    def _fx(cls,_v2):
        cls._v1 = _v2
    
    @staticmethod
    def df1():
        print("this is dummey")

_o1 = cls()
print(_o1._v1)
_o1._fx(300)
print(_o1._v1)
"but now if we create a new obkect it reflcts with new valiable value insted of ortignal"
_o2 = cls()
print(_o2._v1)
_o3 = cls()
print(_o3.df1())




