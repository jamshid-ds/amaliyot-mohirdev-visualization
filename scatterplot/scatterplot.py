# -*- coding: utf-8 -*-
"""04-VISUAL-AMALIYOT-03-scatterplot-JAVOBLAR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14zm1Mq7B9Yi7eN5i14lPw50SHrkASTl0

![Imgur](https://i.imgur.com/5pXzCIu.png)

# Data Science va Sun'iy Intellekt Praktikum

## 4-MODUL. VIZUALIZASIYA

## 3-AMALIYOT. `scatterplot`
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""### Ushbu amaliyotda uybor.uz saytidan yuklab olingan ma'lumotlar tahlili bilan shu'gullanamiz."""

df = pd.read_csv("https://github.com/anvarnarz/praktikum_datasets/blob/main/uybor_scrapping.csv?raw=true")
df.head()

"""#### Yuqoridagi jadvalda Toshkent shahridagi sotildagian uylar haqida ma'lumotlar jamlangan.

### 1-VAZIFA. Uylarning narxi (`price`) va maydoni (`size`) o'rtasida bog'liqlikni ko'rsatuvchi scatter plot chizing.
"""

#JAVOBINGIZNI SHUYERGA YOZING
plt.figure(figsize=(10,6))
sns.scatterplot(data=df,x='price',y='size')
plt.show()

"""### Jadvalda 7000 dan oshiq uy bor, aksar uylarning maydoni 250kv.m dan kam. Keling noodatiy katta qiymatlarni tashlab yuboramiz va yuqoridagi chizmani qaytadan chizamiz."""

#JAVOBINGIZNI SHUYERGA YOZING
df = df[df['size']<250]
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='size',y='price')
plt.show()

"""### 2-VAZIFA. Uylarning narxi (price) va maydoni (size) o'rtasida bog'liqlikni ko'rsatuvchi scatter va to'g'ri chiziqni chizing."""

# JAVOB UCHUN JOY
df = df[df['size']<250]
plt.figure(figsize=(10,6))
sns.regplot(data=df, x='size',y='price')
plt.show()

"""### 3-VAZIFA. Uylarning narxi, maydoni va xonalar soni o'rtasidagi bog'liqlikni ko'rsating."""

#@title Kutilgan natija
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='size', y='price', hue='rooms')
plt.show()

"""### 4-VAZIFA. Uylarning narxi, maydoni va tumanlar o'rtasidagi bog'liqlikni ko'rsating."""

# JAVOBNI SHUYERGA YOZING
df = df[df['size']<250]
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='size',y='price',hue="district")
plt.show()

"""### 5-VAZIFA. Swarm ploit yordamida turli tumanlardag uylarning narxini taqqoslang."""

# JAVOB UCHUN JOY
plt.figure(figsize=(10,6))
sns.swarmplot(data=df, x='district', y='price')
plt.xticks(rotation=90)
plt.show()

