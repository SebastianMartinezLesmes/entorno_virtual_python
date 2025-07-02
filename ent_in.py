import os
import subprocess
import sys

def crear_entorno_virtual(nombre_entorno="venv"):
    """Crea un entorno virtual si no existe."""
    if not os.path.exists(nombre_entorno):
        print(f"[+] Creando entorno virtual: {nombre_entorno}")
        subprocess.run([sys.executable, "-m", "venv", nombre_entorno])
        print(f"[✔] Entorno virtual '{nombre_entorno}' creado correctamente.")
    else:
        print(f"[!] El entorno virtual '{nombre_entorno}' ya existe.")

def instrucciones_para_activar(nombre_entorno="venv"):
    """Imprime instrucciones para activar el entorno virtual según el sistema operativo."""
    print("\n=== Instrucciones para activar el entorno virtual ===\n")
    if os.name == "nt":  # Windows
        print(f"cmd.exe:     {nombre_entorno}\\Scripts\\activate")
        print(f"PowerShell:  .\\{nombre_entorno}\\Scripts\\Activate.ps1")
    else:  # Linux / macOS
        print(f"Bash/zsh:    source {nombre_entorno}/bin/activate")

def inicializar_entorno(nombre_entorno="venv"):
    """Crea el entorno virtual e imprime las instrucciones para activarlo."""
    crear_entorno_virtual(nombre_entorno)
    instrucciones_para_activar(nombre_entorno)

# Ejecutar si se llama el script directamente
if __name__ == "__main__":
    inicializar_entorno("env")
