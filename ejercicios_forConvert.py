def make_lengths(strings_list):
  """
  recibe una lista de cadenas y devuelve una lista de numeros. Los numeros son la
  longitud de cada cadena y la lista conserva la longitud original
  """
  list_of_numbers = []
  for string_element in strings_list:
    list_of_numbers.append(len(string_element))
  return list_of_numbers

def make_inverses(numbers_list):
  """
  recibe una lista de numeros y devuelve otra lista de la misma longitud con los
  inversos de cada uno de los numeros de entrada.
  """
  inverses_list = []
  for number in numbers_list:
    inverses_list.append(number * - 1)
  return inverses_list

def make_reciprocate(numbers_list):
    """
    Recibe una lista de números y devuelve otra lista de igual longitud
    con el recíproco (inverso multiplicativo) de cada número.

    Si un número de la lista es 0, en la lista resultante aparecerá `None`,
    ya que no se puede calcular el recíproco de 0.
    la longitud de la lista de entrada no se altara y para esto se asigna None
    en los espacios en los cuales hay un cero.

    Ejemplo:
    --------
    Entrada: [1, 2, 0, 4]
    Salida: [1.0, 0.5, None, 0.25]
    """
    reciprocate_list = []
    for number in numbers_list:
        if number == 0:  # Caso especial para el 0
            reciprocate_list.append(None)
        else:  # Cualquier otro número
            reciprocate_list.append(1 / number)
    return reciprocate_list

def elevate(numbers_list, exponent):
    """
    :param numbers_list: recibe una lista de numeros
    :param exponent: es un numero que se va a utilizar como un exponente
    que se aplicara a todos los elementos de la lista recibida
    :return: se retorn una lista de la misma longitud que la original, con los
    datos modificados por la operacion exponencial
    """
    result_list = []
    for number in numbers_list:
        result_list.append(number ** exponent)
    return result_list

def to_strings(numbers_list):
    """
      recibe una lista de numeros y devuelve una lista convertida de numeros a cadenas.
      la lista conserva la longitud original
      si la lista se entrega vacia, se devuelve la lista vacia
    """
    to_strings_list = []
    for number in numbers_list:
        to_strings_list.append(str(number))
    return to_strings_list
#print(to_strings([1,2,3,4,5]))

def to_floats(numbers_list):
    """
    :param numbers_list: recibe una lista de numeros
    :return: devuelve una lista de la mismas longitud con los valores
    convertidos a decimales
    """
    to_floats_list = []
    for number in numbers_list:
        to_floats_list.append(float(number))
    return to_floats_list
#print(to_floats([1,2,3,4,5,6]))
def round_list(numbers_list):
  numbers_list = to_floats(numbers_list)
  numbers_rounded = []
  for number in numbers_list:
    numbers_rounded.append(round(number,2))
  return numbers_rounded


# Necesitas una función que recibe una lista de números y los redondea a varias posiciones decimales (1, 2, 4, etc).
# Modifica round_list para que pueda hacer eso.

def round_list_refactored(numbers_list,digits = 1):
  """
  recibe una lista de numeros enteros o decimales y un parametro
  digits que representa el numero de posiciones a redondear
  ,devuelve una lista de decimales
  """
  numbers_list = to_floats(numbers_list)
  numbers_rounded = []
  for number in numbers_list:
    numbers_rounded.append(round(number,digits))
  return numbers_rounded

def update_salaries(numbers_list):
    """
    :param numbers_list: recibe una lista de numeros como nominas
    :return: devuelve una lista de la misma longitud con las operaciones
    realizadas en cada item de acuerdo a si la nomina es:
    nómina < 900 se incrementa en un 30%
    900 <= nómina < 1500, se incrementa en un 12%
    1500 <= nómina < 6000, se queda tal cual
    nómina > 6000, se incrementa en un 100%
    """
    salaries_list_result = []
    for number in numbers_list:
        if number < 900:
            salaries_list_result.append(number * 1.3)
        elif 900 <= number < 1500:
            salaries_list_result.append(number * 1.12)
        elif 1500 <= number < 6000:
            salaries_list_result.append(number)
        elif number > 6000:
            salaries_list_result.append(number * 2)
    return salaries_list_result

#print(update_salaries([200,900, 800, 1000, 1400, 2000, 7000]))

