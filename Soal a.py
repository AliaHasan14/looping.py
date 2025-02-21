import matplotlib.pyplot as plt

# Parameter gerak benda
kecepatan = 20 # kecepatan konstan dalam meter per detik
waktu_total = 300 # 5 menit = 300 detik

# variabel untuk menyimpan data waktu dan posisi
waktu = []
posisi = []

# loop untuk menghitung posisi setiap detik
for t in range (0,waktu_total + 1, 10):
    x = kecepatan * t # persamaan posisi = kecepatan * waktu
    waktu.append(t)
    posisi.append(x)

# plot grafik posisi terhadap waktu
plt.plot(waktu, posisi, marker='o',color='b',linestyle='-')
plt.title('Grafik gerak benda dengan kecepatan konstan 20m/s')
plt.xlabel('waktu(detik)')
plt.ylabel('posisi(meter)')
plt.grid(True)
plt.show()