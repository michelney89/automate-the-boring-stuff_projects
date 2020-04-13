#! python3
"""
printTable.py - from list of string to nice table
Author : Michel NEY
Date : 2020-04-13
idea from 'Automate the boring Stuff' Book p.143
"""

def printTable(tableData):
    """Function that takes a list of lists of strings and displays it in a well-organized table
    with each column right-justified. Assume that all the inner lists will contain the same number of strings."""

    n1= len(tableData[0])
    n2 = len(tableData)

    # Get max str length of each column using list comprehension
    colWidths = [max([len(tableData[a][b]) for b in range(n1)]) for a in range(n2)]

    for j in range(n1):
        for i in range(n2):
            # print all elements of a line with corresponding justify width
            print(tableData[i][j].rjust(colWidths[i]), end=' ')
        print()  # Begin a new line


print(printTable([['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]))
