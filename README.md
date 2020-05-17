












# CPrint

- [������� ����](#rus)
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

## <a name="rus"></a> ������� ����

����� ������������� ������

### ������ ������

```
from cprint import cprint
```

### ���������

���� ������ ���������� ��� �� ��� � ������� print, �� � ���������� ���������

- ����� ���������� � �������

```
cprint(text)
```

- ������� � ���� ����� ��� ����� �������� ���� ���������� �������� ����� �� �����

```
~{���� ������:���� ����:�����������}~
```

��������� ����� ���������, ���� �� ����� ������ ��� ����� 

- ��� ������ �������������� ��������

```
~{reset}~
```

### �������� ����������

- ��� � �����

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

- ������������

```
l - ������ �����
n - ����������� ���
b - ������ �����
```