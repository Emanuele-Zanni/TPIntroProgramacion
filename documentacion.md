# Proyecto: Gestor de Mesas para Restaurante


## 🧩 **Descripción General del Proyecto**

El proyecto es un **Gestor de Mesas para un Restaurante**, diseñado para funcionar íntegramente en consola. Permite administrar todos los flujos operativos del salón y delivery, registrar ventas, gestionar mozos, controlar productos, visualizar reportes y concluir el día con un cierre contable.

El sistema está dividido en **5 módulos principales**, cada uno con responsabilidades bien definidas.

---

## 📦 **Módulos del Sistema**

### 1. **Mesas**

Gestiona todas las mesas del salón y los pedidos de delivery. Permite:

* Levantar, Anular y Cobrar mesas (Salon)
* Configurar cantidad de Mesas en el Local
* Cargar y Anular pedidos (Delivery)
* Cargar, Modificar y Editar productos
* Calcular totales
* Actualizar estadísticas

### 2. **Mozos**

Administra toda la información y estadísticas relacionadas con los mozos:

* Crear y Eliminar Mozos
* Editar datos de los mozos
* Estadísticas de trabajo

### 3. **Productos / Stock**

Permite gestionar el catálogo de productos vendidos:

* Alta, baja y modificación de productos
* Listado completo de los productos disponibles

### 4. **Caja**

Módulo dedicado a la visualización de datos agregados del día:

* Información global del salón y delivery
* Totales recaudados por método de pago
* Estadísticas generales de mesas y mozos
* Visualización de logs
* Reportes de porcentajes, promedios y comportamiento del restaurante

### 5. **Inicio**

Permite iniciar un nuevo ciclo de trabajo:

* Limpia estadísticas del día
* Vacía los logs acumulados
* Resetea las mesas
* Regenera estructuras de datos

---

## 📁 **Estructura General del Código**

A medida que envíes los archivos, este README incluirá:

### ✔️ Descripción de cada archivo

### ✔️ Explicación detallada de cada función

### ✔️ Parámetros, retornos y efectos

### ✔️ Ejemplos de uso

### ✔️ Flujo lógico entre módulos

---

## 🟦 Documentación de Módulos

# 📘 Caja

A continuación se listan las funciones del módulo **Caja**, organizadas por archivo y explicadas brevemente.

---

## functions.py

* **printInfoGeneral(mesas,pedidos,mozos,productos,e,td,tc,ch,d,ed,tdd,tcd,chd,dd)**
  Recibe datos de mesas, pedidos, mozos, productos y montos recaudados por método de pago. Obtiene mesas activas mediante `printMesasActivas`, imprime información general del estado del restaurante y una tabla alineada con ingresos de salón, delivery y totales. No retorna valores.

* **printInfoMozos()**
  Muestra en consola el menú de la sección "Info Mozos". No recibe ni devuelve datos; únicamente imprime texto.

* **infoMozosSubmenu(listaMozos, mozoStats)**
  Maneja la interacción del usuario dentro del submenú de mozos. Valida nombre o número del mozo mediante `isMozoNameValid`, `checkAndConvertToInt` e `isMozoValid`. Si es válido, llama a `printInfoMozo`. Controla flujo y no retorna nada.

* **infoMesasSubmenu(mesas,statsMesas,dtc,cantPedidosVendidos,listaProductos,logs)**
  Controla el submenú de información de mesas. Llama a `menus.printInfoMesas` para imprimir menú, a `printMesaStats` para estadísticas detalladas y a `verLogs` para navegación de registros. No retorna valores.

* **printInfoMozo(listaMozos,mozoStats,numMozo)**
  Recibe un número de mozo y muestra su información completa: código, nombre, mesas activas, mesas cobradas, deliveries realizados, ingresos, costos de anulaciones y total final. Usa `numMozo` como índice y no devuelve valores.

* **printMesaStats(listaMesas,statsMesas)**
  Solicita al usuario el número de mesa, valida el input y muestra estadísticas de esa mesa: veces levantada, anulaciones, dinero recaudado, dinero anulado, mozos asignados, productos cargados y anulados, y porcentaje de elección. No retorna valores.

