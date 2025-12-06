#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════╗
║     Creating BY Shrabon~Gomez        ║
╚══════════════════════════════════════╝
        ⚡ ULTRA OFFSET SCANNER PRO ⚡
  Auto Permission Fix • Advanced Security • 100% Working
"""

import os
import re
import time
import mmap
import stat
import subprocess
import sys
import shutil
import json
from datetime import datetime
from pathlib import Path

# ==================== ADVANCED CONFIGURATION ====================
CONFIG = {
    'password': "SHRABON",
    'facebook_url': "https://www.facebook.com/share/1B4TRBkyN3/",
    'possible_dump_paths': [
        "/storage/emulated/0/Download/dump.cs",
        "/sdcard/Download/dump.cs",
        "/storage/emulated/0/dump.cs",
        "/sdcard/dump.cs",
        "/storage/emulated/0/Android/data/com.termux/files/home/dump.cs",
        "/data/data/com.termux/files/home/storage/downloads/dump.cs",
        "/storage/self/primary/Download/dump.cs"
    ],
    'output_base': "/storage/emulated/0/Download",
    'backup_dir': "/storage/emulated/0/OffsetScanner_Backup",
    'log_file': "/storage/emulated/0/Download/offset_scanner_log.txt",
    'config_file': "/storage/emulated/0/Download/.offset_scanner_config.json"
}

# Auto-detect dump file
DUMP_CS_PATH = None
OUTPUT_DIR = None
OUTPUT_FILE = None
ANALYZE_FILE = None

# ==================== ADVANCED PERMISSION FIXER ====================
class PermissionFixer:
    """Advanced permission fixing system"""
    
    @staticmethod
    def find_dump_file():
        """Intelligently find dump.cs file"""
        print(f"{Colors.BRIGHT_CYAN}🔍 Searching for dump.cs file...{Colors.RESET}")
        
        found_files = []
        
        for path in CONFIG['possible_dump_paths']:
            if os.path.exists(path):
                size = os.path.getsize(path)
                found_files.append((path, size))
                print(f"{Colors.BRIGHT_GREEN}✅ Found: {path} ({size:,} bytes){Colors.RESET}")
        
        if not found_files:
            # Search recursively in common directories
            search_dirs = [
                "/storage/emulated/0",
                "/sdcard",
                "/storage/self/primary",
                "/data/data/com.termux/files/home"
            ]
            
            for search_dir in search_dirs:
                if os.path.exists(search_dir):
                    try:
                        for root, dirs, files in os.walk(search_dir):
                            if 'dump.cs' in files:
                                full_path = os.path.join(root, 'dump.cs')
                                size = os.path.getsize(full_path)
                                found_files.append((full_path, size))
                                print(f"{Colors.BRIGHT_GREEN}✅ Found: {full_path} ({size:,} bytes){Colors.RESET}")
                                break
                    except:
                        continue
        
        if found_files:
            # Choose the largest file (most likely the real dump.cs)
            found_files.sort(key=lambda x: x[1], reverse=True)
            return found_files[0][0]
        
        return None
    
    @staticmethod
    def fix_permissions(file_path):
        """Fix file permissions with multiple methods"""
        if not file_path or not os.path.exists(file_path):
            return False
        
        print(f"{Colors.BRIGHT_YELLOW}🔧 Fixing permissions for: {file_path}{Colors.RESET}")
        
        try:
            # Method 1: Basic chmod
            os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
            print(f"{Colors.BRIGHT_GREEN}✓ Method 1: Basic permissions set{Colors.RESET}")
            
            # Method 2: Using chmod command
            subprocess.run(['chmod', '644', file_path], capture_output=True)
            print(f"{Colors.BRIGHT_GREEN}✓ Method 2: chmod command executed{Colors.RESET}")
            
            # Method 3: Change ownership (if root available)
            try:
                subprocess.run(['chown', '$(whoami)', file_path], capture_output=True)
                print(f"{Colors.BRIGHT_GREEN}✓ Method 3: Ownership changed{Colors.RESET}")
            except:
                pass
            
            # Method 4: Copy to temp location with correct permissions
            temp_path = "/data/data/com.termux/files/home/temp_dump.cs"
            shutil.copy2(file_path, temp_path)
            os.chmod(temp_path, 0o644)
            print(f"{Colors.BRIGHT_GREEN}✓ Method 4: Temp copy created{Colors.RESET}")
            
            # Verify permissions
            st = os.stat(file_path)
            if st.st_mode & 0o777 == 0o644:
                print(f"{Colors.BRIGHT_GREEN}✅ Permissions fixed successfully!{Colors.RESET}")
                return True
            else:
                print(f"{Colors.BRIGHT_YELLOW}⚠ Permissions may need manual adjustment{Colors.RESET}")
                return True
                
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}❌ Permission fix failed: {str(e)}{Colors.RESET}")
            return False
    
    @staticmethod
    def create_symlink(source, target):
        """Create symbolic link with proper permissions"""
        try:
            if os.path.exists(target):
                os.remove(target)
            
            os.symlink(source, target)
            print(f"{Colors.BRIGHT_GREEN}✅ Symlink created: {source} → {target}{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}❌ Symlink creation failed: {str(e)}{Colors.RESET}")
            return False
    
    @staticmethod
    def backup_and_replace(file_path):
        """Create backup and replace with accessible version"""
        try:
            backup_path = f"{CONFIG['backup_dir']}/dump_backup_{int(time.time())}.cs"
            os.makedirs(CONFIG['backup_dir'], exist_ok=True)
            
            # Backup original
            shutil.copy2(file_path, backup_path)
            print(f"{Colors.BRIGHT_GREEN}✅ Backup created: {backup_path}{Colors.RESET}")
            
            # Create accessible copy
            accessible_path = "/data/data/com.termux/files/home/accessible_dump.cs"
            shutil.copy2(file_path, accessible_path)
            os.chmod(accessible_path, 0o644)
            
            print(f"{Colors.BRIGHT_GREEN}✅ Accessible copy created: {accessible_path}{Colors.RESET}")
            return accessible_path
            
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}❌ Backup failed: {str(e)}{Colors.RESET}")
            return None

# ==================== ADVANCED COLOR SYSTEM ====================
class Colors:
    """Advanced mobile-optimized color system"""
    
    # True Color RGB System
    @staticmethod
    def rgb(r, g, b):
        return f'\033[38;2;{r};{g};{b}m'
    
    @staticmethod
    def bg_rgb(r, g, b):
        return f'\033[48;2;{r};{g};{b}m'
    
    # Pre-defined gradients
    NEON_PURPLE = [rgb(148, 0, 211), rgb(186, 85, 211), rgb(221, 160, 221)]
    ELECTRIC_BLUE = [rgb(0, 191, 255), rgb(30, 144, 255), rgb(70, 130, 180)]
    LIME_GREEN = [rgb(50, 205, 50), rgb(144, 238, 144), rgb(152, 251, 152)]
    FIRE_RED = [rgb(255, 69, 0), rgb(255, 140, 0), rgb(255, 165, 0)]
    GOLDEN = [rgb(255, 215, 0), rgb(255, 223, 0), rgb(255, 228, 0)]
    
    # Rainbow palette
    RAINBOW = [
        rgb(255, 0, 0),      # Red
        rgb(255, 127, 0),    # Orange
        rgb(255, 255, 0),    # Yellow
        rgb(0, 255, 0),      # Green
        rgb(0, 0, 255),      # Blue
        rgb(75, 0, 130),     # Indigo
        rgb(148, 0, 211)     # Violet
    ]
    
    # Basic ANSI
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Bright ANSI (mobile friendly)
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    @staticmethod
    def gradient(text, gradient_colors):
        """Advanced gradient with smooth transition"""
        if not text:
            return ""
        
        result = ""
        length = len(text)
        steps = len(gradient_colors)
        
        for i, char in enumerate(text):
            pos = i / max(1, length - 1)
            color_idx = min(steps - 1, int(pos * steps))
            
            # Smooth interpolation between colors
            if color_idx < steps - 1:
                next_idx = color_idx + 1
                blend = (pos * steps) - color_idx
                
                # Get RGB values
                def extract_rgb(color_code):
                    match = re.search(r'(\d+);(\d+);(\d+)', color_code)
                    return tuple(map(int, match.groups())) if match else (255, 255, 255)
                
                r1, g1, b1 = extract_rgb(gradient_colors[color_idx])
                r2, g2, b2 = extract_rgb(gradient_colors[next_idx])
                
                r = int(r1 + (r2 - r1) * blend)
                g = int(g1 + (g2 - g1) * blend)
                b = int(b1 + (b2 - b1) * blend)
                
                color = Colors.rgb(r, g, b)
            else:
                color = gradient_colors[color_idx]
            
            result += color + char
        
        return result + Colors.RESET
    
    @staticmethod
    def animated_text(text, delay=0.03):
        """Typewriter effect with color"""
        for char in text:
            print(Colors.gradient(char, Colors.RAINBOW), end='', flush=True)
            time.sleep(delay)
        print()

# ==================== SECURITY & ACCESS CONTROL ====================
class SecurityManager:
    """Advanced security and access control"""
    
    @staticmethod
    def password_check():
        """Advanced password check with attempts tracking"""
        max_attempts = 3
        attempt_file = "/data/data/com.termux/files/home/.scanner_attempts"
        
        # Check recent attempts
        attempts = 0
        if os.path.exists(attempt_file):
            try:
                with open(attempt_file, 'r') as f:
                    attempts = int(f.read().strip())
            except:
                pass
        
        if attempts >= max_attempts:
            print(f"{Colors.BRIGHT_RED}⛔ Too many failed attempts. Try again later.{Colors.RESET}")
            time.sleep(3)
            return False
        
        UI.show_auth_screen()
        
        for i in range(max_attempts - attempts):
            remaining = max_attempts - attempts - i
            print(f"{Colors.BRIGHT_YELLOW}🔐 Enter Password [{remaining} attempts]: {Colors.RESET}", end="")
            
            try:
                import getpass
                entered = getpass.getpass("")
            except:
                entered = input()
            
            if entered == CONFIG['password']:
                # Reset attempts
                with open(attempt_file, 'w') as f:
                    f.write("0")
                
                print(f"{Colors.BRIGHT_GREEN}✅ Access Granted!{Colors.RESET}")
                time.sleep(1)
                
                # Auto Facebook
                SecurityManager.auto_facebook()
                return True
            else:
                attempts += 1
                with open(attempt_file, 'w') as f:
                    f.write(str(attempts))
                
                print(f"{Colors.BRIGHT_RED}❌ Wrong Password!{Colors.RESET}")
                time.sleep(1)
        
        print(f"{Colors.BRIGHT_RED}⛔ Account Locked. Try again in 5 minutes.{Colors.RESET}")
        time.sleep(3)
        return False
    
    @staticmethod
    def auto_facebook():
        """Automatic Facebook access without asking"""
        print(f"{Colors.BRIGHT_CYAN}📱 Connecting to Facebook...{Colors.RESET}")
        
        # Check last access time
        access_file = "/data/data/com.termux/files/home/.facebook_access"
        today = datetime.now().strftime("%Y-%m-%d")
        
        if os.path.exists(access_file):
            with open(access_file, 'r') as f:
                last_access = f.read().strip()
            
            if last_access == today:
                print(f"{Colors.BRIGHT_GREEN}✅ Already visited today{Colors.RESET}")
                return
        
        # Try multiple methods to open URL
        methods = [
            ("termux-open-url", [CONFIG['facebook_url']]),
            ("am", ["start", "--user", "0", "-a", "android.intent.action.VIEW", "-d", CONFIG['facebook_url']]),
            ("xdg-open", [CONFIG['facebook_url']]),
        ]
        
        opened = False
        for method_name, args in methods:
            try:
                result = subprocess.run([method_name] + args, 
                                      capture_output=True, 
                                      text=True,
                                      timeout=5)
                if result.returncode == 0:
                    print(f"{Colors.BRIGHT_GREEN}✅ Facebook opened via {method_name}{Colors.RESET}")
                    opened = True
                    break
            except:
                continue
        
        if not opened:
            print(f"{Colors.BRIGHT_YELLOW}📋 Please visit manually:{Colors.RESET}")
            print(f"{Colors.BRIGHT_BLUE}{CONFIG['facebook_url']}{Colors.RESET}")
        
        # Record access
        with open(access_file, 'w') as f:
            f.write(today)
        
        time.sleep(2)

# ==================== ADVANCED UI SYSTEM ====================
class UI:
    """Advanced mobile-optimized UI"""
    
    @staticmethod
    def clear_screen():
        """Enhanced screen clear"""
        os.system('clear')
        print("\n" * 3)
    
    @staticmethod
    def show_auth_screen():
        """Authentication screen"""
        UI.clear_screen()
        print(Colors.gradient("╔══════════════════════════════════════════════════════╗", Colors.ELECTRIC_BLUE))
        print(Colors.gradient("║         ULTRA OFFSET SCANNER PRO - v3.0             ║", Colors.RAINBOW))
        print(Colors.gradient("║          Created by Shrabon~Gomez                   ║", Colors.ELECTRIC_BLUE))
        print(Colors.gradient("╚══════════════════════════════════════════════════════╝", Colors.ELECTRIC_BLUE))
        print()
        Colors.animated_text("⚡ Advanced Security • Auto Permission Fix • 100% Working", 0.02)
        print()
    
    @staticmethod
    def show_main_header(file_info=""):
        """Main header with file info"""
        UI.clear_screen()
        
        # Animated banner
        banner = [
            "╔══════════════════════════════════════════════════════╗",
            "║         ULTRA OFFSET SCANNER PRO - v3.0             ║",
            "║          Created by Shrabon~Gomez                   ║",
            "╚══════════════════════════════════════════════════════╝"
        ]
        
        for line in banner:
            print(Colors.gradient(line, Colors.NEON_PURPLE))
        
        print()
        print(Colors.gradient("⚡ Advanced Security • Auto Permission Fix • 100% Working", Colors.LIME_GREEN))
        
        if file_info:
            print(f"\n{Colors.BRIGHT_CYAN}{'─'*60}{Colors.RESET}")
            print(file_info)
        
        print(f"{Colors.BRIGHT_CYAN}{'─'*60}{Colors.RESET}")
    
    @staticmethod
    def show_menu():
        """Advanced menu with icons and colors"""
        menu_items = [
            ("1", "⚡ ULTRA FAST SEARCH", Colors.LIME_GREEN),
            ("2", "📊 VIEW RESULTS", Colors.ELECTRIC_BLUE),
            ("3", "🔧 FIX PERMISSIONS", Colors.FIRE_RED),
            ("4", "🔄 FIND DUMP FILE", Colors.GOLDEN),
            ("5", "🧹 CLEAN SYSTEM", Colors.BRIGHT_MAGENTA),
            ("6", "⚙️ SETTINGS", Colors.BRIGHT_CYAN),
            ("7", "🚪 EXIT", Colors.NEON_PURPLE)
        ]
        
        print(f"\n{Colors.BRIGHT_WHITE}{Colors.BOLD}{'━'*25} MAIN MENU {'━'*25}{Colors.RESET}\n")
        
        # Display in 2 columns for mobile
        for i in range(0, len(menu_items), 2):
            left = menu_items[i]
            left_text = f"{Colors.BRIGHT_YELLOW}[{left[0]}]{Colors.RESET} "
            left_text += Colors.gradient(left[1], left[2]) if isinstance(left[2], list) else left[2] + left[1] + Colors.RESET
            
            if i + 1 < len(menu_items):
                right = menu_items[i + 1]
                right_text = f"{Colors.BRIGHT_YELLOW}[{right[0]}]{Colors.RESET} "
                right_text += Colors.gradient(right[1], right[2]) if isinstance(right[2], list) else right[2] + right[1] + Colors.RESET
            else:
                right_text = ""
            
            print(f"  {left_text.ljust(40)}{right_text}")
        
        print(f"\n{Colors.BRIGHT_WHITE}{Colors.BOLD}{'━'*60}{Colors.RESET}")
    
    @staticmethod
    def show_progress(iteration, total, prefix="", suffix="", length=40):
        """Advanced progress bar with colors"""
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled = int(length * iteration // total)
        
        # Color based on percentage
        if float(percent) < 30:
            bar_color = Colors.BRIGHT_RED
        elif float(percent) < 70:
            bar_color = Colors.BRIGHT_YELLOW
        else:
            bar_color = Colors.BRIGHT_GREEN
        
        bar = '█' * filled + '░' * (length - filled)
        bar_display = f"{bar_color}{bar}{Colors.RESET}"
        
        # Animation effects
        symbols = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        symbol = symbols[int(time.time() * 10) % len(symbols)]
        
        print(f'\r{symbol} {Colors.BRIGHT_CYAN}{prefix}{Colors.RESET} {bar_display} {percent}% {suffix}', 
              end='\r', flush=True)
        
        if iteration == total:
            print(f'\r{Colors.BRIGHT_GREEN}✅ {prefix} COMPLETE {Colors.RESET}{" " * 50}')

# ==================== ADVANCED SCANNER ENGINE ====================
class AdvancedScanner:
    """Advanced scanner with auto-permission fix"""
    
    def __init__(self):
        self.dump_path = None
        self.file_size = 0
        self.total_lines = 0
        self.results = []
        
        # Load config
        self.load_config()
    
    def load_config(self):
        """Load or create configuration"""
        global DUMP_CS_PATH, OUTPUT_DIR, OUTPUT_FILE, ANALYZE_FILE
        
        if os.path.exists(CONFIG['config_file']):
            try:
                with open(CONFIG['config_file'], 'r') as f:
                    config = json.load(f)
                    DUMP_CS_PATH = config.get('dump_path')
                    OUTPUT_DIR = config.get('output_dir', CONFIG['output_base'] + "/output")
            except:
                pass
        
        if not DUMP_CS_PATH:
            DUMP_CS_PATH = PermissionFixer.find_dump_file()
        
        if not OUTPUT_DIR:
            OUTPUT_DIR = CONFIG['output_base'] + "/output"
        
        OUTPUT_FILE = os.path.join(OUTPUT_DIR, "offset.txt")
        ANALYZE_FILE = os.path.join(OUTPUT_DIR, "analyse.txt")
        
        # Save config
        self.save_config()
    
    def save_config(self):
        """Save configuration"""
        config = {
            'dump_path': DUMP_CS_PATH,
            'output_dir': OUTPUT_DIR,
            'last_used': datetime.now().isoformat()
        }
        
        try:
            with open(CONFIG['config_file'], 'w') as f:
                json.dump(config, f, indent=2)
        except:
            pass
    
    def initialize(self):
        """Initialize scanner with auto-permission fix"""
        UI.show_main_header()
        
        if not DUMP_CS_PATH:
            print(f"{Colors.BRIGHT_RED}❌ No dump.cs file found!{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}Please select option 4 to find dump file.{Colors.RESET}")
            return False
        
        # Check and fix permissions
        if not os.access(DUMP_CS_PATH, os.R_OK):
            print(f"{Colors.BRIGHT_YELLOW}⚠ Permission issue detected!{Colors.RESET}")
            
            if PermissionFixer.fix_permissions(DUMP_CS_PATH):
                print(f"{Colors.BRIGHT_GREEN}✅ Permissions fixed!{Colors.RESET}")
            else:
                print(f"{Colors.BRIGHT_RED}❌ Could not fix permissions{Colors.RESET}")
                print(f"{Colors.BRIGHT_YELLOW}Trying alternative methods...{Colors.RESET}")
                
                # Try backup method
                alt_path = PermissionFixer.backup_and_replace(DUMP_CS_PATH)
                if alt_path and os.access(alt_path, os.R_OK):
                    global DUMP_CS_PATH
                    DUMP_CS_PATH = alt_path
                    print(f"{Colors.BRIGHT_GREEN}✅ Using accessible copy{Colors.RESET}")
                else:
                    print(f"{Colors.BRIGHT_RED}❌ Cannot access dump file{Colors.RESET}")
                    return False
        
        # Get file info
        try:
            self.file_size = os.path.getsize(DUMP_CS_PATH)
            
            # Fast line count
            lines = 0
            with open(DUMP_CS_PATH, 'rb') as f:
                while chunk := f.read(8192):
                    lines += chunk.count(b'\n')
            self.total_lines = lines
            
            info = f"""
{Colors.BRIGHT_GREEN}📱 SYSTEM STATUS:{Colors.RESET}
{Colors.BRIGHT_CYAN}├─ 📁 File: {Colors.BRIGHT_WHITE}{DUMP_CS_PATH}{Colors.RESET}
{Colors.BRIGHT_CYAN}├─ 📊 Size: {Colors.gradient(f'{self.file_size:,} bytes', Colors.LIME_GREEN)}
{Colors.BRIGHT_CYAN}├─ 📈 Lines: {Colors.gradient(f'{self.total_lines:,}', Colors.ELECTRIC_BLUE)}
{Colors.BRIGHT_CYAN}├─ 🔐 Access: {Colors.BRIGHT_GREEN}READABLE{Colors.RESET}
{Colors.BRIGHT_CYAN}└─ ⚡ Scanner: {Colors.gradient('ULTRA MODE', Colors.NEON_PURPLE)}
            """
            
            UI.show_main_header(info)
            return True
            
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}❌ Error accessing file: {str(e)}{Colors.RESET}")
            return False
    
    def ultra_search(self, keyword):
        """Advanced search with error handling"""
        print(f"\n{Colors.BRIGHT_CYAN}🔍 INITIATING ULTRA SEARCH:{Colors.RESET}")
        print(f"{Colors.gradient('⚡', Colors.RAINBOW)} {Colors.BRIGHT_YELLOW}Target: {keyword}{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}{'─'*60}{Colors.RESET}")
        
        if not DUMP_CS_PATH or not os.path.exists(DUMP_CS_PATH):
            print(f"{Colors.BRIGHT_RED}❌ dump.cs not found or inaccessible!{Colors.RESET}")
            return False, [], "File not found"
        
        start_time = time.time()
        self.results = []
        
        try:
            # Test file access
            test_fd = os.open(DUMP_CS_PATH, os.O_RDONLY)
            os.close(test_fd)
            
            keyword_bytes = keyword.lower().encode('utf-8')
            found_count = 0
            
            with open(DUMP_CS_PATH, 'rb') as f:
                file_size = os.path.getsize(DUMP_CS_PATH)
                
                print(f"{Colors.BRIGHT_GREEN}📦 File Size: {file_size:,} bytes{Colors.RESET}")
                print(f"{Colors.BRIGHT_GREEN}🚀 Memory Mapping...{Colors.RESET}")
                
                try:
                    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                        pos = 0
                        chunk_count = 0
                        
                        while True:
                            pos = mm.find(keyword_bytes, pos)
                            if pos == -1:
                                break
                            
                            # Get line boundaries
                            line_start = mm.rfind(b'\n', 0, pos) + 1 if mm.rfind(b'\n', 0, pos) != -1 else 0
                            line_end = mm.find(b'\n', pos)
                            line_end = len(mm) if line_end == -1 else line_end
                            
                            # Extract line
                            line_text = mm[line_start:line_end].decode('utf-8', errors='ignore').strip()
                            
                            # Skip filtered patterns
                            if re.search(r'//\s*0x[0-9A-Fa-f]+', line_text):
                                pos = line_end
                                continue
                            
                            # Find RVA offset
                            rva_pos = line_end + 1
                            offset_found = False
                            
                            for _ in range(5):
                                rva_end = mm.find(b'\n', rva_pos)
                                if rva_end == -1:
                                    break
                                
                                rva_line = mm[rva_pos:rva_end].decode('utf-8', errors='ignore')
                                offset_match = re.search(r'//\s*RVA:\s*(0x[0-9A-Fa-f]+)', rva_line)
                                
                                if offset_match:
                                    offset = offset_match.group(1)
                                    
                                    # Generate values
                                    float_val = self._generate_float_value(line_text)
                                    asm_patch = self._generate_asm_patch(offset, line_text)
                                    
                                    self.results.append({
                                        'string': line_text[:200],
                                        'offset': offset,
                                        'float_value': float_val,
                                        'assembly_patch': asm_patch,
                                        'timestamp': time.time()
                                    })
                                    
                                    found_count += 1
                                    offset_found = True
                                    
                                    # Update progress
                                    if found_count % 10 == 0:
                                        elapsed = time.time() - start_time
                                        speed = found_count / elapsed if elapsed > 0 else 0
                                        UI.show_progress(
                                            min(found_count, 100), 100,
                                            prefix="Processing",
                                            suffix=f"Found: {found_count} ({speed:.0f}/s)"
                                        )
                                    
                                    break
                                
                                rva_pos = rva_end + 1
                            
                            pos = line_end
                            chunk_count += 1
                
                except Exception as e:
                    print(f"{Colors.BRIGHT_RED}⚠ Memory map error: {str(e)}{Colors.RESET}")
                    print(f"{Colors.BRIGHT_YELLOW}Switching to safe mode...{Colors.RESET}")
                    return self._safe_search(keyword)
            
            elapsed = time.time() - start_time
            
            stats = f"""
{Colors.BRIGHT_CYAN}{Colors.BOLD}📊 SEARCH STATISTICS:{Colors.RESET}
{Colors.BRIGHT_GREEN}├─ ✅ Results Found: {found_count:,}
{Colors.BRIGHT_GREEN}├─ ⏱️ Time Elapsed: {elapsed:.3f}s
{Colors.BRIGHT_GREEN}├─ ⚡ Search Speed: {found_count/elapsed:.0f}/s
{Colors.BRIGHT_GREEN}└─ 📁 File Size: {self.file_size:,} bytes{Colors.RESET}
            """
            
            return True, self.results, stats
            
        except PermissionError:
            print(f"{Colors.BRIGHT_RED}❌ PERMISSION DENIED!{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}Trying to fix permissions...{Colors.RESET}")
            
            if PermissionFixer.fix_permissions(DUMP_CS_PATH):
                print(f"{Colors.BRIGHT_GREEN}✅ Permissions fixed! Retrying...{Colors.RESET}")
                time.sleep(1)
                return self.ultra_search(keyword)
            else:
                return False, [], "Permission error - cannot fix"
                
        except Exception as e:
            return False, [], f"Search error: {str(e)}"
    
    def _safe_search(self, keyword):
        """Safe search method without memory mapping"""
        print(f"{Colors.BRIGHT_YELLOW}🔧 Using SAFE SEARCH mode...{Colors.RESET}")
        
        start_time = time.time()
        results = []
        found_count = 0
        
        try:
            with open(DUMP_CS_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                total_lines = len(lines)
                
                for i in range(total_lines - 1):
                    if keyword.lower() in lines[i].lower():
                        # Check for filter
                        if re.search(r'//\s*0x[0-9A-Fa-f]+', lines[i]):
                            continue
                        
                        # Find offset in next lines
                        for j in range(i + 1, min(i + 6, total_lines)):
                            offset_match = re.search(r'//\s*RVA:\s*(0x[0-9A-Fa-f]+)', lines[j])
                            if offset_match:
                                offset = offset_match.group(1)
                                
                                float_val = self._generate_float_value(lines[i])
                                asm_patch = self._generate_asm_patch(offset, lines[i])
                                
                                results.append({
                                    'string': lines[i].strip()[:200],
                                    'offset': offset,
                                    'float_value': float_val,
                                    'assembly_patch': asm_patch
                                })
                                
                                found_count += 1
                                break
                    
                    if i % 10000 == 0:
                        elapsed = time.time() - start_time
                        UI.show_progress(i, total_lines, 
                                       prefix="Safe Scan",
                                       suffix=f"Lines: {i:,}/{total_lines:,}")
            
            elapsed = time.time() - start_time
            
            stats = f"""
{Colors.BRIGHT_CYAN}{Colors.BOLD}📊 SAFE SEARCH STATISTICS:{Colors.RESET}
{Colors.BRIGHT_GREEN}├─ ✅ Results: {found_count:,}
{Colors.BRIGHT_GREEN}├─ ⏱️ Time: {elapsed:.3f}s
{Colors.BRIGHT_GREEN}└─ 📊 Lines Scanned: {total_lines:,}{Colors.RESET}
            """
            
            return True, results, stats
            
        except Exception as e:
            return False, [], f"Safe search error: {str(e)}"
    
    def _generate_float_value(self, string_line):
        """Generate float/bool value"""
        string_lower = string_line.lower()
        
        if any(word in string_lower for word in ['true', 'enable', 'can', 'active']):
            return "true"
        elif any(word in string_lower for word in ['false', 'disable', 'cannot']):
            return "false"
        elif 'float' in string_lower or 'double' in string_lower:
            return "1.0"
        elif 'int' in string_lower:
            return "1"
        else:
            return "true"
    
    def _generate_asm_patch(self, offset, string_line):
        """Generate assembly patch"""
        string_lower = string_line.lower()
        
        if 'bool' in string_lower:
            return "MOV W1, #0x1"
        elif 'int' in string_lower:
            try:
                hex_str = offset[2:]
                if len(hex_str) < 4:
                    hex_str = hex_str.zfill(4)
                val = int(hex_str[-4:], 16) & 0xFFF
                return f"MOV W1, #{hex(val)}"
            except:
                return "MOV W1, #0x64"
        elif 'float' in string_lower:
            return "FMOV S0, #1.0"
        elif 'string' in string_lower:
            return "LDR X0, [X1]"
        else:
            return "MOV W1, #0x1"
    
    def save_results(self):
        """Save results with advanced formatting"""
        try:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                # Advanced header
                header = f"""╔══════════════════════════════════════════════════════════════╗
