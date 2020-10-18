def difference(self,setB):
        differenceSet = Set()
        differenceSet.items = self.items[:]
        a=0; b=0
        while a < len(differenceSet.items) and b < len(setB.items): 
            valueA = differenceSet.items[a]
            valueB = setB.items[b]
            if valueA < valueB : a+=1
            elif valueA > valueB : b+=1
            else:
                differenceSet.delete(valueA)
                a+=1; b+=1
        return differenceSet