"""
Recibes un misterioso email de una lamasería en el Tíbet. Te encargan crear una función que recibe una cadena y debes de comprobar si pasa un cierto test, devolviendo un booleano.

¡No es más que un predicado! piensas mientras lees el resto del mensaje. El test es relativamente sencillo:

la cadena tiene que tener 9 letras, ni más ni menos.
no puede contener números, sólo letras del alfabeto español "abcdefghijklmnñopqrstuvwxyz"
las letras tienen que estar en minúsculas (las mayúsculas no son aceptables)
la cadena no puede contener más de 3 consonantes seguidas. Puede no tener ninguna, una, dos o tres, pero nunca 4 o más.
Además, te especifican que consideran como consonantes las siguientes letras: "bcdfghjklmnñpqrstvwxyz".

Te aportan algunos ejemplos:

"aaaaaa" No es válida (longitud)
"o22iUijpq" No es válida (contiene números y mayúsculas)
"auertctoa" No es válida (demasiadas consonantes seguidas)
"aaaaaaaaa" es válida
"azaxaaktp" es válida
"aoieyasul" es válida
"""

def letters_limit(string,limit=9):
  """
  recibe una cadena, verifica que la cadena solo tenga 9 elementos dentro
  del abecedario español. devuelve false si es mas o menos de 9 elementos y
  false si contiene algun otro caracter fuera de la variable alphabet
  """
  between_string_limit = True
  alphabet = "abcdefghijklmnñopqrstuvwxyz"
  if len(string) == limit:
      for string_element in string:
          if string_element not in alphabet:
              between_string_limit = False
              break
  else:
      between_string_limit = False
  return between_string_limit
#print(letters_limit("aolaautfu"))

def only_lowercase(string):
    """
    :param string: recibe una cadena que debe solo contener letras en minuscula
    :return: retorna falso si hay algun caracter en mayuscula y verdaero si todos los
    caracteres estan en minusculas
    """
    result_only_lowercase = False
    if string == '' or string == ' ':
        return False
    if string == string.lower():
        result_only_lowercase = True
    return result_only_lowercase

#print(only_lowercase('gtzhdjahab'))

def consonants_limit(string,limit = 3):
    """
    :param string: recibe una cadena de caracteres
    :param limit: la cadena de caracteres no debe tener más de 3 consonantes
    repetidas
    :return: devuelve False si hay más de 3 consonantes seguidas
    """
    result_consonants_within_limit = True
    consonants_occ = 0
    consonants = "bcdfghjklmnñpqrstvwxyz"
    for string_element in string:
        if string_element in consonants:
            consonants_occ += 1
            if consonants_occ > limit:
                result_consonants_within_limit = False
                break
        else:
            consonants_occ = 0
    return result_consonants_within_limit

def is_valid_name_for_god(string):
    """
    :param string: cadena de caracteres que debe ser verificada con una serie de predicados
    :return: devuelve un booleano True o False, devuelve True si la cadena cumple con las
    siguientes condiciones:
    1. la cadena tiene que tener 9 letras, ni más ni menos.
    2. no puede contener números, sólo letras del alfabeto español "abcdefghijklmnñopqrstuvwxyz"
    3. las letras tienen que estar en minúsculas (las mayúsculas no son aceptables)
    4. la cadena no puede contener más de 3 consonantes seguidas. Puede no tener ninguna, una, dos o tres, pero nunca 4 o más.
    """
    result_is_valid_name = False
    if string != str(string):
        return False
    if only_lowercase(string):
        if letters_limit(string):
            if consonants_limit(string):
                result_is_valid_name = True
    return result_is_valid_name

print(is_valid_name_for_god('aaaaa'))
print(is_valid_name_for_god('o22iUijpq'))
print(is_valid_name_for_god('auertctoa'))
print(is_valid_name_for_god('aaaaaaaaa'))
print(is_valid_name_for_god('azaxaaktp'))
print(is_valid_name_for_god('aoieyasul'))
print(is_valid_name_for_god(8))




