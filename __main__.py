import os


# line added
def check_dir():
    return os.getcwd()


def example():
    # redundant comment
    for i in range(5):
        print(i)


if __name__ == "__main__":
    print(check_dir())
    print('hello world')
    example()
