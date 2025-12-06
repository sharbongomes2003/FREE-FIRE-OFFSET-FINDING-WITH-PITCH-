#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════╗
║     Creating BY Shrabon~Gomez        ║
╚══════════════════════════════════════╝
        ⚡ ULTRA OFFSET SCANNER MAX ⚡
      Mobile Optimized • Auto Facebook
"""

import os
import re
import time
import mmap
import subprocess
import sys
from datetime import datetime

# ==================== CONFIGURATION ====================
PASSWORD = "SHRABON"
FACEBOOK_URL = "https://www.facebook.com/share/1B4TRBkyN3/"
DUMP_CS_PATH = "/storage/emulated/0/Download/dump.cs"
OUTPUT_DIR = "/storage/emulated/0/Download/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "offset.txt")
ANALYZE_FILE = os.path.join(OUTPUT_DIR, "analyse.txt")
ACCESS_FILE = os.path.join(OUTPUT_DIR, ".access_marker")

# ==================== MOBILE OPTIMIZED COLOR SYSTEM ====================
class MobileColors:
    """Mobile-optimized color system with multi-color effects"""
    
    # True Color (24-bit) for modern terminals
    @staticmethod
    def rgb(r, g, b):
        return f'\033[38;2;{r};{g};{b}m'
    
    @staticmethod
    def bg_rgb(r, g, b):
        return f'\033[48;2;{r};{g};{b}m'
    
    # Gradient Colors
    GRADIENT_PURPLE = [rgb(148, 0, 211), rgb(186, 85, 211), rgb(221, 160, 221)]
    GRADIENT_BLUE = [rgb(0, 0, 255), rgb(65, 105, 225), rgb(135, 206, 235)]
    GRADIENT_GREEN = [rgb(0, 255, 0), rgb(50, 205, 50), rgb(144, 238, 144)]
    GRADIENT_RED = [rgb(255, 0, 0), rgb(255, 69, 0), rgb(255, 140, 0)]
    GRADIENT_RAINBOW = [
        rgb(255, 0, 0),    # Red
        rgb(255, 127, 0),  # Orange
        rgb(255, 255, 0),  # Yellow
        rgb(0, 255, 0),    # Green
        rgb(0, 0, 255),    # Blue
        rgb(75, 0, 130),   # Indigo
        rgb(148, 0, 211)   # Violet
    ]
    
    # Pre-defined colors for performance
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    
    # Bright Colors (mobile friendly)
    BRIGHT = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m'
    }
    
    # Android Terminal Optimized Colors
    ANDROID = {
        'primary': rgb(0, 150, 255),     # Android Blue
        'accent': rgb(255, 193, 7),      # Android Yellow
        'success': rgb(76, 175, 80),     # Android Green
        'warning': rgb(255, 152, 0),     # Android Orange
        'error': rgb(244, 67, 54),       # Android Red
        'surface': rgb(33, 33, 33),      # Dark Surface
        'text': rgb(255, 255, 255)       # White Text
    }
    
    @staticmethod
    def gradient_text(text, gradient_colors):
        """Create smooth gradient text (mobile optimized)"""
        if len(text) <= 1:
            return gradient_colors[0] + text + MobileColors.RESET
        
        result = ""
        length = len(text)
        steps = len(gradient_colors)
        
        for i, char in enumerate(text):
            pos = i / max(1, length - 1)
            color_idx = min(steps - 1, int(pos * steps))
            result += gradient_colors[color_idx] + char
        
        return result + MobileColors.RESET
    
    @staticmethod
    def rainbow_text(text):
        """Rainbow effect optimized for mobile"""
        result = ""
        colors = MobileColors.GRADIENT_RAINBOW
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            result += color + char
        return result + MobileColors.RESET
    
    @staticmethod
    def pulse_text(text, speed=0.1):
        """Pulsing text effect for mobile"""
        import time
        colors = [
            MobileColors.ANDROID['primary'],
            MobileColors.ANDROID['accent'],
            MobileColors.BRIGHT['cyan'],
            MobileColors.ANDROID['primary']
        ]
        
        for color in colors:
            print(f"\r{color}{text}{MobileColors.RESET}", end='', flush=True)
            time.sleep(speed)
        print()

# ==================== MOBILE OPTIMIZED UI ====================
class MobileUI:
    """Mobile-optimized UI with beautiful displays"""
    
    @staticmethod
    def clear_screen():
        """Optimized screen clear for mobile"""
        os.system('clear' if os.name == 'posix' else 'cls')
        # Add some empty lines for better mobile display
        print("\n" * 2)
    
    @staticmethod
    def show_mobile_banner():
        """Mobile optimized banner with effects"""
        MobileUI.clear_screen()
        
        # Top decorative line
        print(MobileColors.gradient_text("╔══════════════════════════════════════════════════════╗", 
              MobileColors.GRADIENT_PURPLE))
        
        # Main title with rainbow effect
        title = "║     Creating BY Shrabon~Gomez        ║"
        print(MobileColors.rainbow_text(title))
        
        # Bottom decorative line
        print(MobileColors.gradient_text("╚══════════════════════════════════════════════════════╝", 
              MobileColors.GRADIENT_PURPLE))
        
        # Subtitle with pulse effect
        subtitle = "        ⚡ ULTRA OFFSET SCANNER MAX ⚡"
        MobileColors.pulse_text(subtitle, speed=0.08)
        
        # Tagline
        print(f"{MobileColors.ANDROID['accent']}{MobileColors.DIM}      Mobile Optimized • Auto Facebook • Ultra Fast{MobileColors.RESET}")
        
        # Separator
        print(MobileColors.gradient_text("─" * 60, MobileColors.GRADIENT_BLUE))
    
    @staticmethod
    def show_mobile_menu():
        """Beautiful mobile-optimized menu"""
        menu_items = [
            ("1", "⚡ LIGHTNING SEARCH", MobileColors.GRADIENT_GREEN),
            ("2", "📄 VIEW RESULTS", MobileColors.GRADIENT_BLUE),
            ("3", "🔍 FILTERED VIEW", MobileColors.GRADIENT_RED),
            ("4", "🧹 CLEAN SYSTEM", MobileColors.ANDROID['warning']),
            ("5", "⚙️ SETTINGS", MobileColors.BRIGHT['magenta']),
            ("6", "🚪 EXIT", MobileColors.GRADIENT_PURPLE)
        ]
        
        print(f"\n{MobileColors.ANDROID['primary']}{MobileColors.BOLD}{'━'*25} MOBILE MENU {'━'*25}{MobileColors.RESET}\n")
        
        # Display in 2 columns for better mobile view
        col_width = 30
        for i in range(0, len(menu_items), 2):
            # Left item
            left = menu_items[i]
            left_text = f"{MobileColors.BRIGHT['yellow']}[{left[0]}]{MobileColors.RESET} "
            
            if isinstance(left[2], list):
                left_text += MobileColors.gradient_text(left[1], left[2])
            else:
                left_text += left[2] + left[1] + MobileColors.RESET
            
            # Right item (if exists)
            right_text = ""
            if i + 1 < len(menu_items):
                right = menu_items[i + 1]
                right_text = f"{MobileColors.BRIGHT['yellow']}[{right[0]}]{MobileColors.RESET} "
                
                if isinstance(right[2], list):
                    right_text += MobileColors.gradient_text(right[1], right[2])
                else:
                    right_text += right[2] + right[1] + MobileColors.RESET
            
            # Print row
            print(f"  {left_text.ljust(col_width)}{right_text}")
        
        print(f"\n{MobileColors.ANDROID['primary']}{MobileColors.BOLD}{'━'*62}{MobileColors.RESET}")
    
    @staticmethod
    def mobile_progress_bar(iteration, total, prefix='', suffix='', length=30):
        """Mobile-optimized progress bar"""
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled = int(length * iteration // total)
        
        # Dynamic color based on progress
        if float(percent) < 30:
            bar_color = MobileColors.BRIGHT['red']
        elif float(percent) < 70:
            bar_color = MobileColors.BRIGHT['yellow']
        else:
            bar_color = MobileColors.BRIGHT['green']
        
        bar = '█' * filled + '░' * (length - filled)
        bar_display = f"{bar_color}{bar}{MobileColors.RESET}"
        
        # Mobile optimized display
        print(f'\r{MobileColors.BRIGHT['cyan']}{prefix}{MobileColors.RESET} {bar_display} {percent}% {suffix}', 
              end='\r', flush=True)
        
        if iteration == total: 
            print(f"\r{MobileColors.BRIGHT['green']}{prefix} ✅ COMPLETE {MobileColors.RESET}{' ' * 50}")

# ==================== PASSWORD & AUTO-FACEBOOK SYSTEM ====================
class AccessManager:
    """Manage password and auto-facebook access"""
    
    @staticmethod
    def check_password():
        """Password check with mobile optimized UI"""
        MobileUI.clear_screen()
        
        # Show beautiful access screen
        print(MobileColors.gradient_text("╔══════════════════════════════════════╗", 
              MobileColors.GRADIENT_PURPLE))
        print(MobileColors.rainbow_text("║     ACCESS VERIFICATION SYSTEM       ║"))
        print(MobileColors.gradient_text("╚══════════════════════════════════════╝", 
              MobileColors.GRADIENT_PURPLE))
        
        print(f"\n{MobileColors.ANDROID['accent']}{MobileColors.BOLD}⚡ ULTRA OFFSET SCANNER MAX ⚡{MobileColors.RESET}")
        print(f"{MobileColors.ANDROID['text']}{MobileColors.DIM}Password Protected System{MobileColors.RESET}")
        print(MobileColors.gradient_text("─" * 50, MobileColors.GRADIENT_BLUE))
        
        attempts = 3
        while attempts > 0:
            print(f"\n{MobileColors.BRIGHT['yellow']}🔐 Enter Password [{attempts} attempts]:{MobileColors.RESET} ", end="")
            
            # For password hiding on mobile
            import getpass
            try:
                entered = getpass.getpass("")
            except:
                # Fallback for mobile
                entered = input()
            
            if entered == PASSWORD:
                print(f"\n{MobileColors.BRIGHT['green']}✅ ACCESS GRANTED!{MobileColors.RESET}")
                print(f"{MobileColors.ANDROID['success']}Welcome to Ultra Offset Scanner Max{MobileColors.RESET}")
                time.sleep(1)
                
                # Auto Facebook without asking
                AccessManager.auto_facebook()
                return True
            
            attempts -= 1
            print(f"\n{MobileColors.BRIGHT['red']}❌ WRONG PASSWORD!{MobileColors.RESET}")
            print(f"{MobileColors.ANDROID['warning']}{attempts} attempts remaining{MobileColors.RESET}")
            time.sleep(1)
        
        print(f"\n{MobileColors.BRIGHT['red']}{MobileColors.BLINK}⛔ ACCESS DENIED!{MobileColors.RESET}")
        print(f"{MobileColors.ANDROID['error']}Too many failed attempts{MobileColors.RESET}")
        time.sleep(2)
        return False
    
    @staticmethod
    def auto_facebook():
        """Automatically open Facebook link without asking"""
        print(f"\n{MobileColors.BRIGHT['cyan']}📱 Auto-Facebook System{MobileColors.RESET}")
        print(f"{MobileColors.ANDROID['primary']}Opening Facebook...{MobileColors.RESET}")
        
        try:
            # Check if already accessed today
            if os.path.exists(ACCESS_FILE):
                with open(ACCESS_FILE, 'r') as f:
                    last_access = f.read().strip()
                    today = datetime.now().strftime("%Y-%m-%d")
                    
                    if last_access == today:
                        print(f"{MobileColors.ANDROID['accent']}✅ Already visited today{MobileColors.RESET}")
                        return
            
            # Try different methods to open URL
            print(f"{MobileColors.BRIGHT['blue']}🔗 Opening: {FACEBOOK_URL}{MobileColors.RESET}")
            
            # Method 1: Using termux-open-url
            try:
                subprocess.run(["termux-open-url", FACEBOOK_URL], check=False)
                print(f"{MobileColors.BRIGHT['green']}✅ Facebook opened successfully!{MobileColors.RESET}")
            except:
                # Method 2: Using am (Android intent)
                try:
                    subprocess.run(["am", "start", "--user", "0", "-a", "android.intent.action.VIEW", 
                                   "-d", FACEBOOK_URL], check=False)
                    print(f"{MobileColors.BRIGHT['green']}✅ Facebook intent sent!{MobileColors.RESET}")
                except:
                    # Method 3: Display link
                    print(f"{MobileColors.BRIGHT['yellow']}📋 Please visit manually:{MobileColors.RESET}")
                    print(f"{MobileColors.ANDROID['primary']}{FACEBOOK_URL}{MobileColors.RESET}")
            
            # Save access record
            with open(ACCESS_FILE, 'w') as f:
                f.write(datetime.now().strftime("%Y-%m-%d"))
            
        except Exception as e:
            print(f"{MobileColors.BRIGHT['red']}⚠ Facebook access error: {str(e)}{MobileColors.RESET}")
        
        time.sleep(1)

# ==================== MOBILE OPTIMIZED SCANNER ====================
class MobileScanner:
    """Mobile optimized scanner with ultra performance"""
    
    def __init__(self):
        self.dump_size = 0
        self.total_lines = 0
        
        # Optimized regex patterns
        self.patterns = {
            'offset': re.compile(rb'//\s*RVA:\s*(0x[0-9A-Fa-f]+)'),
            'filter': re.compile(rb'//\s*0x[0-9A-Fa-f]+'),
        }
    
    def get_mobile_file_info(self):
        """Get file info with mobile display"""
        try:
            if not os.path.exists(DUMP_CS_PATH):
                error_msg = f"{MobileColors.BRIGHT['red']}❌ dump.cs NOT FOUND!{MobileColors.RESET}"
                error_msg += f"\n{MobileColors.ANDROID['warning']}Please place at:{MobileColors.RESET}"
                error_msg += f"\n{MobileColors.ANDROID['primary']}{DUMP_CS_PATH}{MobileColors.RESET}"
                return False, error_msg
            
            self.dump_size = os.path.getsize(DUMP_CS_PATH)
            
            # Ultra fast line counting for mobile
            line_count = 0
            with open(DUMP_CS_PATH, 'rb') as f:
                while chunk := f.read(8192):
                    line_count += chunk.count(b'\n')
            
            self.total_lines = line_count
            size_mb = self.dump_size / (1024 * 1024)
            
            info = f"""
{MobileColors.BRIGHT['green']}📱 FILE STATUS:{MobileColors.RESET}
{MobileColors.ANDROID['accent']}├─ 📁 Path: {MobileColors.ANDROID['text']}{DUMP_CS_PATH}{MobileColors.RESET}
{MobileColors.ANDROID['accent']}├─ 📊 Size: {MobileColors.gradient_text(f'{size_mb:.2f} MB', MobileColors.GRADIENT_BLUE)}
{MobileColors.ANDROID['accent']}├─ 📈 Lines: {MobileColors.gradient_text(f'{self.total_lines:,}', MobileColors.GRADIENT_GREEN)}
{MobileColors.ANDROID['accent']}└─ 🕒 Modified: {MobileColors.ANDROID['text']}{time.ctime(os.path.getmtime(DUMP_CS_PATH))}{MobileColors.RESET}
            """
            return True, info
            
        except Exception as e:
            return False, f"{MobileColors.BRIGHT['red']}❌ Error: {str(e)}{MobileColors.RESET}"
    
    def mobile_lightning_search(self, keyword):
        """Ultra fast mobile optimized search"""
        print(f"\n{MobileColors.BRIGHT['cyan']}🔍 SEARCH INITIATED:{MobileColors.RESET}")
        print(f"{MobileColors.gradient_text('⚡', MobileColors.GRADIENT_RAINBOW)} "
              f"{MobileColors.ANDROID['primary']}Target: {MobileColors.BRIGHT['yellow']}{keyword}{MobileColors.RESET}")
        print(MobileColors.gradient_text("─" * 60, MobileColors.GRADIENT_BLUE))
        
        start_time = time.time()
        results = []
        
        try:
            keyword_bytes = keyword.lower().encode('utf-8')
            
            with open(DUMP_CS_PATH, 'rb') as f:
                file_size = os.path.getsize(DUMP_CS_PATH)
                
                with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                    print(f"{MobileColors.BRIGHT['green']}🚀 Memory Mapping ACTIVATED{MobileColors.RESET}")
                    print(f"{MobileColors.ANDROID['primary']}📦 Buffer: {file_size:,} bytes{MobileColors.RESET}")
                    
                    pos = 0
                    found = 0
                    
                    while True:
                        pos = mm.find(keyword_bytes, pos)
                        if pos == -1:
                            break
                        
                        # Get line
                        line_start = mm.rfind(b'\n', 0, pos)
                        line_start = line_start + 1 if line_start != -1 else 0
                        
                        line_end = mm.find(b'\n', pos)
                        line_end = len(mm) if line_end == -1 else line_end
                        
                        line_text = mm[line_start:line_end].decode('utf-8', errors='ignore').strip()
                        
                        # Filter check
                        if self.patterns['filter'].search(line_text.encode()):
                            pos = line_end
                            continue
                        
                        # Find RVA
                        rva_pos = line_end + 1
                        for _ in range(5):
                            rva_end = mm.find(b'\n', rva_pos)
                            if rva_end == -1:
                                break
                            
                            rva_line = mm[rva_pos:rva_end].decode('utf-8', errors='ignore')
                            offset_match = self.patterns['offset'].search(rva_line.encode())
                            
                            if offset_match:
                                offset = offset_match.group(1).decode()
                                
                                # Generate mobile-optimized values
                                float_val = self._mobile_generate_float(line_text)
                                asm_patch = self._mobile_generate_asm(offset, line_text)
                                
                                results.append({
                                    'string': line_text[:180],
                                    'offset': offset,
                                    'float_value': float_val,
                                    'assembly_patch': asm_patch,
                                    'color': self._get_string_color(line_text)
                                })
                                
                                found += 1
                                
                                # Mobile progress update
                                if found % 5 == 0:
                                    elapsed = time.time() - start_time
                                    speed = found / elapsed if elapsed > 0 else 0
                                    MobileUI.mobile_progress_bar(
                                        found % 100, 100,
                                        prefix='📥 Processing:',
                                        suffix=f'Found: {found} ({speed:.0f}/s)'
                                    )
                                
                                break
                            
                            rva_pos = rva_end + 1
                        
                        pos = line_end
            
            elapsed = time.time() - start_time
            
            stats = f"""
{MobileColors.BRIGHT['cyan']}{MobileColors.BOLD}📊 MOBILE STATS:{MobileColors.RESET}
{MobileColors.ANDROID['accent']}├─ ✅ Results: {MobileColors.gradient_text(str(found), MobileColors.GRADIENT_GREEN)}
{MobileColors.ANDROID['accent']}├─ ⏱️ Time: {MobileColors.gradient_text(f'{elapsed:.3f}s', MobileColors.GRADIENT_BLUE)}
{MobileColors.ANDROID['accent']}├─ ⚡ Speed: {MobileColors.gradient_text(f'{found/elapsed:.0f}/s', MobileColors.GRADIENT_PURPLE) if elapsed > 0 else 'N/A'}
{MobileColors.ANDROID['accent']}└─ 📁 Size: {MobileColors.ANDROID['text']}{self.dump_size:,} bytes{MobileColors.RESET}
            """
            
            return True, results, stats
            
        except Exception as e:
            return False, [], f"{MobileColors.BRIGHT['red']}❌ Search Error: {str(e)}{MobileColors.RESET}"
    
    def _mobile_generate_float(self, string_line):
        """Mobile optimized float generation"""
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
    
    def _mobile_generate_asm(self, offset, string_line):
        """Mobile optimized assembly generation"""
        string_lower = string_line.lower()
        
        if 'bool' in string_lower:
            return "MOV W1, #0x1"
        elif 'int' in string_lower:
            return "MOV W1, #0x64"
        elif 'float' in string_lower:
            return "FMOV S0, #1.0"
        elif 'string' in string_lower:
            return "LDR X0, [X1]"
        else:
            try:
                hex_str = offset[2:]
                if len(hex_str) < 4:
                    hex_str = hex_str.zfill(4)
                val = int(hex_str[-4:], 16) & 0xFFF
                return f"MOV W1, #{hex(val)}"
            except:
                return "MOV W1, #0x1"
    
    def _get_string_color(self, string_line):
        """Get color based on string type"""
        string_lower = string_line.lower()
        
        if 'bool' in string_lower:
            return MobileColors.BRIGHT['green']
        elif 'int' in string_lower:
            return MobileColors.BRIGHT['yellow']
        elif 'float' in string_lower:
            return MobileColors.BRIGHT['cyan']
        elif 'string' in string_lower:
            return MobileColors.BRIGHT['magenta']
        else:
            return MobileColors.ANDROID['text']
    
    def save_mobile_results(self, results):
        """Save results with mobile optimized formatting"""
        try:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                f.write("╔══════════════════════════════════════════════════════════════╗\n")
                f.write("║             MOBILE OFFSET SCANNER REPORT                   ║\n")
                f.write("╠══════════════════════════════════════════════════════════════╣\n")
                f.write(f"║ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"║ Results: {len(results)}\n")
                f.write("╠══════════════════════════════════════════════════════════════╣\n")
                f.write("║ Created by: Shrabon~Gomez\n")
                f.write("║ Password: SHRABON\n")
                f.write("║ Facebook: Auto-accessed\n")
                f.write("╚══════════════════════════════════════════════════════════════╝\n\n")
                
                for idx, result in enumerate(results, 1):
                    f.write(f"{'▰'*70}\n")
                    f.write(f"RESULT #{idx}\n")
                    f.write(f"{'─'*70}\n")
                    f.write(f"String: {result['string']}\n")
                    f.write(f"Offset: {result['offset']}\n")
                    f.write(f"Float Value: {result['float_value']}\n")
                    f.write(f"Assembly Patch: {result['assembly_patch']}\n")
                    f.write(f"{'─'*70}\n\n")
            
            with open(ANALYZE_FILE, 'w') as f:
                for result in results:
                    f.write(f"📍 {result['offset']} | {result['string'][:80]}...\n")
                    f.write(f"  ⚡ {result['float_value']} | 🔧 {result['assembly_patch']}\n\n")
            
            return True, f"{MobileColors.BRIGHT['green']}✅ SAVED TO:{MobileColors.RESET}\n" \
                        f"{MobileColors.ANDROID['primary']}📁 {OUTPUT_FILE}{MobileColors.RESET}\n" \
                        f"{MobileColors.ANDROID['accent']}📊 {ANALYZE_FILE}{MobileColors.RESET}"
                        
        except Exception as e:
            return False, f"{MobileColors.BRIGHT['red']}❌ Save Error: {str(e)}{MobileColors.RESET}"

# ==================== MAIN MOBILE APPLICATION ====================
class MobileOffsetScanner:
    """Main mobile application"""
    
    def __init__(self):
        self.scanner = MobileScanner()
        self.running = True
        self.results = []
    
    def run(self):
        """Run mobile application"""
        # Password check and auto-facebook
        if not AccessManager.check_password():
            return
        
        # Initialize
        self.show_welcome()
        
        # Main loop
        while self.running:
            MobileUI.show_mobile_banner()
            self.show_file_info()
            MobileUI.show_mobile_menu()
            self.handle_choice()
    
    def show_welcome(self):
        """Show welcome screen"""
        MobileUI.clear_screen()
        print(MobileColors.gradient_text("\n" + "═"*60, MobileColors.GRADIENT_RAINBOW))
        print(MobileColors.rainbow_text("       WELCOME TO ULTRA OFFSET SCANNER MAX"))
        print(MobileColors.gradient_text("═"*60, MobileColors.GRADIENT_RAINBOW))
        print(f"\n{MobileColors.ANDROID['accent']}🚀 Initializing Mobile System...{MobileColors.RESET}")
        time.sleep(1)
    
    def show_file_info(self):
        """Show file information"""
        success, info = self.scanner.get_mobile_file_info()
        if success:
            print(info)
        else:
            print(info)
            print(f"\n{MobileColors.BRIGHT['yellow']}⚠ Please fix the issue and restart{MobileColors.RESET}")
            time.sleep(3)
            self.running = False
    
    def handle_choice(self):
        """Handle user choice"""
        try:
            choice = input(f"\n{MobileColors.BRIGHT['yellow']}📱 Select [1-6]: {MobileColors.RESET}").strip()
            
            if choice == '1':
                self.search_menu()
            elif choice == '2':
                self.view_results()
            elif choice == '3':
                self.view_filtered()
            elif choice == '4':
                self.clean_system()
            elif choice == '5':
                self.settings_menu()
            elif choice == '6':
                self.exit_app()
            else:
                print(f"{MobileColors.BRIGHT['red']}❌ Invalid choice!{MobileColors.RESET}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.exit_app()
        except Exception as e:
            print(f"{MobileColors.BRIGHT['red']}❌ Error: {e}{MobileColors.RESET}")
            time.sleep(1)
    
    def search_menu(self):
        """Search menu with mobile UI"""
        MobileUI.show_mobile_banner()
        print(f"{MobileColors.gradient_text('⚡ LIGHTNING SEARCH ⚡', MobileColors.GRADIENT_RAINBOW)}\n")
        
        keyword = input(f"{MobileColors.BRIGHT['cyan']}🔍 Enter keyword: {MobileColors.RESET}").strip()
        
        if not keyword:
            print(f"{MobileColors.BRIGHT['red']}❌ Keyword required!{MobileColors.RESET}")
            time.sleep(1)
            return
        
        print(f"\n{MobileColors.gradient_text('─'*60, MobileColors.GRADIENT_BLUE)}")
        
        success, results, stats = self.scanner.mobile_lightning_search(keyword)
        
        print(f"\n{MobileColors.gradient_text('─'*60, MobileColors.GRADIENT_BLUE)}")
        print(stats)
        
        if success and results:
            self.results = results
            
            # Save results
            save_ok, save_msg = self.scanner.save_mobile_results(results)
            print(f"\n{save_msg}")
            
            # Show mobile preview
            self.show_mobile_preview(results)
        elif success:
            print(f"\n{MobileColors.BRIGHT['yellow']}⚠ No results found{MobileColors.RESET}")
        else:
            print(f"\n{MobileColors.BRIGHT['red']}❌ Search failed{MobileColors.RESET}")
        
        input(f"\n{MobileColors.BRIGHT['cyan']}↵ Press Enter...{MobileColors.RESET}")
    
    def show_mobile_preview(self, results):
        """Show mobile optimized preview"""
        print(f"\n{MobileColors.BRIGHT['cyan']}{MobileColors.BOLD}📱 MOBILE PREVIEW:{MobileColors.RESET}")
        
        for i, result in enumerate(results[:2]):
            print(f"\n{MobileColors.BRIGHT['yellow']}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{MobileColors.RESET}")
            print(f"{MobileColors.BRIGHT['green']}[{i+1}] {result['offset']}{MobileColors.RESET}")
            print(f"{MobileColors.ANDROID['text']}{result['string'][:70]}...{MobileColors.RESET}")
            print(f"{MobileColors.BRIGHT['magenta']}⚡ {result['float_value']}{MobileColors.RESET} | "
                  f"{MobileColors.BRIGHT['cyan']}🔧 {result['assembly_patch']}{MobileColors.RESET}")
        
        if len(results) > 2:
            print(f"\n{MobileColors.ANDROID['accent']}📊 +{len(results)-2} more results...{MobileColors.RESET}")
    
    def view_results(self):
        """View results with mobile UI"""
        MobileUI.show_mobile_banner()
        print(f"{MobileColors.gradient_text('📄 VIEW RESULTS 📄', MobileColors.GRADIENT_BLUE)}\n")
        
        if not os.path.exists(OUTPUT_FILE):
            print(f"{MobileColors.BRIGHT['red']}❌ No results found!{MobileColors.RESET}")
            print(f"{MobileColors.ANDROID['warning']}Run a search first{MobileColors.RESET}")
            time.sleep(2)
            return
        
        try:
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # Mobile optimized display (first 15 lines)
            for i, line in enumerate(lines[:15]):
                if i < 8:  # Header
                    print(f"{MobileColors.BRIGHT['cyan']}{line}{MobileColors.RESET}")
                elif 'String:' in line:
                    print(f"\n{MobileColors.ANDROID['text']}{line}{MobileColors.RESET}")
                elif 'Offset:' in line:
                    print(f"{MobileColors.BRIGHT['green']}{line}{MobileColors.RESET}")
                elif 'Float Value:' in line:
                    print(f"{MobileColors.BRIGHT['magenta']}{line}{MobileColors.RESET}")
                elif 'Assembly Patch:' in line:
                    print(f"{MobileColors.BRIGHT['yellow']}{line}{MobileColors.RESET}")
                elif line.startswith('▰'):
                    print(f"{MobileColors.ANDROID['primary']}{line}{MobileColors.RESET}")
            
            if len(lines) > 15:
                print(f"\n{MobileColors.ANDROID['accent']}📜 {len(lines)-15} more lines...{MobileColors.RESET}")
                
        except Exception as e:
            print(f"{MobileColors.BRIGHT['red']}❌ Read error: {e}{MobileColors.RESET}")
        
        input(f"\n{MobileColors.BRIGHT['cyan']}↵ Press Enter...{MobileColors.RESET}")
    
    def view_filtered(self):
        """View filtered results"""
        MobileUI.show_mobile_banner()
        print(f"{MobileColors.gradient_text('🔍 FILTERED VIEW 🔍', MobileColors.GRADIENT_RED)}\n")
        
        if not os.path.exists(ANALYZE_FILE):
            print(f"{MobileColors.BRIGHT['yellow']}⚠ No analyze file{MobileColors.RESET}")
            time.sleep(1)
            return
        
        try:
            with open(ANALYZE_FILE, 'r') as f:
                lines = f.readlines()
            
            for line in lines[:20]:
                if '📍' in line:
                    print(f"{MobileColors.BRIGHT['green']}{line.strip()}{MobileColors.RESET}")
                elif '⚡' in line:
                    print(f"{MobileColors.BRIGHT['cyan']}{line.strip()}{MobileColors.RESET}")
                elif line.strip():
                    print(f"{MobileColors.ANDROID['text']}{line.strip()}{MobileColors.RESET}")
            
            if len(lines) > 20:
                print(f"\n{MobileColors.ANDROID['accent']}📊 +{len(lines)-20} lines...{MobileColors.RESET}")
                
        except Exception as e:
            print(f"{MobileColors.BRIGHT['red']}❌ Error: {e}{MobileColors.RESET}")
        
        input(f"\n{MobileColors.BRIGHT['cyan']}↵ Press Enter...{MobileColors.RESET}")
    
    def clean_system(self):
        """Clean system files"""
        MobileUI.show_mobile_banner()
        print(f"{MobileColors.gradient_text('🧹 CLEAN SYSTEM 🧹', MobileColors.GRADIENT_RED)}\n")
        
        files = [OUTPUT_FILE, ANALYZE_FILE, ACCESS_FILE]
        cleaned = 0
        
        for file_path in files:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"{MobileColors.BRIGHT['green']}✅ {os.path.basename(file_path)} deleted{MobileColors.RESET}")
                cleaned += 1
        
        if cleaned == 0:
            print(f"{MobileColors.BRIGHT['yellow']}⚠ Nothing to clean{MobileColors.RESET}")
        else:
            print(f"\n{MobileColors.BRIGHT['green']}✨ System cleaned!{MobileColors.RESET}")
        
        self.results = []
        time.sleep(1.5)
    
    def settings_menu(self):
        """Settings menu"""
        MobileUI.show_mobile_banner()
        print(f"{MobileColors.gradient_text('⚙️ SETTINGS ⚙️', MobileColors.GRADIENT_BLUE)}\n")
        
        settings = f"""
{MobileColors.BRIGHT['cyan']}⚙️ SYSTEM SETTINGS:{MobileColors.RESET}
{MobileColors.ANDROID['accent']}├─ 🔐 Password: {MobileColors.BRIGHT['green']}{PASSWORD}{MobileColors.RESET}
{MobileColors.ANDROID['accent']}├─ 📱 Facebook: {MobileColors.ANDROID['primary']}{FACEBOOK_URL}{MobileColors.RESET}
{MobileColors.ANDROID['accent']}├─ 📁 Dump File: {MobileColors.ANDROID['text']}{DUMP_CS_PATH}{MobileColors.RESET}
{MobileColors.ANDROID['accent']}├─ 💾 Output Dir: {MobileColors.ANDROID['text']}{OUTPUT_DIR}{MobileColors.RESET}
{MobileColors.ANDROID['accent']}└─ 🚀 Scanner: {MobileColors.BRIGHT['yellow']}Ultra Mode{MobileColors.RESET}
        """
        print(settings)
        
        input(f"\n{MobileColors.BRIGHT['cyan']}↵ Press Enter...{MobileColors.RESET}")
    
    def exit_app(self):
        """Exit application"""
        MobileUI.show_mobile_banner()
        print(f"{MobileColors.gradient_text('🚪 EXITING 🚪', MobileColors.GRADIENT_PURPLE)}\n")
        
        goodbye = f"""
{MobileColors.rainbow_text("╔══════════════════════════════════════╗")}
{MobileColors.rainbow_text("║     THANK YOU FOR USING             ║")}
{MobileColors.rainbow_text("║     ULTRA OFFSET SCANNER MAX        ║")}
{MobileColors.rainbow_text("╚══════════════════════════════════════╝")}

