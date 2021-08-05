# Crost Api
## Example
main.py
``` python
import api

def start(pygame):
    print('Started!')
api.add(start)

def update(args):
    print('Updated!', len(players), 'players')
api.add(update)
```
api.py
``` python
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
```
## Functions
### On start
``` python
def start(pygame):
    pygame
```
### On update
``` python
def update(args):
    args.pygame
    args.window
    args.scene
    args.bots
    args.players
    args.player
    args.chat
```
### On key pressed
``` python
def keyPressed(key):
    key
```
### On mouse pressed
``` python
def mousePressed(side):
    side
```
### On mouse move
``` python
def mouseMove(before, after):
    before
    after
```
### On mouse scroll
``` python
def mouseScroll(x):
    x
```
### On transition
``` python
def transition(before, after):
    before
    after
```
### On player join
``` python
def playerJoin(player):
    player
```
### On player disconnect
``` python
def playerDisconnect(player):
    player
```
### On message
``` python
def message(player, msg):
    player
    msg
```
### On command
``` python
def command(cmd, args):
    cmd
    args
```
