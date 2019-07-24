class employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first,slef.last)

    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

