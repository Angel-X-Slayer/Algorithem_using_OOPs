class Toy:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity


class ToyStore:
    def findtoy(self, lst):
        find_lst = []
        for i in lst:
            find_lst.append(i.quantity)
        maxi = max(find_lst)
        for i in lst:
            if i.quantity == maxi:
                return (i)

    def sortingToy(self, lst):
        lst = sorted(lst, key=lambda x: x.quantity,
                     reverse=True)  # most important line
        return lst


lst = []
n = int(input())
for i in range(n):
    id = int(input())
    name = input()
    quantity = int(input())
    t1 = Toy(id, name, quantity)
    lst.append(t1)
print()
obj1 = ToyStore()
k = obj1.findtoy(lst)
r = obj1.sortingToy(lst)
print(k.id)
print(k.name)
print(k.quantity)
print()
for i in r:
    print(i.id)


lst = list(map(int, input().split(" ")))
print(lst)


k = 6
if k not in lst:
    print("true")
else:
    print("flase")
