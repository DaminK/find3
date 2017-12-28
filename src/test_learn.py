from learn import *
from server import *

def test_to_base64():
  assert to_base64("testdb") == "dGVzdGRi"

def basic_learning():
    ai = AI()
    ai.learn('../testing/testdb.csv')
    ai.save('dGVzdGRi.de0gee.ai')

def test_basic_learning(benchmark):
    result = benchmark(basic_learning)

def basic_classifying():
    ai = AI()
    ai.load('dGVzdGRi.de0gee.ai')
    return ai.classify()

def test_basic_classifying(benchmark):
    result = benchmark(basic_classifying)

def basic_reloading():
    ai = AI()
    ai.load('dGVzdGRi.de0gee.ai')
    return True

def test_basic_reloading(benchmark):
    result = benchmark(basic_reloading)
    