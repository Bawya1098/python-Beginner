list = ['p', 'q']
number = 5

result_list = ["{}{}".format(alpha, number) for number in range(1, number + 1)for alpha in list]
print("result list is:" ,result_list)
