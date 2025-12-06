#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════╗
║     Creating BY Shrabon~Gomez        ║
╚══════════════════════════════════════╝
        ⚡ LIGHTNING OFFSET SCANNER ⚡
         Advanced Filter System • Ultra Fast
"""

import os
import re
import time
import mmap
import stat
import subprocess
import sys
from datetime import datetime

# ==================== CONFIGURATION ====================
PASSWORD = "SHRABON"
FACEBOOK_URL = "https://www.facebook.com/share/1B4TRBkyN3/"
DUMP_CS_PATH = "/storage/emulated/0/Download/dump.cs"
OUTPUT_DIR = "/storage/emulated/0/Download/output"
OUTPUT_FILE = f"{OUTPUT_DIR}/offset.txt"
ANALYZE_FILE = f"{OUTPUT_DIR}/analyse.txt"

# ==================== AUTO PERMISSION FIXER ====================
class PermissionFixer:
    @staticmethod
    def setup_environment():
        """Setup all required permissions"""
        print("\n🔧 Setting up environment...")
        
        # 1. Fix storage permissions
        PermissionFixer.fix_storage()
        
        # 2. Create directories
        PermissionFixer.create_dirs()
        
        # 3. Fix file permissions
        PermissionFixer.fix_file_permissions()
        
        # 4. Setup Termux storage
        PermissionFixer.setup_termux_storage()
        
        print("✅ Environment setup complete!\n")
    
    @staticmethod
    def fix_storage():
        """Fix storage permissions"""
        try:
            os.system("termux-setup-storage")
            print("✅ Storage permission granted")
        except:
            print("⚠ Could not setup storage automatically")
    
    @staticmethod
    def create_dirs():
        """Create necessary directories"""
        dirs = [OUTPUT_DIR, "/storage/emulated/0/Download/output"]
        for dir_path in dirs:
            try:
                os.makedirs(dir_path, exist_ok=True)
                os.chmod(dir_path, 0o755)
                print(f"✅ Created directory: {dir_path}")
            except:
                pass
    
    @staticmethod
    def fix_file_permissions():
        """Fix dump.cs file permissions"""
        if os.path.exists(DUMP_CS_PATH):
            try:
                os.chmod(DUMP_CS_PATH, 0o644)
                print(f"✅ Fixed permissions for: {DUMP_CS_PATH}")
            except:
                print(f"⚠ Could not fix permissions for: {DUMP_CS_PATH}")
        else:
            print(f"❌ File not found: {DUMP_CS_PATH}")
            print("📁 Searching for dump.cs...")
            PermissionFixer.find_dump_file()
    
    @staticmethod
    def find_dump_file():
        """Find dump.cs file in common locations"""
        locations = [
            "/storage/emulated/0/Download/dump.cs",
            "/sdcard/Download/dump.cs",
            "/storage/emulated/0/dump.cs",
            "/sdcard/dump.cs",
            "/storage/self/primary/Download/dump.cs"
        ]
        
        for loc in locations:
            if os.path.exists(loc):
                print(f"✅ Found dump.cs at: {loc}")
                global DUMP_CS_PATH
                DUMP_CS_PATH = loc
                return loc
        
        print("❌ Could not find dump.cs file")
        return None
    
    @staticmethod
    def setup_termux_storage():
        """Ensure Termux storage is properly setup"""
        try:
            # Create termux files if missing
            termux_dir = "/data/data/com.termux/files/home/storage"
            if not os.path.exists(termux_dir):
                os.makedirs(termux_dir, exist_ok=True)
            
            # Create symlink if needed
            download_link = f"{termux_dir}/downloads"
            if not os.path.exists(download_link):
                os.symlink("/storage/emulated/0/Download", download_link)
                print("✅ Created Termux storage symlink")
        except:
            pass

# ==================== BEAUTIFUL UI SYSTEM ====================
class Colors:
    """Enhanced color system for mobile"""
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Gradient colors
    GRADIENT = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    
    @staticmethod
    def gradient_text(text):
        """Create gradient text effect"""
        result = ""
        for i, char in enumerate(text):
            color = Colors.GRADIENT[i % len(Colors.GRADIENT)]
            result += f"{color}{char}"
        return result + Colors.RESET

class UI:
    """Professional mobile UI"""
    
    @staticmethod
    def clear_screen():
        os.system('clear')
    
    @staticmethod
    def show_banner():
        UI.clear_screen()
        print(Colors.gradient_text("╔══════════════════════════════════════╗"))
        print(Colors.gradient_text("║     Creating BY Shrabon~Gomez        ║"))
        print(Colors.gradient_text("╚══════════════════════════════════════╝"))
        print(f"\n{Colors.CYAN}{Colors.BOLD}        ⚡ LIGHTNING OFFSET SCANNER ⚡{Colors.RESET}")
        print(f"{Colors.YELLOW}        Advanced Filter System • Ultra Fast{Colors.RESET}")
        print(f"{Colors.BLUE}{'═'*60}{Colors.RESET}")
    
    @staticmethod
    def show_menu():
        menu = f"""
{Colors.MAGENTA}{Colors.BOLD}{'━'*30} MENU {'━'*30}{Colors.RESET}

