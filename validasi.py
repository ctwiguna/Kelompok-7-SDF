"""Modul validasi data anggota Kelompok 7 SDF."""

ANGGOTA = {
    "25110300026": "MUHAMMAD FARREL AL GHIFARY",
    "25110300007": "KEVIN ARYA SAPUTRA",
    "25110300017": "CHANDRA TABLIGH WIGUNA",
    "25110300019": "BRILLIANT GIBRAN ADHINATA",
    "25110300022": "NAWWAF DZAKWAN SIGIT",
}


def validasi_nim(nim):
    """Kembalikan True jika NIM terdaftar sebagai anggota Kelompok 7."""
    if not isinstance(nim, str):
        raise TypeError("NIM harus berupa string")
    nim = nim.strip()
    if not nim.isdigit() or len(nim) != 11:
        return False
    return nim in ANGGOTA


def nama_anggota(nim):
    """Ambil nama anggota berdasarkan NIM, atau None jika tidak terdaftar."""
    return ANGGOTA.get(str(nim).strip())


if __name__ == "__main__":
    for n, nama in ANGGOTA.items():
        assert validasi_nim(n), f"NIM {n} seharusnya valid"
        print(f"{n} - {nama}: VALID")
    assert not validasi_nim("00000000000")
    print("Semua validasi lolos.")