{MobileColors.BRIGHT['cyan']}👨‍💻 Created by: {MobileColors.BRIGHT['yellow']}Shrabon~Gomez{MobileColors.RESET}
{MobileColors.BRIGHT['cyan']}🔐 Password: {MobileColors.BRIGHT['green']}SHRABON{MobileColors.RESET}
{MobileColors.BRIGHT['cyan']}📱 Facebook: {MobileColors.ANDROID['primary']}{FACEBOOK_URL}{MobileColors.RESET}
{MobileColors.BRIGHT['cyan']}🚀 Version: {MobileColors.BRIGHT['magenta']}Mobile Ultra v2.0{MobileColors.RESET}

{MobileColors.gradient_text("Happy Modding! 🎮", MobileColors.GRADIENT_RAINBOW)}
        """
        print(goodbye)
        self.running = False
        time.sleep(2)

# ==================== MAIN EXECUTION ====================
def main():
    """Main entry point - Mobile optimized"""
    try:
        # Create output directory
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Set mobile terminal
        os.environ['TERM'] = 'xterm-256color'
        
        # Run mobile app
        app = MobileOffsetScanner()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{MobileColors.BRIGHT['yellow']}👋 Exiting...{MobileColors.RESET}")
    except Exception as e:
        print(f"{MobileColors.BRIGHT['red']}💥 Critical error: {str(e)}{MobileColors.RESET}")

if __name__ == "__main__":
    main()