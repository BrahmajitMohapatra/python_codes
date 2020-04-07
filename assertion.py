def KtoF(temperature):
    assert(temperature >=0),"Colder Than absolute zero"
    return ((temperature - 273)*1.8)+32
try :
    print(KtoF(273))
    print(KtoF(505.78))
    print(KtoF(-5))
except(AssertionError):
    print("Error Occured")
