# Cómo cargar un caso de reparación

1. Guardá las fotos en `assets/casos/<slug>/` (por ejemplo `assets/casos/lg-43um7300-sin-imagen/1.webp`).
   Usá fotos propias del equipo, de la placa o de la pieza dañada, en lo posible de unos 1200 px de ancho.
2. En `tools/casos.py`, copiá el bloque de ejemplo y completalo con los datos reales:
   - `slug`: la dirección de la página, en minúsculas y con guiones (`marca-modelo-falla`).
   - `titulo` y `resumen`: lo que se ve en Google. Incluí la marca, el modelo y la falla.
   - `sintoma`, `diagnostico`, `reparacion`, `resultado`: un párrafo cada uno, contado en primera persona del taller.
   - `servicios`: las páginas relacionadas (por ejemplo `reparacion-tv-no-enciende`, `reparacion-tv-lg`).
   - `"publicado": True`.
3. Desde la carpeta del sitio, corré:

   ```bash
   python tools/build.py
   ```

   Se genera `/casos/<slug>`, el listado `/casos`, se agrega "Casos" al menú y al footer, y se actualiza el `sitemap.xml`.

Con el primer caso publicado aparece la sección completa. Mientras no haya ninguno, no se muestra nada.

## Otras tareas

- **Agregar o cambiar una página de servicio, falla, marca o zona:** se edita en `tools/contenido.py`. Para que aparezca en el menú, hay que sumarla también a `MENU`.
- **Cambiar el menú o el footer:** se hace en `tools/build.py` (`nav_html` y `footer_html`), y después se vuelve a correr el script.

La carpeta `tools/` no se publica (está en `.vercelignore`).
