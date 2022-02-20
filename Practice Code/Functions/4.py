def format_name(f_name, l_name):

    """This is the way of using DocStrings
       which can be multilined too"""  #acts as a comment or an explaination of function needs which using function

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return formated_f_name, formated_l_name

formated_string = format_name("bhuvAn", "Bhuvan")
print(formated_string)