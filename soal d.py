import matplotlib.pyplot as plt

# parameter gerak benda
kecepatan_awal = 60  # kecepatan awal dalam meter per detik
percepatan = -2.25   # perlambatan dalam meter per detik kuadrat
waktu_total = 20     # waktu total dalam detik

# variabel untuk menyimpan data waktu dan posisi
waktu = []
posisi = []

# loop untuk menghitung posisi setiap detik
for t in range(waktu_total + 1):
    # rumus GLBB: x = v0*t + (1/2)*a*t**2
    x = kecepatan_awal * t + 0.5 * percepatan * t**2
    waktu.append(t)
    posisi.append(x)

# plot grafik posisi terhadap waktu
plt.plot(waktu, posisi, marker='o', color='b', linestyle='-')
plt.title('Grafik gerak benda GLBB dengan perlambatan')
plt.xlabel('waktu(detik)')
plt.ylabel('posisi(meter)')
plt.grid(True)
plt.show()