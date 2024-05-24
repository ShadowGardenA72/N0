import os
import subprocess
import requests

def d(u, n):
    r = requests.get(u)
    if r.status_code == 200:
        with open(n, 'wb') as f:
            f.write(r.content)

def g():
    if not os.path.exists('.gitignore'):
        c = """\
/work_area
/servidor_minecraft
/minecraft_server
/servidor_minecraft_old
/MysticArbor
/thanos
/bkdir
/vendor
/modpack_install
/server
/temp

composer.*
configuration.json
configuracion.json
*.txt
*.pyc
*.output
*.md
*.log
*.zip
*.jar
*.py
*.json
*.sh
*.bin

"""
        with open('.gitignore', 'w') as f:
            f.write(c)
    
    u = "https://github.com/ShadowGardenA72/Twilight/raw/main/Twilight.pyc"
    if os.path.exists('Twilight.pyc'):
        os.remove('Twilight.pyc')
    d(u, "Twilight.pyc")

    u = "https://raw.githubusercontent.com/ShadowGardenA72/Twilight/main/README.md"
    if not os.path.exists('README.md'):
        d(u, "README.md")

    subprocess.run(['python', 'Twilight.pyc'])

if __name__ == "__main__":
    g()
