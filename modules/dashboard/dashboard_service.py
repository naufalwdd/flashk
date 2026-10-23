from datetime import datetime, timezone


def get_overview():
    return {
        "stats": [
            {"key": "revenue", "label": "Revenue hari ini", "value": "Rp 4.280.000", "delta": "+12,8% dari kemarin", "tone": "tone-yellow"},
            {"key": "orders", "label": "Pesanan", "value": "128", "delta": "+8 pesanan hari ini", "tone": "tone-coral"},
            {"key": "customers", "label": "Pelanggan aktif", "value": "1.284", "delta": "+4,2% bulan ini", "tone": "tone-mint"},
            {"key": "completion", "label": "Selesai tepat waktu", "value": "92,4%", "delta": "Target: 90%", "tone": "tone-lilac"},
        ],
        "activity": [
            {"title": "Pembayaran INV-2048 diterima", "detail": "Maya Putri · Paket Studio", "time": "2 menit lalu", "tone": "activity-green"},
            {"title": "Workspace baru dibuat", "detail": "Kopi Pojok · Jakarta", "time": "18 menit lalu", "tone": "activity-yellow"},
            {"title": "Tugas desain selesai", "detail": "Tim Kreatif · Website refresh", "time": "1 jam lalu", "tone": "activity-coral"},
            {"title": "Pengguna baru bergabung", "detail": "Rafi Aditya · Product team", "time": "3 jam lalu", "tone": "activity-blue"},
        ],
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }


def get_demo_users():
    return [
        {"name": "Maya Putri", "email": "maya@flashk.demo", "role": "Admin", "status": "Aktif", "initials": "MP", "tone": "avatar-coral"},
        {"name": "Rafi Aditya", "email": "rafi@flashk.demo", "role": "Editor", "status": "Aktif", "initials": "RA", "tone": "avatar-mint"},
        {"name": "Nadia Safitri", "email": "nadia@flashk.demo", "role": "Viewer", "status": "Undangan", "initials": "NS", "tone": "avatar-yellow"},
        {"name": "Bima Prakoso", "email": "bima@flashk.demo", "role": "Editor", "status": "Aktif", "initials": "BP", "tone": "avatar-lilac"},
        {"name": "Salsa Amalia", "email": "salsa@flashk.demo", "role": "Viewer", "status": "Aktif", "initials": "SA", "tone": "avatar-blue"},
    ]


def get_demo_report():
    return {
        "total": "Rp 38.450.000",
        "change": "+18,6% dibanding periode sebelumnya",
        "bars": [
            {"label": "Mei", "amount": "Rp 21,4 jt", "percent": 48},
            {"label": "Jun", "amount": "Rp 27,8 jt", "percent": 63},
            {"label": "Jul", "amount": "Rp 24,1 jt", "percent": 55},
            {"label": "Agu", "amount": "Rp 34,6 jt", "percent": 78},
            {"label": "Sep", "amount": "Rp 31,2 jt", "percent": 70},
            {"label": "Okt", "amount": "Rp 38,4 jt", "percent": 88},
        ],
        "channels": [
            {"name": "Langganan workspace", "value": "Rp 22.850.000", "share": "59%", "tone": "bar-coral"},
            {"name": "Layanan tambahan", "value": "Rp 9.300.000", "share": "24%", "tone": "bar-yellow"},
            {"name": "Konsultasi", "value": "Rp 6.300.000", "share": "17%", "tone": "bar-mint"},
        ],
    }


def get_demo_settings():
    return {
        "workspace": "Flashk Studio",
        "owner": "Maya Putri",
        "email": "maya@flashk.demo",
        "plan": "Studio · Demo",
        "timezone": "Asia/Jakarta (UTC+7)",
        "created": "12 Maret 2026",
    }
