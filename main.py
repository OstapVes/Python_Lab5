import re


def main():
    input_file = "log_file.txt"
    with open(input_file, 'r') as log_file:
        file = log_file.readlines()

    find = r".*INFO.*wildfly.*WFLY.*"
    for line in file:

        result = (re.findall(find, line))

        if result:
            print("Результат:", result)
        else:
            pass


if __name__ == '__main__':
    main()
