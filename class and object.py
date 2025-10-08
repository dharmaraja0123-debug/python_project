class goa:
    def __init__(self,name):
        self.name=name
    name="not registerd"
    drink=""
    def party(self):
        print("lets party.....")
    def beach(self):
        print("Enjoying the beach")

ramesh=goa("ramesh")
suresh=goa("suresh")

ramesh.name="Ramesh"
suresh.name="suresh"

ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name)
print("drink:",ramesh.drink)
print(suresh.name)
print("drink:",suresh.drink)
