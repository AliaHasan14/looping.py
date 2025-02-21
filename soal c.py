import matplotlib.pyplot as plt

# parameter gerak mobil
posisi_awal = 0    # posisi awal dalam meter
kecepatan_awal = 0 # kecepatan awal dalam m/s
percepatan = 2     # percepatan tetap dalam m/s^2
waktu_total = 100  # waktu total dalam detik

# variabel untuk menyimpan data waktu dan posisi
waktu = []
posisi = []

# loop untuk menghitung posisi setiap detik
for t in range(waktu_total + 1):
    # rumus GLBB: x = x₀ + v₀t + 0.5*a*t**2
    x = posisi_awal + (kecepatan_awal * t) + (0.5 * percepatan * t**2)
    waktu.append(t)
    posisi.append(x)

# plot grafik posisi terhadap waktu
plt.plot(waktu, posisi, marker='o', color='b', linestyle='-')
plt.title('Grafik posisi terhadap waktu pada GLBB')
plt.xlabel('waktu(detik)')
plt.ylabel('posisi(meter)')
plt.grid(True)
plt.show()