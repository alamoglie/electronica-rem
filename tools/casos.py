# -*- coding: utf-8 -*-
"""Casos de reparación reales. Ver tools/COMO-CARGAR-CASOS.md.

Solo se publican los casos con "publicado": False. Mientras no haya ninguno,
no se genera /casos ni aparece "Casos" en el menú.

Las fotos van en assets/casos/<slug>/ (formato .webp o .jpg, idealmente 1200px de ancho).
"""

CASOS = [
    # Ejemplo de estructura (no se publica). Copialo, completalo con datos reales
    # y poné "publicado": False.
    {
        "publicado": False,
        "slug": "samsung-un50tu7000-no-enciende",
        "fecha": "2026-10-01",                      # AAAA-MM-DD
        "titulo": "Samsung UN50TU7000 que no encendía: reparación de la fuente",
        "resumen": "Un Smart TV Samsung de 50\" dejó de prender después de un corte de luz. Te contamos qué falló y cómo lo reparamos.",
        "equipo": "Smart TV",                       # Smart TV, TV LED, Monitor, Equipo de audio...
        "marca": "Samsung",
        "modelo": "UN50TU7000",
        "zona": "Ramos Mejía",                      # de dónde era el cliente (opcional)
        "sintoma": "El TV no prendía y la luz de stand-by quedaba apagada. Había dejado de funcionar después de un corte de luz.",
        "diagnostico": "Al revisar la fuente de alimentación encontramos ... (qué se midió, qué componente estaba dañado).",
        "reparacion": "Reemplazamos ... y verificamos las tensiones de la fuente.",
        "resultado": "Lo probamos durante ... horas con distintas fuentes de imagen y se entregó funcionando.",
        "tiempo": "3 días hábiles",                 # opcional
        "fotos": [
            # ("assets/casos/samsung-un50tu7000-no-enciende/1.webp", "Fuente del TV Samsung con el componente dañado"),
        ],
        "servicios": ["reparacion-tv-no-enciende", "reparacion-tv-samsung"],
    },
]
