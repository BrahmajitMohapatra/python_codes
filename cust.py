class Cust:
    cbname = 'sbi'

    def __init__(self, cname, caddr, cacno, cbal):
        self.cname = cname
        self.caddr = caddr
        self.cacno = cacno
        self.cbal = cbal
    def __str__(self):
        return self.cname+" "+self.caddr+ " " + str(self.cacno) + " " + str(self.cbal) + " "+Cust.cbname
    def deposite(self,damt):
        self.cbal=self.cbal+damt
    def withdraw(self,wamt):
        self.cbal=self.cbal-wamt
    def display(self):
        print(self.cbname)
        print(self.caddr)
        print(self.cacno)
        print(self.cbal)
        print(Cust.cbname)
c1=Cust("monali","Mumbai",420,200.00)
c2=Cust("Pankaj","Wardha",786,199.000)
c3=Cust('Arun','Borgaon',888,3500.00)
x=[c1,c2,c3]
for c in x:
    print(c)
x.sort(key=lambda c:c.caddr,reverse=True)
print('after sorting ')
for p in x:
    print(p)




