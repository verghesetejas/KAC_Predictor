# -*- mode: python -*-

block_cipher = None


a = Analysis(['__init__.py'],
             pathex=['C:\\Python36\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'D:\\MajorProject\\Source Code\\Program'],
             binaries=[],
             datas=[('KAC_MinModel.h5', '.'), ('KAC_MaxModel.h5', '.'), ('KAC_ModModel.h5', '.'), ('leX_commodity.npy', '.'), ('leX_district.npy', '.'), ('leX_market.npy', '.'), ('leX_state.npy', '.'), ('sc_X.pkl', '.'), ('sc_y_min.pkl', '.'), ('sc_y_max.pkl', '.'), ('sc_y_mod.pkl', '.'), ('login.db', '.'), ('combo_loader.db', '.'), ('AboutDeveloper.pdf', '.'), ('AboutProject.pdf', '.'), ('login_window.py', '.'), ('selector_window.py', '.'), ('main_window.py', '.'), ('signup_window.py', '.'), ('delete_window.py', '.'), ('update_window.py', '.'), ('about_window.py', '.'), ('kac_predictor.py', '.'), ('about.py', '.')],
             hiddenimports=['h5py', 'h5py.defs', 'h5py.utils', 'h5py.h5ac', 'h5py._proxy'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='KAC Predictor',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='D:\\MajorProject\\Source Code\\Program\\Images\\major_project-logo.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='KAC Predictor')
