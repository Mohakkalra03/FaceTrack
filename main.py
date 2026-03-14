"""FACETRACK application entrypoint."""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from database.db import init_database
from gui.login_window import LoginWindow
from utils.config import APP_NAME, APP_STYLESHEET


def main() -> int:
    """Bootstrap the database and launch the desktop UI."""
    init_database()

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setStyleSheet(APP_STYLESHEET)
    app.setQuitOnLastWindowClosed(False)

    window = LoginWindow()
    window.showMaximized()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
