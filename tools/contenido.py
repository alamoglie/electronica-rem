# -*- coding: utf-8 -*-
"""Contenido de las páginas de servicio generadas por build.py.

Cada página es un dict con:
  slug, title, description, h1, subtitle, crumb, wa_text,
  sections: [{"h2", "intro", "cards": [(titulo, texto, href|None)]}]
  cta, faqs: [(pregunta, respuesta)], related: [slugs], brands: "tv" | "monitor" | "audio"
"""

HORARIO = "Estamos en Av. Pres. Perón 1182, Ramos Mejía, Provincia de Buenos Aires. Atendemos lunes a viernes de 9 a 18 hs y sábados de 9 a 13 hs."
PRESUPUESTO = "Sí. Primero revisamos el equipo, te informamos el problema y el presupuesto, y recién si lo aprobás comenzamos la reparación."

FAQ_HORARIO = ("¿Dónde está el local y en qué horario atienden?", HORARIO)
FAQ_PRESUPUESTO = ("¿Me pasan el presupuesto antes de reparar?", PRESUPUESTO)
FAQ_MARCAS = ("¿Qué marcas de TV reparan?", "Reparamos televisores LED, LCD y Smart TV de marcas como Samsung, LG, Sony, Philips, Panasonic, TCL, Hisense, Noblex, JVC y otras.")

# Bloque reutilizable para páginas de zona: cómo llevar el TV sin dañarlo.
TRASLADO = {
    "h2": "Cómo traer el TV sin dañarlo",
    "intro": "Un mal traslado puede romper el panel. Tené en cuenta esto antes de salir.",
    "cards": [
        ("Siempre parado", "Llevalo en posición vertical. Acostado, el peso del propio panel puede quebrarlo.", None),
        ("Protegé la pantalla", "Si no tenés la caja original, envolvelo con una frazada y no apoyes nada sobre la pantalla.", None),
        ("Sin las patas", "Si podés, sacale las patas o el pie: así viaja más firme. Traé el control remoto si sospechás que la falla puede ser de encendido.", None),
    ],
}

