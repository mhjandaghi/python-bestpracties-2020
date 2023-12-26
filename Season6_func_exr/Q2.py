def longest_str(*args):
    long_string = args[0]

    for string in args:
        if len(string) > len(long_string):
            long_string = string

    print(long_string, len(long_string))

longest_str("ali", "setareh", "ahmadian")