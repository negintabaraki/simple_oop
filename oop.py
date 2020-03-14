
class graph:
    a = 0
    my_node_dict = {}
    my_link_dict = {}
    def add_node(self,x,y):
        graph.a += 1
        graph.my_node_dict[graph.a] = (x,y)
        print(graph.my_node_dict)
    def add_link(self,in_node,out_node,des):
        graph.my_link_dict[in_node,out_node] = des
        print(graph.my_link_dict)
    def del_node(self,a):
        del graph.my_node_dict[graph.a]
        print(graph.my_node_dict)
    def del_link(self,in_node,out_node):
        del graph.my_link_dict[(in_node,out_node)]
        print(graph.my_link_dict)

class node(graph):
    def __init__(self,id,location,degree):
        self.id = id
        self.location = location
        self.degree = degree

class link(graph):
    def __init__(self,in_id,out_id):
        self.in_id = in_id
        self.out_id = out_id

x = graph()
x.add_node(556.5,200)
x.add_link(1,2,599)
x.del_node(1)
x.del_link(1,2)
y = node(1,2,5)
print(y.id)



#To_Do  degree,git