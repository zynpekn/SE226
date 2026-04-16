def remove_duplicates(data_list):
    return list(dict.fromkeys(data_list))

def strip_whitespaces(string_list):
    return [x.strip() for x in string_list]