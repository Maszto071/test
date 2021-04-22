import os


# line added
def check_dir():
    return os.getcwd()


def example(name):
    # redundant comment
    pass


def title_it(name):
    return name.title()


if __name__ == "__main__":
    print(check_dir())
    print('hello world')
    print(title_it("hello world!"))
