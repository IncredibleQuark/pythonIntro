import matplotlib.pyplot as plt

# Basic plot
# years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
# pops = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]
# deaths = [1.2, 1.7, 1.8, 2.0, 2.2, 2.2, 2.3, 2.1, 2.7, 3.0, 3.3, 3.0, 3.4, 3.5]
#
# lines = plt.plot(years, pops, years, deaths)
# # plt.plot(years, pops, color=(255/255, 100/255, 100/255))
# # plt.plot(years, deaths, '--', color=(0, 0, 0))
# plt.grid(True)
# plt.setp(lines, color=(1, .4, .4), marker="o")
#
# plt.ylabel("World population in billions")
# plt.xlabel("Year")
# plt.title("Population growth by year")
# plt.show()


# Pie chart
labels = ['Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl']
sizes = [33, 52, 12, 17, 69, 2]
separated = (.5, 0, .1, .1, .1, .1)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
plt.axis('equal')
plt.show()
