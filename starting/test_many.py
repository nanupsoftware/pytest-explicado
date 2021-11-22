"""
Para executar vários testes simultaneamente é necessário que o nome
do seu teste comece  com 'test_*.py' ou *_test.py, ou seja, seu teste
precisa conter a string 'test' seja no início ou no fim de seu arquivo.

A razão para o nome do seu arquivo ter essa string é que quando executamos o pytest
é realizado uma varredura em seu diretório procurando por arquivos relacionados a
seus testes; por fim não se esqueça de identificar seu diretório de testes como
um módulo(usando o __init__), para o pytest reconhecê-los.
"""