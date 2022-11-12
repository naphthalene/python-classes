import typing

# ---------------------------------------------------------------------
# This lesson deals with functions in Python. Follow along the examples
# to get a feeling for what they can do, and what shapes they can take.

# Arguments and parameters are used interchangeably. These are the
# variables we define inside the function definition itself.

# Throughout this code, I have added type annotations to all of the
# inputs and outputs. This makes it easy to verify we are composing
# functions correctly.

# Pay close attention to the comments and doc-strings in the functions.


def no_op_function() -> None:
    """This function accepts no args and does nothing (no-operation)!"""


def void_function(something: typing.Any) -> None:
    """This function consumes a value but returns nothing."""
    print(f'I only print {something}, I do not return anything!')


def pure_function(x: int) -> int:
    """
    This function transforms its input argument into an output.
    It is 'pure' because it doesn't consider any values outside its arguments.

    You can reference other pure functions, such as the no-op at its
    simplest:
    """
    no_op_function()
    return x + 1


global_counter = 0


def non_pure_function() -> int:
    """
    This function is not pure - it touches a global variable.
    """
    global global_counter
    # This tells python we care about the global variable with this name

    global_counter += 1
    # Increment the counter - tracks how many times This function has
    # been called

    # Return the new value stored in the global var
    return global_counter


def recursive_function(number: int):
    """
    This function counts down by calling itself.
    """
    print(f'Numero: {number}')
    if number > 0:
        recursive_function(number - 1)


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
    Functions that are defined inside of a class are usually called methods.

    Define functions inside classes when the function deals with
    that class or object instances of that class in some way.

    There are multple types of methods
    """

    def __init__(self, *, value):
        """
        Create an instance of this class.

        The *, in the arguments list means `value` must be passed as a
        keyword argument, and not as a positional argument.
        """
        self.value = value

    def instance_method(self) -> int:
        """
        Set a value on the object.

        `self` is a reference to the object created using

        my_object = FunctionContainer()
        my_object.instance_method()  # self == my_object
        """
        self.instance_method_has_been_called = True
        return self.value

    @staticmethod
    def static_method() -> str:
        """
        Do something class-related, not object-related.

        For example, this method returns a generic string.
        """
        return "Function Container"

    def __str__(self) -> str:
        """
        This is a special function, whose definition we are overriding.

        It is defined for all objects by default, but we can customize it.

        This method's result is a string, and is used when you
        `print` an object, or call `str(my_object)` to convert it
        into a string.

        In our case, we want to return the result of the static method above,
        since we know it returns a string too.
        """
        return f'{FunctionContainer.static_method()} with value {self.value}'

    @classmethod
    def make_1337_class(
            cls: typing.Type['FunctionContainer']
    ) -> 'FunctionContainer':
        """
        A classmethod's first argument is the class's type.

        It must also return an object of a type matching the arg `cls`.

        Class methods allow you to create shortcut methods to create
        objects of this class, with various default inputs for example.
        """
        return cls(value=1337)
