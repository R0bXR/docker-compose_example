Пример сборки приложений с помощью Docker-Compose
=================================================

Установка на Linux (Debian/Ubuntu)
----------------------------------

```sh
cd packages/

sudo dpkg -i containerd.io_1.6.21-1_amd64.deb \
docker-ce_24.0.4-1~debian.11~bullseye_amd64.deb \
docker-ce-cli_24.0.4-1~debian.11~bullseye_amd64.deb \
docker-buildx-plugin_0.11.1-1~debian.11~bullseye_amd64.deb \
docker-compose-plugin_2.19.1-1~debian.11~bullseye_amd64.deb
```

Проверка что Docker работает
----------------------------

```sh
sudo service docker status
```

Небольшое описание
------------------

Сервис `db` -- условная база данных, которая слушает порт 6200/TCP

Сервис `app` -- небольшое приложение которое проверяет доступность
порта базы данных по адресу `db:6200` и возвращает в консоль `Port is open`

Запуск сервисов
---------------

```sh
sudo docker compose up -d # -d запустит контейнеры в автономном режиме
```

Проверка вывода приложения
--------------------------

```sh
sudo docker compose logs -f app # 'app' здесь имя сервиса как в docker-compose.yml
```
