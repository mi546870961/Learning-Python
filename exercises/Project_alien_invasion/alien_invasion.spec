# -*- mode: python -*-

block_cipher = None


a = Analysis(['alien_invasion.py'],
             pathex=['D:\\github\\Learning-Python\\exercises\\Project_alien_invasion'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [("images\\alien.bmp","D:\\github\\Learning-Python\\exercises\\Project_alien_invasion\\images\\alien.bmp","DATA"),("images\\ship.bmp","D:\\github\\Learning-Python\\exercises\\Project_alien_invasion\\images\\ship.bmp","DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='alien_invasion',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