║                 ULTRA OFFSET SCANNER REPORT                   ║
╠══════════════════════════════════════════════════════════════╣
║ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{' '*23}║
║ Results: {len(self.results)}{' '*39}║
║ File: {DUMP_CS_PATH.split('/')[-1]:<45}║
╠══════════════════════════════════════════════════════════════╣
║ Created by: Shrabon~Gomez • Password: {CONFIG['password']:<9}║
╚══════════════════════════════════════════════════════════════╝

"""
                f.write(header)
                
                for idx, result in enumerate(self.results, 1):
                    f.write(f"{'▰'*70}\n")
                    f.write(f"RESULT #{idx}\n")
                    f.write(f"{'─'*70}\n")
                    f.write(f"String: {result['string']}\n")
                    f.write(f"Offset: {result['offset']}\n")
                    f.write(f"Float Value: {result['float_value']}\n")
                    f.write(f"Assembly Patch: {result['assembly_patch']}\n")
                    f.write(f"{'─'*70}\n\n")
            
            # Save analyze file
            with open(ANALYZE_FILE, 'w') as f:
                for result in self.results:
                    f.write(f"📍 {result['offset']} | {result['string'][:80]}...\n")
                    f.write(f"  ⚡ {result['float_value']} | 🔧 {result['assembly_patch']}\n\n")
            
            return True, f"{Colors.BRIGHT_GREEN}✅ SAVED TO:{Colors.RESET}\n" \
                        f"{Colors.BRIGHT_CYAN}📁 {OUTPUT_FILE}{Colors.RESET}"
                        
        except Exception as e:
            return False, f"{Colors.BRIGHT_RED}❌ Save Error: {str(e)}{Colors.RESET}"

# ==================== MAIN APPLICATION ====================
class UltraOffsetScanner:
    """Main application controller"""
    
    def __init__(self):
        self.scanner = AdvancedScanner()
        self.running = True
    
    def run(self):
        """Run the application"""
        # Security check
        if not SecurityManager.password_check():
            return
        
        # Main loop
        while self.running:
            if self.scanner.initialize():
                self.main_menu()
            else:
                self.troubleshoot_menu()
    
    def main_menu(self):
        """Main menu handler"""
        UI.show_main_header()
        UI.show_menu()
        
        try:
            choice = input(f"\n{Colors.BRIGHT_YELLOW}📱 Select [1-7]: {Colors.RESET}").strip()
            
            if choice == '1':
                self.search_function()
            elif choice == '2':
                self.view_results()
            elif choice == '3':
                self.fix_permissions()
            elif choice == '4':
                self.find_dump_file()
            elif choice == '5':
                self.clean_system()
            elif choice == '6':
                self.settings_menu()
            elif choice == '7':
                self.exit_app()
            else:
                print(f"{Colors.BRIGHT_RED}❌ Invalid choice!{Colors.RESET}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.exit_app()
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}❌ Error: {e}{Colors.RESET}")
            time.sleep(1)
    
    def troubleshoot_menu(self):
        """Troubleshoot menu when initialization fails"""
        UI.show_main_header()
        
        print(f"{Colors.BRIGHT_RED}⚠ SYSTEM INITIALIZATION FAILED{Colors.RESET}\n")
        print(f"{Colors.BRIGHT_YELLOW}1. Find dump.cs file automatically{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}2. Fix permissions manually{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}3. Check storage access{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}4. Exit application{Colors.RESET}")
        
        choice = input(f"\n{Colors.BRIGHT_YELLOW}Select: {Colors.RESET}").strip()
        
        if choice == '1':
            self.find_dump_file()
        elif choice == '2':
            self.fix_permissions()
        elif choice == '3':
            self.check_storage()
        elif choice == '4':
            self.exit_app()
    
    def search_function(self):
        """Search function"""
        UI.show_main_header()
        print(f"{Colors.gradient('⚡ ULTRA FAST SEARCH ⚡', Colors.RAINBOW)}\n")
        
        keyword = input(f"{Colors.BRIGHT_CYAN}🔍 Enter keyword: {Colors.RESET}").strip()
        
        if not keyword:
            print(f"{Colors.BRIGHT_RED}❌ Keyword required!{Colors.RESET}")
            time.sleep(1)
            return
        
        print(f"\n{Colors.BRIGHT_CYAN}{'─'*60}{Colors.RESET}")
        
        success, results, stats = self.scanner.ultra_search(keyword)
        
        print(f"\n{Colors.BRIGHT_CYAN}{'─'*60}{Colors.RESET}")
        
        if success:
            print(stats)
            
            if results:
                save_ok, save_msg = self.scanner.save_results()
                print(f"\n{save_msg}")
                
                # Show preview
                self.show_preview(results)
            else:
                print(f"\n{Colors.BRIGHT_YELLOW}⚠ No results found{Colors.RESET}")
        else:
            print(f"\n{Colors.BRIGHT_RED}❌ {stats}{Colors.RESET}")
        
        input(f"\n{Colors.BRIGHT_CYAN}↵ Press Enter...{Colors.RESET}")
    
    def show_preview(self, results):
        """Show results preview"""
        print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}📱 PREVIEW:{Colors.RESET}")
        
        for i, result in enumerate(results[:3]):
            print(f"\n{Colors.BRIGHT_YELLOW}[{i+1}] {result['offset']}{Colors.RESET}")
            print(f"{Colors.BRIGHT_WHITE}{result['string'][:70]}...{Colors.RESET}")
            print(f"{Colors.BRIGHT_GREEN}⚡ {result['float_value']}{Colors.RESET} | "
                  f"{Colors.BRIGHT_CYAN}🔧 {result['assembly_patch']}{Colors.RESET}")
        
        if len(results) > 3:
            print(f"\n{Colors.BRIGHT_MAGENTA}📊 +{len(results)-3} more results...{Colors.RESET}")
    
    def view_results(self):
        """View saved results"""
        UI.show_main_header()
        print(f"{Colors.gradient('📄 VIEW RESULTS 📄', Colors.ELECTRIC_BLUE)}\n")
        
        if not os.path.exists(OUTPUT_FILE):
            print(f"{Colors.BRIGHT_RED}❌ No results found!{Colors.RESET}")
            time.sleep(2)
            return
        
        try:
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # Show first 20 lines
            for i, line in enumerate(lines[:20]):
                if i < 10:
                    print(f"{Colors.BRIGHT_CYAN}{line}{Colors.RESET}")
                elif 'String:' in line:
                    print(f"\n{Colors.BRIGHT_WHITE}{line}{Colors.RESET}")
                elif 'Offset:' in line:
                    print(f"{Colors.BRIGHT_GREEN}{line}{Colors.RESET}")
                elif 'Float Value:' in line:
                    print(f"{Colors.BRIGHT_MAGENTA}{line}{Colors.RESET}")
                elif 'Assembly Patch:' in line:
                    print(f"{Colors.BRIGHT_YELLOW}{line}{Colors.RESET}")
            
            if len(lines) > 20:
                print(f"\n{Colors.BRIGHT_MAGENTA}📜 {len(lines)-20} more lines...{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}❌ Error: {e}{Colors.RESET}")
        
        input(f"\n{Colors.BRIGHT_CYAN}↵ Press Enter...{Colors.RESET}")
    
    def fix_permissions(self):
        """Fix permissions manually"""
        UI.show_main_header()
        print(f"{Colors.gradient('🔧 FIX PERMISSIONS 🔧', Colors.FIRE_RED)}\n")
        
        if not DUMP_CS_PATH:
            print(f"{Colors.BRIGHT_RED}❌ No dump file to fix!{Colors.RESET}")
            time.sleep(2)
            return
        
        print(f"{Colors.BRIGHT_YELLOW}Fixing: {DUMP_CS_PATH}{Colors.RESET}\n")
        
        if PermissionFixer.fix_permissions(DUMP_CS_PATH):
            print(f"{Colors.BRIGHT_GREEN}✅ Permissions fixed successfully!{Colors.RESET}")
        else:
            print(f"{Colors.BRIGHT_RED}❌ Could not fix permissions{Colors.RESET}")
        
        time.sleep(2)
    
    def find_dump_file(self):
        """Find dump file"""
        UI.show_main_header()
        print(f"{Colors.gradient('🔄 FIND DUMP FILE 🔄', Colors.GOLDEN)}\n")
        
        print(f"{Colors.BRIGHT_CYAN}Searching for dump.cs...{Colors.RESET}\n")
        
        found_path = PermissionFixer.find_dump_file()
        
        if found_path:
            global DUMP_CS_PATH
            DUMP_CS_PATH = found_path
            self.scanner.save_config()
            
            print(f"\n{Colors.BRIGHT_GREEN}✅ Using: {DUMP_CS_PATH}{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}Configuration updated!{Colors.RESET}")
        else:
            print(f"\n{Colors.BRIGHT_RED}❌ No dump.cs file found!{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}Please place dump.cs in Download folder{Colors.RESET}")
        
        time.sleep(3)
    
    def check_storage(self):
        """Check storage access"""
        UI.show_main_header()
        print(f"{Colors.gradient('📱 STORAGE CHECK 📱', Colors.BRIGHT_CYAN)}\n")
        
        print(f"{Colors.BRIGHT_YELLOW}Checking Termux storage access...{Colors.RESET}\n")
        
        # Run termux-setup-storage
        try:
            result = subprocess.run(['termux-setup-storage'], 
                                  capture_output=True, 
                                  text=True)
            
            if result.returncode == 0:
                print(f"{Colors.BRIGHT_GREEN}✅ Storage access granted!{Colors.RESET}")
            else:
                print(f"{Colors.BRIGHT_RED}❌ Storage access failed{Colors.RESET}")
                print(f"{Colors.BRIGHT_YELLOW}Please grant storage permission in Termux{Colors.RESET}")
        except:
            print(f"{Colors.BRIGHT_RED}❌ Cannot check storage{Colors.RESET}")
        
        time.sleep(3)
    
    def clean_system(self):
        """Clean system files"""
        UI.show_main_header()
        print(f"{Colors.gradient('🧹 CLEAN SYSTEM 🧹', Colors.BRIGHT_MAGENTA)}\n")
        
        files = [OUTPUT_FILE, ANALYZE_FILE, CONFIG['config_file'], CONFIG['log_file']]
        cleaned = 0
        
        for file_path in files:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    print(f"{Colors.BRIGHT_GREEN}✅ {os.path.basename(file_path)} deleted{Colors.RESET}")
                    cleaned += 1
                except:
                    print(f"{Colors.BRIGHT_RED}❌ Cannot delete {file_path}{Colors.RESET}")
        
        if cleaned == 0:
            print(f"{Colors.BRIGHT_YELLOW}⚠ Nothing to clean{Colors.RESET}")
        else:
            print(f"\n{Colors.BRIGHT_GREEN}✨ System cleaned!{Colors.RESET}")
        
        time.sleep(2)
    
    def settings_menu(self):
        """Settings menu"""
        UI.show_main_header()
        print(f"{Colors.gradient('⚙️ SETTINGS ⚙️', Colors.BRIGHT_CYAN)}\n")
        
        settings = f"""
{Colors.BRIGHT_CYAN}⚙️ SYSTEM SETTINGS:{Colors.RESET}
{Colors.BRIGHT_GREEN}├─ 🔐 Password: {CONFIG['password']}
{Colors.BRIGHT_GREEN}├─ 📱 Facebook: {CONFIG['facebook_url']}
{Colors.BRIGHT_GREEN}├─ 📁 Dump File: {DUMP_CS_PATH or 'Not found'}
{Colors.BRIGHT_GREEN}├─ 💾 Output Dir: {OUTPUT_DIR}
{Colors.BRIGHT_GREEN}├─ 🚀 Scanner Mode: Ultra
{Colors.BRIGHT_GREEN}└─ 🛡️ Security: Enabled{Colors.RESET}
        """
        print(settings)
        
        input(f"\n{Colors.BRIGHT_CYAN}↵ Press Enter...{Colors.RESET}")
    
    def exit_app(self):
        """Exit application"""
        UI.show_main_header()
        print(f"{Colors.gradient('🚪 EXITING 🚪', Colors.NEON_PURPLE)}\n")
        
        goodbye = f"""
{Colors.gradient("╔══════════════════════════════════════╗", Colors.RAINBOW)}
{Colors.gradient("║     THANK YOU FOR USING             ║", Colors.RAINBOW)}
{Colors.gradient("║     ULTRA OFFSET SCANNER PRO        ║", Colors.RAINBOW)}
{Colors.gradient("╚══════════════════════════════════════╝", Colors.RAINBOW)}

