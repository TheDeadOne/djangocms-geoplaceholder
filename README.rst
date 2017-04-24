=========================
djangocms-geoplaceholder
=========================

Плагин-контейнер для Django CMS, выводящий дочерние плагины только для
посетителей из определённых регионов, определяемых с помощью `django-geoip <https://github.com/futurecolors/django-geoip>`_.

Установка и настройка
----------------------

Проще всего установить его с помощью `pip <https://pypi.python.org/pypi/pip>`_ ::

$ pip install djangocms-geoplaceholder

Добавьте 'djangocms_geoplaceholder' в INSTALLED_APPS вашего проекта и запустите ::

$ manage.py migrate

Не забудьте обновить базу адресов django-geoip ::

$ manage.py geoip_update
