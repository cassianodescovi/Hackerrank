# On the class:
class Example:
    def __init__(self, who_are_you, name):
        self.who_are_you = who_are_you
        self.name = name

	# getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, new_name):
        self._name = new_name

# On the program:
def main():
    object = Example(1, "negao")
    print(object)
    print(object.name)
    object.name = "cassiano"
    print(object.name)


if __name__ == "__main__":
    main()