# HillsValleysCastles
Originally part of my Codility screen for IG application. Done in about an hour, most of which was spent sorting out the off-by-one errors in the recursion.

A variation of the standard peaks/valleys algorithm, this one iterates through an array of digits that indicates a set of heights and defines a hill/valley as any continuous segment surrounded by lower or higher values, then returns the total number of found hills/peaks as an answer. Values at the beginning/end of the array can be treated as either lower/higher. 

In the case of [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5], we have [2,2], [4], [1,1], and [5] for a total of four peaks/hills.. 
