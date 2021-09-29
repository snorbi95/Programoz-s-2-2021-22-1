class MyList(list):

    def __init__(self, p1):
        super().__init__(p1)

    def print_items_with_indices(self):
        for i, item in enumerate(self):
            print(f'{i}: {item}')

a = MyList([3,4,5,8,9,6,3])
a.print_items_with_indices()
