#Credit goes to https://github.com/Apexofacircle 
print("Standard to factored form calculator")
print("Version: 1.0")
print("Asuming: Ax^2 + Bx + C")

#Get inputs
_A = float(input("A: "))
_B = float(input("B: "))
_C = float(input("C: "))
 
#Set starting variables
_Div = 1
_Ac = _A *_C
 
#Calculate
if _Ac <= 0: #If in the negatives 
        _Div = -1
        while not (_Ac / _Div) + _Div == _B :
            _Div -= 1
            print (_Div, _Ac / _Div, _B)
else: #If in the positives 
    while not (_Div / _Ac ) + _Div == _B :
        _Div += 1
        print (_Div, _Div / _Ac , _B)
 
#Turn calculation into readable format
_DivAns = _Div / _A
try:
    _Ans2 = (_Ac / _Div) / _A
except: 
    _Ans2 = 0
 
 
#Print answer
print("-----")
print("Answer: ")
print(f"{_A}(x + {_DivAns})(x + {_Ans2})")
