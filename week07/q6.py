import sys

n_lines = 10
if len(sys.argv) > 1:
    if sys.argv[1][0] == '-':
        argument = sys.argv.pop(1)
        number = argument[1:]
        n_lines = int(number)
        # Todo: check number is a valid integer

# print(sys.argv)

for file in sys.argv[1:]:
    # open file
    with open(file) as f:
        for i, line in enumerate(f):
            if i == n_lines:
                break
            line = line.strip()
            print(line)
        # print lines

# i = 0
# for line in sys.stdin:
#     if i == n_lines:
#         break
#     line = line.strip()
#     i += 1
#     print(line)

# for index, line in enumerate(sys.stdin, start=1):
#     if index > n_lines:
#         break
#     line = line.strip()
#     print(line)


