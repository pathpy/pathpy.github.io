import pathpy as pp
u = pp.Node('u', color='green', shape='rectangle')
net = pp.Network()
net.add_node(u)
plt = net.plot()
plt.show('png')