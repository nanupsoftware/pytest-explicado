"""
Quando é necessário levantar alguma exceção use o raises, que é uma função
nativa do pytest
"""
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
