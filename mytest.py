s = "Vamos a probar que tal funciona esta cosa que pusimos aqui para ver si sirve."
sa = ""
for i in range(0, len(s),20):
	sa+=s[i:i+20]+"\n\r"

print( sa )