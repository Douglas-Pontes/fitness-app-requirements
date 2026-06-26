# Site estatico das apresentacoes do Vela (servido por Nginx).
# Tudo que estiver em apresentacoes/ fica acessivel publicamente.
FROM nginx:alpine

# Config do Nginx (com autoindex para listar os arquivos da pasta)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copia apenas a pasta de apresentacoes para a raiz servida
COPY apresentacoes/ /usr/share/nginx/html/

EXPOSE 80
