import matplotlib.pyplot as plt

labels = 'Python', 'JavaScript', 'GoLang', 'Java', 'C++', 'PHP'
sizes = [215, 130, 245, 210, 130, 200]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'blue']
explode = (0, 0, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title("Bahasa Pemrograman Favorit\n")
plt.show()
