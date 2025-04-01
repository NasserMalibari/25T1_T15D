import sys

n_lines = 10
if len(sys.argv) > 1:
    if sys.argv[1][0] == '-':
        number = sys.argv[1][1:]
        n_lines = int(number)
        # Todo: check number is a valid integer
    else:
        print("error")
        sys.exit(1)
    # print('more than 1 arg')
    # print(sys.argv)

# i = 0
# for line in sys.stdin:
#     if i == n_lines:
#         break
#     line = line.strip()
#     i += 1
#     print(line)

for index, line in enumerate(sys.stdin, start=1):
    if index > n_lines:
        break
    line = line.strip()
    print(line)


