import os

# Ruta Resultados
ruta_resultados = './resultados'
existe_ruta = os.path.exists(ruta_resultados)
if not existe_ruta:
    os.makedirs(ruta_resultados)

existe_ruta = os.path.exists(ruta_resultados + '/evolucion')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/evolucion')

existe_ruta = os.path.exists(ruta_resultados + '/comunidad')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/comunidad')

existe_ruta = os.path.exists(ruta_resultados + '/efectos')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/efectos')

existe_ruta = os.path.exists(ruta_resultados + '/caracteristicas_tecnicas')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/caracteristicas_tecnicas')

existe_ruta = os.path.exists(ruta_resultados + '/determinantes_semanticos')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/determinantes_semanticos')

existe_ruta = os.path.exists(ruta_resultados + '/evolucion/histograma')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/evolucion/histograma')

existe_ruta = os.path.exists(ruta_resultados + '/determinantes_semanticos/nube')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/determinantes_semanticos/nube')

existe_ruta = os.path.exists(ruta_resultados + '/determinantes_semanticos/bigrama')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/determinantes_semanticos/bigrama')

existe_ruta = os.path.exists(ruta_resultados + '/comunidad/referentes')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/comunidad/referentes')

existe_ruta = os.path.exists(ruta_resultados + '/comunidad/influenciadores')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/comunidad/influenciadores')

existe_ruta = os.path.exists(ruta_resultados + '/comunidad/movilizadores')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/comunidad/movilizadores')

existe_ruta = os.path.exists(ruta_resultados + '/comunidad/activistas')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/comunidad/activistas')

existe_ruta = os.path.exists(ruta_resultados + '/comunidad/categorizar_sexo')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/comunidad/categorizar_sexo')

existe_ruta = os.path.exists(ruta_resultados + '/comunidad/masificadores')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/comunidad/masificadores')

existe_ruta = os.path.exists(ruta_resultados + '/efectos/valorizacion')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/efectos/valorizacion')

existe_ruta = os.path.exists(ruta_resultados + '/efectos/categorizacion')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/efectos/categorizacion')

existe_ruta = os.path.exists(ruta_resultados + '/efectos/muestra')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/efectos/muestra')

existe_ruta = os.path.exists(ruta_resultados + '/caracteristicas_tecnicas/caracteres')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/caracteristicas_tecnicas/caracteres')

existe_ruta = os.path.exists(ruta_resultados + '/caracteristicas_tecnicas/multimedia')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/caracteristicas_tecnicas/multimedia')

existe_ruta = os.path.exists(ruta_resultados + '/caracteristicas_tecnicas/dispositivos')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/caracteristicas_tecnicas/dispositivos')

existe_ruta = os.path.exists(ruta_resultados + '/caracteristicas_tecnicas/porcentaje_georeferencia')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/caracteristicas_tecnicas/porcentaje_georeferencia')

existe_ruta = os.path.exists(ruta_resultados + '/caracteristicas_tecnicas/ranking_georeferencia')
if not existe_ruta:
    os.makedirs(ruta_resultados + '/caracteristicas_tecnicas/ranking_georeferencia')