import psutil

# Menampilkan header kolom
print(f"{'PID':<10}{'Name':<30}{'Status':<20}")

# Mendapatkan semua proses yang berjalan
for process in psutil.process_iter(['pid', 'name', 'status']):
    try:
        # Mengambil informasi proses
        pid = process.info['pid']
        name = process.info['name']
        status = process.info['status']

        # Menampilkan informasi proses
        print(f"{pid:<10}{name:<30}{status:<20}")

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Menangani exception jika proses sudah tidak ada atau akses ditolak
        pass
