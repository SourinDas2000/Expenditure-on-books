
'''                       
              Expenditure On Books : 

          1996-1997           1997-98

        Economis - 5200     Econimics - 8000
        Commerce - 10000    Commerce - 14000
        Math - 5000         Math - 7000
        Language - 6000     Language - 6000                                                                     

'''


import matplotlib.pyplot as plt


plt.style.use('ggplot')


# Data :
    
labels = ['Econimics', 'Commerce', 'Math', 'Languages']

scale1 = [5200, 10000, 5000, 6000]

scale2 = [8000, 14000, 7000, 6000]


# Ploting the data :
    
plt.pie(scale2, labels = labels, radius = 1, autopct = '%1.1f%% \n (1997-98)', startangle = 90, pctdistance = 0.77, textprops = {'family' : 'Serif', 'fontweight' : 'bold'})

plt.pie(scale1, radius = 0.60, autopct = '%1.1f%% \n (1996-97)', startangle = 90,textprops = {'family' : 'Serif', 'fontweight' : 'bold'})

plt.title('Expenditure On Books')

plt.legend(loc = 'center left')

plt.tight_layout()

plt.axis('equal')

plt.show()


''' Created By Sourin Das '''
