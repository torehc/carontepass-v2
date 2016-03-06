CarontePass: Open Access Control
===================
*Access Control for Colaborative Spaces*

CarontePass is an access control designed for collaborative spaces where there is much movement of people and it is impossible that all people have conventional physical key.
**Ideal for Hackerspaces, Makerspace, FabLabs, Hacklabs, etc ...**

 - Open Source
 - Open Hardware
 - Low Cost
 - Easy!

> **Note English:**

> - Project currently in development.
> - From November 2015 changes will be evaluated for the [Free Software University Contest](https://www.concursosoftwarelibre.org).
> - University Student (no time or $)
> 
> **Note Spanish:**

> - Proyecto actuamente en desarrollo.
> - A partir de Noviembre 2015 los cambios realizados serÃ¡n valorados para el [Consurso Universitario de Software Libre 2016.](https://www.concursosoftwarelibre.org)
> -  Estudiante universitario (sin tiempo ni €)

----------
How does it work?:
-------------
The project is based on a **client-server structure**, where you have a single server (In *Raspberry Pi 2*) and customers are the doors.

Clients connect to wifi and establish communication through a REST API made with ***Django*** and ***Django REST framework*** that is in the server. As it is a very delicate service the idea is not to have the server on the Internet but in the local area.

The system creates a URL with the tag received by the reader and asks the server. Checks whether the tag has a user and if you have access permissions (as can be if the current monthly payments) to activate the relay which opens the door.

As a client there is a Raspberry has a **relay** that opens an electronic lock a **reader NFC model RC522**.
Development version: ESP8266 with RC522(rfid/nfc) reader.

Support bots Telegram: When entering the first person into space in a group alerts Telegram which is open and equal to leave.


----------
## Documentation:
(In Spanish at the moment)
[Wiki](http://wiki.kreitek.org/proyectos:control_acceso)
[Blog](https://carontepass.wordpress.com/)

**Web Panel:**
![Login Page](https://carontepass.files.wordpress.com/2016/02/captura-de-pantalla-2016-02-15-14-02-56.png?w=775)
![User Panel](https://carontepass.files.wordpress.com/2016/02/captura-de-pantalla-2016-02-15-14-02-46.png)

**Django DataBase:**
![Database Model](https://carontepass.files.wordpress.com/2016/03/my_models3.png)

**Integration with Telegram Bot:**
![Telegram Bot](https://carontepass.files.wordpress.com/2016/02/captura-de-pantalla-2016-02-29-22-52-02.png)

Technology used:
-------------

 - Python
 - Django 1.9
 - Dango REST framework
 - Bootstrap with AdminLTE theme
 - PyTelegramBotAPI
 (Read more at the web/carontepass/requirements.txt)