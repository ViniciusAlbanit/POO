from pylab import plot, show, grid, axis, title, xlabel, ylabel

xs = [1,2,3]
ys1 = [2,4,6]
ys2 = [5,8,12]

plot(xs, ys1, 'b:o') #O b é a cor, : é a linha pontilhada e o o é a marcação
plot(xs, ys2, 'r-o')
axis((0, 12, 0, 12)) #Muda o valor que fica no eixo x e y
grid(True)
title('Economias')
xlabel('Meses')
ylabel('Valor (R$)')

show()
