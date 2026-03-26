# Portafolio: Sistema de Gestión de Clientes (Django)

Este proyecto forma parte de mi formación en el programa Full Stack Python. Es una aplicación web profesional que implementa operaciones CRUD y gestión avanzada de usuarios.

## 🛠️ Tecnologías y Habilidades Aplicadas
- **Django Framework:** Uso de arquitectura MTV.
- **Vistas Basadas en Clases (CBV):** Implementación de `UpdateView` para una lógica de código limpia.
- **Modelos Avanzados:** Extensión del modelo `User` nativo mediante una relación `OneToOneField` para perfiles con biografía.
- **UX/UI Feedback:** Uso del Framework de Mensajes de Django para notificaciones contextuales de éxito.
- **Seguridad:** Implementación de tokens CSRF en todos los formularios.

## 📂 Estructura del Producto
- `web/`: Aplicación principal.
- `gestion_clientes/`: Configuración del core.
- `templates/`: Diseño modular con herencia de plantillas (`base.html`).
