#!/usr/bin/env python3
import os, re, time, mmap, sys

DUMP_CS = "/storage/emulated/0/Download/dump.cs"
OUTPUT_FILE = "/storage/emulated/0/Download/output/offset.txt"
FILTERED_FILE = "/storage/emulated/0/Download/output/filtered.txt"

class Color:
    # ANSI Color Codes
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    
    # Bright Colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'

class FastScanner:
    def __init__(self):
        self.filter_pat = re.compile(r'//\s*0x[0-9A-Fa-f]+')
        self.offset_pat = re.compile(r'//\s*RVA:\s*(0x[0-9A-Fa-f]+)')
    
    def search(self, keyword):
        print(f"\n{Color.BRIGHT_CYAN}🔍 Searching: {Color.BRIGHT_YELLOW}{keyword}{Color.RESET}")
        print(f"{Color.CYAN}⏳ Please wait...{Color.RESET}")
        
        start = time.time()
        results = []
        found_count = 0
        filtered_count = 0
        
        try:
            with open(DUMP_CS, 'rb') as f:
                file_size = os.path.getsize(DUMP_CS)
                print(f"{Color.BRIGHT_GREEN}📊 File Size: {file_size:,} bytes{Color.RESET}")
                
                with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                    print(f"{Color.BRIGHT_GREEN}🚀 Memory mapping activated...{Color.RESET}")
                    
                    keyword_bytes = keyword.lower().encode('utf-8')
                    pos = 0
                    
                    while True:
                        pos = mm.find(keyword_bytes, pos)
                        if pos == -1:
                            break
                        
                        # Find line start
                        line_start = mm.rfind(b'\n', 0, pos)
                        if line_start == -1:
                            line_start = 0
                        else:
                            line_start += 1
                        
                        # Find line end
                        line_end = mm.find(b'\n', pos)
                        if line_end == -1:
                            line_end = len(mm)
                        
                        # Extract line
                        line_bytes = mm[line_start:line_end]
                        line_text = line_bytes.decode('utf-8', errors='ignore').strip()
                        
                        # Filter out // 0x patterns
                        if self.filter_pat.search(line_text):
                            filtered_count += 1
                            pos = line_end
                            continue
                        
                        # Find RVA offset in next lines
                        rva_start = line_end + 1
                        offset_found = False
                        
                        for _ in range(5):  # Check next 5 lines
                            rva_end = mm.find(b'\n', rva_start)
                            if rva_end == -1:
                                break
                            
                            rva_line = mm[rva_start:rva_end].decode('utf-8', errors='ignore')
                            offset_match = self.offset_pat.search(rva_line)
                            
                            if offset_match:
                                offset = offset_match.group(1)
                                
                                # Generate bool value
                                line_lower = line_text.lower()
                                if any(word in line_lower for word in ['true', 'enable', 'can', 'is', 'has']):
                                    bool_val = "true"
                                elif any(word in line_lower for word in ['false', 'disable', 'cannot']):
                                    bool_val = "false"
                                else:
                                    bool_val = "true"
                                
                                # Generate assembly patch
                                if 'bool' in line_lower:
                                    asm_patch = "MOV W1, #0x1"
                                elif 'int' in line_lower or 'uint' in line_lower:
                                    asm_patch = "MOV W1, #0x64"
                                elif 'float' in line_lower or 'double' in line_lower:
                                    asm_patch = "FMOV S0, #1.0"
                                elif 'string' in line_lower or 'char' in line_lower:
                                    asm_patch = "LDR X1, [X0]"
                                else:
                                    asm_patch = "MOV W1, #0x1"
                                
                                results.append({
                                    'string': line_text[:150],
                                    'offset': offset,
                                    'bool_value': bool_val,
                                    'assembly_patch': asm_patch
                                })
                                
                                found_count += 1
                                offset_found = True
                                
                                # Show progress
                                if found_count % 10 == 0:
                                    elapsed = time.time() - start
                                    speed = found_count / elapsed if elapsed > 0 else 0
                                    print(f"{Color.BRIGHT_GREEN}✓ Found: {found_count} | Speed: {speed:.0f}/sec{Color.RESET}", end='\r')
                                
                                break
                            
                            rva_start = rva_end + 1
                        
                        pos = line_end
            
            elapsed = time.time() - start
            
            if found_count > 0:
                print(f"\n{Color.BRIGHT_GREEN}✅ Search completed!{Color.RESET}")
            
            stats = f"""
{Color.BRIGHT_CYAN}📊 SEARCH STATISTICS:{Color.RESET}
{Color.CYAN}├─ Results Found: {found_count:,}
├─ Lines Filtered: {filtered_count:,}
├─ Time Elapsed: {elapsed:.3f} seconds
└─ Search Speed: {found_count/elapsed:.0f} results/sec{Color.RESET}""" if elapsed > 0 else ""
            
            return True, results, stats
            
        except Exception as e:
            return False, [], f"{Color.RED}❌ Error: {str(e)}{Color.RESET}"
    
    def save_results(self, results):
        try:
            # Create output directory
            os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
            
            # Save main results
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                f.write("╔══════════════════════════════════════════════════════════════╗\n")
                f.write("║               OFFSET SCAN REPORT                           ║\n")
                f.write("╠══════════════════════════════════════════════════════════════╣\n")
                f.write(f"║ Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}{' '*20}║\n")
                f.write(f"║ Total Results: {len(results)}{' '*30}║\n")
                f.write("╠══════════════════════════════════════════════════════════════╣\n")
                f.write("║ Created by: Shrabon~Gomez                                 ║\n")
                f.write("╚══════════════════════════════════════════════════════════════╝\n\n")
                
                for idx, result in enumerate(results, 1):
                    f.write(f"{'='*70}\n")
                    f.write(f"RESULT #{idx}\n")
                    f.write(f"{'-'*70}\n")
                    f.write(f"String: {result['string']}\n")
                    f.write(f"Offset: {result['offset']}\n")
                    f.write(f"Bool Value: {result['bool_value']}\n")
                    f.write(f"Assembly Patch: {result['assembly_patch']}\n")
                    f.write(f"{'-'*70}\n\n")
            
            # Save filtered results (without // 0x patterns)
            filtered_results = [r for r in results if not self.filter_pat.search(r['string'])]
            if filtered_results:
                with open(FILTERED_FILE, 'w', encoding='utf-8') as f:
                    f.write("FILTERED RESULTS (No // 0x patterns)\n")
                    f.write(f"Total: {len(filtered_results)}\n")
                    f.write("="*50 + "\n\n")
                    
                    for result in filtered_results:
                        f.write(f"Offset: {result['offset']}\n")
                        f.write(f"String: {result['string'][:100]}...\n")
                        f.write(f"Patch: {result['assembly_patch']}\n")
                        f.write("-"*50 + "\n")
            
            return True, f"{Color.GREEN}✓ Results saved to:{Color.RESET}\n  {Color.CYAN}{OUTPUT_FILE}{Color.RESET}\n  {Color.CYAN}{FILTERED_FILE}{Color.RESET}"
            
        except Exception as e:
            return False, f"{Color.RED}❌ Save error: {str(e)}{Color.RESET}"

