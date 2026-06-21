import os, sys, time, threading
sys.path.insert(0, os.path.dirname(__file__))
os.environ['DISPLAY'] = ''

from playwright.sync_api import sync_playwright

ROUTES = {
    'dashboard': '/',
    'check': '/check',
    'settings': '/settings',
    'license': '/license',
    'results': '/results',
    'vault': '/vault',
    'hub': '/hub',
    'read': '/read?email=user@example.com&password=mypassword',
    'intel': '/intel?email=user@example.com&password=mypassword',
    'dob': '/dob?email=user@example.com&password=mypassword',
}

OUT = '/tmp/Tchekly-Download/docs/screenshots'

def take_screenshots():
    print('[+] Starting Flask server...')
    from tchekly.web.app import run_app
    t = threading.Thread(target=run_app, daemon=True)
    t.start()
    time.sleep(5)

    print('[+] Launching browser...')
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1440, 'height': 900},
            device_scale_factor=2,
        )
        page = context.new_page()

        os.makedirs(OUT, exist_ok=True)

        for name, path in ROUTES.items():
            url = f'http://localhost:5000{path}'
            print(f'  → {name} ({url})')
            try:
                page.goto(url, wait_until='networkidle', timeout=15000)
                time.sleep(2)
                # Handle any modals/dialogs
                try:
                    page.wait_for_selector('.form-section', timeout=5000)
                except:
                    pass
                time.sleep(1)
                page.screenshot(path=os.path.join(OUT, f'{name}.png'), full_page=True)
                print(f'    ✓ {name}.png')
            except Exception as e:
                print(f'    ✗ {name}: {e}')

        browser.close()

    print(f'[+] Done! {len(ROUTES)} screenshots saved to {OUT}')

if __name__ == '__main__':
    take_screenshots()
