#!/usr/bin/env python

from muffins import *

from bounds import upper_bound

import pickle

bad = []

def run(m,s):
    global bad
    print len(bad),"total bad"
    print "Solving for m =",m,"and s =",s
    ans = solve(m,s)
    print "Solved"
    if ans[0] != ans[1]:
        bad.append((m,s))
        pickle.dump(bad,open("Failures.bin","wb"))

run(67,15)


        
