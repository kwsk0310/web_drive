# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\lplpl\\Desktop\\test_debug\\web_drive\\main.py'],
    pathex=[],
    binaries=[],
    datas=[("C:\\Users\\lplpl\\Desktop\\test_debug\\web_drive\\icon.png",'.'),
        ("C:\\Users\\lplpl\\Desktop\\test_debug\\web_drive\\rclone-v1.68.2-windows-amd64\\rclone.exe",'.\\rclone-v1.68.2-windows-amd64'),
        ("C:\\Users\\lplpl\\Desktop\\test_debug\\web_drive\\rclone-v1.68.2-windows-amd64\\rclone.conf",'.\\rclone-v1.68.2-windows-amd64')
        ],
    hiddenimports=[],
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
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
