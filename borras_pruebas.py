import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

ruta= "C:\\Users\\herre\\OneDrive\\Escritorio\\TESIS DE GRADO UNAL\\Tabla_Datos.xlsx"
datos = pd.read_excel(ruta)

df = pd.DataFrame(datos)
c=0
print(df.columns)
print(df.index)
media =np.mean(df)
desv =np.std(df)

for i in df.columns:
	print
	hist = sns.distplot(df[i],hist=True, kde=False, 
             bins=20, color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 1})
	#df.plot(kind='kde')
	c +=1
	path= 'C:\\Users\\herre\\OneDrive\\Escritorio\\TESIS DE GRADO UNAL\\Imagenes'
	plt.savefig(path + '\\'+ str(c) + '.png')
	print(c)

df.plot(kind='kde',legend=False, title='Sample Data Graph')
plt.grid(False)
path= 'C:\\Users\\herre\\OneDrive\\Escritorio\\TESIS DE GRADO UNAL\\Imagenes'
plt.savefig(path + '\\' 'Densidad.png')
#plt.show()