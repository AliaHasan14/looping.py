import matplotlib.pyplot as plt

# Parameter gerak jatuh bebas
g = 9.8 # Percepatan gravitasi dalam m/s**2
waktu_total = 120 # waktu total dalam detik (2 menit)

# Variabel untuk menyimpan data waktu dan posisi
waktu = []
posisi = []

# loop untuk menghitung posisi setiap detik
for t in range (waktu_total + 1):
    y = 0.5 * g * t**2 # posisi pada waktu t
    waktu.append(t)
    posisi.append(y)

# plot grafik posisi terhadao waktu
plt.plot(waktu, posisi, marker='o',color='b',linestyle='-')
plt.title('grafik gerak jatuh bebas')
plt.xlabel('waktu(detik)')
plt.ylabel('posisi(meter)')
plt.grid(True)
plt.show()