* **verLogs(listaProductos,logs)**
  Permite recorrer la lista de logs identificando si el usuario está viendo el primer, último, único o un log intermedio. Muestra el log actual mediante `printLog` y permite navegar con anterior/siguiente o ingresar ID. No retorna datos.

* **printLog(listaProductos,logs,id=1)**
  Devuelve un string formateado con información completa del log solicitado: hora, tipo (salón/delivery), mesa o dirección, mozo, productos (usando `printProducts`) y total con método de pago. Es usado por `verLogs` y no imprime directamente.

* **printTableOrAddress(logs,id)**
  Recibe los logs y decide si debe imprimirse "Mesa: X | Mozo: Y" o "Direccion: X | Mozo: Y" dependiendo del tipo de operación. Devuelve texto.

* **calcCantidadMesasSold(statsMesa)**
  Suma `statsMesa[i][0]` para todas las mesas, representando las veces levantadas (ventas). Devuelve un entero.

* **calcProductosMasyMenosVendidos(listaProductos,listaProductosVendidos)**
  Procesa la lista de códigos vendidos, calcula ocurrencias por producto y determina cuál(es) fueron los más y menos vendidos. Devuelve dos textos describiendo producto(s) más y menos vendidos con cantidad y porcentaje.

---

## menus.py

* **cajaMenu()**
  Imprime el menú principal de Caja con opciones para consultar información general, mozos, mesas y stock. No tiene parámetros ni retorno.

* **printInfoMesas(listaMesas,statsMesa,dtc,pedidosVendidos,pedidosAnulados)**
  Recibe estadísticas de mesas y pedidos, calcula porcentajes salón/delivery, muestra costos promedio y un menú con opciones para ver estadísticas detalladas o logs. No retorna valores.

* **printInfoStock(listaProductos,codigosProductosVendidos,prodStats)**
  Muestra información de stock, incluyendo productos más y menos vendidos usando `calcProductosMasyMenosVendidos`. Ofrece opciones para ver una tabla comparativa o salir. No retorna nada.

* **pct(parte,total)**
  Función auxiliar que devuelve el porcentaje `parte * 100 / (total or 1)`, evitando divisiones por cero.

* **listaComparativaProductos(listaProductos,codigosProductosVendidos,prodStats)**
  Para cada producto, calcula stock inicial, ventas y anulaciones en salón y delivery, porcentajes de vendido, anulado y restante. Construye e imprime una tabla alineada con toda la información. No retorna valores.

---

# 📘 General

A continuación se listan las funciones auxiliares del módulo **General**, organizadas por archivo.

---

## functions.py

- **clearConsole()**  
  No recibe parámetros ni devuelve valores. Limpia la consola ejecutando `cls` en Windows o `clear` en otros sistemas operativos, usando `os.system`.

- **ordenarBubble(lista, mode="asc")**  
  Recibe una lista y un modo de ordenamiento (`"asc"` para ascendente, cualquier otro valor para descendente). Implementa el algoritmo de bubble sort in-place, recorriendo la lista y swap-eando elementos según el criterio elegido. No retorna valores; modifica la lista original.

- **ordenarBubbleParalela(Lista, ListaParalela, mode="asc")**  
  Recibe dos listas (`Lista` y `ListaParalela`) y un modo de ordenamiento. Ordena `Lista` mediante bubble sort y, cada vez que intercambia elementos en `Lista`, realiza el mismo intercambio en `ListaParalela`, manteniendo la relación entre ambas. No retorna nada; modifica ambas listas in-place.

- **checkAndConvertToInt(value)**  
  Recibe un string `value` y verifica si representa un entero positivo (solo dígitos). Si es válido, devuelve `(True, int(value))`; si no, devuelve `(False, value)` sin convertir. Se usa para validar y castear inputs numéricos.

- **checkAndConvertToFloat(value)**  
  Recibe un string `value` y comprueba si representa un número flotante positivo simple (permitiendo un solo punto decimal). Si es válido, devuelve `(True, float(value))`; si no, devuelve `(False, value)`. Se usa para validar montos y precios.

---

## menus.py

- **mainMenu()**  
  No recibe parámetros ni retorna valores. Imprime en consola el menú principal del sistema, mostrando las opciones para acceder a Mesas, Mozos, Stock, Caja o Finalizar Día.

---

# 📘 Inicio

