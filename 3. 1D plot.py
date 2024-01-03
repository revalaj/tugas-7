import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 500  # Koefisien Difusivitas Termal [m^2/s]
panjang = 2.5  # Panjang plat [m]
waktu = 1  # Waktu simulasi [s]
node = 50  # Jumlah titik grid

dx = panjang / node  # Jarak antar titik grid [m]
dt = 0.5 * dx ** 2 / a  # Ukuran waktu simulasi [s]
t_n = int(waktu / dt)  # Jumlah iterasi simulasi

u = np.zeros(node) + 20  # Suhu awal plat [degC]

# Kondisi Batas
u[0] = 0  # Suhu ujung kiri plat [degC]
u[-1] = 100  # Suhu ujung kanan plat [degC]

# Visualisasi
fig, ax = plt.subplots()
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)  # Plot distribusi suhu
plt.colorbar(pcm, ax=ax)
ax.set_ylim([-2, 3])  # Batas skala y

# Inisialisasi plot suhu rata-rata terhadap waktu
fig_avg, ax_avg = plt.subplots()
ax_avg.set_xlabel("Waktu (s)")
ax_avg.set_ylabel("Suhu Rata-rata (°C)")
line_avg, = ax_avg.plot([], [], color='red')

t_nodes = int(waktu / dt)  # Jumlah iterasi simulasi
# Inisialisasi plot suhu rata-rata terhadap waktu
time_values = np.linspace(0, waktu, t_nodes + 1)
avg_temperature_values = []

# Simulation Loop
counter = 0
while counter < waktu:
    w = u.copy()
    for i in range(1, node - 1):
        u[i] = (dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx**2) + w[i]
    print("t: {:.3f} s, Suhu rata - rata: {:.2f} Celsius".format(counter, np.mean(u)))

    pcm.set_array([u])
    ax.set_title("Temperature Distribution at t: {:.3f} s".format(counter))
    counter += dt
    
    t_mean = np.mean(u)
    # Update plot suhu rata-rata terhadap waktu
    avg_temperature_values.append(t_mean)
    line_avg.set_data(time_values[:len(avg_temperature_values)], avg_temperature_values)
    ax_avg.relim()
    ax_avg.autoscale_view()
    
    plt.pause(0.01)

plt.show()  # Show the final plot
