# Função que inverte uma string
def reverse_string(word):
    return ''.join(reversed(word))


# Teste da função reverse_string
def test_reverse_string():
    input_str = "TripleTen"

    reversed_str = reverse_string(input_str)

    assert reversed_str == "neTelpirT"

    print("Teste Aprovado! " + input_str + " invertido é " + reversed_str)