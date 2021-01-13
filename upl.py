import os
try:
  import magic
  import requests
  pass
except:
  os.system('pip install python-magic requests')
  pass

def upload_to_server(file, server):
  mime = magic.Magic(mime=True)
  sudop = mime.from_file(file)
  url = server+'/upload.php'
  print(sudop)
  print(url)
  files = {'file': (file, open(file, 'rb'), str(sudop))}
  r = requests.post(url, files=files)
  print(r.text)
  return (r.text)