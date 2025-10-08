class person:
    def __init__(day,n1,n2):
        day.n1=n1
        day.n2=n2
    def greet(day):
        print(f"hello gyz i have buy a new car {day.n1} and its model {day.n2}")
p1=person("toyato",2025)
p1.greet()
