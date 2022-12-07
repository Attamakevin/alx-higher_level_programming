#!/usr/bin/python3
# a function that computes the square value of all integers of a matrix
def square_matrix_simple(matrix=[]):
    new = []
    if not matrix:
        return new
    new = [[x**2 for x in row] for row in matrix]
    return new
