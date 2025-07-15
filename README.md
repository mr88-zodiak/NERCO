# 🧠 Named Entity Recognition (NER) Bahasa Indonesia

Proyek ini adalah implementasi sederhana dari **Named Entity Recognition (NER)** untuk Bahasa Indonesia. Model ini dirancang untuk mendeteksi tiga entitas utama dalam teks:

- 🧍 **PER** — Person (nama orang)
- 📍 **LOC** — Location (nama tempat)
- 📅 **DATE** dan 🕒 **TIME** — Tanggal dan waktu

---

## 📌 Tujuan

Mendeteksi entitas penting dari kalimat Bahasa Indonesia yang umum digunakan dalam percakapan, berita, atau teks lainnya.

### Contoh Kalimat:

> **Presiden Joko Widodo** berkunjung ke **Jakarta** pada hari **Senin, 10 Juli 2023 pukul 08.00 pagi**.

### Output Model:

- `Joko Widodo` → `PER`
- `Jakarta` → `LOC`
- `10 Juli 2023` → `DATE`
- `08.00 pagi` → `TIME`

---

## 📂 Label Entitas yang Didukung

| Label  | Deskripsi                    | Contoh                           |
| ------ | ---------------------------- | -------------------------------- |
| `PER`  | Nama orang                   | Joko Widodo, Siti Nurhaliza      |
| `LOC`  | Lokasi atau tempat geografis | Jakarta, Surabaya, Gunung Merapi |
| `DATE` | Tanggal, hari, atau bulan    | 17 Agustus, 10 Juli 2023         |
| `TIME` | Waktu spesifik               | 08.00 pagi, jam 2 siang          |

---

## 🗃️ Format Dataset

Dataset ditulis dalam format JSON dengan struktur seperti berikut:

```json
{
  "text": "Presiden Joko Widodo ke Jakarta pada 10 Juli 2023 pukul 08.00",
  "entities": [
    [9, 21, "PER"],
    [25, 32, "LOC"],
    [37, 50, "DATE"],
    [57, 64, "TIME"]
  ]
}
```
