# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/11/2022
# Description:A class called Person that has two private data members - the person's name and age.
class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_age(self):
        return self.__age
def std_dev(p_list):
    total = 0
    for person in p_list:
        total += person.get_age()
    mean_age = total / len(p_list)
    square_sum = 0
    for person in p_list:
        square_sum += (mean_age - person.get_age()) ** 2
    return (square_sum / len(p_list)) ** 0.5

p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
p_list = [p1, p2, p3]
answer = std_dev(p_list)
print('Standard Deviation of Age:',answer)