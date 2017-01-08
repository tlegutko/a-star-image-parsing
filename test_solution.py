#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import itertools
import atexit

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def on_fail():
    global fail
    fail = True

def has_finished(car_state):
    return car_state[0] == car_state[1] == car_state[2] == car_state[3] == -1


if len(sys.argv) > 1:
    f = open(sys.argv[1])
    atexit.register(f.close)
else:
    eprint("Reading solution from standard input")
    f = sys.stdin

steps, cars = map(int, f.readline().split())
prev_states = None
fail = False

for step in range(steps):
    states = []
    for __ in range(cars):
        states.append(map(int, f.readline().split()))

    # check collisions
    for i in range(cars):
        car1 = states[i]
        if has_finished(car1):
            continue
        for j in range(i + 1, cars):
            if has_finished(car2):
                continue
            car2 = states[j]
            if car1[0] == car2[0] and car1[1] == car2[1]:
                eprint("Error: collision in step %d, cars %d and %d" % (step, i+1, j+1))
                on_fail()

    # check if achievable
    if prev_states:
        for i in range(cars):
            oldX, newX = prev_states[i][0], states[i][0]
            oldY, newY = prev_states[i][1], states[i][1]
            oldVx, newVx = prev_states[i][2], states[i][2]
            oldVy, newVy = prev_states[i][3], states[i][3]

            if has_finished(prev_states[i]):
                continue
            elif has_finished(states[i]):
                # check if legally moved to finished state
                if not oldVx == 0:
                    eprint("Error: Vx != 0 befor moving to finished state on step %d" % (step))
                    on_fail()
                if not oldVy == 0:
                    eprint("Error: Vy != 0 befor moving to finished state on step %d" % (step))
                    on_fail()
                continue

            if not oldVx - 1 <= newVx <= oldVx + 1:
                eprint("Error: illegal Vx change in step %d for car %d: %d -> %d" % (step, i+1, oldVx, newVx))
                on_fail()
            if not oldVy - 1 <= newVy <= oldVy + 1:
                eprint("Error: illegal Vy change in step %d for car %d: %d -> %d" % (step, i+1, oldVy, newVy))
                on_fail()
            if newX != oldX + newVx:
                eprint("Error: illegal X in step %d for car %d: <new X> %d != <old X> %d + <new Vx> %d" % (step, i+1, newX, oldX, newVx))
                on_fail()
            if newY != oldY + newVy:
                eprint("Error: illegal Y in step %d for car %d: <new Y> %d != <old Y> %d + <new Vy> %d" % (step, i+1, newY, oldY, newVy))
                on_fail()

    prev_states = states

print("Solution seems to be %s" % ("wrong" if fail else "OK"))
