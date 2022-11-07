import typing

# ---------------------------------------------------------------------
# This lesson deals with functions in Python. Follow along the examples
# to get a feeling for what they can do, and what shapes they can take.

# Pay close attention to the comments and doc-strings in the functions.


def no_op_function() -> None:
    """This function accepts no args and does nothing (no-operation)!"""


def void_function(something: typing.Any) -> None:
    """This function consumes a value but returns nothing."""
    print(f'I only print {something}, I do not return anything!')


def pure_function(x: int) -> int:
    """
    This function transforms its input argument into an output.
    It is 'pure' because it doesn't consider any values outside its parameters.
    """
    return x + 1


global_counter = 0


def non_pure_function() -> int:
    """
    This function is not pure - it touches a global variable.
    """
    global global_counter  # This tells python we care about
                           # the global variable with this name
    global_counter += 1    # Increment the counter - tracks how many times
                           # This function has been called
    return global_counter  # Return the new value stored in the global var


def higher_order_function(
        function_a: typing.Callable[[str], str],
        function_b: typing.Callable[[str], str]
) -> typing.Callable[[str], str]:
    """
    A higher order function is one that accepts functions as arguments,
    or returns functions as a return value.

    This function does both - return a new function that composes
    the provided functions `a` and `b`.

    All of these functions must accept strings and return strings.
    """
    def _composed_function(input_value: str) -> str:
        """
        Call function a with provided arguments, then use its output
        to call function b
        """
        return function_b(function_a(input_value))

    return _composed_function


class FunctionContainer:
    """
    Functions that are defined as part of a class are usually called methods.

    Define functions inside classes when the function deals with
    that class or object instances of that class in some way.
    """

    def class_method(self):
        """
        Set a value on the object.

        `self` is a reference to the object created using

        my_object = FunctionContainer()
        my_object.class_method()  # self == my_object
        """
        self.class_method_has_been_called = True

    @staticmethod
    def static_method() -> str:
        """
        Do something class-related, not object-related.

        For example, this method returns a string representation.
        """
        return "Function Container"

    def __str__(self) -> str:
        """
        This is a special function, whose definition we are overriding.

        It is defined for all objects by default, but we can customize it.

        This method's result is a string, and is used when you
        `print` an object, or call `str(my_object)` to convert it
        into a string

        In our case, we want to return the result of the static method above,
        since we know it returns a string too.
        """
        return FunctionContainer.static_method()

    @classmethod
    def make_class(
            cls: typing.Type['FunctionContainer']
    ) -> 'FunctionContainer':
        """
        A classmethod's first argument is the class itself.

        It must also return an object of a type matching the arg `cls`.

        Class methods allow you to create shortcut methods to create
        objects of this class, with various default inputs for example.
        """
        return cls()
