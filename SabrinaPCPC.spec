# -*- mode: python ; coding: utf-8 -*-
# SabrinaPCPC - PyInstaller spec file
# Uso: pyinstaller SabrinaPCPC.spec

import sys
from pathlib import Path

block_cipher = None

a = Analysis(
    ['SabrinaPCPC.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PIL',
        'PIL.Image',
        'PIL.ImageFile',
        'PIL.JpegImagePlugin',
        'PIL.PngImagePlugin',
        'PIL.TiffImagePlugin',
        'PIL.BmpImagePlugin',
        'PIL.GifImagePlugin',
        # PyAV nascosto (opzionale)
        'av',
        'av.container',
        'av.stream',
        'av.video',
        'av.audio',
        # OpenCV (fallback)
        'cv2',
        # Standard library
        'hashlib',
        'threading',
        'csv',
        'pathlib',
        'shutil',
        'datetime',
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.scrolledtext',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'scipy',
        'pandas',
        'jupyter',
        'IPython',
        'setuptools',
        'pkg_resources',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SabrinaPCPC',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
)
