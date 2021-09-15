class NumberList:

    def __init__(self, lst):
        self.my_list = lst

    def get_triples(self):
        res_list = []
        for i in range(len(self.my_list) - 2):
            for j in range(i + 1, len(self.my_list) - 1):
                for k in range(j + 1, len(self.my_list)):
                    if self.my_list[i] + self.my_list[j] + self.my_list[k] == 0:
                        res_list.append([self.my_list[i], self.my_list[j], self.my_list[k]])
        return res_list

n_list = NumberList([-25, -10, -7, -3, 2, 4, 8, 10])
print(n_list.get_triples())