def show_header():
    os.system('clear')
    print(f"{Color.BRIGHT_MAGENTA}{'═'*60}{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}{Color.BOLD}       ╔══════════════════════════════════════╗{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}{Color.BOLD}       ║     Creating BY Shrabon~Gomez        ║{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}{Color.BOLD}       ╚══════════════════════════════════════╝{Color.RESET}")
    print(f"{Color.BRIGHT_YELLOW}{' ' * 10}⚡ LIGHTNING OFFSET SCANNER PRO ⚡{Color.RESET}")
    print(f"{Color.BRIGHT_GREEN}{' ' * 8}Advanced Filter System • Ultra Fast{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}{'═'*60}{Color.RESET}\n")

def show_menu():
    print(f"{Color.BRIGHT_MAGENTA}{'━'*30} MENU {'━'*30}{Color.RESET}")
    print(f"{Color.BRIGHT_GREEN}[1]{Color.RESET} {Color.BOLD}⚡ Lightning Search{Color.RESET}")
    print(f"{Color.BRIGHT_GREEN}[2]{Color.RESET} {Color.BOLD}📄 View Results{Color.RESET}")
    print(f"{Color.BRIGHT_GREEN}[3]{Color.RESET} {Color.BOLD}🔍 View Filtered Results{Color.RESET}")
    print(f"{Color.BRIGHT_GREEN}[4]{Color.RESET} {Color.BOLD}🧹 Clear Output{Color.RESET}")
    print(f"{Color.BRIGHT_GREEN}[5]{Color.RESET} {Color.BOLD}🚪 Exit{Color.RESET}")
    print(f"{Color.BRIGHT_MAGENTA}{'━'*65}{Color.RESET}")

