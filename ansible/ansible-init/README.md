# ansible-init

За последние несколько лет Ansible быстро стал одним из самых популярных инструментов автоматизации.

Ansible — это платформа автоматизации ИТ общего назначения, которую можно использовать для самых разных целей:

- Установка необходимых пакетов
- Конфигурирование настроек сервера и приложений
- Развертывание приложений
- Установка много-компонетных систем на разных серверах и их соединение

Ansible не требует агентов, поэтому может работать с устаревшими инструментами, его легко устанавливать, настраивать и поддерживать.

Особенности Ansible:

- **Понятный** - Ansible использует простой синтаксис YAML, который понятен всем: разработчикам и системным администраторам.
- **Быстрый** - Быстро настраивается. Вам не нужно устанавливать дополнительные агенты или демоны на ваши сервера.
- **Эффективный** - Отсутствие дополнительных сервисов на ваших серверах означает больше ресурсов для ваших приложений.
- **Безопасный** - Ansible использует SSH и не требует дополнительных открытых портов или потенциально уязвимых демонов на ваших серверах.

## Настройка серверов

Многие разработчики и системные администраторы управляют серверами следующим образом:

1. входят на сервер через SSH,
2. вносят свои изменения,
3. выходят из системы.

Если администратору нужно было внести одно и то же изменение на многих серверах
(например, изменить одно значение в файле конфигурации), администратор вручную
заходил бы на каждый сервер и повторно вносил это изменение на каждый сервер.

Этот процесс не был бы проблемой, если у нас мало серверов и изменения происходят редко.

Но чаще всего, в компаниях серверов много и они устроены сложно — на них могут быть
запущены десятки, а то и сотни различных приложений. При внесении изменений в ручную
может получиться так, что про некоторые серверы забудут или какие-то конфигурации могут быть пропущены.

Если бы системные администраторы хотели настроить новый сервер точно так же, как другой,
им пришлось бы потратить много времени на просмотр установленных пакетов с определенными
версиями, документирование конфигураций и настроек. Далее они потратят много времени на
ручную установку, обновление и настройку всего, чтобы заставить новый сервер работать
так же как и остальные.

## Ansible решает проблему конфигурации серверов

Ansible был создан для тех, кто уже знаком с командной строкой Linux.
Ansible помогает управлять серверами так же, как это делали раньше с
помощью скриптов, но повторяемым и централизованно-управляемым способом.

У Ansible есть и другие полезные функции, что делает его универсальным инструментом для DevOps'еров.

Сильной стороной у Ansible является то, что команды запускаемые в плейбуках являются идемпотентными.

> 💡 Идемпотентность — это способность запускать команду, которая дает один и тот же результат независимо от того, запускается ли она один раз или несколько раз.

> 💡 Плейбук - это набор команд в формате Ansible, которая запускается на серверах.

## Установка Ansible

Единственная зависимость Ansible — это Python. После установки Python
самый простой способ запустить Ansible — использовать pip.

```bash
pip3 install ansible
```

После установки убедитесь, что Ansible работает.

```bash
ansible --version
```