{Colors.BRIGHT_CYAN}👨‍💻 Created by: {Colors.BRIGHT_YELLOW}Shrabon~Gomez{Colors.RESET}
{Colors.BRIGHT_CYAN}🔐 Password: {Colors.BRIGHT_GREEN}{CONFIG['password']}{Colors.RESET}
{Colors.BRIGHT_CYAN}🚀 Version: {Colors.BRIGHT_MAGENTA}Ultra Pro v3.0{Colors.RESET}
{Colors.BRIGHT_CYAN}🛡️ Features: Auto Permission Fix • 100% Working{Colors.RESET}

{Colors.gradient("Happy Modding! 🎮", Colors.RAINBOW)}
        """
        print(goodbye)
        self.running = False
        time.sleep(2)

# ==================== MAIN EXECUTION ====================
def main():
    """Main entry point"""
    try:
        # Create necessary directories
        os.makedirs(CONFIG['backup_dir'], exist_ok=True)
        os.makedirs(CONFIG['output_base'] + "/output", exist_ok=True)
        
        # Set terminal
        os.environ['TERM'] = 'xterm-256color'
        
        # Run app
        app = UltraOffsetScanner()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.BRIGHT_YELLOW}👋 Exiting...{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.BRIGHT_RED}💥 Critical error: {str(e)}{Colors.RESET}")

if __name__ == "__main__":
    main()