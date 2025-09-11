int_str = input("Integer (space separated):")
int_list = [int(i) for i in int_str.split()]
print(int_list)
sum_of_integers = sum(int_list)
average = sum_of_integers/len(int_list)
print(sum_of_integers)
print(average)

filename = 'numbers_data.txt'
with open(filename, 'w') as writer:
    writer.write(f'List: {int_list}\n')
    writer.write(f'Sum: {sum_of_integers}\n')
    writer.write(f'Average: {average}')

with open(filename, 'r') as reader:
    integer_list = reader.readline()
    Sum = reader.readline()
    Average = reader.readline()
    print(integer_list)
    print(Sum)
    print(Average)