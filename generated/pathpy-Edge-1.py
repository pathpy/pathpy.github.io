import pathpy as pp
ab = pp.Edge('a','b')
net = pp.Network()
net.add_edge(ab)
plt = net.plot()
plt.show('png')