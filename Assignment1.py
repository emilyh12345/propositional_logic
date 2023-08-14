# CSCI 220/620
# Summer 2022
# Assignment 1 - Propositional Logic
# Emily Haller


import inspect
import pandas as pd #pandas package for data science, as creates an aleas so dont need to write pandas
from itertools import product


def get_func_body(f):
    body = inspect.getsource(f) # gets the code
    idx = body.index("return") #get part after return
    return '"' + body[7+idx:].strip() + '"'


def f_not(x):
    return not x #~x didnt work


def f_and(x, y):
    return x and y #x & y


def f_or(x, y):
    return x or y #x \y


def f_xor(x, y):
    return x ^ y


def f_impl(x, y):
    return not x or y


def f_bi_impl(x, y):
    return f_impl(x, y) and f_impl(y, x)


def f_rev_impl(x, y):
    return f_impl(y, x)


def f0(p, q, r):
    return (p or q) and r


def f1(p):
    return p and not p # (p & ~p)


def f2(p):
    return p or not p # (p | ~p)


def f3(p, q):
    return not p and f_impl(p, q)


def f4(p, q):
    return f_impl(p, q) or f_rev_impl(p, q)


def f5(p,q):
    return (p or q) or (not p and not q)


def f6(p, q):
    return (p or q) and (not p and not q)


def f7(p, q, r):
    return f_impl(p, q) and f_impl(q, r)


# Hypothetical syllogism
def f8(p,q,r):
    return f_impl(f_impl(p, q) and f_impl(q, r), f_impl(p, r))


# DeMorgans first law
def f9(p, q):
    return f_bi_impl(not (p or q), (not p and not q))


# DeMorgans second law
def f10(p, q, r):
    return f_bi_impl(not(p and q), (not p or not q))


def f11(p, q):
    return f_bi_impl(not(p or (not p and q)), (not p and not q))


def f12(p, q, r):
    return f_bi_impl(not (f_impl(p, q)) or f_impl(r, p), (p or not r or p) and (not q or not r or p))


# https://stackoverflow.com/questions/29548744/creating-a-truth-table-for-any-expression-in-python
def truth_table(f): #creates truth table in data frame format
    values = [list(x) + [f(*x)] for x in product([False,True], repeat=f.__code__.co_argcount)]
    return pd.DataFrame(values,columns=(list(f.__code__.co_varnames) + [f.__name__])) #grid


def analyze_truth_table(f): #analyzes number of rows, variables, etc
   tt = truth_table(f)
   tt_rows = tt.shape[0]
   tt_cols = tt.shape[1]
   tt_vars = tt_cols - 1
   tt_type = None
   last_col = tt.iloc[:, tt_vars]
   if last_col.all(): #if all last columns are true then its a tautology
       tt_type = "Tautology"
   elif last_col.any(): #else if anything is true its a contingency(know from above not all true)
       tt_type = "Contingency"
   else: #else if nothing is true its a contradiction
       tt_type = "Contradiction"
   print("Name:", f.__name__, get_func_body(f)) # get the body of the function
   print(tt)
   print("Rows:", tt_rows, ", Cols:", tt_cols, "Vars:", tt_vars, ", Type:", tt_type)
   print() # blank line at end of function


def main():
    #before deleted said: analyze_truth_table(f0) then tried for each f, which printed table for f
    functions = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]
    for function in functions: # iterate through functions which is a list
        analyze_truth_table(function) # pass in the functions


if __name__ == "__main__":
    main()

