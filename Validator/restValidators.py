
def return_errors(func):
    """
    The function is a wrapper which catches a function exception and returns its instead of the function return value.
    @param func: The running function.
    @return: If the function runs succeed, it returns its value, else, it returns its exception message.
    """
    def wrap(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as e:
            res = str(e)
        return res

    return wrap


if __name__ == '__main__':
    @return_errors
    def an_exception_thrower(*args, **kwargs):
        tries_to_create_string = f"1: {args[0]}, "\
                                 f"2: {args[1]}, "\
                                 f"3: {args[2]}, "\
                                 f"4: {args[3]},"\
                                 f"error: {kwargs['error']}"
        raise Exception('string build has succeed')
    print(an_exception_thrower('1', 'v', '33', '124', error='1231234444'))
    print(an_exception_thrower('1', 'v', '33', '124'))
    print(an_exception_thrower('1', 'v', '33', error='1231234444'))
