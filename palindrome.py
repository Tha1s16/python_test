# Um palíndromo é uma sequência que pode ser lida da mesma forma de trás para frente.

def is_palindrome(original_string):
    reversed_str = ''.join(reversed(original_string))
    return original_string == reversed_str  # Verifique se a palavra original é a mesma que sua versão invertida.


def test_is_palindrome():
    input_str = "arara"
    result = is_palindrome(input_str)

    assert result == True

    print("Teste Aprovado! " + input_str + " é um palíndromo!")
