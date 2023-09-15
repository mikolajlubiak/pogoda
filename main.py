# Importuj potrzebne biblioteki
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

mpl.use('Agg')

# Wczytaj dane z pliku CSV
data = pd.read_csv('main.csv')

# Wyświetl początkowe rekordy danych
print(data.head())

# Sprawdź podstawowe informacje o danych
print(data.info())

# Podsumowanie statystyk opisowych
print(data.describe())

# Histogramy kilku wybranych zmiennych
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.histplot(data['fixed acidity'], bins=30, kde=True, color='blue')
plt.title('Histogram Fixed Acidity')

plt.subplot(2, 2, 2)
sns.histplot(data['volatile acidity'], bins=30, kde=True, color='green')
plt.title('Histogram Volatile Acidity')

plt.subplot(2, 2, 3)
sns.histplot(data['alcohol'], bins=30, kde=True, color='red')
plt.title('Histogram Alcohol')

plt.subplot(2, 2, 4)
sns.histplot(data['pH'], bins=30, kde=True, color='purple')
plt.title('Histogram pH')

plt.tight_layout()
plt.show()
plt.savefig('wykres1.png')

# Wykres zależności między dwiema zmiennymi
plt.figure(figsize=(8, 6))
sns.scatterplot(x='alcohol', y='quality', data=data, color='blue', alpha=0.5)
plt.title('Wykres zależności Alcohol vs. Quality')
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.savefig('wykres2.png')
