import numpy as np
print("***********************")
print("Gráficas con caracteres")
print("***********************")
for i in range(60):
	for j in range(np.abs(int(25*np.sin(i*np.pi/15)))):
		print('%', end='')
	print()
print('*FIN*') 