El módulo **Inicio** actúa como pantalla de apertura y cierre del sistema, permitiendo iniciar un nuevo día de trabajo o finalizar el programa, y reseteando todas las estadísticas cuando corresponde.

---

## functions.py

- **Inicio()**  
  No recibe parámetros directos. Muestra un menú de inicio de día mediante `InicioDiaMenu`, dentro de un bucle que permanece activo mientras el usuario no salga. Si el usuario elige la opción `"1"`, rompe el bucle y retorna `(False, True, True)` para indicar que debe iniciarse un nuevo día y habilitar los demás módulos. Si elige `"2"`, muestra un mensaje de placeholder para “Logs días anteriores”. Si elige `"X"` o `"x"`, finaliza retornando `(False, False)` para indicar que debe cerrarse el programa. En cualquier otro caso, imprime un mensaje de opción inválida y vuelve al menú.

- **resetAllStats(statsMesas,statsDelivery,mozoStats,listaProductosVendidos,cantPedidosVendidos,logs,ec,tdc,tcc,cc,dc,ecd,tdcd,tccd,ccd,dcd)**  
  Recibe todas las estructuras de estadísticas y contadores globales del sistema (mesas, delivery, mozos, productos vendidos, cantidad de pedidos, logs e ingresos por método de pago tanto en salón como en delivery). Internamente reinicia todos los acumuladores de caja a cero, vacía la lista de logs, limpia la lista de productos vendidos y reconstruye `statsMesas` con una fila nueva `[0, [], 0, 0, 0, 0, 0]` por cada mesa existente. También vacía `statsDelivery` y reconstruye `mozoStats` con una estructura base `[[0,0,0,0],[0,0,0,0]]` para cada mozo. Devuelve todas las estructuras reiniciadas en el mismo orden en que las recibe, para que el programa principal pueda reasignarlas y comenzar un nuevo día con datos limpios.

---

## menus.py

- **InicioDiaMenu()**  
  No recibe parámetros ni devuelve valores. Imprime en consola el menú de inicio del programa, con las opciones para iniciar un nuevo día, ver el resumen de días previos o finalizar el programa.

- **printFinalLog(listaProductos,logs,id=1)**  
  Recibe la lista de productos, la lista de logs y opcionalmente un ID de log. Devuelve un string formateado que representa un “log de día”, incluyendo cabecera, hora de facturación, tipo (salón/delivery) y total de la mesa con método de pago. Actualmente contiene comentarios y placeholders (como `X` en el título y secciones sin completar) pensados para expandir la funcionalidad de resumen de días previos.


---

# 📘 Mesas

El módulo **Mesas** gestiona tanto las mesas de salón como los pedidos de delivery, incluyendo levantar, cobrar, anular, mover, cambiar mozo, listar y mostrar estadísticas, además de varias funciones auxiliares para formato de salida.

---

## functions.py

- **levantarMesa(listaMesas, listaMozos, listaProductos, mesaStats, prodsTutorial)**  
  Permite levantar una mesa de salón: valida número de mesa y mozo, carga productos con soporte para tutorial (`prodsTutorial`), calcula el total, actualiza `listaMesas` con `[numMozo, pedidosMesa, disponible=False, total]`, registra la mesa en el mozo correspondiente, incrementa estadísticas de la mesa en `mesaStats` (veces levantada, mozos asignados, cantidad de productos) y ordena los productos de la mesa. No retorna valor.

- **anularMesa(listaMesas, listaMozos, listaProductos, mesaStats, prodStats, pedidosAnulados, numMesa, place)**  
  Anula una mesa o pedido según el origen (`place = "Salon"` o `"Delivery"`). Quita la mesa de la lista de mesas asignadas al mozo, actualiza `mesaStats` (veces anulada, productos anulados, dinero anulado) si es salón, actualiza `prodStats` mediante `updateProdStats` con modo `"Anular"`, para delivery además ajusta stock con `ajustarStock`, incrementa `pedidosAnulados` y elimina la entrada de la lista. Retorna `pedidosAnulados` en el caso de delivery.

