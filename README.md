# Graph
Simple Graph Class file and Demo file

graph.py defines a class called Graph. This class will accept an input function, plot it, and save the file.
  The class runs the function over the domain [0 10] and range [0 10]. This is also the window of the plot produced.
  The function is evaluated at a step size of 0.1.
  
graph_demo.py shows a sample version of how to call this code.
  You may call this class as shown, g1=Graph().
    Note: the default function is y=x. You may input a function here.
  You may call the plot as g1.plot("title").
    This title will appear on the graph, and the file with save as a png named with the "title" input.
