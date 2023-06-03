
def get_ser_lst() -> list:
    """
    The function enters the Series directory and returns a list of all the directories inside it which means, all
    the series the application support.
    If the dir scan fails, the function return an empty list
    @param rootpath: Because the azure web-app's app.py runs on different path then on the computer, there is
    a need for the app variable's root path to create the path to the Series path.
    @return: A list of the series the application support.
    """
    from Macros.ModelMacros import SERIES_LIST, NOTHING_VALUE
    return [serie for serie in filter(lambda i: i != NOTHING_VALUE, SERIES_LIST)]
