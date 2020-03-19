import pathpy as pp
cd = pp.Edge('c','d',directed=False)
net = pp.Network(directed=False)
net.add_edge(cd)
plt = net.plot()
plt.show('png')