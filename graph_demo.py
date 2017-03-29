from graph import Graph

def f(x):
	return x**2

g1 = Graph()
g1.plot("Linear Function")

g2 = Graph(f)
g2.plot("Quadratic Function")