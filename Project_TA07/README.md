# TA-07 — Dynamic System Modelling
**Studi kasus:** Sistem pengisian dan pengosongan tangki air otomatis.

## Menjalankan project
1. Install Python 3.10 atau lebih baru.
2. Buka folder ini di VS Code.
3. (Opsional) buat virtual environment.
4. Jalankan `pip install -r requirements.txt`.
5. Jalankan `python main.py`.

Grafik akan tampil dan disimpan pada folder `outputs/`.

## Model
A dh/dt = Qin*u - K*sqrt(h)
- A = 0.05 m²
- Qin = 0.0002 m³/s
- K = 0.001
- dt = 0.1 s
- h steady state = (Qin/K)^2 = 0.04 m

Input yang diuji: konstan, step, impulse (pulsa pendek), ramp, dan sinusoidal.
Metode numerik: Euler eksplisit.
