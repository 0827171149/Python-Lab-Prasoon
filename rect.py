class rect:
    def __init__(self,len=0,br=0):
        self.l=len
        self.b=br
    def calc_area(self,rec):
        area=rec.l*rec.b
        print("area is")
        print(area)
a=rect(10,20)
b=rect()
b.calc_area(a)