def main():
    # Check if dump.cs exists
    if not os.path.exists(DUMP_CS):
        print(f"{Color.RED}❌ ERROR: dump.cs file not found!{Color.RESET}")
        print(f"{Color.YELLOW}Please place dump.cs at:{Color.RESET}")
        print(f"{Color.CYAN}{DUMP_CS}{Color.RESET}")
        input(f"\n{Color.YELLOW}Press Enter to exit...{Color.RESET}")
        return
    
    # Create output directory
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    scanner = FastScanner()
    
    while True:
        show_header()
        
        # Show file info
        try:
            file_size = os.path.getsize(DUMP_CS)
            size_mb = file_size / (1024 * 1024)
            print(f"{Color.BRIGHT_GREEN}📁 File: {Color.CYAN}{DUMP_CS}{Color.RESET}")
            print(f"{Color.BRIGHT_GREEN}📊 Size: {Color.YELLOW}{size_mb:.2f} MB{Color.RESET} | {Color.BRIGHT_GREEN}Lines: {Color.YELLOW}{file_size // 80:,}{Color.RESET}")
        except:
            pass
        
        print(f"{Color.BRIGHT_CYAN}{'═'*60}{Color.RESET}")
        
        show_menu()
        
        choice = input(f"\n{Color.BRIGHT_YELLOW}🎯 Select option [1-5]: {Color.RESET}").strip()
        
        if choice == '1':
            show_header()
            print(f"{Color.BRIGHT_CYAN}{'⚡ LIGHTNING SEARCH ⚡':^60}{Color.RESET}\n")
            
            keyword = input(f"{Color.BRIGHT_YELLOW}🔍 Enter keyword: {Color.RESET}").strip()
            
            if not keyword:
                print(f"{Color.RED}❌ Keyword cannot be empty!{Color.RESET}")
                time.sleep(1)
                continue
            
            print(f"\n{Color.CYAN}{'═'*60}{Color.RESET}")
            
            # Perform search
            success, results, stats = scanner.search(keyword)
            
            print(f"\n{Color.CYAN}{'═'*60}{Color.RESET}")
            
            if success:
                if stats:
                    print(stats)
                
                if results:
                    # Save results
                    save_success, save_msg = scanner.save_results(results)
                    print(f"\n{save_msg}")
                    
                    # Show preview
                    print(f"\n{Color.BRIGHT_CYAN}{'📋 RESULTS PREVIEW 📋':^60}{Color.RESET}")
                    
                    for i, result in enumerate(results[:3]):
                        print(f"\n{Color.BRIGHT_YELLOW}[{i+1}]{Color.RESET}")
                        print(f"{Color.CYAN}String:{Color.RESET} {result['string'][:80]}...")
                        print(f"{Color.GREEN}Offset:{Color.RESET} {result['offset']}")
                        print(f"{Color.MAGENTA}Bool Value:{Color.RESET} {result['bool_value']}")
                        print(f"{Color.YELLOW}Assembly Patch:{Color.RESET} {result['assembly_patch']}")
                    
                    if len(results) > 3:
                        print(f"\n{Color.BRIGHT_BLUE}... and {len(results)-3} more results{Color.RESET}")
                else:
                    print(f"{Color.YELLOW}⚠ No results found for '{keyword}'{Color.RESET}")
            else:
                print(f"{Color.RED}❌ Search failed!{Color.RESET}")
            
            input(f"\n{Color.CYAN}Press Enter to continue...{Color.RESET}")
            
        elif choice == '2':
            show_header()
            print(f"{Color.BRIGHT_CYAN}{'📄 VIEW RESULTS 📄':^60}{Color.RESET}\n")
            
            if not os.path.exists(OUTPUT_FILE):
                print(f"{Color.RED}❌ No results file found!{Color.RESET}")
                print(f"{Color.YELLOW}Run a search first.{Color.RESET}")
                time.sleep(2)
                continue
            
            try:
                with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                lines = content.split('\n')
                
                # Show header and first 15 results
                for i, line in enumerate(lines[:200]):
                    if i < 10:  # Show header
                        print(f"{Color.BRIGHT_CYAN}{line}{Color.RESET}")
                    elif 'String:' in line:
                        print(f"\n{Color.CYAN}{line}{Color.RESET}")
                    elif 'Offset:' in line:
                        print(f"{Color.GREEN}{line}{Color.RESET}")
                    elif 'Bool Value:' in line:
                        print(f"{Color.MAGENTA}{line}{Color.RESET}")
                    elif 'Assembly Patch:' in line:
                        print(f"{Color.YELLOW}{line}{Color.RESET}")
                    elif line.startswith('='):
                        print(f"{Color.BRIGHT_BLUE}{line}{Color.RESET}")
                    elif line.startswith('RESULT'):
                        print(f"{Color.BRIGHT_YELLOW}{line}{Color.RESET}")
                
                if len(lines) > 200:
                    print(f"\n{Color.BRIGHT_BLUE}... {len(lines)-200} more lines{Color.RESET}")
                    
            except Exception as e:
                print(f"{Color.RED}❌ Error reading file: {str(e)}{Color.RESET}")
            
            input(f"\n{Color.CYAN}Press Enter to continue...{Color.RESET}")
            
        elif choice == '3':
            show_header()
            print(f"{Color.BRIGHT_CYAN}{'🔍 FILTERED RESULTS 🔍':^60}{Color.RESET}\n")
            
            if not os.path.exists(FILTERED_FILE):
                print(f"{Color.YELLOW}⚠ No filtered results file found{Color.RESET}")
                print(f"{Color.CYAN}Run a search first to generate filtered results.{Color.RESET}")
                time.sleep(2)
                continue
            
            try:
                with open(FILTERED_FILE, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                print(f"{Color.GREEN}📁 File: {FILTERED_FILE}{Color.RESET}")
                print(f"{Color.CYAN}══════════════════════════════════════════════════════════{Color.RESET}\n")
                print(content)
                
            except Exception as e:
                print(f"{Color.RED}❌ Error: {str(e)}{Color.RESET}")
            
            input(f"\n{Color.CYAN}Press Enter to continue...{Color.RESET}")
            
        elif choice == '4':
            show_header()
            print(f"{Color.BRIGHT_CYAN}{'🧹 CLEAR OUTPUT 🧹':^60}{Color.RESET}\n")
            
            files_to_clear = [OUTPUT_FILE, FILTERED_FILE]
            cleared = 0
            
            for file_path in files_to_clear:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"{Color.GREEN}✓ {os.path.basename(file_path)} cleared{Color.RESET}")
                    cleared += 1
            
            if cleared == 0:
                print(f"{Color.YELLOW}⚠ No files to clear{Color.RESET}")
            else:
                print(f"\n{Color.BRIGHT_GREEN}✅ Output cleared successfully!{Color.RESET}")
            
            time.sleep(1.5)
            
        elif choice == '5':
            show_header()
            print(f"{Color.BRIGHT_CYAN}{'🚪 EXITING 🚪':^60}{Color.RESET}\n")
            print(f"{Color.BRIGHT_GREEN}✨ Thank you for using Offset Scanner!{Color.RESET}")
            print(f"{Color.BRIGHT_YELLOW}👨‍💻 Created by Shrabon~Gomez{Color.RESET}")
            print(f"{Color.BRIGHT_CYAN}⚡ Lightning Speed Technology{Color.RESET}\n")
            break
            
        else:
            print(f"{Color.RED}❌ Invalid option! Please choose 1-5{Color.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.YELLOW}👋 Exiting...{Color.RESET}")
    except Exception as e:
        print(f"{Color.RED}💥 Critical error: {str(e)}{Color.RESET}")