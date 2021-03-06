# -*- coding: utf-8 -*-
"""Covid19 Indonesia Total Cases (18/03/2020 - 23/08/2021).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xXHJSr7blr1_tKRddKllOSGFQwCmNxGu

**Persiapan Data**
"""

import pandas as pd
import numpy as np

df = pd.read_excel('COVID-19 di Indonesia @kawalcovid19.xlsx', sheet_name='Timeline')

df.columns

"""**Pengambilan Posisi Data yang Dibutuhkan**"""

#mengambil baris data yang diperlukan (baris 0 - 524)
df = df.iloc[:524, :]

#drop kolom yang tidak diperlukan
df = df.drop(columns=['?', 'Unnamed: 36'])
df

#Set Index pada kolom "Total Kasus"
df = df.set_index('Total Kasus')

#menghilangkan tanda koma (,) pada angka ribuan di DataFrame
df = df.replace(",", "", regex=True)

#konversi DataFrame ke tipe numeric data
df = df.apply(pd.to_numeric)

df.tail()

"""**Persiapan Library bar_chart_race**"""

#Install library bar chart race

!pip install bar_chart_race

"""**Visualisasi**"""

#Membuat visualisasi menggunakan bar chart race

#import library
import bar_chart_race as bcr

#Membuat summary berupa total kasus untuk ditampilkan di bar chart race
def summary(values, ranks):
  total_cases = round(values.sum(), 0)
  s = f'Total Cases : {total_cases:,.0f}'
  return {'x': .99, 'y': .05, 's': s, 'ha': 'right', 'size': 9}

#Eksekusi visualisasi bar chart race
bcr.bar_chart_race(df=df, title = "Covid-19 Total Cases in Indonesia (18 Mar 2020 - 23 Aug 2021)", 
                   n_bars=10, orientation='h', fixed_order= False, cmap = 'prism', 
                   period_summary_func=summary, perpendicular_bar_func='mean')