depan = input("Nama Depan: ")
belakang = input("Nama Belakang: ")
jeniskelamin = input("laki-laki/perempuan (l/p)? ")

lengkap = depan + " " + belakang
print(f"Nama lengkap: {lengkap}")
print(f"Jenis kelamin: {'Laki-laki' if jeniskelamin == 'l' else 'Perempuan'}")