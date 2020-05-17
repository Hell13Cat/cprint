












# CPrint

- [Русский язык](#rus)
- [English language](#eng)

## <a name="eng"></a> English language

Multicolored text output

### Import module

```
from cprint import cprint
```

### Syntax

This module is used in the same way as regular print, but with some differences.

- The call is made using

```
cprint(text)
```

- Starting from the place where you want to change the color, you need to insert text according to the scheme

```
~{text color:background color:modifier}~
```

Parameters can be released if you do not need to change this part 

- To reset formatting, add

```
~{reset}~
```

### Parameter Values

- Background and text

```
black
red
green
yellow
blue
magneta
cyan
white
n
```

- Modifiers

```
l - Thin lines
n - Standard view
b - Thumbnail
```

## <a name="rus"></a> Русский язык

Вывод разноцветного текста

### Импорт модуля

```
from cprint import cprint
```

### Синтаксис

Этот модуль испозуется так же как и обычный print, но с некоторыми отличиями

- Вызов происходит с помощью

```
cprint(text)
```

- Начиная с того места где нужно поменять цвет необходимо вставить текст по схеме

```
~{цвет текста:цвет фона:модификатор}~
```

Параметры можно отпускать, если не нужно менять эту часть 

- Для сброса форматирования добавьте

```
~{reset}~
```

### Значения параметров

- Фон и текст

```
black
red
green
yellow
blue
magneta
cyan
white
n
```

- Модификаторы

```
l - Тонкие линии
n - Стандартный вид
b - Жирный текст
```