import socket
import json

def get_parking_data():
    # Mengambil data parkir dari pengguna
    nomor_tiket = input("Masukkan Nomor Tiket: ")
    nomor_plat = input("Masukkan Nomor Plat Kendaraan: ")
    waktu_masuk = input("Masukkan Waktu Masuk (format HH:MM): ")
    jenis_kendaraan = input("Masukkan Jenis Kendaraan: ")
    
    # Membuat dictionary dari data yang diinput
    data = {
        "nomor_tiket": nomor_tiket,
        "nomor_plat": nomor_plat,
        "waktu_masuk": waktu_masuk,
        "jenis_kendaraan": jenis_kendaraan
    }
    
    return data

def main():
    # Inisialisasi socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Terhubung ke server
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))
    
    # Mengambil data parkir dari pengguna
    parking_data = get_parking_data()
    
    # Mengirim data ke server dalam format JSON
    message = json.dumps(parking_data)
    client_socket.send(message.encode('utf-8'))
    
    # Menerima balasan dari server
    data = client_socket.recv(1024).decode('utf-8')
    print("Received from server:", data)
    
    # Menutup koneksi
    client_socket.close()

if __name__ == "__main__":
    main()
