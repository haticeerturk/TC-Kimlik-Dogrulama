print "-TC Kimlik Numarasi,"
print "-11 hanelidir."
print "-Her hanesi rakamsal deger icerir."
print "-Ilk hane 0 olamaz."

kimlik = raw_input("lutfen bir TC Kimlik Numarasi giriniz: ")

print "tc kimlik numarasi: ",kimlik


if (((int(kimlik[0])+int(kimlik[2])+int(kimlik[4])+int(kimlik[6])+int(kimlik[8]))*7)-(int(kimlik[1])+int(kimlik[3])+int(kimlik[5])+int(kimlik[7])))%10 == int(kimlik[9]) : 
	if  (int(kimlik[0])+int(kimlik[1])+int(kimlik[2])+int(kimlik[3])+int(kimlik[4])+int(kimlik[5])+int(kimlik[6])+int(kimlik[7])+int(kimlik[8])+int(kimlik[9]))%10 == int(kimlik[10]) :
		print "Girdiginiz",kimlik,"TC Kimlik Numarasi dogru numaradir."
