"""Application-wide configuration values."""

from __future__ import annotations

from pathlib import Path


APP_NAME = "FACETRACK"
APP_TAGLINE = "A Role-Based Smart Identity and Management System Using Face Recognition"
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FACES_DIR = DATA_DIR / "faces"
DATABASE_PATH = DATA_DIR / "database.db"
LOGS_DIR = DATA_DIR / "logs"
LOG_FILE = LOGS_DIR / "facetrack.log"

FACE_SAMPLE_TARGET = 15
FACE_SAMPLE_MAX = 20
FACE_DISTANCE_THRESHOLD = 0.52
CAMERA_INDEX = 0
FACULTY_DEFAULT_USERNAME = "admin"
FACULTY_DEFAULT_PASSWORD = "admin123"
FACULTY_DEFAULT_NAME = "Administrator"
BATCH_OPTIONS = [f"B{i}" for i in range(1, 97)]

APP_STYLESHEET = """
QWidget {
    background-color: #0b1220;
    color: #d7dfeb;
    font-family: "Segoe UI Variable";
    font-size: 13px;
}
QMainWindow, QDialog {
    background: #0b1220;
}
QFrame#Sidebar {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #111c31, stop:0.55 #152742, stop:1 #1a3256);
    border: 1px solid #24344e;
    border-radius: 24px;
}
QFrame#Card, QFrame#SectionCard, QFrame#MetricCard {
    background: #111827;
    border: 1px solid #223047;
    border-radius: 20px;
}
QFrame#HeroCard {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #16233b, stop:0.55 #1f3558, stop:1 #17456a);
    border: 1px solid #2a4165;
    border-radius: 24px;
}
QFrame#BrandMarkOuter {
    min-width: 76px;
    min-height: 76px;
    max-width: 76px;
    max-height: 76px;
    border-radius: 24px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #4dd7fa, stop:1 #3674ff);
}
QFrame#BrandMarkInner {
    background: #dfe9f7;
    border-radius: 18px;
}
QLabel#BrandInitials {
    color: #1a2f52;
    font-size: 28px;
    font-weight: 800;
    letter-spacing: 2px;
}
QLabel#LogoText {
    color: #f4f7fb;
    font-size: 30px;
    font-weight: 800;
    letter-spacing: 1px;
    background: transparent;
}
QLabel#LogoSubtext {
    color: #aebdd2;
    font-size: 14px;
    font-weight: 600;
    background: transparent;
}
QLabel#SidebarMeta {
    color: #93a3ba;
    font-size: 13px;
    background: transparent;
}
QLabel#Title {
    font-size: 28px;
    font-weight: 750;
    color: #eef4fb;
    background: transparent;
}
QLabel#Subtitle {
    font-size: 13px;
    color: #93a3ba;
    background: transparent;
}
QLabel#HeroTitle {
    font-size: 30px;
    font-weight: 800;
    color: #f8fbff;
    background: transparent;
}
QLabel#HeroSubtitle {
    font-size: 14px;
    color: #c1d0e3;
    background: transparent;
}
QLabel#Eyebrow {
    color: #77d5ff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    background: transparent;
}
QLabel#MetricLabel {
    font-size: 12px;
    font-weight: 600;
    color: #8fa4bf;
    background: transparent;
}
QLabel#MetricValue {
    font-size: 30px;
    font-weight: 800;
    color: #eef4fb;
    background: transparent;
}
QLabel#MetricFootnote {
    font-size: 12px;
    color: #7f91aa;
    background: transparent;
}
QTabWidget::pane {
    border: 1px solid #223047;
    border-radius: 20px;
    top: -1px;
    background: #111827;
}
QTabBar::tab {
    background: transparent;
    color: #95a8c0;
    padding: 12px 18px;
    margin-right: 6px;
    border-radius: 14px;
    font-weight: 600;
}
QTabBar::tab:selected {
    background: #1d365b;
    color: #f4f8ff;
}
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2f7df6, stop:1 #13b1ff);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 18px;
    font-weight: 700;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #266bda, stop:1 #0fa0e7);
}
QPushButton:disabled {
    background: #44556f;
    color: #b7c3d2;
}
QPushButton[variant="secondary"] {
    background: #182638;
    color: #d9e4f2;
    border: 1px solid #29405f;
}
QPushButton[variant="secondary"]:hover {
    background: #1b2e45;
}
QPushButton[variant="danger"] {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #a53a52, stop:1 #d0545e);
}
QPushButton[variant="ghost"] {
    background: #182638;
    color: #eef4fb;
    border: 1px solid #2a3c58;
}
QLineEdit, QComboBox, QSpinBox, QTimeEdit {
    background: #0f1726;
    color: #e4ebf5;
    border: 1px solid #29384e;
    border-radius: 14px;
    padding: 10px 12px;
    selection-background-color: #2f7df6;
}
QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTimeEdit:focus {
    border: 1px solid #3e9dff;
}
QTableWidget, QListWidget {
    background: #0f1726;
    alternate-background-color: #111d30;
    border: 1px solid #223047;
    border-radius: 18px;
    gridline-color: #1d2a3e;
    outline: 0;
}
QHeaderView::section {
    background: #152033;
    color: #99aec7;
    padding: 10px;
    border: none;
    border-bottom: 1px solid #26364f;
    font-weight: 700;
}
QListWidget#NavList {
    background: transparent;
    border: none;
    color: #e3ebf5;
    outline: 0;
}
QListWidget#NavList::item {
    padding: 14px 16px;
    border-radius: 16px;
    margin: 4px 0;
    font-size: 14px;
    font-weight: 600;
}
QListWidget#NavList::item:selected {
    background: #1f3558;
    border: 1px solid #33507a;
}
QProgressBar {
    border: 1px solid #29384e;
    border-radius: 12px;
    background: #0f1726;
    text-align: center;
    min-height: 12px;
    color: #d7dfeb;
}
QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2f7df6, stop:1 #16b7ff);
    border-radius: 10px;
}
QMessageBox {
    background: #111827;
}
QScrollBar:vertical {
    background: transparent;
    width: 12px;
    margin: 4px;
}
QScrollBar::handle:vertical {
    background: #32455f;
    border-radius: 6px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
    border: none;
}
"""
