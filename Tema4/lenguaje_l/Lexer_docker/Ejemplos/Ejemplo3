# Ejemplo 3: incluye un caracter no valido (&) para mostrar deteccion de error lexico
FROM ubuntu:22.04
RUN apt-get update & apt-get install -y curl
ENV APP_HOME=/opt/app
WORKDIR $APP_HOME
CMD ["bash"]
