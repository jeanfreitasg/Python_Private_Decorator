from inspect import stack
from functools import wraps

def private(replacement_function=lambda: None):

    def _private(func):

        @wraps(func)
        def function_wrapper(*args, **kwargs):

            try:
                function_call = stack()[1][4][0].strip()

                if not function_call.startswith("self."):
                    return replacement_function()
            except Exception as e:
                return replacement_function()

            return func(*args, **kwargs)

        return function_wrapper

    return _private
