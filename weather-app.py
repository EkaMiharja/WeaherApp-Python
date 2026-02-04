import requests
import json
import os

api_key = "your_api_key_here"


def get_weather_data(city):
    """Mengambil data cuaca saat ini"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=id"

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] != 200:
            return None, "Kota tidak ditemukan!"

        return data, None

    except requests.exceptions.ConnectionError:
        return None, "Koneksi internet bermasalah!"
    except Exception as e:
        return None, f"Terjadi kesalahan: {str(e)}"


def get_5day_forecast(city):
    """Prediksi cuaca 5 hari ke depan"""
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=id"

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] != "200":
            return None, "Kota tidak ditemukan!"

        return data, None

    except:
        return None, "Gagal mengambil data forecast"


def display_current_weather(data, city):
    """Menampilkan data cuaca saat ini"""
    weather_desc = data['weather'][0]['description']
    weather_natural = translate_to_natural(weather_desc)  # Gunakan terjemahan natural
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']

    print("\n" + "=" * 40)
    print(f"CUACA SAAT INI - {city.upper()}")
    print("=" * 40)
    print(f"Kondisi   : {weather_natural}")  # Ganti weather dengan weather_natural
    print(f"Suhu      : {temp:.1f}°C")
    print(f"Terasa    : {feels_like:.1f}°C")
    print(f"Kelembaban: {humidity}%")
    print("=" * 40)


def display_forecast(data, city):
    """Menampilkan forecast 5 hari"""
    print(f"\n(FORECAST 5 HARI - {city.upper()})")
    print("=" * 50)
    print("Hari         Suhu    Kondisi")
    print("-" * 50)

    # Dictionary untuk mapping hari
    days = {}

    # Kelompokkan data per hari
    for forecast in data['list']:
        date = forecast['dt_txt'].split()[0]  # Ambil tanggal
        day_name = date  # Bisa dikembangkan jadi nama hari

        if date not in days:
            days[date] = {
                'temps': [],
                'conditions': []
            }

        days[date]['temps'].append(forecast['main']['temp'])
        days[date]['conditions'].append(forecast['weather'][0]['description'])

    # Tampilkan rata-rata per hari (ambil 5 hari pertama)
    for i, (date, info) in enumerate(list(days.items())[:5]):
        avg_temp = sum(info['temps']) / len(info['temps'])
        most_common_condition = max(set(info['conditions']), key=info['conditions'].count)
        natural_condition = translate_to_natural(most_common_condition)  # Gunakan terjemahan natural

        print(f"{date}  {avg_temp:5.1f}°C  {natural_condition}")

def multi_city_weather():
    """Cek cuaca beberapa kota sekaligus"""
    print("\n" + "=" * 50)
    print("PERBANDINGAN CUACA BEBERAPA KOTA")
    print("=" * 50)

    cities_input = input("Masukkan nama kota (pisahkan dengan koma): ")
    cities = [city.strip() for city in cities_input.split(',')]

    print("\n" + "-" * 55)
    print(f"{'KOTA':<18} {'SUHU':<10} {'KONDISI':<20}")
    print("-" * 55)

    for city in cities[:6]:  # Maksimal 6 kota
        if city:  # Skip jika kosong
            data, error = get_weather_data(city)
            if not error and data:
                temp = data['main']['temp']
                weather_desc = data['weather'][0]['description']
                weather_natural = translate_to_natural(weather_desc)
                # Format: {suhu:6.1f}°C -> total 9 karakter (6 untuk angka, 3 untuk °C)
                print(f"{city:<15} {temp:6.1f}°C      {weather_natural:<20}")
            else:
                print(f"{city:<16} {'-':^9} { 'Kota tidak ditemukan':<20}")

def save_to_history(city, temp):
    """Simpan riwayat pencarian sederhana"""
    history_file = "weather_history.txt"

    with open(history_file, 'a') as f:
        f.write(f"{city}: {temp:.1f}°C\n")


def show_menu():
    """Tampilkan menu utama"""
    print("\n" + "=" * 40)
    print("APLIKASI CUACA PYTHON")
    print("=" * 40)
    print("1. Cek Cuaca Kota (Saat Ini)")
    print("2. Forecast 5 Hari")
    print("3. Perbandingan Beberapa Kota")
    print("4. Keluar")
    print("=" * 40)


def main():
    """Program utama dengan menu"""

    while True:
        show_menu()

        try:
            choice = input("\nPilih menu (1-4): ").strip()

            if choice == "1":
                print("\n[CEK CUACA SAAT INI]")
                city = input("Masukkan nama kota: ").strip()

                if city:
                    data, error = get_weather_data(city)
                    if error:
                        print(f"❌ {error}")
                    else:
                        display_current_weather(data, city)
                        save_to_history(city, data['main']['temp'])
                else:
                    print("⚠️  Nama kota tidak boleh kosong!")

            elif choice == "2":
                print("\n[FORECAST 5 HARI]")
                city = input("Masukkan nama kota: ").strip()

                if city:
                    data, error = get_5day_forecast(city)
                    if error:
                        print(f"❌ {error}")
                    else:
                        display_forecast(data, city)
                else:
                    print("⚠️  Nama kota tidak boleh kosong!")

            elif choice == "3":
                multi_city_weather()

            elif choice == "4":
                print("\n👋 Terima kasih telah menggunakan aplikasi cuaca!")
                print("Sampai jumpa!")
                break

            else:
                print("⚠️  Pilihan tidak valid! Silakan pilih 1-4")

            # Tanya apakah ingin kembali ke menu
            if choice != "4":
                input("\n🔽 Tekan Enter untuk kembali ke menu...")

        except KeyboardInterrupt:
            print("\n\n⏹️  Program dihentikan oleh user")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {e}")
            input("\nTekan Enter untuk melanjutkan...")


def translate_to_natural(weather_desc):
    """Ubah ke istilah yang lebih natural untuk Indonesia"""
    translations = {
        "langit cerah": "Cerah",
        "sedikit awan": "Cerah Berawan",
        "awan tersebar": "Berawan",
        "awan pecah": "Berawan Tebal",
        "awan mendung": "Mendung",
        "hujan ringan": "Gerimis",
        "hujan sedang": "Hujan",
        "hujan lebat": "Hujan Lebat",
        "hujan rintik-rintik": "Rintik-rintik",
        "hujan badai": "Badai",
        "badai petir": "Badai Petir",
        "badai dengan hujan ringan": "Badai dan Gerimis",
        "badai dengan hujan": "Badai dan Hujan",
        "badai dengan hujan lebat": "Badai dan Hujan Lebat",
        "salju": "Salju",
        "salju ringan": "Salju Ringan",
        "salju lebat": "Salju Lebat",
        "hujan salju": "Hujan Salju",
        "kabut": "Kabut",
        "kabut tipis": "Berkabut",
        "berkabut": "Berkabut",
        "asap": "Berkabut Asap",
        "debu": "Berdebu",
        "pasir": "Berdebu Pasir",
        "abu": "Abu Vulkanik",
        "tornado": "Angin Puting Beliung",
        "angin kencang": "Angin Kencang",
        "berangin": "Berangin"
    }

    # Cari terjemahan yang cocok (case-insensitive)
    for key in translations:
        if key in weather_desc.lower():
            return translations[key]

    # Jika tidak ditemukan, kembalikan aslinya dengan format judul
    return weather_desc.title()

if __name__ == "__main__":
    # Cek apakah API key sudah diisi
    if api_key == "your_api_key_here":
        print("⚠️  WARNING: Ganti 'api_key' dengan API key OpenWeather Anda!")
        print("Dapatkan API key gratis di: https://home.openweathermap.org/users/sign_up")
    else:
        main()