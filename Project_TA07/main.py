"""
TA-07 Dynamic System Modelling
Studi kasus: pengisian tangki air dengan kebocoran gravitasi.
Jalankan: python main.py
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

A = 0.05          # luas penampang tangki (m^2)
Q_IN = 0.0002     # debit masuk maksimum (m^3/s)
K = 0.001         # koefisien debit kebocoran
DT = 0.1          # langkah waktu (s)
T_END = 600       # durasi simulasi (s)
OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

def input_signal(t, kind):
    """Nilai relatif bukaan/debit inlet."""
    if kind == "constant":
        return 1.0
    if kind == "step":
        return 1.0 if t < 150 else 0.55
    if kind == "impulse":
        return 1.8 if 100 <= t < 110 else 1.0  # pulsa pendek
    if kind == "ramp":
        return min(1.5, 0.5 + t / 600)
    if kind == "sinusoidal":
        return 1.0 + 0.35 * np.sin(2 * np.pi * t / 180)
    raise ValueError("Jenis input tidak dikenal")

def simulate(kind="constant"):
    t = np.arange(0, T_END + DT, DT)
    h = np.zeros_like(t)
    u = np.array([input_signal(x, kind) for x in t])
    for i in range(1, len(t)):
        q_out = K * np.sqrt(max(h[i-1], 0.0))
        dh_dt = (Q_IN * u[i-1] - q_out) / A
        h[i] = max(0.0, h[i-1] + dh_dt * DT)
    return t, h, u

def main():
    h_ss = (Q_IN / K) ** 2
    results = {}
    for kind in ["constant", "step", "impulse", "ramp", "sinusoidal"]:
        t, h, u = simulate(kind)
        results[kind] = h
        plt.plot(t, h, label=kind.capitalize())
    plt.axhline(h_ss, linestyle="--", color="black",
                label=f"Steady state teoritis = {h_ss:.3f} m")
    plt.xlabel("Waktu (detik)")
    plt.ylabel("Tinggi air (m)")
    plt.title("Respons Tinggi Air terhadap Berbagai Sinyal Input")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "respons_semua_sinyal.png", dpi=180)
    plt.show()

    t, h, _ = simulate("constant")
    plt.figure()
    plt.plot(t, h, label="Tinggi air")
    plt.axhline(h_ss, linestyle="--", label=f"Steady state {h_ss:.3f} m")
    plt.xlabel("Waktu (detik)"); plt.ylabel("Tinggi air (m)")
    plt.title("Simulasi Steady State Tangki Air")
    plt.grid(True, alpha=0.3); plt.legend(); plt.tight_layout()
    plt.savefig(OUT / "steady_state.png", dpi=180)
    plt.show()

    print(f"Steady state teoritis: {h_ss:.4f} m")
    print(f"Tinggi akhir simulasi: {h[-1]:.4f} m")

if __name__ == "__main__":
    main()
