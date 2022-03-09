from tkinter import CENTER
from matplotlib import pyplot as plt, pyplot as plt
x=[2015,2017,2019]
y=[12000,10000,16000]
x2=[2014,2016,2018,2020]
y2=[5000,4000,6000,10000]
plt.bar(x,y,color='b',align='center',label='Indan')
plt.bar(x2,y2,color='g',align='center',label='Srilanka')
plt.title('Population')
plt.xlabel('Year')
plt.legend()
plt.show()