{Colors.GREEN}[1]{Colors.RESET} {Colors.BOLD}⚡ Lightning Search{Colors.RESET}
{Colors.GREEN}[2]{Colors.RESET} {Colors.BOLD}📄 View Results{Colors.RESET}
{Colors.GREEN}[3]{Colors.RESET} {Colors.BOLD}🔍 View Filtered Results{Colors.RESET}
{Colors.GREEN}[4]{Colors.RESET} {Colors.BOLD}🧹 Clear Output{Colors.RESET}
{Colors.GREEN}[5]{Colors.RESET} {Colors.BOLD}🚪 Exit{Colors.RESET}

{Colors.MAGENTA}{Colors.BOLD}{'━'*65}{Colors.RESET}
"""
        print(menu)
    
    @staticmethod
    def progress_bar(current, total, prefix="", length=40):
        percent = current / total
        filled = int(length * percent)
        bar = '█' * filled + '░' * (length - filled)
        
        if percent < 0.3:
            color = Colors.RED
        elif percent < 0.7:
            color = Colors.YELLOW
        else:
            color = Colors.GREEN
        
        print(f'\r{prefix} {color}{bar}{Colors.RESET} {percent:.1%}', end='\r')
        if current == total: 
            print()

# ==================== SECURITY & FACEBOOK ====================
class Security:
    @staticmethod
    def check_password():
        UI.clear_screen()
        print(Colors.gradient_text("╔══════════════════════════════════════╗"))
        print(Colors.gradient_text("║        ACCESS VERIFICATION          ║"))
        print(Colors.gradient_text("╚══════════════════════════════════════╝"))
        print(f"\n{Colors.YELLOW}🔐 Enter Password to continue:{Colors.RESET}")
        
        attempts = 3
        while attempts > 0:
            print(f"{Colors.CYAN}Attempts left: {attempts}{Colors.RESET}")
            password = input(f"{Colors.GREEN}Password: {Colors.RESET}")
            
            if password == PASSWORD:
                print(f"\n{Colors.GREEN}✅ Access Granted!{Colors.RESET}")
                time.sleep(1)
                Security.open_facebook()
                return True
            else:
                attempts -= 1
                print(f"{Colors.RED}❌ Wrong password!{Colors.RESET}")
                time.sleep(1)
        
        print(f"\n{Colors.RED}⛔ Access Denied!{Colors.RESET}")
        return False
    
    @staticmethod
    def open_facebook():
        print(f"\n{Colors.BLUE}🌐 Opening Facebook...{Colors.RESET}")
        try:
            subprocess.run(["termux-open-url", FACEBOOK_URL], 
                         capture_output=True, timeout=5)
            print(f"{Colors.GREEN}✅ Facebook opened!{Colors.RESET}")
        except:
            print(f"{Colors.YELLOW}⚠ Please visit manually: {FACEBOOK_URL}{Colors.RESET}")
        time.sleep(2)

# ==================== LIGHTNING FAST SCANNER ====================
class LightningScanner:
    def __init__(self):
        self.file_size = 0
        self.total_lines = 0
        
    def get_file_info(self):
        """Get dump.cs information"""
        try:
            if not os.path.exists(DUMP_CS_PATH):
                return False, f"{Colors.RED}❌ dump.cs not found!{Colors.RESET}"
            
            self.file_size = os.path.getsize(DUMP_CS_PATH)
            
            # Fast line counting
            lines = 0
            with open(DUMP_CS_PATH, 'rb') as f:
                while chunk := f.read(8192):
                    lines += chunk.count(b'\n')
            self.total_lines = lines
            
            size_mb = self.file_size / (1024 * 1024)
            info = f"""
{Colors.GREEN}📁 File: {DUMP_CS_PATH}{Colors.RESET}
{Colors.BLUE}📊 Size: {size_mb:.2f} MB | Lines: {self.total_lines:,}{Colors.RESET}
"""
            return True, info
        except Exception as e:
            return False, f"{Colors.RED}❌ Error: {str(e)}{Colors.RESET}"
    
    def search(self, keyword):
        """Lightning fast search using memory mapping"""
        print(f"\n{Colors.CYAN}🔍 Searching: {Colors.YELLOW}{keyword}{Colors.RESET}")
        print(f"{Colors.BLUE}⚡ Initializing lightning scanner...{Colors.RESET}")
        
        start_time = time.time()
        results = []
        
        try:
            # Test file access
            if not os.access(DUMP_CS_PATH, os.R_OK):
                print(f"{Colors.RED}❌ Permission denied! Fixing...{Colors.RESET}")
                PermissionFixer.fix_file_permissions()
                if not os.access(DUMP_CS_PATH, os.R_OK):
                    return False, [], "Cannot access dump.cs file"
            
            keyword_bytes = keyword.lower().encode()
            found = 0
            
            with open(DUMP_CS_PATH, 'rb') as f:
                with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                    print(f"{Colors.GREEN}🚀 Memory mapping activated{Colors.RESET}")
                    
                    pos = 0
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
                        
                        # Skip filtered patterns
                        if '// 0x' in line_text:
                            pos = line_end
                            continue
                        
                        # Find RVA in next lines
                        rva_pos = line_end + 1
                        for _ in range(5):
                            rva_end = mm.find(b'\n', rva_pos)
                            if rva_end == -1:
                                break
                            
                            rva_line = mm[rva_pos:rva_end].decode('utf-8', errors='ignore')
                            offset_match = re.search(r'//\s*RVA:\s*(0x[0-9A-Fa-f]+)', rva_line)
                            
                            if offset_match:
                                offset = offset_match.group(1)
                                
                                # Generate values
                                float_val = self._generate_float(line_text)
                                asm_patch = self._generate_asm(offset, line_text)
                                
                                results.append({
                                    'string': line_text[:150],
                                    'offset': offset,
                                    'float_value': float_val,
                                    'assembly_patch': asm_patch
                                })
                                
                                found += 1
                                
                                # Update progress
                                if found % 10 == 0:
                                    elapsed = time.time() - start_time
                                    speed = found / elapsed if elapsed > 0 else 0
                                    print(f"{Colors.GREEN}✓ Found: {found} ({speed:.0f}/sec){Colors.RESET}", end='\r')
                                
                                break
                            
                            rva_pos = rva_end + 1
                        
                        pos = line_end
            
            if found > 0:
                print(f"{Colors.GREEN}✓ Found: {found}{Colors.RESET}")
            
            elapsed = time.time() - start_time
            
            stats = f"""
{Colors.CYAN}📊 Statistics:{Colors.RESET}
{Colors.BLUE}├─ Results: {found:,}
├─ Time: {elapsed:.3f}s
└─ Speed: {found/elapsed:.0f}/sec{Colors.RESET}""" if elapsed > 0 else ""
            
            return True, results, stats
            
        except Exception as e:
            return False, [], f"{Colors.RED}❌ Search error: {str(e)}{Colors.RESET}"
    
    def _generate_float(self, string_line):
        """Generate float/bool value"""
        string_lower = string_line.lower()
        
        if any(word in string_lower for word in ['true', 'enable', 'can', 'active']):
            return "true"
        elif any(word in string_lower for word in ['false', 'disable', 'cannot']):
            return "false"
        elif 'float' in string_lower:
            return "1.0"
        elif 'int' in string_lower:
            return "1"
        else:
            return "true"
    
    def _generate_asm(self, offset, string_line):
        """Generate assembly patch"""
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
            return "MOV W1, #0x1"
    
    def save_results(self, results):
        """Save results with beautiful formatting"""
        try:
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                f.write("╔══════════════════════════════════════════════════════════════╗\n")
                f.write("║               ⚡ OFFSET SCAN REPORT ⚡                      ║\n")
                f.write("╠══════════════════════════════════════════════════════════════╣\n")
                f.write(f"║ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"║ Results: {len(results)}\n")
                f.write("╠══════════════════════════════════════════════════════════════╣\n")
                f.write("║ Created by: Shrabon~Gomez\n")
                f.write("╚══════════════════════════════════════════════════════════════╝\n\n")
                
                for result in results:
                    f.write(f"{'.'*70}\n")
                    f.write(f"String: {result['string']}\n")
                    f.write(f"Offset: {result['offset']}\n")
                    f.write(f"Float value: {result['float_value']}\n")
                    f.write(f"Assembly patch: {result['assembly_patch']}\n")
                    f.write(f"{'.'*70}\n\n")
            
            # Save analyze file
            with open(ANALYZE_FILE, 'w') as f:
                for result in results:
                    f.write(f"{result['offset']} | {result['string'][:80]}...\n")
                    f.write(f"  Value: {result['float_value']} | Patch: {result['assembly_patch']}\n")
                    f.write("-"*50 + "\n")
            
            return True, f"{Colors.GREEN}✅ Results saved to:{Colors.RESET}\n{Colors.CYAN}{OUTPUT_FILE}{Colors.RESET}"
            
        except Exception as e:
            return False, f"{Colors.RED}❌ Save error: {str(e)}{Colors.RESET}"

# ==================== MAIN APPLICATION ====================
class OffsetScanner:
    def __init__(self):
        self.scanner = LightningScanner()
        self.running = True
    
    def run(self):
        """Main application"""
        # Setup environment first
        PermissionFixer.setup_environment()
        
        # Password check
        if not Security.check_password():
            return
        
        # Main loop
        while self.running:
            self.show_main_screen()
            self.handle_choice()
    
    def show_main_screen(self):
        """Show main screen with file info"""
        UI.show_banner()
        
        success, info = self.scanner.get_file_info()
        if success:
            print(info)
        else:
            print(info)
            print(f"\n{Colors.YELLOW}Please ensure dump.cs exists in Download folder{Colors.RESET}")
        
        print(f"{Colors.BLUE}{'═'*60}{Colors.RESET}")
        UI.show_menu()
    
    def handle_choice(self):
        """Handle menu choice"""
        try:
            choice = input(f"\n{Colors.YELLOW}🎯 Select option [1-5]: {Colors.RESET}").strip()
            
            if choice == '1':
                self.search_function()
            elif choice == '2':
                self.view_results()
            elif choice == '3':
                self.view_filtered()
            elif choice == '4':
                self.clear_output()
            elif choice == '5':
                self.exit_app()
            else:
                print(f"{Colors.RED}❌ Invalid option!{Colors.RESET}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.exit_app()
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
            time.sleep(1)
    
    def search_function(self):
        """Search function"""
        UI.show_banner()
        print(f"{Colors.CYAN}{'⚡ LIGHTNING SEARCH ⚡':^60}{Colors.RESET}\n")
        
        keyword = input(f"{Colors.YELLOW}🔍 Enter keyword: {Colors.RESET}").strip()
        
        if not keyword:
            print(f"{Colors.RED}❌ Keyword required!{Colors.RESET}")
            time.sleep(1)
            return
        
        print(f"\n{Colors.BLUE}{'═'*60}{Colors.RESET}")
        
        success, results, stats = self.scanner.search(keyword)
        
        print(f"\n{Colors.BLUE}{'═'*60}{Colors.RESET}")
        
        if success:
            print(stats)
            
            if results:
                save_ok, save_msg = self.scanner.save_results(results)
                print(f"\n{save_msg}")
                
                # Show preview
                print(f"\n{Colors.CYAN}{'📋 RESULTS PREVIEW 📋':^60}{Colors.RESET}")
                
                for i, result in enumerate(results[:3]):
                    print(f"\n{Colors.YELLOW}[{i+1}]{Colors.RESET}")
                    print(f"{Colors.CYAN}String:{Colors.RESET} {result['string'][:80]}...")
                    print(f"{Colors.GREEN}Offset:{Colors.RESET} {result['offset']}")
                    print(f"{Colors.MAGENTA}Float Value:{Colors.RESET} {result['float_value']}")
                    print(f"{Colors.YELLOW}Assembly Patch:{Colors.RESET} {result['assembly_patch']}")
                
                if len(results) > 3:
                    print(f"\n{Colors.BLUE}... and {len(results)-3} more results{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}⚠ No results found{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Search failed!{Colors.RESET}")
        
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
    
    def view_results(self):
        """View saved results"""
        UI.show_banner()
        print(f"{Colors.CYAN}{'📄 VIEW RESULTS 📄':^60}{Colors.RESET}\n")
        
        if not os.path.exists(OUTPUT_FILE):
            print(f"{Colors.RED}❌ No results file found!{Colors.RESET}")
            time.sleep(2)
            return
        
        try:
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # Show first 20 lines
            for i, line in enumerate(lines[:20]):
                if i < 8:
                    print(f"{Colors.CYAN}{line}{Colors.RESET}")
                elif 'String:' in line:
                    print(f"\n{Colors.CYAN}{line}{Colors.RESET}")
                elif 'Offset:' in line:
                    print(f"{Colors.GREEN}{line}{Colors.RESET}")
                elif 'Float value:' in line:
                    print(f"{Colors.MAGENTA}{line}{Colors.RESET}")
                elif 'Assembly patch:' in line:
                    print(f"{Colors.YELLOW}{line}{Colors.RESET}")
                elif line.startswith('.'):
                    print(f"{Colors.BLUE}{line}{Colors.RESET}")
            
            if len(lines) > 20:
                print(f"\n{Colors.BLUE}... {len(lines)-20} more lines{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
        
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
    
    def view_filtered(self):
        """View filtered results"""
        UI.show_banner()
        print(f"{Colors.CYAN}{'🔍 FILTERED RESULTS 🔍':^60}{Colors.RESET}\n")
        
        if not os.path.exists(ANALYZE_FILE):
            print(f"{Colors.YELLOW}⚠ No analyze file found{Colors.RESET}")
            time.sleep(1)
            return
        
        try:
            with open(ANALYZE_FILE, 'r') as f:
                lines = f.readlines()
            
            for line in lines[:20]:
                if '0x' in line and '|' in line:
                    print(f"{Colors.GREEN}{line.strip()}{Colors.RESET}")
                elif 'Value:' in line:
                    print(f"{Colors.MAGENTA}{line.strip()}{Colors.RESET}")
                elif line.strip():
                    print(f"{Colors.CYAN}{line.strip()}{Colors.RESET}")
            
            if len(lines) > 20:
                print(f"\n{Colors.BLUE}... {len(lines)-20} lines{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
        
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
    
    def clear_output(self):
        """Clear output files"""
        UI.show_banner()
        print(f"{Colors.CYAN}{'🧹 CLEAR OUTPUT 🧹':^60}{Colors.RESET}\n")
        
        files = [OUTPUT_FILE, ANALYZE_FILE]
        cleared = 0
        
        for file_path in files:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"{Colors.GREEN}✓ {os.path.basename(file_path)} cleared{Colors.RESET}")
                cleared += 1
        
        if cleared == 0:
            print(f"{Colors.YELLOW}⚠ No files to clear{Colors.RESET}")
        else:
            print(f"\n{Colors.GREEN}✅ Output cleared!{Colors.RESET}")
        
        time.sleep(1.5)
    
    def exit_app(self):
        """Exit application"""
        UI.show_banner()
        print(f"{Colors.CYAN}{'🚪 EXITING 🚪':^60}{Colors.RESET}\n")
        print(f"{Colors.GREEN}✨ Thank you for using Offset Scanner!{Colors.RESET}")
        print(f"{Colors.YELLOW}👨‍💻 Created by Shrabon~Gomez{Colors.RESET}")
        print(f"{Colors.BLUE}🔐 Password: SHRABON{Colors.RESET}\n")
        self.running = False
        time.sleep(2)

# ==================== MAIN EXECUTION ====================
def main():
    """Main entry point"""
    try:
        # Run scanner
        scanner = OffsetScanner()
        scanner.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Exiting...{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}💥 Critical error: {str(e)}{Colors.RESET}")

if __name__ == "__main__":
    main()