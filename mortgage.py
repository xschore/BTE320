class Mortgage:
    def __init__(self,loan,term,ir):
        self.loan=loan
        self.term=term*12
        self.ir=ir/100
    
    def monthly_payment(self):
        M=self.loan*(self.ir*(1+self.ir)**self.term)/((1+self.ir)**self.term-1)
        print(f'The monthly payment of the mortgage is ${round(M,2)}')

    def __str__(self):
        return f'Mortgage info:\n Initial loan amount: ${self.loan}\n Maturity term: {int(self.term/12)} years\n Interest rate: {self.ir*100}%'
    
a=Mortgage(100000,30,6)

a.monthly_payment()

print(a)