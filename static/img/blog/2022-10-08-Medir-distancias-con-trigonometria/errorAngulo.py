# %matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# sacado de https://martinaramayo.gitlab.io/posts/improve-your-matplotlib-plots-with-this-post/
style_args = {
    "font.family":       "serif",
    "font.size":         12,
    "text.usetex":       True,
    "axes.titlesize":    15,
    "axes.labelsize":    18,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "xtick.bottom":      True,
    "xtick.color":       "black",
    "xtick.labelsize":   15,
    "ytick.left":        True,
    "ytick.color":       "black",
    "ytick.labelsize":   15,
    "legend.fontsize":   12,
    "pgf.rcfonts":       False,
}
plt.style.use(style_args)

# creamos los valores
x = np.linspace(0,89.5,100)
y = 1 / ( np.cos(x * 2 * np.pi/360)**2 )

# creamos el grafico con especificando estilo y demas detalles
fig, ax = plt.subplots()
ax.plot(x,y, color='red')
ax.axvline(x=90, color='black', ls='--')

ax.set_ylim([-0.5,95.5])
ax.set_xlim([-0.5,95.5])

ax.xaxis.set_ticks(np.arange(0, 100, 10))
ax.yaxis.set_ticks(np.arange(0, 100, 10))

ax.set_xlabel(r'$\alpha (\mathring{ \ })$')
ax.set_ylabel(r'$sec^2(\alpha)$')

# lo guardamos en un png
fig.tight_layout()
fig.savefig('errorAngulo.png',)
 
