class Item:
    def __init__(self,p,w):
        self.profit= p
        self.weight = w


def knapsack_using_greedyalg(c,arr):

    #sorting based on p/w ratio
    arr.sort(key=lambda x: x.profit / x.weight, reverse=True)

    max_profit = 0
    for item in arr:
        if item.weight <= c:
            c = c-item.weight
            max_profit += item.profit

        else:
            max_profit += item.profit * c/item.weight
            break

    return max_profit



items = [Item(5,1), Item(10,3), Item(15,5), Item(7,4), Item(8,1), Item(9,3), Item(4,2)]
capacity = 15
max_profit = knapsack_using_greedyalg(capacity,items)
print(max_profit)