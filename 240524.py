# -*- coding: utf-8 -*-
"""240524.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VIWi3b5sV6msxig99Gjq5lnCf_QbvzT2
"""

#데이터 파일 읽어오기
import pandas as pd
iris_df=pd.read_csv('iris.csv')
iris_df

#데이터의 기본 정보 출력
iris_df.info()

iris_df.describe()

iris_df['species'].value_counts()

iris_df.isnull().sum()

#중복 데이터 확인하기
iris_df[iris_df.duplicated()]

#중복 데이터 모두 확인하기
idx=(iris_df['sepal_length']==5.8) & (iris_df['petal_width']==1.9)
iris_df.loc[idx,:]

iris_df2=iris_df.drop_duplicates()

iris_df2

iris_df2.groupby('species').sum()

iris_df2.groupby('species').mean()

import matplotlib.pyplot as plt
sepal_length = iris_df2['sepal_length']
plt.bar(range(len(sepal_length)), sepal_length)
plt.show()

sepal_length_mean = iris_df2.groupby('species')['sepal_length'].mean()
sepal_length_mean

plt.bar(sepal_length_mean.index, sepal_length_mean.values, color='skyblue')
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length (cm)')
plt.title('Mean Sepal Length of Iris Species')
plt.show()

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# sepal_length
axes[0, 0].hist(iris_df2['sepal_length'], color='skyblue', edgecolor='black')
axes[0, 0].set_title('Sepal Length Histogram')
axes[0, 0].set_xlabel('Sepal Length (cm)')
axes[0, 0].set_ylabel('Frequency')

# sepal_width
axes[0, 1].hist(iris_df2['sepal_width'], color='skyblue', edgecolor='black')
axes[0, 1].set_title('Sepal Width Histogram')
axes[0, 1].set_xlabel('Sepal Width (cm)')
axes[0, 1].set_ylabel('Frequency')

# petal_length
axes[1, 0].hist(iris_df2['petal_length'], color='skyblue', edgecolor='black')
axes[1, 0].set_title('Petal Length Histogram')
axes[1, 0].set_xlabel('Petal Length (cm)')
axes[1, 0].set_ylabel('Frequency')

# petal_width
axes[1, 1].hist(iris_df2['petal_width'], color='skyblue', edgecolor='black')
axes[1, 1].set_title('Petal Width Histogram')
axes[1, 1].set_xlabel('Petal Width (cm)')
axes[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

plt.scatter(x=df['petal_length'], y=df['petal_width'])
plt.show()
