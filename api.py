import sys
import pickle
import os
import shutil

functions = {}

def add(func):
    name = func.__name__
    functions.update({name: func})

def start():
    func = sys.argv[1]
    arguments = []
    for i in sys.argv:
        if i != sys.argv[0] and i != sys.argv[1]:
            arguments.append(pickle.loads(i))
    functions[func](**arguments)
