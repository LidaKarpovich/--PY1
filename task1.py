from pprint import pprint

dict_ = [{'dec': number, 'bin': bin(number), 'hex': hex(number), 'oct': oct(number)} for number in range(0, 16)]
list_of_dict = [value for value in dict_]

pprint(dict_)