def sum_all(numbers_list):
    """
    :param numbers_list: recibe una lista de numeros
    :return: devuelve un numero resultado de la suma de todos los
    numeros de la lista
    """
    result = 0
    for number in numbers_list:
        result += number
    return result
#print(sum_all(update_salaries([200,900, 800, 1000, 1400, 2000, 7000])))

def double_if_neg(numbers_list):
    """
    :param numbers_list: recibe una lista de numeros
    :return: devuelve una lista de la misma longitud con los
    numeros negativas multiplicados por dos, los numeros positivos se dejan
    tal cual
    """
    list_modified = []
    for number in numbers_list:
        if number < 0:
            list_modified.append(number * 2)
        elif number > 0:
            list_modified.append(number)
    return list_modified
#print(double_if_neg([1,2,3,4,5,-6,-7,-8,-9]))

def to_lists(numbers_list):
    """
    :param numbers_list: recibe una lista de numeros
    :return: devuelve una lista con cada numero como una lista.
    se devuelve una lista de listas
    """
    list_result = []
    for number in numbers_list:
        list_result.append([number])
    return list_result
# print(to_lists([1,2,3,4,5]))
def explode(string):
    """
    :param string: recibe una cadena de caracteres
    :return: devuelve una lista con cada caracter como elemento
    de la lista
    """
    strings_list = []
    for string_element in string:
        strings_list.append(string_element)
    return strings_list
#print(explode('hola'))

def implode(strings_list):
    string_result = ''
    for string_element in strings_list:
        string_result += string_element
    return string_result
#print(implode(['h', 'o', 'l','a']))

#print(implode(explode('holamundo')))

def to_p_sentence(string):
    """
    :param string: recibe una cadena
    :return: devuelve una cadena modificada. Si se encuentra un vocal se
    transforma en una silaba con la p y las dos vocales
    a -> apa
    e -> epe
    i -> ipi
    o -> opo
    u -> upu
    """
    string_transformed_result = ''
    string = string.lower()
    vowels = 'aeiou'
    string_exploded = explode(string)
    string_list = []
    for string_element in string_exploded:
        if string_element in vowels:
            string_list.append(string_element + 'p' + string_element)
        else:
            string_list.append(string_element)
    string_transformed_result = implode(string_list)
    return string_transformed_result.capitalize()

# print(to_p_sentence('Alamo'))
# print(to_p_sentence('Basico'))
# print(to_p_sentence('Raro'))

def to_p_sentence_2(string):
    string = string.lower()
    string_transformed_result = ''
    vowels = 'aeiou'
    for string_element in string:
        if string_element in vowels:
            string_transformed_result += string_element + 'p' + string_element
        else:
            string_transformed_result += string_element
    return string_transformed_result.capitalize()
# print('-------------------------------------')
# print(to_p_sentence_2('Alamo'))
# print(to_p_sentence_2('Basico'))
# print(to_p_sentence_2('Raro'))

def to_p_sentence_refactored(string):
    """
    :param string: recibe una cadena
    :return: devuelve una cadena modificada to_p_sentence(), pero
    solo modifica la vocal si el indice es par.
    """
    string = string.lower()
    string_transformed_result = ''
    vowels = 'aeiou'
    i = 0
    for string_element in string:
        if string_element in vowels:
            if i % 2 == 0:
                string_transformed_result += string_element + 'p' + string_element
                i += 1
            else:
                string_transformed_result += string_element
                i += 1
        else:
            string_transformed_result += string_element
            i += 1
    return string_transformed_result.capitalize()

#print(to_p_sentence_refactored('Atrapa'))

def foo(numbers_list):
    """
    :param numbers_list: recibe una lista de numeros
    :return: devuelve una lista aplicando modificada de acuerdo a las
    siguientes reglas:
    1. si el índice es par, el valor se multiplica por 2
    2. si el índice es divisible por 3, el valor se divide por 4
    3. sino, el valor se eleva al cuadrado.
    """
    result_list = []
    i = 0
    for number in numbers_list:
        if i % 2 == 0:
            result_list.append(number * 2)
            i += 1
        elif i % 3 == 0:
            result_list.append(number / 4)
            i += 1
        else:
            result_list.append(number ** 2)
            i += 1
    return result_list
print(foo([1,2,3,4,5,6,7,8,9,10]))



