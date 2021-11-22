"""
-Para criar nosso primeiro test com Pytest Vamos criar uma função bem simples chamada
func a princípio, apenas com caráter de mostrar como funciona o framework.

-Para executar o teste, execute o comando:
    pytest test_sample.py

Quando executamos o teste test_answer é realizado um assert para verificar se o retorno
da função func é igual a 5, neste caso o teste vai passar 100% pois 5 é igual 5.

-Ao final será possivel conferir se o teste passou e qual a porcentagem de cobertura.
"""


def func(number):
    return number + 1


def test_answer():
    assert func(4) == 5
