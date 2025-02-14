"""FOR SELECT"""
reference_string1 = 'madera roja'
slice_string = reference_string1[0:len(reference_string1)]
print(slice_string)

def select_starts(reference_string, strings_list):
    """
    :param reference_string: cadena que debe ser encontrada en los elementos
    de la lista
    :param strings_list: lista de cadenas en la cual se va a iterar para encontrar
    reference_string
    :return: se retorna una lista con las cadenas que contienen reference_string al inicio
    """
    result_list = []
    for string in strings_list:
        if reference_string == string[0:len(reference_string)]:
            result_list.append(string)
    return result_list

print(select_starts('mar',['martes','marte','marta','aracucho','amar','mar','mamar','aaracucho']))







