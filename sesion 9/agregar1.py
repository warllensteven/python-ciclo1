fd = open("sesion 9/data2.txt", "a")

lcad = ["Nos vamos de azadpn\n", "Invita Anderson"]
fd.writelines(lcad)

fd.close()
