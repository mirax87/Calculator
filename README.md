# Calculator

A basic command-line calculator to add, subtract, multiply and divided numbers. 

# Usage
```
> python Calculator.py "<operations>"
```
## Example
```
> python Calculator.py "5+3"
8
```

# How does it compute the results?

The calculator takes [infix notation](https://de.wikipedia.org/wiki/Infixnotation) and converts it to a postfix notation using the [Shunting Yard algorithm](https://de.wikipedia.org/wiki/Shunting-yard-Algorithmus). The postfix notation is then converted into a tree structure, which recursively evaluates the nodes and thereby computes the results. 

# Keywords
calculator, expression trees, algorihtm implementation, unittesting, python module packaging, python2, python
