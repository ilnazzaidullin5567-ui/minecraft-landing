---
name: photo_filters_skill
description: Применяет фотофильтры к изображению через Pillow — негатив (инверсия цветов) и чёрно-белый фильтр. Используй, когда пользователь просит сделать фото ч/б, негатив, инвертировать цвета или протестировать фотофильтры.
---

# Photo Filters Skill

## КОГДА запускать

Запускай этот скилл, если пользователь:
- просит сделать фотографию **чёрно-белой** (ч/б, оттенки серого, grayscale, black and white);
- просит наложить эффект **негатива** или **инвертировать цвета** (инверсия, negative, invert);
- просит **протестировать фотофильтры** или показать, как фильтры меняют изображение.

## КАК использовать

Инструмент: `image_tool.py` (лежит рядом с этим файлом). Требуется Python 3 и `Pillow` (`pip install Pillow`).

### Синтаксис вызова (bash)

```bash
python photo_filters_skill/image_tool.py <mode> <input_path> <output_path>
```

### Аргументы

| Аргумент      | Описание                                                        |
|---------------|-----------------------------------------------------------------|
| `mode`        | `negative` — негатив (`ImageOps.invert`); `bw` — ч/б (`ImageOps.grayscale`) |
| `input_path`  | путь к исходному изображению (jpg, png и т. д.)                 |
| `output_path` | путь, куда сохранить результат                                  |

### Примеры

Негатив:
```bash
python photo_filters_skill/image_tool.py negative original.jpg output_negative.jpg
```

Чёрно-белое фото:
```bash
python photo_filters_skill/image_tool.py bw original.jpg output_bw.jpg
```

После запуска проверь, что выходной файл создан, и сообщи пользователю путь к результату.
