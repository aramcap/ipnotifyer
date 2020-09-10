# IP Notifyer

Script en Python3 que notifica el cambio de IP pública.

En la primera ejecución almacena en `/tmp` un archivo con la IP actual, y las posteriores ejecuciones realiza una comparación enviando un email únicamente cuando esta ha cambiado.

1. Descarga el repositorio:
```sh
cd /opt
git clone https://github.com/aramcap/ipnotifyer.git
chmod +x /opt/ipnotifyer/ipnotifyer.py
```

2. Edita el archivo `ipnotifyer.py` para establecer los valores del servidor SMTP.

3. Crea una entrada de `crontab` para que se ejecute periódicamente:
```sh
* * * * * /opt/ipnotifyer/ipnotifyer.py
```

---

Python3 script to notify public IP changes.

First execution save current IP on `/tmp`, then next executions it checks and sends email if IP changes.

1. Download repository:
```sh
cd /opt
git clone https://github.com/aramcap/ipnotifyer.git
chmod +x /opt/ipnotifyer/ipnotifyer.py
```

2. Edit the file `ipnotifyer.py` to set SMTP server configuration.

3. Set entry on  `crontab` to auto execute:
```sh
* * * * * /opt/ipnotifyer/ipnotifyer.py
```