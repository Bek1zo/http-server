#pyinstaller http_server.py --hidden-import=PyQt5.sip -w --add-data "favicon.png:." --icon='favicon.png'

mkdir -p package/opt
mkdir -p package/usr/share/applications
mkdir -p package/usr/share/icons/hicolor/scalable/apps

cp -r dist/http_server package/opt/http_server

cp favicon.png package/usr/share/icons/hicolor/scalable/apps/http_server.png
cp http_server.desktop package/usr/share/applications

find package/opt/http_server -type f -exec chmod 644 -- {} +
find package/opt/http_server -type d -exec chmod 755 -- {} +
find package/usr/share -type f -exec chmod 644 -- {} +
chmod +x package/opt/http_server/http_server

fpm -C package -s dir -t deb -n "http_server" -v 0.1.0 -p http_server.deb