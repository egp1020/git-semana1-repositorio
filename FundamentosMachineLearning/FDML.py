import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

""" np.array([10, 10, 24, 25, 62, 61])
a = np.array([10 , 104, 41, 550, 20 ,52])
#print(a[4])
b = a[3:]
#print(b)
b = a[3:5]
#print("segundo b: ", b)
b = a[2::2]
#print("tercer b: ", b)
b = np.zeros(5)
#print(b)
b = np.ones((4, 5)) #el primer número da filas, el segundo columnas.
#print(b)
#print(type(b))
#print(type(b[3][3]))
b = np.linspace(4, 11, 6)# primer argumento (numero inicial), segundo argumento (numero final), tercer argumento (cantidad de datos)
#print(b)
b = np.array([['x', 'y','z'], ['a', 'c', 'e']])
#print(b)
#print(type(b))
#print(b.ndim)
c = [12, 4, 10, 20, 31, 2]
c = np.sort(c)
#print(c)
cabeceras = [('nombre', 'S10'),('edad', int)]
datos = [('juan', 10), ('maria', 70), ('javier', 42), ('samuel', 15)]
usuarios = np.array(datos, dtype = cabeceras)
b = np.sort(usuarios, order = 'edad')
#print(b)
b = np.arange(25)
#print(b)

c = []
for i in range(25):
    c.append(i)
    #print(c)
b = np.full((3,5), range(10, 20, 2))
#print(b)
b = np.diag([1,2,3,4,5,6,7,8])
#print(b)
cabeceras = [('nombre', 'S20'), ('edad', int),('pais', 'S20')]
datos = [('edtefanis', 21, 'india'), ('mia khalifa', 27, 'india tambien'), ('josh', 775, 'no de india'), ('aselignsliingareoi', 1, 'alewribkbgaig')]
usuarios = np.array(datos, dtype=cabeceras)
b = np.sort(usuarios, order='pais')
#print(b)

# ------------------pandas-----------------
series = pd.Series([5,10,15,20,25])
#print(series)
#print(type(series))
#print(series[3])
cad = pd.Series(['p', 'l', 'a', 't', 'z', 'i'])
#print(cad)

lst = ['Hola', 'mundo', 'robotico']
df = pd.DataFrame(lst)
#print(df)
data = {'nombre': ['juan', 'ana', 'jose', 'arturo' ], 'Edad': [25, 18,32,25], 'Pais': ['MX', 'CO', 'BR', 'MX']}
df = pd.DataFrame(data)
#print(df)
#print(df[['nombre', 'Pais']])
data = pd.read_csv('files/canciones-2018.csv')#para leer el archivo separado por comas.
#data.head(5) #leer los primeros 5
#print(data)
artista = data.artists
#print(artista)
info = data.iloc[2]
#print(info)
#data.tail()
#print(data)
a = data.shape
#print(a)
a = data.columns
#print(data.columns)
a = data['tempo'].describe()
#print(a)
#data.sort_index(axis= 0, ascending= False)
#print(data)
a = data.sort_values(by='name', axis=0, ascending= True)
print(a[['id', 'name', 'artists']]) """


print("""# -----------------------------------------
#               Scikit-learn
# -----------------------------------------""")
"""
    * Variedad de modulos
    * Versatilidad
    * Facilidad de uso

    Importar modulos de scikit-learn (sklearn)
    from sklearn import [modelo]
"""


from sklearn import tree

df = pd.read_csv("files/pokemon.csv")
#df["victorias"] = [np.random.randint(0, 100) for i in range(len(df))]
""" df["fuerza"]=[np.random.randint(1,10) for i in range(len(df))]
df["defensa"]=[np.random.randint(1,10) for i in range(len(df))]
df["velocidad"]=np.random.rand(len(df))*100
print(df)
df.to_csv("files/pokemon.csv", index=False)
"""


dataset_salarios = pd.read_csv("files/salarios.csv")
print(dataset_salarios)
print(dataset_salarios.head(5))
print(df.head(3))
print("---------------------------------------")
print(dataset_salarios.shape)
print("---------------------------------------")
print(dataset_salarios.columns)
print("---------------------------------------")

print("              SALARIOS")
x_salarios = dataset_salarios.iloc[:, :-1].values
y_salarios = dataset_salarios.iloc[:, 1].values
""" print("salarios \n", x_salarios)
print(y_salarios)
x_train, x_test, y_train, y_test = train_test_split(x_salarios, y_salarios, test_size=0.2, random_state=0)

print(x_train,"\n", x_test,"\n", y_train,"\n", y_test) """
"""
lista_promedio = []
for fila in range(len(df)):
    suma = df.iloc[fila]["fuerza"] + df.iloc[fila]["defensa"]
    promedio = suma/2
    lista_promedio.append(promedio)

df["promedio"] = lista_promedio
print("PROMEDIO: \n", df) 
df.to_csv("files/pokemon.csv", index=False)
"""


print("---------------------------------------")
print("            POKEMON")
x_pokemon = df.iloc[:, -1:].values
y_pokemon = df.iloc[:, 6].values
""" print(x_pokemon)
print(y_pokemon) """
print("---------------------------------------")
x_train_pokemon, x_test_pokemon, y_train_pokemon, y_test_pokemon = train_test_split(x_pokemon, y_pokemon, test_size=0.2, random_state=0)
#print(x_train_pokemon,"\n", x_test_pokemon,"\n", y_train_pokemon,"\n", y_test_pokemon)

regressor = LinearRegression()
regressor.fit(x_train_pokemon, y_train_pokemon)
#viz_train = plt
#plt.scatter(x_train_pokemon, y_train_pokemon, color="green")
""" plt.scatter(x_test_pokemon, y_test_pokemon, color="green")
plt.plot(x_train_pokemon, regressor.predict(x_train_pokemon), color="blue")
plt.title("Promedio vs Victoria")
plt.xlabel("Promedio")
plt.ylabel("Victoria")
plt.show()   """

print(regressor.score(x_test_pokemon, y_test_pokemon))
