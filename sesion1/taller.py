nom = str(input("Ingrese su nombre: "))
placa = str(input("Ingrese su placa: "))
valorPasaje = int(input("Ingrese el pago total de los pasajes: "))
valorEncomienda = int(input("Ingrese el pago total de encomiendas: "))

pagPasaje = valorPasaje * 0.25
pagEncomienda = valorPasaje * 0.15
pagoTotal = pagEncomienda + pagPasaje

print(f"Señor {nom} del vehiculo con numero de placa: {placa},el total del valor de pasajes fue por valor de {valorPasaje:,.0f} , su pago por pasajes es de : {pagPasaje:,.0f} y el total del valor de encomienda es de {valorEncomienda:,.0f} , su pago por encomienda es de {pagEncomienda:,.0f} , su pago total es de {pagoTotal:,.0f}")