# Sudoku Solver

## Description

This is a web-application built using Django, primarily with vanilla JavaScript, although refactored with React along the way.
Purpose of this tool was to create a self-generating sudoku puzzle to solve. Alternatively, if anyone needs help
solving sudoku from other source, like a magazine or other website, they can input these values into the custom section
of this web-app and get the solution automatically from the backend that uses the backtracking algorithm.

Currently, React is being added directly using HTML script tags. In the future possible division between back and front with React
fully installed, although for such a small project it might not be needed.

## Planned works

- If user provides invalid values in the custom section and tries to get a solution - show which cells exactly are invalid
- Consider changing prompting from Javascript's alert() to something more aesthetically pleasing
