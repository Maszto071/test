import os


# line added
def check_dir():
    return os.getcwd()


def example(name):
    # redundant comment
    for i in range(5):
        print(i)


def title_it(name):
    return name.title()

def sum_numbers(a, b):
    return  a + b


if __name__ == "__main__":
    print(check_dir())
    print('hello world')
    print(title_it("hello world!"))
    example()
    sum_numbers(5, 10)
