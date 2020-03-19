import pathpy as pp
p = pp.Path('a','b','c','d')
net = pp.Network()
net.add_path(p)
plt = net.plot()
plt.show('png')