- **cobrarMesa(listaMesas, listaMozos, listaProductos, prodStats, table, e, td, tc, ch, d, totalCaja, productosVendidos, logs)**  
  Cobra una mesa de salón: valida que la mesa exista y no esté vacía, desasigna la mesa del mozo, solicita el método de pago (`metodoPagoMenu`), suma el total a la variable correspondiente (efectivo, débito, crédito, cheque o deuda) y a `totalCaja`, registra productos vendidos en `productosVendidos`, genera un log en `logs` con hora (`datetime.now()`), tipo `"Salon"` y detalle de mesa, descuenta stock con `ajustarStock`, actualiza `prodStats` con `updateProdStats` modo `"Cobrar"` y resetea la mesa con `resetMesa`. Retorna las variables actualizadas: `e, td, tc, ch, d, totalCaja, productosVendidos`.

- **updateProdStats(listaProductos, prodStats, pedidosMesa, mode, place)**  
  Agrupa los códigos de productos de la mesa con `agruparProductos` y, para cada producto, busca su índice en `listaProductos`. Si `mode` es `"Cobrar"`, suma la cantidad vendida al contador de salón (`[0]`) o delivery (`[2]`); si es `"Anular"`, suma al contador de anulaciones de salón (`[1]`) o delivery (`[3]`. Devuelve la estructura `prodStats` actualizada.

- **ajustarStock(listaProductos, codigos)**  
  Agrupa los códigos de productos en `codigos`, contando cuántas unidades se usaron de cada uno, y por cada producto encontrado descuenta esa cantidad del stock (`listaProductos[j][3]`). No devuelve nada; modifica `listaProductos` in-place.

- **agruparProductos(codigos)**  
  Recibe una lista de códigos de productos (posiblemente repetidos) y devuelve una lista de pares `[codigo, cantidad]` con el conteo de cada producto único.

- **cobrarPedido(listaMesas, listaMozos, listaProductos, prodStats, listaProductosVendidos, pedido, e, td, tc, ch, d, totalCaja, pedidosVendidos, logs)**  
  Igual a `cobrarMesa`, pero para pedidos de delivery: valida la “mesa” (pedido) indicada, desasigna al mozo, muestra el detalle del pedido con `printMesa`, cobra según método de pago, acumula en `e, td, tc, ch, d` y `totalCaja`, registra productos vendidos en `listaProductosVendidos`, genera un log con tipo `"Delivery"` y dirección, descuenta stock, actualiza `prodStats` y elimina el pedido de `listaMesas`. Incrementa `pedidosVendidos` y retorna `e, td, tc, ch, d, totalCaja, pedidosVendidos`.

- **resetMesa(listaMesas, table)**  
  Resetea una mesa de salón fijando `listaMesas[table-1]` a `[0, [], True, 0]`, es decir: sin mozo, sin productos, disponible y total en 0.

- **moverMesa(mesas, mesaMovidas)**  
  Solicita una mesa origen y una destino, valida que ambas existan, que la origen no esté vacía y la destino esté libre. Si es válido, copia el contenido de la mesa origen a la destino y resetea la origen. Pensada para incrementar un contador de mesas movidas (variable externa), retorna la lista de mesas actualizada.

- **getMesa(listaMesas, mesa)**  
  Devuelve directamente el registro de `listaMesas[mesa-1]` (mozo, productos, disponibilidad y total).

- **cambiarMozo(listaMesas, listaMozos, table)**  
  Cambia el mozo asignado a una mesa. Obtiene el mozo actual, pide nombre o código del nuevo mozo y valida la entrada con `checkAndConvertToInt`, `isMozoValid` o `isMozoNameValid`. Si es válido, actualiza el código de mozo en `listaMesas[table-1][0]` y muestra un mensaje de éxito. Retorna la lista de mesas modificada.

- **printCargaProdsTutorial()**  
  Limpia la consola y muestra un mini-tutorial de cómo cargar productos (uso de `x`, `-`, `*` y `?` para finalizar, restar, agregar cantidades y ver ayuda). No recibe ni devuelve datos.

- **printMesa(listaMesas, listaProductos, numMesa, showAllProducts=False, maxShowProducts=3)**  
  Genera una representación en forma de “caja” de una mesa específica. Si la mesa está vacía, muestra un recuadro con “MESA VACIA”; si está ocupada, muestra mozo, productos (nombre x cantidad con subtotal a la derecha) y total, formateados usando `_box_line`, `_box_line_lr` y `construir_lineas_productos_lr`. Retorna un string listo para imprimir.

- **printMesas(listaMesas, listaProductos)**  
  Limpia la consola, construye los bloques de texto de cada mesa con `printMesa` y los muestra en forma de grilla usando `render_side_by_side`, con varias mesas por fila. No devuelve nada.

- **printMesasActivas(listaMesas)**  
  Recorre la lista de mesas, detecta las que están ocupadas (`disponible == False`) y devuelve una tupla `(mesasActivas, texto)` donde `mesasActivas` es la lista de números de mesa y `texto` es una cadena con el mensaje “Mesas Activas: [...]”.

- **printPedidosActivos(listaMesas)**  
  Similar a `printMesasActivas`, pero devuelve todos los índices como “pedidos activos” sin filtrar por disponibilidad. Retorna `(pedidosActivos, texto)`.

- **printMesasLibres(listaMesas)**  
  Construye una lista con los índices de mesas disponibles (`True` en posición de disponibilidad) e imprime en consola `"Mesas Disponibles: [...]"`. No retorna valor.

- **printMozosMesa(stats)**  
  A partir de una lista de estadísticas por mozo en una mesa, arma un texto multi-línea con formato `Mozo <id> x <veces>` por cada entrada. Devuelve este string para ser incluido en otros prints.

- **editMesasQuantity(listaMesas, statsMesas)**  
  Llama a `tableSettingsMenu` para determinar si se deben agregar o eliminar mesas. Si se agregan, apendea nuevas mesas `[0, [], True, 0]` y stats `[0, [], 0, 0, 0, 0, 0]`. Si se eliminan, crea copias y solo recorta si las últimas mesas están vacías. Imprime mensajes según el resultado y retorna `(listaMesas, statsMesas)` actualizados.

- **levantarPedido(listaPedidos, listaMozos, listaProductos, stats, prodsTutorial)**  
  Levanta un pedido de delivery: genera un ID incremental de pedido, valida mozo, dirección y carga productos de forma similar a `levantarMesa` (con soporte para el tutorial de carga). Calcula el total, ordena los productos, crea un nuevo pedido `[numMozo, pedidosMesa, direccion, total]` y lo agrega a `listaPedidos`, además de registrar la mesa en el mozo correspondiente. No retorna nada.

- **seleccionarMesa(mesas, productos, mozos, mesaStats, prodStats, mozoStats, ec, tdc, tcc, cc, dc, dtc, listaProductosVendidos, logs)**  
  Permite seleccionar una mesa de salón para operar: muestra mesas activas, solicita una mesa y valida. Si es válida y no está vacía, muestra el detalle con `printMesa` y el menú de operaciones (`seleccionarMesaMenu`): cobrar, anular, cambiar mozo, mover o convertir. Si se cobra, actualiza estadísticas del mozo (`mozoStats`), llama a `cobrarMesa` y retorna las variables de caja y lista de productos vendida actualizadas (`ec, tdc, tcc, cc, dc, dtc, listaProductosVendidos`).

- **seleccionarPedido(mesas, productos, mozos, prodStats, mozoStats, listaProductosVendidos, ecd, tdcd, tccd, ccd, dcd, dtcd, pedidosVendidos, pedidosAnulados, logs)**  
  Igual a `seleccionarMesa`, pero para pedidos de delivery: lista pedidos activos, permite elegir uno y, mediante `seleccionarPedidoMenu`, permite cobrar o anular. Al cobrar, actualiza `mozoStats` de delivery, llama a `cobrarPedido` y devuelve las variables de caja y contadores de pedidos (`ecd, tdcd, tccd, ccd, dcd, dtcd, pedidosVendidos, pedidosAnulados`).

- **Salon(mesas, mozos, productos, statsMesas, mozoStats, prodStats, cargaProdTutorial, listaProductosVendidos, ec, tdc, tcc, cc, dc, dtc, logs)**  
  Controla el submenú de salón: permite ver mesas (`printMesas`), levantar mesa (`levantarMesa`) o seleccionar mesa (`seleccionarMesa`). Ajusta `cargaProdTutorial` tras la primera vez y retorna las variables de caja y estado de tutorial (`ec, tdc, tcc, cc, dc, dtc, cargaProdTutorial, listaProductosVendidos`).

- **Delivery(listaPedidos, listaMozos, listaProductos, mozoStats, prodStats, listaProductosVendidos, ecd, tdcd, tccd, ccd, dcd, dtcd, prodsTutorial, pedidosVendidos, pedidosAnulados, logs)**  
  Controla el submenú de delivery: permite ver pedidos (`printMesas` sobre `listaPedidos`), levantar pedido (`levantarPedido`) y seleccionar pedido (`seleccionarPedido`). Al final retorna los acumuladores de caja de delivery y contadores de pedidos (`ecd, tdcd, tccd, ccd, dcd, dtcd, pedidosVendidos, pedidosAnulados`).

- **checkStock(producto, codigos)**  
  Cuenta cuántas veces aparece el código de `producto` en la lista `codigos` y lo compara contra el stock disponible (`producto[3]`). Devuelve `False` si ya se alcanzó o superó el stock, `True` en caso contrario.

- **BOX_WIDTH (constante)**  
  Define el ancho de las cajas usadas en los prints de mesas (`printMesa`), controlando el tamaño horizontal del recuadro.

- **_fit(texto, inner)**  
  Función auxiliar de formato: si el texto es más corto que `inner`, lo rellena con espacios; si es más largo, lo recorta y agrega puntos suspensivos. Devuelve el texto adaptado al ancho.

- **_box_line(texto, inner)**  
  Envuelve texto en un cuadro añadiendo barras verticales a los costados (`|...|`) y ajusta el contenido a `inner` usando `_fit`. Devuelve la línea formateada.

- **_box_line_lr(left, right, inner, min_gap=1, padding_right=2)**  
  Construye una línea con dos columnas dentro de una caja: `left` alineado a la izquierda y `right` pegado a la derecha, respetando un espacio mínimo (`min_gap`) y padding a la derecha. Se usa para mostrar nombre de producto y precio alineados.

- **construir_lineas_productos_lr(listaProductos, codigos)**  
  A partir de una lista de códigos, cuenta la cantidad de cada producto, busca su nombre y precio unitario en `listaProductos` y devuelve una lista de tuplas `(texto_izquierda, texto_derecha)` preparada para `printMesa` (por ejemplo `"- Pizza x 2", "2000$"`).

- **render_side_by_side(bloques, cols=4, padding=4)**  
  Recibe una lista de strings (cada uno, un “bloque” como el de `printMesa`) y los imprime en varias columnas, alineando las líneas de cada bloque y respetando un padding horizontal. Se usa para mostrar varias mesas/pedidos en grilla.

---

## menus.py

- **mesasMenu()**  
  Imprime el menú principal del módulo Mesas, con opciones para ver salón, delivery, configurar cantidad de mesas o volver al menú anterior.

- **salonMenu()**  
  Imprime el submenú de salón con opciones para ver mesas, levantar mesa, seleccionar mesa o volver.

- **deliveryMenu()**  
  Imprime el submenú de delivery con opciones para ver pedidos, levantar pedido, seleccionar pedido o volver.

- **seleccionarMesaMenu(numMesa)**  
  Imprime el menú de operaciones para una mesa de salón específica (`numMesa`): cobrar, anular, cambiar mozo, mover o convertir a delivery, además de cancelar la operación.

- **seleccionarPedidoMenu(numMesa)**  
  Igual que el anterior, pero para pedidos de delivery: opciones para cobrar, anular, cambiar mozo o convertir hacia salón (no implementado), y cancelar.

- **metodoPagoMenu()**  
  Muestra el menú de métodos de pago: efectivo, tarjeta débito, tarjeta crédito, cheque, deuda o cancelar operación. Usado por `cobrarMesa` y `cobrarPedido`.

- **statsMenu()**  
  Menú simple (actualmente auxiliar) para elegir entre ver estadísticas generales, estadísticas de mesa o volver.

- **tableSettingsMenu(mesas)**  
  Recibe la lista de mesas y pregunta por una nueva cantidad total deseada. Calcula la diferencia respecto de `len(mesas)` y devuelve una tupla `(mode, newTableQuantity)` donde `mode` indica la operación: `1` para agregar mesas, `-1` para eliminar, `0` si no hay cambios, `-2` si se intenta eliminar más mesas de las que existen, `4` si el input está vacío y `5` si el valor no es numérico.

---

## validations.py

- **isMesaEmpty(listaMesas, numMesa)**  
  Comprueba el campo de disponibilidad de la mesa indicada (`listaMesas[numMesa-1][2]`). Devuelve `True` si la mesa está vacía/disponible, `False` si está ocupada.

- **isMesaReal(listaMesas, numMesa)**  
  Valida que `numMesa` esté dentro del rango válido de índices (mayor que 0 y menor o igual a `len(listaMesas)`). Devuelve `True` si la mesa existe, `False` en caso contrario.

- **isMesaValid(listaMesas, numMesa)**  
  Combina validaciones de existencia y disponibilidad: recorre la lista de mesas, verifica si el número existe y si la mesa está libre. Devuelve una tupla `(mesaValida, error)` donde `mesaValida` es `True` si la mesa es válida para levantarla y `error` contiene un mensaje descriptivo en caso de que no exista o esté ocupada.

---

# 📘 Mozos

El módulo **Mozos** administra la lista de mozos del restaurante (alta, baja, visualización) y provee validaciones y funciones auxiliares para integrarlos con mesas y estadísticas.

---

## functions.py

- **buscar_indice(lista_mozos, id_mozo)**  
  Recorre secuencialmente `lista_mozos` buscando un mozo cuyo ID (`mozo[0]`) coincida con `id_mozo`. Devuelve el índice encontrado o `-1` si no existe. Se usa para localizar mozos al eliminar, asignar mesas, etc.

- **mostrar_mozos(lista_mozos)**  
  Imprime en consola un listado simple de todos los mozos en formato `ID, Nombre, Mesas asignadas`. No modifica datos ni retorna valores; es puramente visual.

- **agregar_mozo(lista_mozos, mozoStats)**  
  Solicita el nombre de un nuevo mozo, valida que no esté vacío, que no comience con un número y que no exista ya un mozo con ese nombre. Si es válido, genera un nuevo ID incremental, crea la entrada `[ID, nombre, [], 0]` (ID, nombre, lista de mesas asignadas, recaudado) y una estructura de estadísticas `[[0,0,0,0],[0,0,0,0]]` para `mozoStats`. Agrega ambos a sus listas y muestra un mensaje de confirmación. Retorna la lista de mozos actualizada.

- **eliminar_mozo(lista_mozos, mozoStats)**  
  Solicita el ID de un mozo, valida que sea un número usando `checkAndConvertToInt` y busca el índice con `buscar_indice`. Si lo encuentra y el mozo no tiene mesas asignadas (`len(mozo[2]) == 0`), lo elimina tanto de `lista_mozos` como de `mozoStats`. Si aún tiene mesas o no existe el ID, informa el error. No retorna valor; modifica las listas in-place.

- **agrupar_productos(codigos)**  
  Toma una lista de códigos (por ejemplo, productos vendidos por un mozo) y construye una lista de códigos únicos, contando cuántas veces aparece cada uno. Devuelve una lista de pares `[codigo, cantidad]`. Es útil para resumir ventas por producto.

---

## menus.py

- **menu_mozos(lista_mozos, mozoStats)**  
  Controla el flujo del menú de mozos. Muestra opciones para ver todos los mozos, agregar uno nuevo o eliminarlo, y delega en `mostrar_mozos`, `agregar_mozo` y `eliminar_mozo` según la opción seleccionada. El bucle se mantiene activo hasta que el usuario ingresa `"X"` o `"x"` para volver al menú principal. No retorna valor; opera sobre las listas pasadas por referencia.

---

## validations.py

- **isMozoValid(listaMozos, numMozo)**  
  Recibe el número de mozo (`numMozo`) y revisa si corresponde a una posición válida dentro de `listaMozos`. Devuelve `True` si el mozo existe, `False` en caso contrario. Se utiliza para validar inputs numéricos al asignar o seleccionar mozos.

- **isMozoNameValid(listaMozos, nombreMozo)**  
  Busca un mozo cuyo nombre coincida exactamente con `nombreMozo`. Si lo encuentra, devuelve `(True, codigoMozo)` donde `codigoMozo` es el ID asociado; si no, devuelve `(False, "")`. Se utiliza para permitir búsquedas por nombre además de por ID.

---

# 🧾 Productos

El módulo **Productos** (Stock) gestiona el catálogo de ítems vendidos por el restaurante, incluyendo alta, baja, edición, búsqueda y visualización de productos, además de estadísticas de ventas/anulaciones asociadas.

---

## functions.py

- **addProducto(listaProductos, prodStats)**  
  Inicia un flujo interactivo en consola para dar de alta un nuevo producto. Valida paso a paso: código numérico único, nombre no vacío, precio `> 0` y cantidad `> 0`. Si el usuario no cancela con `"x"`, agrega a `listaProductos` una entrada `[codigo, nombre, precio, cantidad]` y a `prodStats` una entrada `[0, 0, 0, 0]` para estadísticas (ventas/anulaciones salón/delivery). Finalmente ordena ambas listas en paralelo por código usando `ordenarBubbleParalela`. No retorna valor; modifica las listas in-place.

- **editProduct(listaProductos)**  
  Pide el código del producto a editar, valida que exista con `isCodeReal` y muestra un submenú para modificar uno de los campos: código, nombre, precio o cantidad. Cada campo tiene sus propias validaciones (código numérico y único, nombre no vacío ni numérico, precio `> 0`, cantidad numérica). Si las validaciones pasan, actualiza el producto directamente en `listaProductos`. No retorna valor; solo modifica in-place y muestra mensajes en consola.

- **deleteProduct(listaProductos, prodStats)**  
  Solicita el código del producto a eliminar, verifica si existe en `listaProductos` y, si se encuentra, muestra un resumen del producto y una confirmación. Si el usuario confirma, elimina la entrada de `listaProductos` y la entrada correspondiente de `prodStats` en el mismo índice. En caso de cancelación o código inválido, muestra mensajes de error o cancelación. No retorna valor; modifica las listas in-place.

- **getProduct(listaProductos, codigo)**  
  Recorre `listaProductos` buscando un producto cuyo código (`producto[0]`) coincida con `codigo`. Si lo encuentra, devuelve esa lista `[codigo, nombre, precio, cantidad]`. Si no existe, imprime un mensaje de error y devuelve la cadena vacía `""`. Se usa como función auxiliar en varias operaciones de cálculo y visualización.

- **printProducts(listaProductos, codigos)**  
  Recibe la lista de productos y una lista de códigos (por ejemplo, productos cargados en una mesa). Agrupa los códigos para contar cuántas unidades de cada producto hay, arma una lista `[codigo, cantidad]` ordenada con `ordenarBubble`, y genera un texto multilinea donde cada línea tiene el formato:  
  `- NOMBRE x CANT == SUBTOTAL$`.  
  Devuelve ese texto como `str` para ser embebido en otros prints (no imprime directamente).

- **calculateTotal(listaProductos, codigos)**  
  Calcula el importe total de una venta sumando el precio (`producto[2]`) de cada código presente en `codigos`. Usa `getProduct` para obtener la información del producto y acumula el total. Devuelve un `float` o `int` con el total de la operación.

- **printTablaProductos(listaProductos)**  
  Genera e imprime en consola una tabla en formato de “caja” con bordes ASCII, mostrando todos los productos actuales. Las columnas son `CODIGO`, `NOMBRE`, `PRECIO`, `CANTIDAD` y cada valor se centra dentro de su celda. Si `listaProductos` está vacía, muestra un mensaje informando que no hay productos. No retorna valor; es puramente visual.

---

## menus.py

- **stockMenu(listaProductos, prodStats)**  
  Controla el menú principal del módulo Stock. Muestra opciones para ver productos, añadir, modificar o eliminar. Según la opción del usuario, llama a `printTablaProductos`, `addProducto`, `editProduct` o `deleteProduct`. El bucle se mantiene hasta que se selecciona `"X"` para volver al menú principal. No retorna valor; actúa sobre `listaProductos` y `prodStats` recibidos por referencia.

---

## validations.py

- **isCodeReal(listaStock, code)**  
  Recorre `listaStock` buscando si algún elemento tiene `item[0] == code`. Devuelve `True` si el código de producto ya existe en el stock, `False` en caso contrario. Se utiliza para validar códigos en altas y modificaciones de productos.


