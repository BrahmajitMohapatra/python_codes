import re
def checkio(data: str):
   flag =1
   while True:
        if not 10<= len(data)<64 :
            flag =0
            break
        elif not re.search('[a-z]',data):
            flag =0
            break
        elif not re.search('[A-Z]',data):
            flag =0
            break
        elif not re.search('[0-9]',data):
            flag =0
            break
        elif  re.search('\s',data):
            flag =0
            break
        else :
            flag =1
            break        
   return flag
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
