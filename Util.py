def get_size(list):
    return str(len(list))


def print_error(string):
    error = []
    error.append('~~~~~~~~~~~~~~~~~~ERROR~~~~~~~~~~~~~~~~~~')
    error.append(string)
    error.append('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("\n".join(error))
