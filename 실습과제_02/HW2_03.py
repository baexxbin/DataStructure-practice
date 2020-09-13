class Bag:
    def __init__(self, bag = []):
        self.bag = bag
    
    def contains(self, e):
        return e in self.bag
    def insert(self, e):
        self.bag.append(e)
    def remove(self, e):
        self.bag.remove(e)
    def count(self):
        return len(self.bag)
    def numOf(self, item):
        count = 0
        for i in range(len(self.bag)):
            if self.bag[i] == item :
                count += 1
        return count

myBag = Bag()

myBag.insert("아이폰")
myBag.insert("에어팟")
myBag.insert("초콜릿")
myBag.insert("필통")
myBag.insert("전공책")
myBag.insert("종이")
print('가방속의 물건: ',myBag.bag)

myBag.insert('과제')
myBag.remove('초콜릿')
print('가방속의 물건: ',myBag.bag)

print('전공책의 개수:',myBag.numOf('전공책'))
