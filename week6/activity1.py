def add_sprinkles(func):

    def wrapper():
        print("Adding sprinkles...")
        func()

    return wrapper


@add_sprinkles
def make_ice_cream():
    print("Making ice cream...")


def add_chocolate(func):

    def wrapper():
        print("Adding chocolate...")
        func()

    return wrapper


@add_chocolate
def make_chocolate_ice_cream():
    print("Making chocolate ice cream...")


# Call the functions
make_ice_cream()
make_chocolate_ice_cream()