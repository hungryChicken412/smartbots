## Smartbots






WSGIDaemonProcess SMS python-home=/www/brainshell/brainshellEnv python-path=/www/brainshell/smartbots/SMS
WSGIProcessGroup SMS
WSGIScriptAlias / /www/brainshell/smartbots/SMS/SMS/wsgi.py