PAGES = [
    # ---------------------------------------------------------------- FALLAS
    {
        "slug": "reparacion-tv-lineas-en-pantalla",
        "group": "fallas",
        "nav": "TV con líneas en pantalla",
        "title": "TV con líneas en la pantalla | Reparación en Ramos Mejía",
        "description": "¿Tu TV muestra líneas verticales u horizontales, franjas de colores o media pantalla? Diagnóstico y reparación de TV LED y Smart TV en Ramos Mejía.",
        "h1": "TV con líneas en la pantalla: reparación en Ramos Mejía",
        "subtitle": "Líneas verticales u horizontales, franjas de colores, imagen partida o duplicada. Revisamos tu TV LED o Smart TV y te decimos con claridad si conviene repararlo.",
        "crumb": "TV con líneas en pantalla",
        "wa_text": "Hola, mi TV tiene líneas en la pantalla. Quiero consultar por la reparación",
        "sections": [
            {
                "h2": "¿Cómo se ven las líneas?",
                "intro": "El tipo de línea orienta el diagnóstico. Si podés, sacale una foto y mandala por WhatsApp.",
                "cards": [
                    ("Líneas verticales finas", "Una o varias líneas de color fijas, de arriba a abajo. Suelen estar relacionadas con el panel o sus conexiones.", None),
                    ("Líneas o franjas horizontales", "Bandas que cruzan la pantalla de lado a lado, a veces con colores alterados.", None),
                    ("Media pantalla oscura o duplicada", "La imagen aparece partida, repetida o con una mitad distinta a la otra.", None),
                    ("Colores invertidos o \"negativo\"", "Los colores se ven alterados, como un negativo, o con mucho ruido.", None),
                    ("Líneas que aparecen y desaparecen", "Cambian con la temperatura o al tocar el marco del TV.", None),
                    ("Manchas o zonas más claras", "Áreas con brillo desparejo. En este caso suele tratarse de la retroiluminación.", "/reparacion-tv-sin-imagen"),
                ],
            },
            {
                "h2": "Qué puede estar fallando",
                "intro": "No todas las líneas se reparan igual. Esto es lo que revisamos.",
                "cards": [
                    ("Placa T-CON", "Es la placa que controla el panel. Cuando falla puede generar líneas, colores alterados o imagen duplicada, y en general tiene arreglo.", None),
                    ("Placa principal", "Si la señal sale mal de la placa principal, las líneas aparecen en cualquier fuente de imagen.", None),
                    ("Conexiones del panel", "Los cables planos y conectores que llegan al panel pueden aflojarse o dañarse.", None),
                ],
            },
            {
                "h2": "Antes de traerlo, probá esto",
                "intro": "Te ayuda a saber si la falla es del TV o de lo que tiene conectado.",
                "cards": [
                    ("1. Abrí el menú del TV", "Si las líneas también se ven sobre el menú, la falla es interna. Si solo aparecen en un canal o entrada, puede ser la fuente de señal.", None),
                    ("2. Cambiá cable y entrada HDMI", "Probá otro cable y otra entrada para descartar el decodificador, la consola o el cable.", None),
                    ("3. No presiones la pantalla", "Apretar el marco o el panel para \"probar\" puede empeorar el daño.", None),
                ],
            },
        ],
        "cta": "¿Tu TV tiene líneas? Mandanos una foto por WhatsApp",
        "faqs": [
            ("¿Las líneas en la pantalla del TV tienen arreglo?", "Depende de la causa. Si la falla está en la placa T-CON, en la placa principal o en una conexión, en general se repara. Si el daño está en el propio panel, la reparación puede no ser conveniente y te lo decimos antes de hacer cualquier trabajo."),
            ("¿Por qué aparecieron líneas de un día para el otro?", "Puede ser por el desgaste de una conexión, por un golpe, por humedad o por un pico de tensión. El diagnóstico permite saber cuál fue la causa."),
            ("¿Sirve mandar una foto antes de llevar el TV?", "Sí. Una foto de la pantalla con el menú abierto nos ayuda a darte una primera orientación por WhatsApp."),
            FAQ_MARCAS,
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-sin-imagen", "reparacion-tv-no-enciende", "service-smart-tv"],
        "brands": "tv",
    },
    {
        "slug": "reparacion-tv-sin-sonido",
        "group": "fallas",
        "nav": "TV sin sonido",
        "title": "TV sin sonido o con audio distorsionado | Ramos Mejía",
        "description": "¿Tu TV tiene imagen pero no tiene sonido, el audio se escucha bajo o distorsionado? Reparación de TV LED y Smart TV en Ramos Mejía y Zona Oeste.",
        "h1": "TV sin sonido: reparación en Ramos Mejía",
        "subtitle": "Se ve bien pero no se escucha, el volumen es muy bajo, el audio sale distorsionado o con ruidos. Revisamos tu TV y te pasamos el presupuesto antes de reparar.",
        "crumb": "TV sin sonido",
        "wa_text": "Hola, mi TV no tiene sonido. Quiero consultar por la reparación",
        "sections": [
            {
                "h2": "Síntomas más comunes",
                "intro": "Contanos cuál de estos se parece a lo que le pasa a tu TV.",
                "cards": [
                    ("Imagen sí, sonido no", "El TV funciona normalmente pero no sale nada de audio por los parlantes.", None),
                    ("Audio distorsionado", "El sonido se escucha roto, saturado o con vibraciones, incluso a volumen bajo.", None),
                    ("Volumen muy bajo", "Aunque subas el volumen al máximo, casi no se escucha.", None),
                    ("Ruidos o zumbidos", "Se escuchan chasquidos, zumbidos o soplidos constantes.", None),
                    ("El audio se corta", "El sonido aparece y desaparece, o se pierde en algunas aplicaciones.", None),
                    ("Sonido desfasado", "La voz no coincide con el movimiento de la boca.", None),
                ],
            },
            {
                "h2": "Causas habituales",
                "intro": "Qué revisamos cuando un TV no tiene sonido.",
                "cards": [
                    ("Amplificador de audio", "En la mayoría de los TV está en la placa principal. Si falla, deja de salir sonido o sale distorsionado.", None),
                    ("Parlantes", "Con el uso y el calor los parlantes se dañan y empiezan a sonar rotos.", None),
                    ("Configuración o software", "Una salida de audio mal configurada o una falla de software también pueden dejar al TV mudo.", None),
                ],
            },
            {
                "h2": "Antes de traerlo, probá esto",
                "intro": "Muchas veces el problema es de configuración.",
                "cards": [
                    ("1. Revisá la salida de audio", "En el menú de sonido, verificá que la salida esté en \"Parlantes del TV\" y no en óptica, HDMI ARC o Bluetooth.", None),
                    ("2. Probá con otra fuente", "Fijate si pasa lo mismo con la TV abierta, con YouTube y con lo que tengas por HDMI.", None),
                    ("3. Desconectá barras y auriculares", "Una barra de sonido o un dispositivo Bluetooth vinculado puede estar tomando el audio.", None),
                ],
            },
        ],
        "cta": "¿Tu TV se quedó sin sonido? Escribinos",
        "faqs": [
            ("Mi TV tiene imagen pero no sonido, ¿qué puede ser?", "Puede ser la configuración de la salida de audio, el amplificador de la placa principal o los parlantes. Si ya revisaste la configuración y sigue sin sonido, conviene traerlo a diagnóstico."),
            ("¿Se puede reparar el sonido distorsionado de un TV?", "Sí, en general se repara. Revisamos los parlantes y la etapa de amplificación para encontrar la causa."),
            ("Uso una barra de sonido, ¿la pueden revisar también?", "Sí. Revisamos también barras de sonido y equipos de audio, así descartamos si la falla es del TV o del equipo externo."),
            FAQ_MARCAS,
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-equipos-de-audio", "reparacion-tv-sin-imagen", "service-smart-tv"],
        "brands": "tv",
    },
    {
        "slug": "reparacion-tv-se-apaga-solo",
        "group": "fallas",
        "nav": "TV que se apaga solo",
        "title": "TV que se apaga solo o se reinicia | Reparación en Ramos Mejía",
        "description": "¿Tu TV se apaga solo, se reinicia o queda trabado en el logo? Diagnóstico y reparación de TV LED y Smart TV en Ramos Mejía y Zona Oeste.",
        "h1": "TV que se apaga solo: reparación en Ramos Mejía",
        "subtitle": "Prende, funciona un rato y se apaga. O se reinicia una y otra vez en el logo de la marca. Te ayudamos a encontrar la causa y te pasamos el presupuesto antes de reparar.",
        "crumb": "TV que se apaga solo",
        "wa_text": "Hola, mi TV se apaga solo. Quiero consultar por la reparación",
        "sections": [
            {
                "h2": "¿Cómo se apaga?",
                "intro": "El momento en que se apaga da muchas pistas.",
                "cards": [
                    ("A los pocos segundos de prender", "Arranca, muestra la imagen un instante y se apaga. Suele activar una protección.", None),
                    ("Después de un rato de uso", "Funciona bien 20 o 30 minutos y después se apaga, a veces con el equipo caliente.", None),
                    ("Se reinicia en el logo", "Queda en un ciclo: logo de la marca, pantalla negra y vuelta a empezar.", None),
                    ("Se apaga siempre a la misma hora", "Puede ser un temporizador o una opción de ahorro de energía.", None),
                    ("Se apaga al apagar otro equipo", "El decodificador o la consola pueden estar apagando el TV por HDMI.", None),
                    ("Se apaga y la luz parpadea", "Queda apagado y el indicador titila: ver TV que no enciende.", "/reparacion-tv-no-enciende"),
                ],
            },
            {
                "h2": "Causas más habituales",
                "intro": "Qué revisamos cuando un TV se apaga solo.",
                "cards": [
                    ("Fuente de alimentación", "Componentes desgastados que no sostienen la tensión cuando el TV se calienta.", None),
                    ("Protección por retroiluminación", "Si fallan los LEDs de la pantalla, muchos TV se apagan solos para protegerse.", None),
                    ("Placa principal o software", "Fallas de memoria o de sistema que provocan reinicios, sobre todo en Smart TV.", None),
                ],
            },
            {
                "h2": "Antes de traerlo, probá esto",
                "intro": "Descartá primero los ajustes que apagan el TV a propósito.",
                "cards": [
                    ("1. Revisá temporizadores", "Buscá en el menú \"temporizador de apagado\", \"apagado automático\" o \"ahorro de energía\" y desactivalos.", None),
                    ("2. Desactivá el control por HDMI", "Según la marca se llama Anynet+, SimpLink, Bravia Sync o HDMI-CEC. Si el problema desaparece, no es una falla.", None),
                    ("3. Anotá cuándo pasa", "Fijate si se apaga a los segundos, a los minutos o en un horario fijo, y contanos.", None),
                ],
            },
        ],
        "cta": "¿Tu TV se apaga solo? Escribinos y lo revisamos",
        "faqs": [
            ("¿Por qué mi TV se apaga solo después de un rato?", "Si no es un temporizador, lo más común es una fuente de alimentación desgastada o una protección que se activa por la retroiluminación. Con el diagnóstico confirmamos la causa."),
            ("Mi Smart TV se reinicia en el logo, ¿tiene arreglo?", "En muchos casos sí. Puede ser una falla de software, de memoria o de la placa principal. Lo revisamos y te informamos qué conviene hacer."),
            ("¿Es peligroso seguir usando un TV que se apaga solo?", "Conviene no forzarlo. Prenderlo y apagarlo muchas veces puede agravar una falla de fuente que hoy quizás tiene una reparación simple."),
            FAQ_MARCAS,
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-no-enciende", "reparacion-tv-sin-imagen", "service-smart-tv"],
        "brands": "tv",
    },

    # --------------------------------------------------------------- EQUIPOS
    {
        "slug": "reparacion-monitores",
        "group": "servicios",
        "nav": "Monitores",
        "title": "Reparación de monitores en Ramos Mejía | Electrónica REM",
        "description": "Reparación de monitores LED y LCD para PC y gaming en Ramos Mejía: monitor que no enciende, sin señal, sin imagen o con líneas. Samsung, LG, Dell, BenQ y más.",
        "h1": "Reparación de monitores en Ramos Mejía",
        "subtitle": "Monitores LED y LCD de PC, oficina y gaming. Si no enciende, no tiene señal o se ve con fallas, lo revisamos y te pasamos el presupuesto antes de reparar.",
        "crumb": "Reparación de monitores",
        "wa_text": "Hola, quiero consultar por la reparación de un monitor",
        "sections": [
            {
                "h2": "Fallas que reparamos",
                "intro": "Las consultas más frecuentes sobre monitores.",
                "cards": [
                    ("No enciende", "No prende la luz o queda parpadeando. Muchas veces es la fuente interna o el adaptador.", None),
                    ("Sin señal", "El monitor prende pero muestra \"sin señal\" aunque la PC funcione.", None),
                    ("Pantalla oscura", "La imagen se ve muy oscura o desaparece a los segundos: suele ser la retroiluminación.", None),
                    ("Líneas o colores alterados", "Líneas fijas, franjas o colores que no corresponden.", None),
                    ("Parpadeos", "La imagen titila o el brillo cambia solo.", None),
                    ("Puertos dañados", "Entradas HDMI, DisplayPort o VGA flojas o que dejaron de funcionar.", None),
                ],
            },
            {
                "h2": "Antes de traerlo, probá esto",
                "intro": "Descartá la PC y los cables.",
                "cards": [
                    ("1. Cambiá el cable", "Probá con otro cable HDMI o DisplayPort y en otra salida de la placa de video.", None),
                    ("2. Elegí la entrada correcta", "Desde los botones del monitor, verificá que esté seleccionada la entrada donde conectaste la PC.", None),
                    ("3. Probá con otro equipo", "Conectá una notebook u otra PC para saber si la falla es del monitor.", None),
                ],
            },
        ],
        "cta": "¿Tu monitor falla? Escribinos con la marca y el modelo",
        "faqs": [
            ("¿Conviene reparar un monitor?", "En muchos casos sí, sobre todo cuando la falla está en la fuente, la retroiluminación o la placa. Si el daño es del panel, te lo decimos antes para que decidas."),
            ("¿Qué marcas de monitores reparan?", "Reparamos monitores Samsung, LG, Dell, BenQ, Philips, NEC, AOC y otras marcas, de uso hogareño, de oficina y gaming."),
            ("¿Tengo que traer el cable o el adaptador?", "Sí, traé el adaptador de corriente si el monitor usa uno externo: muchas veces la falla está ahí."),
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-ramos-mejia", "reparacion-tv-lineas-en-pantalla", "reparacion-equipos-de-audio"],
        "brands": "monitor",
        "device": "Monitor",
    },
    {
        "slug": "reparacion-equipos-de-audio",
        "group": "servicios",
        "nav": "Equipos de audio",
        "title": "Reparación de equipos de audio en Ramos Mejía | Electrónica REM",
        "description": "Reparación de amplificadores, receivers, minicomponentes y barras de sonido en Ramos Mejía: sin sonido, distorsión, zumbidos o equipos que no encienden.",
        "h1": "Reparación de equipos de audio en Ramos Mejía",
        "subtitle": "Amplificadores, receivers, minicomponentes, parlantes potenciados y barras de sonido. Reparamos fallas de encendido, de sonido y de conexión, con presupuesto previo.",
        "crumb": "Reparación de equipos de audio",
        "wa_text": "Hola, quiero consultar por la reparación de un equipo de audio",
        "sections": [
            {
                "h2": "Equipos que reparamos",
                "intro": "Audio hogareño, vintage y profesional.",
                "cards": [
                    ("Amplificadores y receivers", "Equipos estéreo y home theater, incluidos modelos vintage.", None),
                    ("Minicomponentes", "Equipos de música completos, con sus etapas de radio, CD y Bluetooth.", None),
                    ("Parlantes potenciados", "Bafles activos y parlantes con amplificador incorporado.", None),
                    ("Barras de sonido", "Barras y subwoofers que dejaron de funcionar o perdieron la conexión con el TV.", None),
                    ("Bandejas y equipos de época", "Revisión y puesta a punto de equipos de las grandes marcas de audio.", None),
                    ("Audio del TV", "Si el problema está en el sonido del televisor, mirá TV sin sonido.", "/reparacion-tv-sin-sonido"),
                ],
            },
            {
                "h2": "Fallas habituales",
                "intro": "Contanos qué le pasa a tu equipo.",
                "cards": [
                    ("Sin sonido en un canal", "Se escucha solo un parlante o un lado suena más bajo.", None),
                    ("Distorsión y ruidos", "Zumbidos, soplidos, chasquidos al girar el volumen o sonido saturado.", None),
                    ("No enciende o entra en protección", "El equipo no prende, o prende y se corta enseguida.", None),
                ],
            },
        ],
        "cta": "¿Tu equipo de audio falla? Escribinos",
        "faqs": [
            ("¿Reparan equipos de audio vintage?", "Sí. Revisamos amplificadores, receivers y equipos de época, y te informamos qué necesita cada uno antes de trabajar."),
            ("¿Qué marcas de audio reparan?", "Trabajamos con Technics, Pioneer, Denon, Onkyo, Sony, JBL, Bose, Philips, Samsung, LG y otras marcas."),
            ("Mi equipo hace ruido al girar el volumen, ¿tiene arreglo?", "Sí, es una falla frecuente por desgaste o suciedad en los controles y en general tiene solución."),
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-sin-sonido", "reparacion-monitores", "reparacion-tv-ramos-mejia"],
        "brands": "audio",
        "device": "Equipo de audio",
    },

    # ---------------------------------------------------------------- MARCAS
    {
        "slug": "reparacion-tv-lg",
        "group": "marcas",
        "nav": "LG",
        "title": "Reparación de TV LG en Ramos Mejía | Smart TV y LED",
        "description": "Service de TV LG en Ramos Mejía: TV LED, Smart TV webOS, OLED y NanoCell que no enciende, sin imagen, con líneas o sin sonido. Más de 40 años de experiencia.",
        "h1": "Reparación de TV LG en Ramos Mejía",
        "subtitle": "Reparamos TV LG LED, Smart TV con webOS, NanoCell y otras líneas. Diagnóstico claro y presupuesto antes de empezar.",
        "crumb": "Reparación de TV LG",
        "wa_text": "Hola, quiero consultar por la reparación de un TV LG",
        "sections": [
            {
                "h2": "Fallas frecuentes en TV LG",
                "intro": "Las consultas que más recibimos sobre televisores LG.",
                "cards": [
                    ("Sonido sin imagen", "Se escucha pero la pantalla queda negra. En TV LG LED suele estar relacionado con las tiras de retroiluminación.", "/reparacion-tv-sin-imagen"),
                    ("No enciende", "La luz roja queda fija o el TV no responde al control.", "/reparacion-tv-no-enciende"),
                    ("Se reinicia en el logo", "El Smart TV queda en el logo de LG o se reinicia una y otra vez.", "/reparacion-tv-se-apaga-solo"),
                    ("Líneas o colores alterados", "Líneas verticales, franjas o imagen duplicada.", "/reparacion-tv-lineas-en-pantalla"),
                    ("Problemas de webOS", "Aplicaciones que se cierran, lentitud o falta de conexión WiFi.", "/service-smart-tv"),
                    ("Sin sonido", "Imagen correcta pero sin audio o con audio distorsionado.", "/reparacion-tv-sin-sonido"),
                ],
            },
            {
                "h2": "Antes de consultar",
                "intro": "Estos datos nos ayudan a orientarte más rápido.",
                "cards": [
                    ("Modelo exacto", "Está en la etiqueta de atrás del TV, con un código del tipo 43UN7300, 50UQ8050 o similar.", None),
                    ("Qué hace exactamente", "Si prende la luz, si se escucha sonido, si se ve el logo de LG.", None),
                    ("Desde cuándo", "Si empezó de golpe, después de un corte de luz o se fue agravando.", None),
                ],
            },
        ],
        "cta": "¿Tu TV LG tiene una falla? Escribinos",
        "faqs": [
            ("¿Reparan Smart TV LG?", "Sí. Reparamos TV LG LED, Smart TV con webOS, NanoCell y otras líneas de la marca."),
            ("Mi TV LG tiene sonido pero no imagen, ¿tiene arreglo?", "En muchos casos sí. Suele estar relacionado con la retroiluminación LED, aunque hay que revisarlo para confirmar la causa y pasarte el presupuesto."),
            ("¿Son el service oficial de LG?", "No. Somos un servicio técnico independiente con más de 40 años de experiencia en reparación de televisores de todas las marcas."),
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-samsung", "reparacion-tv-philips", "reparacion-tv-sin-imagen"],
        "brands": "tv",
    },
    {
        "slug": "reparacion-tv-philips",
        "group": "marcas",
        "nav": "Philips",
        "title": "Reparación de TV Philips en Ramos Mejía | Smart TV y LED",
        "description": "Service de TV Philips en Ramos Mejía: Smart TV, Android TV y TV LED que no enciende, sin imagen, se reinicia o tiene líneas. Presupuesto antes de reparar.",
        "h1": "Reparación de TV Philips en Ramos Mejía",
        "subtitle": "Reparamos TV Philips LED, Smart TV y Android TV. Revisamos la falla y te pasamos el presupuesto antes de reparar.",
        "crumb": "Reparación de TV Philips",
        "wa_text": "Hola, quiero consultar por la reparación de un TV Philips",
        "sections": [
            {
                "h2": "Fallas frecuentes en TV Philips",
                "intro": "Lo que más nos consultan sobre televisores Philips.",
                "cards": [
                    ("No enciende o la luz parpadea", "El TV queda en stand-by o el indicador titila sin arrancar.", "/reparacion-tv-no-enciende"),
                    ("Sonido sin imagen", "Se escucha pero la pantalla está negra o muy oscura.", "/reparacion-tv-sin-imagen"),
                    ("Se traba o reinicia", "El Smart TV queda en el logo, se reinicia o las apps se cierran.", "/reparacion-tv-se-apaga-solo"),
                    ("Líneas en la pantalla", "Franjas, líneas fijas o colores alterados.", "/reparacion-tv-lineas-en-pantalla"),
                    ("Problemas de Smart TV", "Fallas de WiFi, de aplicaciones o de actualización.", "/service-smart-tv"),
                    ("Sin sonido", "Audio bajo, distorsionado o inexistente.", "/reparacion-tv-sin-sonido"),
                ],
            },
            {
                "h2": "Antes de consultar",
                "intro": "Con estos datos te orientamos mejor por WhatsApp.",
                "cards": [
                    ("Modelo exacto", "Está en la etiqueta de atrás, con un código del tipo 50PUD7406 o similar.", None),
                    ("Qué hace exactamente", "Si la luz prende o parpadea, si hay sonido, si aparece el logo.", None),
                    ("Desde cuándo", "Si fue de golpe, tras un corte de luz o se fue agravando.", None),
                ],
            },
        ],
        "cta": "¿Tu TV Philips tiene una falla? Escribinos",
        "faqs": [
            ("¿Reparan Smart TV y Android TV Philips?", "Sí. Reparamos TV Philips LED, Smart TV y Android TV."),
            ("Mi TV Philips se reinicia solo, ¿qué puede ser?", "Puede ser una falla de software, de la placa principal o de la fuente. Lo revisamos y te informamos qué conviene hacer."),
            ("¿Son el service oficial de Philips?", "No. Somos un servicio técnico independiente con más de 40 años de experiencia en reparación de televisores de todas las marcas."),
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-lg", "reparacion-tv-noblex", "reparacion-tv-no-enciende"],
        "brands": "tv",
    },
    {
        "slug": "reparacion-tv-tcl",
        "group": "marcas",
        "nav": "TCL",
        "title": "Reparación de TV TCL en Ramos Mejía | Smart TV y LED",
        "description": "Service de TV TCL en Ramos Mejía: Android TV, Google TV y TV LED que no enciende, tiene sonido sin imagen, se traba en el logo o tiene líneas.",
        "h1": "Reparación de TV TCL en Ramos Mejía",
        "subtitle": "Reparamos TV TCL LED, Android TV y Google TV. Diagnóstico claro y presupuesto antes de reparar.",
        "crumb": "Reparación de TV TCL",
        "wa_text": "Hola, quiero consultar por la reparación de un TV TCL",
        "sections": [
            {
                "h2": "Fallas frecuentes en TV TCL",
                "intro": "Las consultas más comunes sobre televisores TCL.",
                "cards": [
                    ("Sonido sin imagen", "La pantalla queda negra o muy oscura aunque se escucha. Suele estar ligado a la retroiluminación.", "/reparacion-tv-sin-imagen"),
                    ("Trabado en el logo", "El Android TV o Google TV no pasa del logo o se reinicia.", "/reparacion-tv-se-apaga-solo"),
                    ("No enciende", "El TV no responde o la luz queda fija.", "/reparacion-tv-no-enciende"),
                    ("Líneas o manchas", "Líneas en la imagen o zonas con brillo desparejo.", "/reparacion-tv-lineas-en-pantalla"),
                    ("WiFi y aplicaciones", "No conecta a internet o las apps no abren.", "/service-smart-tv"),
                    ("Sin sonido", "Imagen correcta pero sin audio.", "/reparacion-tv-sin-sonido"),
                ],
            },
            {
                "h2": "Antes de consultar",
                "intro": "Con estos datos te orientamos más rápido.",
                "cards": [
                    ("Modelo exacto", "Está en la etiqueta de atrás del TV, con un código del tipo 50P635 o similar.", None),
                    ("Qué hace exactamente", "Si prende la luz, si hay sonido, si ves el logo de TCL o de Android/Google TV.", None),
                    ("Desde cuándo", "Si empezó de golpe o se fue agravando con el tiempo.", None),
                ],
            },
        ],
        "cta": "¿Tu TV TCL tiene una falla? Escribinos",
        "faqs": [
            ("¿Reparan TV TCL con Android TV o Google TV?", "Sí. Reparamos TV TCL LED, Android TV y Google TV."),
            ("Mi TV TCL tiene sonido pero no imagen, ¿tiene arreglo?", "En muchos casos sí. Suele estar relacionado con la retroiluminación LED, pero hay que revisarlo para confirmar la causa y pasarte el presupuesto."),
            ("¿Son el service oficial de TCL?", "No. Somos un servicio técnico independiente con más de 40 años de experiencia en reparación de televisores de todas las marcas."),
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-noblex", "reparacion-tv-samsung", "reparacion-tv-sin-imagen"],
        "brands": "tv",
    },
    {
        "slug": "reparacion-tv-noblex",
        "group": "marcas",
        "nav": "Noblex",
        "title": "Reparación de TV Noblex en Ramos Mejía | Smart TV y LED",
        "description": "Service de TV Noblex en Ramos Mejía: TV LED y Smart TV que no enciende, sin imagen, se reinicia, tiene líneas o no tiene sonido. Presupuesto antes de reparar.",
        "h1": "Reparación de TV Noblex en Ramos Mejía",
        "subtitle": "Reparamos TV Noblex LED y Smart TV. Revisamos la falla y te pasamos el presupuesto antes de empezar.",
        "crumb": "Reparación de TV Noblex",
        "wa_text": "Hola, quiero consultar por la reparación de un TV Noblex",
        "sections": [
            {
                "h2": "Fallas frecuentes en TV Noblex",
                "intro": "Lo que más nos consultan sobre televisores Noblex.",
                "cards": [
                    ("Sonido sin imagen", "Se escucha pero la pantalla queda negra u oscura.", "/reparacion-tv-sin-imagen"),
                    ("No enciende", "No prende o la luz de stand-by parpadea.", "/reparacion-tv-no-enciende"),
                    ("Se reinicia o se traba", "Queda en el logo, se reinicia o se apaga solo.", "/reparacion-tv-se-apaga-solo"),
                    ("Líneas en la pantalla", "Líneas fijas, franjas o colores alterados.", "/reparacion-tv-lineas-en-pantalla"),
                    ("Smart TV y WiFi", "Fallas de conexión, de aplicaciones o de sistema.", "/service-smart-tv"),
                    ("Sin sonido", "Imagen correcta pero sin audio o con distorsión.", "/reparacion-tv-sin-sonido"),
                ],
            },
            {
                "h2": "Antes de consultar",
                "intro": "Con estos datos te orientamos mejor.",
                "cards": [
                    ("Modelo exacto", "Está en la etiqueta de atrás del TV, con un código del tipo 50X7100 o similar.", None),
                    ("Qué hace exactamente", "Si la luz prende o parpadea, si hay sonido, si aparece el logo.", None),
                    ("Desde cuándo", "Si fue de golpe, tras una tormenta o se fue agravando.", None),
                ],
            },
        ],
        "cta": "¿Tu TV Noblex tiene una falla? Escribinos",
        "faqs": [
            ("¿Reparan Smart TV Noblex?", "Sí. Reparamos TV Noblex LED y Smart TV de distintas líneas."),
            ("Mi TV Noblex no prende, ¿tiene arreglo?", "En muchos casos sí. Revisamos la fuente, la placa principal y las protecciones para encontrar la causa y te pasamos el presupuesto."),
            ("¿Son el service oficial de Noblex?", "No. Somos un servicio técnico independiente con más de 40 años de experiencia en reparación de televisores de todas las marcas."),
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-tcl", "reparacion-tv-philips", "reparacion-tv-no-enciende"],
        "brands": "tv",
    },

    # ----------------------------------------------------------------- ZONAS
    {
        "slug": "reparacion-tv-san-justo",
        "group": "zonas",
        "nav": "San Justo",
        "title": "Reparación de TV en San Justo | Service LED y Smart TV",
        "description": "Service de TV LED y Smart TV para vecinos de San Justo, La Matanza. Local en Ramos Mejía con más de 40 años de experiencia. Presupuesto antes de reparar.",
        "h1": "Reparación de TV para San Justo",
        "subtitle": "Servicio técnico de TV LED y Smart TV para vecinos de San Justo y La Matanza. Nuestro local está en Ramos Mejía y reparamos televisores desde 1983.",
        "crumb": "Reparación de TV en San Justo",
        "wa_text": "Hola, soy de San Justo y quiero consultar por la reparación de un TV",
        "sections": [
            {
                "h2": "Service de TV para San Justo",
                "intro": "Atendemos a clientes de San Justo y del resto de La Matanza en nuestro local de Ramos Mejía.",
                "cards": [
                    ("Nuestro local", "Av. Pres. Perón 1182, Ramos Mejía, Provincia de Buenos Aires.", None),
                    ("Horarios", "Lunes a viernes de 9 a 18 hs y sábados de 9 a 13 hs.", None),
                    ("Consultá antes de venir", "Escribinos por WhatsApp con la marca, el modelo y la falla, y te orientamos antes de que viajes.", None),
                ],
            },
            {
                "h2": "Qué reparamos",
                "intro": "Fallas frecuentes en TV LED y Smart TV.",
                "cards": [
                    ("TV que no enciende", "No prende, la luz parpadea o se apaga solo.", "/reparacion-tv-no-enciende"),
                    ("TV sin imagen", "Se escucha pero la pantalla está negra u oscura.", "/reparacion-tv-sin-imagen"),
                    ("Líneas en la pantalla", "Líneas, franjas o colores alterados.", "/reparacion-tv-lineas-en-pantalla"),
                    ("TV sin sonido", "Imagen correcta pero sin audio.", "/reparacion-tv-sin-sonido"),
                    ("Smart TV", "Reinicios, apps y conexión WiFi.", "/service-smart-tv"),
                    ("Monitores y audio", "También reparamos monitores y equipos de audio.", "/reparacion-monitores"),
                ],
            },
            TRASLADO,
        ],
        "cta": "¿Sos de San Justo y tu TV falla? Escribinos",
        "faqs": [
            ("¿Atienden clientes de San Justo?", "Sí. Recibimos equipos de San Justo y de toda La Matanza en nuestro local de Ramos Mejía."),
            ("¿Puedo consultar antes de llevar el TV?", "Sí. Mandanos por WhatsApp la marca, el modelo y una descripción o foto de la falla, y te damos una primera orientación."),
            FAQ_MARCAS,
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-villa-luzuriaga", "reparacion-tv-ramos-mejia", "reparacion-tv-haedo"],
        "brands": "tv",
        "place": "San Justo",
    },
    {
        "slug": "reparacion-tv-villa-luzuriaga",
        "group": "zonas",
        "nav": "Villa Luzuriaga",
        "title": "Reparación de TV en Villa Luzuriaga | Service LED y Smart TV",
        "description": "Service de TV LED y Smart TV para vecinos de Villa Luzuriaga. Local en Ramos Mejía con más de 40 años de experiencia. Presupuesto antes de reparar.",
        "h1": "Reparación de TV para Villa Luzuriaga",
        "subtitle": "Servicio técnico de TV LED y Smart TV para vecinos de Villa Luzuriaga. Nuestro local está en Ramos Mejía y reparamos televisores desde 1983.",
        "crumb": "Reparación de TV en Villa Luzuriaga",
        "wa_text": "Hola, soy de Villa Luzuriaga y quiero consultar por la reparación de un TV",
        "sections": [
            {
                "h2": "Service de TV para Villa Luzuriaga",
                "intro": "Atendemos a clientes de Villa Luzuriaga en nuestro local de Ramos Mejía.",
                "cards": [
                    ("Nuestro local", "Av. Pres. Perón 1182, Ramos Mejía, Provincia de Buenos Aires.", None),
                    ("Horarios", "Lunes a viernes de 9 a 18 hs y sábados de 9 a 13 hs.", None),
                    ("Consultá antes de venir", "Escribinos por WhatsApp con la marca, el modelo y la falla, y te orientamos antes de que vengas.", None),
                ],
            },
            {
                "h2": "Qué reparamos",
                "intro": "Fallas frecuentes en TV LED y Smart TV.",
                "cards": [
                    ("TV que no enciende", "No prende, la luz parpadea o se apaga solo.", "/reparacion-tv-no-enciende"),
                    ("TV sin imagen", "Se escucha pero la pantalla está negra u oscura.", "/reparacion-tv-sin-imagen"),
                    ("Líneas en la pantalla", "Líneas, franjas o colores alterados.", "/reparacion-tv-lineas-en-pantalla"),
                    ("TV que se apaga solo", "Se apaga o se reinicia después de un rato.", "/reparacion-tv-se-apaga-solo"),
                    ("Smart TV", "Reinicios, apps y conexión WiFi.", "/service-smart-tv"),
                    ("Equipos de audio", "Amplificadores, minicomponentes y barras de sonido.", "/reparacion-equipos-de-audio"),
                ],
            },
            TRASLADO,
        ],
        "cta": "¿Sos de Villa Luzuriaga y tu TV falla? Escribinos",
        "faqs": [
            ("¿Atienden clientes de Villa Luzuriaga?", "Sí. Recibimos equipos de Villa Luzuriaga en nuestro local de Ramos Mejía."),
            ("¿Puedo consultar antes de llevar el TV?", "Sí. Mandanos por WhatsApp la marca, el modelo y una descripción o foto de la falla, y te damos una primera orientación."),
            FAQ_MARCAS,
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-san-justo", "reparacion-tv-ramos-mejia", "reparacion-tv-haedo"],
        "brands": "tv",
        "place": "Villa Luzuriaga",
    },
    {
        "slug": "reparacion-tv-ciudadela",
        "group": "zonas",
        "nav": "Ciudadela",
        "title": "Reparación de TV en Ciudadela | Service LED y Smart TV",
        "description": "Service de TV LED y Smart TV para vecinos de Ciudadela, Tres de Febrero. Local en Ramos Mejía con más de 40 años de experiencia. Presupuesto previo.",
        "h1": "Reparación de TV para Ciudadela",
        "subtitle": "Servicio técnico de TV LED y Smart TV para vecinos de Ciudadela y Tres de Febrero. Nuestro local está en Ramos Mejía y reparamos televisores desde 1983.",
        "crumb": "Reparación de TV en Ciudadela",
        "wa_text": "Hola, soy de Ciudadela y quiero consultar por la reparación de un TV",
        "sections": [
            {
                "h2": "Service de TV para Ciudadela",
                "intro": "Atendemos a clientes de Ciudadela en nuestro local de Ramos Mejía.",
                "cards": [
                    ("Nuestro local", "Av. Pres. Perón 1182, Ramos Mejía, Provincia de Buenos Aires.", None),
                    ("Horarios", "Lunes a viernes de 9 a 18 hs y sábados de 9 a 13 hs.", None),
                    ("Consultá antes de venir", "Escribinos por WhatsApp con la marca, el modelo y la falla, y te orientamos antes de que vengas.", None),
                ],
            },
            {
                "h2": "Qué reparamos",
                "intro": "Fallas frecuentes en TV LED, Smart TV y monitores.",
                "cards": [
                    ("TV que no enciende", "No prende, la luz parpadea o se apaga solo.", "/reparacion-tv-no-enciende"),
                    ("TV sin imagen", "Se escucha pero la pantalla está negra u oscura.", "/reparacion-tv-sin-imagen"),
                    ("Líneas en la pantalla", "Líneas, franjas o colores alterados.", "/reparacion-tv-lineas-en-pantalla"),
                    ("TV sin sonido", "Imagen correcta pero sin audio.", "/reparacion-tv-sin-sonido"),
                    ("Smart TV", "Reinicios, apps y conexión WiFi.", "/service-smart-tv"),
                    ("Monitores", "Monitores de PC que no encienden o no dan señal.", "/reparacion-monitores"),
                ],
            },
            TRASLADO,
        ],
        "cta": "¿Sos de Ciudadela y tu TV falla? Escribinos",
        "faqs": [
            ("¿Atienden clientes de Ciudadela?", "Sí. Recibimos equipos de Ciudadela y de Tres de Febrero en nuestro local de Ramos Mejía."),
            ("¿Puedo consultar antes de llevar el TV?", "Sí. Mandanos por WhatsApp la marca, el modelo y una descripción o foto de la falla, y te damos una primera orientación."),
            FAQ_MARCAS,
            FAQ_HORARIO,
            FAQ_PRESUPUESTO,
        ],
        "related": ["reparacion-tv-ramos-mejia", "reparacion-tv-haedo", "reparacion-tv-moron"],
        "brands": "tv",
        "place": "Ciudadela",
    },
]

# Títulos de las páginas que ya existían, para el menú, footer y tarjetas relacionadas.
EXISTING = {
    "reparacion-tv-ramos-mejia": ("servicios", "Reparación de TV LED", "Reparación de TV en Ramos Mejía", "TV LED y Smart TV de todas las marcas."),
    "service-smart-tv": ("servicios", "Service Smart TV", "Service Smart TV", "Reinicios, aplicaciones, WiFi y fallas de placa."),
    "reparacion-tv-no-enciende": ("fallas", "TV que no enciende", "TV que no enciende", "No prende o la luz de stand-by parpadea."),
    "reparacion-tv-sin-imagen": ("fallas", "TV sin imagen", "TV sin imagen", "Se escucha pero la pantalla está negra u oscura."),
    "reparacion-tv-samsung": ("marcas", "Samsung", "Reparación de TV Samsung", "TV LED y Smart TV Samsung."),
    "reparacion-tv-haedo": ("zonas", "Haedo", "Reparación de TV en Haedo", "Service de TV para vecinos de Haedo."),
    "reparacion-tv-moron": ("zonas", "Morón", "Reparación de TV en Morón", "Service de TV para vecinos de Morón."),
}

# Orden de los ítems en cada menú desplegable. Un ítem puede ser "slug" o ("slug", "texto").
MENU = [
    ("Servicios", ["reparacion-tv-ramos-mejia", "service-smart-tv", "reparacion-monitores", "reparacion-equipos-de-audio"]),
    ("Fallas", ["reparacion-tv-no-enciende", "reparacion-tv-sin-imagen", "reparacion-tv-lineas-en-pantalla", "reparacion-tv-sin-sonido", "reparacion-tv-se-apaga-solo"]),
    ("Marcas", ["reparacion-tv-samsung", "reparacion-tv-lg", "reparacion-tv-philips", "reparacion-tv-tcl", "reparacion-tv-noblex"]),
    ("Zonas", [("reparacion-tv-ramos-mejia", "Ramos Mejía"), "reparacion-tv-haedo", "reparacion-tv-moron", "reparacion-tv-san-justo", "reparacion-tv-villa-luzuriaga", "reparacion-tv-ciudadela"]),
]

# Enlaces "También te puede interesar" que se agregan a las páginas que ya existían.
RELATED_EXISTING = {
    "reparacion-tv-ramos-mejia": ["reparacion-tv-no-enciende", "reparacion-tv-sin-imagen", "reparacion-tv-lineas-en-pantalla"],
    "service-smart-tv": ["reparacion-tv-se-apaga-solo", "reparacion-tv-sin-sonido", "reparacion-tv-lg"],
    "reparacion-tv-no-enciende": ["reparacion-tv-se-apaga-solo", "reparacion-tv-sin-imagen", "reparacion-tv-samsung"],
    "reparacion-tv-sin-imagen": ["reparacion-tv-lineas-en-pantalla", "reparacion-tv-no-enciende", "reparacion-tv-lg"],
    "reparacion-tv-samsung": ["reparacion-tv-lg", "reparacion-tv-tcl", "reparacion-tv-sin-imagen"],
    "reparacion-tv-haedo": ["reparacion-tv-moron", "reparacion-tv-ramos-mejia", "reparacion-tv-san-justo"],
    "reparacion-tv-moron": ["reparacion-tv-haedo", "reparacion-tv-ciudadela", "reparacion-tv-ramos-mejia"],
}
