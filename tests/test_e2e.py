import os, socket, subprocess, sys, time, pytest
from playwright.sync_api import sync_playwright
# SRC = os.path.join(os.path.dirname(__file__), "..", "src")
SRC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "src")
).replace("\\", "/")

@pytest.fixture(scope="module")
def servidor():
    s = socket.socket(); s.bind(("127.0.0.1", 0))
    porta = s.getsockname()[1]; s.close()
    proc = subprocess.Popen([sys.executable, "-c",
        f"import sys; sys.path.insert(0,'{SRC}');"
        f"from app import app; app.run(port={porta})"])
    time.sleep(2); yield f"http://127.0.0.1:{porta}"
    proc.terminate(); proc.wait()

def test_interface(servidor):
    with sync_playwright() as p:
        pag = p.chromium.launch().new_page()
        pag.goto(servidor); pag.click("#calcular")
        pag.wait_for_selector("#resultado")
        assert "1795.86" in pag.inner_text("#resultado")