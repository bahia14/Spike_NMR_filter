#!/usr/bin/env python 
# encoding: utf-8

"""
This module contains several utilities for baseline correction of spectra


Created by Marc-Andre on 2015-03-26.

"""

from __future__ import print_function
from scipy.optimize import minimize
import numpy as np
#from numpy.polynomial.legendre import legval as poly
import unittest

def poly(x,coeff):
    "computes the polynomial over x with coeff"
    lcoeff = list(coeff)
    y = np.zeros_like(x)
    y += lcoeff.pop()    # a
    while lcoeff:
        y *= x          # ax + b
        y += lcoeff.pop()
    return y

def fitpolyL1(x, y, degree=2, power=1, method="Powell"):
    "fit with L1 norm a polynome to a function y over x, returns coefficients"
    coeff0 = [0]*(degree+1)
    #pmin = lambda c, x, y: np.sum(np.abs(y-poly(x,c)) )
    pmin = lambda c, x, y: np.sum(np.power(np.abs(y-poly(x,c)), power) )
    res = minimize(pmin, coeff0, args=(x,y), method=method)
    return res.x

def bcL1(y, degree=2, power=1, method="Powell"):
    "compute a baseline on y using fitpolyL1"
    x = np.arange(1.0*y.size)
    coeff = fitpolyL1(x, y, degree=degree, power=power, method=method)
    return poly(x,coeff)

def baseline(y, degree=2, power=1, method="Powell", chunksize=2000):
    """
    compute a piece-wise baseline on y using fitpolyL1
    degree is the degree of the underlying polynome
    chunksize defines the size of the pieces
    a cosine roll-off is used to smooth out chunks junctions

    y - baseline(y) produces a baseline corrected spectrum
    """
    nchunk = y.size/chunksize
    if nchunk <2:
        bl = bcL1(y, degree=degree, power=power, method=method)
    else:
        lsize = y.size/nchunk
        recov = lsize/10  # recovering parts
        corr = np.linspace(0.0,1.0,2*recov)
        corr = np.sin( np.linspace(0,np.pi/2,2*recov) )**2  # cosine roll-off
        corrm1 = 1.0-corr
        bl = np.zeros_like(y)
        bl[0:lsize+recov] = bcL1(y[0:lsize+recov], degree=degree, power=power)
        i = 0 # if nchunk == 2 !
        for i in range(1,nchunk-1):
            tbl = bcL1(y[i*lsize-recov:(i+1)*lsize+recov], degree=degree, power=power)
            bl[i*lsize-recov:i*lsize+recov] = bl[i*lsize-recov:i*lsize+recov]*corrm1 + tbl[:2*recov]*corr
            bl[i*lsize+recov:(i+1)*lsize+recov] = tbl[2*recov:]
        i = i+1
        tbl = bcL1(y[i*lsize-recov:-1], degree=degree)
        bl[i*lsize-recov:i*lsize+recov] = bl[i*lsize-recov:i*lsize+recov]*corrm1 + tbl[:2*recov]*corr
        bl[i*lsize+recov:] = tbl[2*recov-1:]
    return bl


def minbl(bl, y):
    '''
    Used in correctbaseline for making the fusion of the intermediate baseline with the points under the baseline. 
    '''
    blmin = bl.copy()
    blmin[bl-y>0]=y[bl-y>0]
    return blmin

def correctbaseline(y, iterations=1, chunksize=100, firstpower=0.3, secondpower=7, degree=2,  chunkratio=1.0, ymaxratio = 1.0, method="Powell", debug = False):
    '''
    Find baseline by using low norm value and then high norm value to attract the baseline on the small values.
    iterations : number of iterations for convergence toward the small values. 
    chunksize : size of each chunk on which is done the minimization.
    firstdeg : degree used for the first minimization 
    degree : degree of the polynome used for approaching each signal chunk. 
    chunkratio : ratio for changing the chunksize inside main loop
    ymaxratio : ratio for cutting the spectrum to a maximal values (avoids issues with water pick)
    '''
    ylim = y.max()*ymaxratio
    z = np.ones(y.size)*ylim
    y[y>ylim] = z[y>ylim]
    bl = baseline(y, degree=degree, power=firstpower, chunksize = chunksize, method="Powell")
    bls = {'bl':[], 'blmin':[]}
    for i in range(iterations):
        blmin = minbl(bl, y)
        bl = baseline(blmin, degree=degree, power=secondpower, chunksize = int(chunksize*chunkratio), method=method)
        bls['bl'].append(bl)
        bls['blmin'].append(blmin)
    if debug:
        return bl, bls
    else:
        return bl

class BC_Tests(unittest.TestCase):
    def test_poly(self):
        "tests the poly function"
        p = poly(np.arange(10.0),(.1,.2,.3,.4))
        self.assertEqual(p[6], 98.5)
        self.assertAlmostEqual(sum(p), 905.5)
    def test_baseline(self):
        N = 100000
        x = np.linspace(0,10,N)
        y = np.sin(x/2) + 0.2*np.random.randn(N)
        b = baseline(y,chunksize=N/20)
        corr = y-b
        self.assertTrue(np.std(corr) < 0.21)
    def test_correctbaseline(self):
        N = 100000
        x = np.linspace(0,10,N)
        y = np.sin(x/2) + 0.2*np.random.randn(N)
        b = correctbaseline(y, iterations=10, chunksize=N/20)
        corr = y-b
        self.assertTrue(np.std(corr) < 0.25)
        
if __name__ == '__main__':
    unittest.main()

