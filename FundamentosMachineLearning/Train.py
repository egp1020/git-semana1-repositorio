import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import math as m

# PERFECTO
df = pd.read_csv("files/pokemon.csv")
""" df = df.drop(["victorias"], axis=1)
df["victorias"] = [np.random.randint(4, 5)*df.iloc[i]["promedio"] for i in range(len(df))]
df.to_csv("files/pokemon.csv", index=False) """

""" x_pokemon = df.iloc[:, 6:7].values
y_pokemon = df.iloc[:, 7].values
print(x_pokemon)
print(y_pokemon)

x_train_pokemon, x_test_pokemon, y_train_pokemon, y_test_pokemon = train_test_split(x_pokemon, y_pokemon, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train_pokemon, y_train_pokemon)

#plt.scatter(x_train_pokemon, y_train_pokemon, color="green")
plt.scatter(x_test_pokemon, y_test_pokemon, color="green")
plt.plot(x_train_pokemon, regressor.predict(x_train_pokemon), color="blue")
plt.title("Promedio vs Victoria")
plt.xlabel("Promedio")
plt.ylabel("Victoria")
#plt.show()
print(regressor.score(x_test_pokemon, y_test_pokemon))
 """
# NO PERFECTO

#df =df.drop(["victorias"], axis=1)
#df["victorias"] = [np.random.randint(5, 7)*m.sqrt(df.iloc[i]["promedio"]) for i in range(len(df))]
#df.to_csv("files/pokemon.csv", index=False)

x = df.iloc[:,6:7].values
y = df.iloc[:,7].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .2, random_state = 0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

plt.scatter(x_test, y_test, color = "yellow")
plt.plot(x_train, regressor.predict(x_train), color = "green")
plt.title("Promedio vs Victoria")
plt.xlabel("Promedio")
plt.ylabel("Victoria")
plt.show()

print(regressor.score(x_test, y_test))



