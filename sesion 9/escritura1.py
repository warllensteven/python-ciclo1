fd = open("sesion 9/data2.txt", "w")

lcad = ["los pollitos dicen\n", "Yo sere la mascota"]
fd.writelines(lcad)


fd.close()