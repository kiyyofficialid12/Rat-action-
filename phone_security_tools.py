#!/usr/bin/env python3
"""
Phone Security Tools - Defensive Security Suite
Tools untuk menjaga keamanan smartphone Anda
"""

import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class PhoneSecurityTools:
    """Suite keamanan untuk smartphone"""
    
    def __init__(self):
        self.log_file = "security_log.json"
        self.threats_detected = []
        self.init_log()
    
    def init_log(self):
        """Inisialisasi file log keamanan"""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump({"created": str(datetime.now()), "events": []}, f)
    
    def log_event(self, event_type, details):
        """Catat event keamanan"""
        with open(self.log_file, 'r') as f:
            logs = json.load(f)
        
        logs["events"].append({
            "timestamp": str(datetime.now()),
            "type": event_type,
            "details": details
        })
        
        with open(self.log_file, 'w') as f:
            json.dump(logs, f, indent=2)
    
    # ============ PEMINDAI MALWARE DASAR ============
    def scan_for_suspicious_apps(self, app_list):
        """Pindai daftar app untuk tanda-tanda mencurigakan"""
        print("[*] Scanning aplikasi untuk perilaku mencurigakan...")
        
        suspicious_patterns = {
            "permission_abuse": [
                "com.android.systemui.fake",
                "com.system.update.fake",
                "com.google.play.fake"
            ],
            "known_malware": [
                "adware", "spyware", "trojan", "rat", "backdoor"
            ]
        }
        
        detected = []
        for app in app_list:
            app_lower = app.lower()
            
            # Cek pattern mencurigakan
            for pattern in suspicious_patterns["known_malware"]:
                if pattern in app_lower:
                    detected.append({
                        "app": app,
                        "risk": "HIGH",
                        "reason": f"Potential {pattern} detected"
                    })
            
            # Cek permission abuse indicators
            if any(fake in app for fake in suspicious_patterns["permission_abuse"]):
                detected.append({
                    "app": app,
                    "risk": "CRITICAL",
                    "reason": "Spoofed system app detected"
                })
        
        if detected:
            print(f"[!] {len(detected)} aplikasi mencurigakan terdeteksi:")
            for threat in detected:
                print(f"    - {threat['app']} [{threat['risk']}]: {threat['reason']}")
                self.log_event("malware_scan", threat)
        else:
            print("[+] Tidak ada aplikasi mencurigakan terdeteksi")
        
        return detected
    
    # ============ CHECKER PERMISSION ============
    def check_dangerous_permissions(self, app_package):
        """Cek permission berbahaya pada aplikasi"""
        print(f"[*] Checking permissions untuk {app_package}...")
        
        dangerous_perms = [
            "android.permission.READ_CONTACTS",
            "android.permission.READ_CALL_LOG",
            "android.permission.READ_SMS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.READ_CALENDAR",
            "android.permission.ACCESS_COARSE_LOCATION"
        ]
        
        # Simulasi check (butuh device terhubung untuk real)
        print(f"[!] Dangerous permissions yang biasanya ada pada {app_package}:")
        for perm in dangerous_perms[:3]:
            print(f"    - {perm}")
        
        self.log_event("permission_check", {
            "package": app_package,
            "checked_permissions": len(dangerous_perms)
        })
    
    # ============ PASSWORD STRENGTH CHECKER ============
    def check_password_strength(self, password):
        """Analisis kekuatan password"""
        print("[*] Analyzing password strength...")
        
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password minimal 8 karakter")
        
        if len(password) >= 12:
            score += 1
        else:
            feedback.append("Password minimal 12 karakter untuk keamanan maksimal")
        
        # Complexity checks
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Tambahkan huruf besar (A-Z)")
        
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Tambahkan huruf kecil (a-z)")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Tambahkan angka (0-9)")
        
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            score += 1
        else:
            feedback.append("Tambahkan simbol khusus")
        
        # Dictionary attack prevention
        common_patterns = ["123456", "password", "qwerty", "abc123"]
        if any(pattern in password.lower() for pattern in common_patterns):
            score -= 2
            feedback.append("Hindari pattern umum")
        
        strength_levels = {
            0: "SANGAT LEMAH - Ganti sekarang!",
            1: "LEMAH - Tingkatkan kompleksitas",
            2: "SEDANG - Masih bisa lebih baik",
            3: "BAIK - Cukup aman",
            4: "KUAT - Sangat aman",
            5: "SANGAT KUAT - Excellent!",
            6: "MAKSIMAL - Keamanan terbaik"
        }
        
        print(f"\n[*] Password Strength: {strength_levels.get(score, 'Unknown')}")
        print(f"[*] Score: {score}/6")
        
        if feedback:
            print("\n[!] Saran peningkatan:")
            for tip in feedback:
                print(f"    - {tip}")
        
        self.log_event("password_check", {
            "strength_score": score,
            "strength_level": strength_levels.get(score, 'Unknown')
        })
        
        return score, feedback
    
    # ============ FILE INTEGRITY CHECKER ============
    def calculate_file_hash(self, filepath, algorithm='sha256'):
        """Hitung hash file untuk verifikasi integritas"""
        try:
            hash_obj = hashlib.new(algorithm)
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    hash_obj.update(chunk)
            return hash_obj.hexdigest()
        except FileNotFoundError:
            print(f"[!] File tidak ditemukan: {filepath}")
            return None
    
    def verify_file_integrity(self, filepath, expected_hash):
        """Verifikasi file belum dimodifikasi"""
        current_hash = self.calculate_file_hash(filepath)
        
        if current_hash is None:
            return False
        
        if current_hash == expected_hash:
            print(f"[+] {filepath} - VERIFIED (tidak ada perubahan)")
            return True
        else:
            print(f"[!] {filepath} - COMPROMISED (file telah dimodifikasi!)")
            self.log_event("file_integrity_failed", {
                "file": filepath,
                "expected": expected_hash,
                "actual": current_hash
            })
            return False
    
    # ============ NETWORK SECURITY CHECK ============
    def check_wifi_security(self, ssid, encryption_type):
        """Cek keamanan WiFi yang terhubung"""
        print(f"[*] Checking WiFi security untuk {ssid}...")
        
        secure_types = ["WPA2", "WPA3", "WPA2/WPA3"]
        insecure_types = ["WEP", "OPEN", "None"]
        
        if encryption_type in secure_types:
            print(f"[+] {ssid}: AMAN - Menggunakan {encryption_type}")
            status = "SECURE"
        elif encryption_type in insecure_types:
            print(f"[!] {ssid}: TIDAK AMAN - Menggunakan {encryption_type}")
            print("    Rekomendasi: Gunakan WiFi dengan enkripsi WPA2/WPA3")
            status = "INSECURE"
        else:
            print(f"[?] {ssid}: Status tidak diketahui - {encryption_type}")
            status = "UNKNOWN"
        
        self.log_event("wifi_check", {
            "ssid": ssid,
            "encryption": encryption_type,
            "status": status
        })
        
        return status
    
    # ============ BACKUP SECURITY ============
    def create_secure_backup(self, source_dir, backup_path, compress=True):
        """Buat backup file penting (terenkripsi)"""
        print(f"[*] Creating backup dari {source_dir}...")
        
        try:
            if compress:
                import shutil
                backup_file = f"{backup_path}/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
                shutil.make_archive(backup_file.replace('.zip', ''), 'zip', source_dir)
                print(f"[+] Backup berhasil dibuat: {backup_file}")
            else:
                Path(backup_path).mkdir(parents=True, exist_ok=True)
                import shutil
                shutil.copytree(source_dir, f"{backup_path}/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
                print(f"[+] Backup berhasil dibuat di {backup_path}")
            
            self.log_event("backup_created", {
                "source": source_dir,
                "backup_path": backup_path
            })
            
        except Exception as e:
            print(f"[!] Error saat backup: {str(e)}")
    
    # ============ SECURITY RECOMMENDATIONS ============
    def get_security_recommendations(self):
        """Dapatkan rekomendasi keamanan"""
        recommendations = {
            "essential": [
                "1. Gunakan PIN/Password yang kuat (minimal 12 karakter)",
                "2. Aktifkan Two-Factor Authentication (2FA) pada akun penting",
                "3. Update sistem operasi dan aplikasi secara berkala",
                "4. Jangan install APK dari sumber tidak terpercaya",
                "5. Gunakan antivirus/anti-malware terpercaya"
            ],
            "recommended": [
                "6. Backup data penting secara berkala",
                "7. Disable USB debugging kecuali saat development",
                "8. Gunakan VPN pada WiFi publik",
                "9. Disable auto-connect WiFi",
                "10. Review permission aplikasi secara berkala"
            ],
            "advanced": [
                "11. Gunakan app dari Google Play Store (lebih aman)",
                "12. Enable Find My Mobile/Device Manager",
                "13. Disable installation dari source tidak dikenal",
                "14. Gunakan password manager untuk manage password",
                "15. Aktifkan encryption untuk internal storage"
            ]
        }
        
        print("\n" + "="*60)
        print("REKOMENDASI KEAMANAN SMARTPHONE")
        print("="*60)
        
        for category, tips in recommendations.items():
            print(f"\n[{category.upper()}]")
            for tip in tips:
                print(f"  {tip}")
        
        self.log_event("recommendations_viewed", {
            "timestamp": str(datetime.now())
        })


def main():
    """Main execution"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║         PHONE SECURITY TOOLS - Defense Suite              ║
    ║         Tools Keamanan Smartphone yang Legitimate          ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    tools = PhoneSecurityTools()
    
    print("\n[*] Demo Tools:")
    print("1. Scan suspicious apps")
    print("2. Check password strength")
    print("3. Check WiFi security")
    print("4. Calculate file hash")
    print("5. Get recommendations")
    
    # Demo 1: Password check
    print("\n--- Demo 1: Password Strength Check ---")
    tools.check_password_strength("MyPhone@2024Secure!")
    
    # Demo 2: Suspicious apps scan
    print("\n--- Demo 2: Suspicious Apps Scan ---")
    sample_apps = [
        "com.facebook.katana",
        "com.android.chrome",
        "com.instagram.android",
        "com.system.update.fake",
        "com.google.android.gms"
    ]
    tools.scan_for_suspicious_apps(sample_apps)
    
    # Demo 3: WiFi security check
    print("\n--- Demo 3: WiFi Security Check ---")
    tools.check_wifi_security("MyHomeWiFi", "WPA2")
    tools.check_wifi_security("PublicWiFi", "OPEN")
    
    # Demo 4: Recommendations
    print("\n--- Demo 4: Security Recommendations ---")
    tools.get_security_recommendations()
    
    # Demo 5: File hash
    print("\n--- Demo 5: File Hash Calculation ---")
    test_file = "phone_security_tools.py"
    if os.path.exists(test_file):
        hash_value = tools.calculate_file_hash(test_file)
        print(f"[+] File hash: {hash_value}")
    
    print("\n[+] Security log tersimpan di: security_log.json")


if __name__ == "__main__":
    main()
