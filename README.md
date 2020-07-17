# django-amp

amp - это Django приложение для имплементации и автоматизации обработки AMP страниц.

Установка
===
1. ``pip install django-amp-by-ByteCore``
2. Добавить ``amp`` в список ``INSTALLED_APPS``
3. Добавить ``amp.middleware.AMPMiddleware`` в список ``MIDDLEWARE``

Базовое использование
===

1. Создать шаблон ``index.html`` и ``amp/index.html``

2. ``views.py``
code-block:: python
    
    from django.shortcuts import render
    from amp import get_temaplte_name
    
    def ShowIndex(request):
        render(request, get_template_name('index.html')) 

note:: При такой записи в случае отсутствия признака amp будет отрисовон шаблон ``index.html``, а в случае его наличия (по умолчанию ``/?amp=1``) будет отрисован шаблон ``amp/index.html``


Настройки
===

* ``USE_AMP`` - Активация приложения (по умолчанию ``False``)

* ``AMP_GET_PARAMETER`` - Указывает GET параметр для определения AMP (по умолчанию ``amp``)

* ``AMP_GET_VALUE`` - Указывает значение GET параметра для определения AMP (по умолчанию ``1``)

note:: Для примера при ``AMP_GET_PARAMETER = 'amp-content'`` и ``AMP_GET_PARAMETER = 'amp'`` то признаком AMP станет запрос ``/?amp-content=amp``

* ``AMP_TEMPLATE_PREFIX`` - Указывает префикс для пути к шаблону с AMP (по умолчанию ``amp/``)

* ``AMP_GEN_PATH`` - Указывает нужно ли генерировать путь с признаком AMP (по умолчанию ``True``)

* ``AMP_DEFAULT_WIDTH`` и ``AMP_DEFAULT_HEIGHT`` - Задают пропорции сторон (или размеры) для елементов ``<amp-img>`` и ``<amp-iframe>`` в содержимом по умолчнию (по умолчанию ``1.5`` и ``1`` соответственно)

* ``AMP_IMG_TEMPLATE`` = Задаёт шаблон для ``<amp-img>`` (по умолчанию ``u'<amp-img src="$src" width="$width" height="$height" layout="responsive" alt="$alt"></amp-img>'``)

* ``AMP_IFRAME_TEMPLATE`` = Задаёт шаблон для ``<amp-iframe>`` (по умолчанию ``u'<amp-iframe width="$width" height="$height" sandbox="allow-scripts allow-same-origin" layout="responsive" frameborder="0" src="$src"></amp-iframe>'``)

Теги и значения
===
### Значения
* ``request.amp_path`` - Эквивалент ``request.path`` с признаком AMP

* ``request.is_amp`` - Указывает на необходимлсть отобразить пользователю AMP страницу

* ``request.get_full_amp_path()`` - Эквивалент ``request.get_full_path()`` с признаком AMP


### Теги
 
* ``{% amp_url '' %}`` - Эквиваленит ``{% url %}``. Возвращяет ссылку, а при необходимости отображения AMP-стриницы добавляет признак AMP

* ``{% import_file '' %}`` - Импортирует содержимое файла в шаблон. 

note:: Данная функция создана для удобства. Так-как AMP требует чтобы все стили (и скрипты - в эксперементальной версии) находились в ``.html`` файле. А работать с ними не так удобно как в отдельном файле. Поэтому этот тег импортирует стороний файл (путь указывать относительно ``BASE_DIR``) в шаблон как будто он всегда был его частью.

### Фильтры

* ``amp_link`` - Фильтр преобразовующий ссылку в ссылку с признаком AMP с сохранением параметров

* ``amp_safe`` - Эквивалент фильтра ``safe``. Преобразовует контент в AMP-совместимый

note:: Для использования тегов и фильтров необходимо добавить ``{% load amp %}`` в шаблон