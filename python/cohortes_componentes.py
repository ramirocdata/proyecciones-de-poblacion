"""
Proyección por componentes por cohortes (población cerrada).

Reproduce paso a paso la plantilla excel/11_cohortes_componentes.xlsx
para mostrar cómo el mismo procedimiento se automatiza en Python.

Uso:
    python python/cohortes_componentes.py
"""
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
datos = pd.read_csv(RAIZ / "datos" / "ficticio_base.csv")

ANIO_BASE = 2020
PERIODOS = 4          # 2020 → 2040
L0 = 100_000          # raíz de las tablas de vida
IMN = 1.05            # índice de masculinidad al nacer
FERTILES = slice(3, 10)  # filas 15-19 a 45-49


def relaciones_supervivencia(Lx):
    """Sx para pasar del grupo x al x+5; la posición 16 es la del grupo abierto."""
    S = [Lx[i + 1] / Lx[i] for i in range(16)]
    S.append(Lx[17] / (Lx[16] + Lx[17]))
    return S


def sobrevivir(pob, S):
    """Mueve cada cohorte un grupo de edad (excepto 0-4, que viene de los nacimientos)."""
    nueva = [0.0] * 18
    for j in range(1, 17):
        nueva[j] = pob[j - 1] * S[j - 1]
    nueva[17] = (pob[16] + pob[17]) * S[16]
    return nueva


SF = relaciones_supervivencia(datos["Lx_mujeres"].tolist())
SM = relaciones_supervivencia(datos["Lx_hombres"].tolist())
sb_f = datos["Lx_mujeres"][0] / (5 * L0)
sb_m = datos["Lx_hombres"][0] / (5 * L0)
asfr = datos["asfr"].to_numpy()[FERTILES]

mujeres = {ANIO_BASE: datos["mujeres"].astype(float).tolist()}
hombres = {ANIO_BASE: datos["hombres"].astype(float).tolist()}
nacimientos = {}

for k in range(1, PERIODOS + 1):
    t0, t1 = ANIO_BASE + 5 * (k - 1), ANIO_BASE + 5 * k
    f1 = sobrevivir(mujeres[t0], SF)
    h1 = sobrevivir(hombres[t0], SM)
    # nacimientos del periodo: mujeres fértiles promedio entre t0 y t1
    w0 = pd.Series(mujeres[t0][FERTILES]).to_numpy()
    w1 = pd.Series(f1[FERTILES]).to_numpy()
    B = float((5 * asfr * (w0 + w1) / 2).sum())
    bf = B / (1 + IMN)
    nacimientos[f"{t0}-{t1}"] = B
    f1[0] = bf * sb_f
    h1[0] = (B - bf) * sb_m
    mujeres[t1], hombres[t1] = f1, h1

resultado = pd.DataFrame({
    "año": list(mujeres),
    "mujeres": [sum(v) for v in mujeres.values()],
    "hombres": [sum(v) for v in hombres.values()],
})
resultado["total"] = resultado["mujeres"] + resultado["hombres"]

if __name__ == "__main__":
    pd.options.display.float_format = "{:,.0f}".format
    print("TGF:", round(5 * asfr.sum(), 2))
    print("\nNacimientos por periodo:")
    for p, b in nacimientos.items():
        print(f"  {p}: {b:,.0f}")
    print("\nPoblación proyectada:")
    print(resultado.to_string(index=False))
