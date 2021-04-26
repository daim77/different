import re


def sum_num(my_list):
    counter = 0
    my_list = str(my_list).lower()
    my_list = re.sub(r'true', 'x1x', my_list)
    for i in re.findall(r"[+-]?\d+\.\d+|[+-]?\d+", my_list):
        counter += float(i)
    return counter


if __name__ == '__main__':
    data = [1, 's3True', '-4.5', 'true']
    print(sum_num(data))
