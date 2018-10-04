def espacio(parkingLot, carDimensions, la_x, lb_x, la_y, lb_y):
	alto  = (lb_x+1)-la_x
	ancho = (lb_y+1)-la_y
	tam_bool = (alto >= carDimensions[1]) and (ancho >= carDimensions[0])
	return tam_bool
def acceder(parkingLot, la_x, lb_x, la_y, lb_y):
	access = False
	z = False
	for x in range(la_x, lb_x+1):
		for y in range(0, la_y+1):
			if parkingLot[ x ][ y ] != 1:
				access = True
			else:
				access = False
				z = True
				break
		if z:
			break
	return access
def estacionar(parkingLot, la_x, lb_x, la_y, lb_y):
	estacion = False
	z = False
	for x in range(la_x, lb_x+1):
		for y in range(la_y, lb_y+1	):
			if parkingLot[ x ][ y ] != 1:
				estacion = True
			else:
				estacion = False
				z = True
		if z:
			break
	return estacion
def parkingSpot(carDimensions, parkingLot, luckySpot):
	la_x = luckySpot[0]
	la_y = luckySpot[1]
	lb_x = luckySpot[2]
	lb_y = luckySpot[3]


	acc = acceder(parkingLot,la_x, lb_x, la_y, lb_y)
	est = estacionar(parkingLot,la_x, lb_x, la_y, lb_y)
	esp = espacio(parkingLot, carDimensions,la_x, lb_x, la_y, lb_y)
	
	print( acc )
	print( est )
	print( esp )
	
print( parkingSpot( [3,2] ,[
	[1,0,1,0,1,0], 
	[0,0,0,0,1,0], 
	[0,0,0,0,0,1], 
	[1,0,1,1,1,1]
 ], [1, 1, 2, 3] ) )