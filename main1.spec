# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[
        'C:\\Users\\lplpl\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages',
        'C:\\Users\\lplpl\\AppData\\Local\\pypoetry\\Cache\\virtualenvs\\web-drive-SSEfnMEl-py3.11\\Lib\\site-packages'
    ],
    binaries=[],
    datas=[("C:\\Users\\lplpl\\Desktop\\test_debug\\web_drive\\icon.png",'.'),
        ("C:\\Users\\lplpl\\Desktop\\test_debug\\web_drive\\rclone-v1.68.2-windows-amd64\\rclone.exe",'.\\rclone-v1.68.2-windows-amd64'),
        ("C:\\Users\\lplpl\\Desktop\\test_debug\\web_drive\\rclone-v1.68.2-windows-amd64\\rclone.conf",'.\\rclone-v1.68.2-windows-amd64')
        ],
    hiddenimports=[
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)

