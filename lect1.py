""" Module: Test """

class S:
    def __init__(self):
        self.s = 1
    
    def print_values(self):
        for i in range(1, 4):
            m = i
            print(i + 1)
            print(m)
            print(self.s)
        self.s = 2
        print(self.s)
        print(i + 1)
        print(m)
        print(self.s)
    
    def set_m(self):
        if self.s == 1:
            m = 2
        else:
            m = 4
        return m

s = S()
s.print_values()
m = s.set_m()
