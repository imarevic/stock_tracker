
def write_string_to_file(multi_str):

    html_file = open("html_file.html","w")
    html_file.write(multi_str)
    html_file.close()


def rename_cols(df, rename_dict):
    return df.rename(columns=rename_dict, inplace=False)