# 1. Function using *args (arbitrary positional arguments)
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


# 2. Function using **kwargs (arbitrary keyword arguments)
def print_user_info(**kwargs):
    return kwargs


# 3. Function using both normal arguments and *args
def multiply_by_number(number, *args):
    result = []
    for value in args:
        result.append(value * number)
    return result


# 4. Function using default argument and *args
def greet_all(greeting="Hello", *names):
    messages = []
    for name in names:
        messages.append(f"{greeting}, {name}!")
    return messages


# 5. Function using **kwargs to build a sentence
def describe_person(**kwargs):
    description = ""
    for key, value in kwargs.items():
        description += f"{key}: {value}, "
    return description.strip(", ")


# 6. Function combining positional, *args and **kwargs
def full_example(a, b, *args, **kwargs):
    return {
        "a": a,
        "b": b,
        "args": args,
        "kwargs": kwargs
    }


# 7. Function that finds maximum from *args
def find_max(*args):
    return max(args)


# 8. Function that updates dictionary using **kwargs
def update_dict(data, **kwargs):
    data.update(kwargs)
    return data


# 9. Function that counts how many arguments were passed
def count_args(*args):
    return len(args)


# 10. Function that prints formatted key-value pairs
def format_kwargs(**kwargs):
    formatted = []
    for key, value in kwargs.items():
        formatted.append(f"{key} = {value}")
    return formatted