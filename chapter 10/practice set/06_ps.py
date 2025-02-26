from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time.")
    
    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")
    

t = Train(16925)
t.book("Vadnagar","Bharuch")
t.getstatus()
t.getfare("Vadnagar","Bharuch")