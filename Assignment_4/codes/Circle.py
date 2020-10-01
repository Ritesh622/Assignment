import matplotlib.pyplot as plt

figure, axes = plt.subplots()
plt.ylim(0, 12)
plt.xlim(0, 12)
draw_circle = plt.Circle((1, 1), 1,fill=False, color='green')
axes.set_aspect(1)
axes.add_artist(draw_circle)
plt.title('Circle')

draw_circle = plt.Circle((5,5), 5, fill =False, color='red')
axes.set_aspect(1)
axes.add_artist(draw_circle)
plt.title('Circle')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of circles ')
#plt.legend()
plt.grid(color='blue')
plt.annotate("P(1,2)", (1, 2)) #Point of intersection
#plt.annotate("C1 (1,1)", (1, 1)) # centre of 1st circle
#plt.annotate("C2 (5,5)", (5, 5)) # centre of 2nd circle
plt.show()


