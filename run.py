"""Start DATA Analysis: python run.py  (opens the browser; add --no-browser for servers)."""
from __future__ import annotations

import argparse
import multiprocessing as mp
import threading
import webbrowser


def main() -> None:
    from dataanalysis.config import HOST, PORT

    p = argparse.ArgumentParser(description="DATA Analysis")
    p.add_argument("--host", default=None)
    p.add_argument("--port", type=int, default=PORT)
    p.add_argument("--no-browser", action="store_true")
    p.add_argument("--window", action="store_true", help="Open in a native window (needs: pip install pywebview)")
    p.add_argument("--allow-open", action="store_true", help="Allow a non-local address without logins (not recommended)")
    a = p.parse_args()
    import sys
    if getattr(sys, "frozen", False) and not a.no_browser:
        a.window = True

    from dataanalysis.config import AUTH_ENABLED
    from dataanalysis import mobile
    phone = mobile.enabled()
    if a.host is None:
        a.host = "0.0.0.0" if phone and HOST in ("127.0.0.1", "localhost") else HOST
    import os as _os
    _os.environ["DA_BOUND_HOST"], _os.environ["DA_BOUND_PORT"] = a.host, str(a.port)
    if a.host not in ("127.0.0.1", "localhost", "::1") and not AUTH_ENABLED and not a.allow_open and not phone:
        raise SystemExit(
            "\n  Təhlükəsizlik: şəbəkəyə açıq ünvanda giriş olmadan işə salmaq olmaz.\n"
            "  DA_AUTH=1 təyin edin və ya --host 127.0.0.1 istifadə edin.\n"
        )

    from dataanalysis.web import create_app
    import uvicorn

    app = create_app()
    url = f"http://127.0.0.1:{a.port}"
    if not a.no_browser:
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    print(f"\n  DATA Analysis: {url}\n")
    uvicorn.run(app, host=a.host, port=a.port, log_level="info")


if __name__ == "__main__":
    mp.freeze_support()
    main()
