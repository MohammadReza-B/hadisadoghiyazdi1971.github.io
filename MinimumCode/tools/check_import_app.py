# tools/check_import_app.py
try:
    import app
    print('Imported app module successfully')
except Exception as e:
    import traceback
    traceback.print_exc()
    print('ERROR:', e)
