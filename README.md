# 🐍 entorno_virtual_python

Este proyecto proporciona un sistema automatizado para la **creación, activación y desactivación de entornos virtuales Python**, facilitando la configuración y el aislamiento del entorno de desarrollo.

Ideal para quienes buscan una forma rápida, organizada y multiplataforma de trabajar con entornos virtuales en sus proyectos.

---

## ✅ ¿Qué hace este sistema?

- ✔️ Crea automáticamente un entorno virtual si no existe.
- ✔️ Muestra instrucciones claras para activarlo.
- ✔️ Proporciona scripts para activación y desactivación en diferentes sistemas operativos.
- ❌ No activa el entorno desde el script `.py` (limitación del lenguaje).

---
## 📁 Estructura del proyecto

```
ENTORNO_VIRTUAL_PYTHON/
│
├── .gitignore 
├── create_ent.py 
├── linux_in.sh 
├── linux_out.sh 
├── windows_in.bat 
├── windows_out.bat 
└── README.md 
```

---

## 🧭 Sistemas compatibles

Este sistema está diseñado para funcionar correctamente en los siguientes entornos operativos:

1. 🪟 **Windows**  
   Scripts `.bat` para activar y desactivar el entorno virtual desde CMD o PowerShell.

2. 🐧 **Linux / macOS**  
   Scripts `.sh` compatibles con terminales Bash/zsh para activar y desactivar el entorno virtual.

Cada sistema tiene su propio conjunto de scripts dedicados para facilitar la gestión del entorno virtual con un solo comando.

---

## 📝 Notas
- Si tu sistema no permite activar scripts por seguridad (como PowerShell), es posible que necesites cambiar la política de ejecución (Set-ExecutionPolicy en Windows).

- La carpeta env/ está incluida en .gitignore para evitar que se suba al repositorio.