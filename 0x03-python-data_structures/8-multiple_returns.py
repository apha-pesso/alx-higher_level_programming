#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if sentence is None:
        a = None
    return (a, sentence[0])
