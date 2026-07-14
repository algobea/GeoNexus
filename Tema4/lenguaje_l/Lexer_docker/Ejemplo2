# Ejemplo 2: Dockerfile multi-etapa con ARG, ENV, USER y VOLUME
ARG VERSION=1.0
FROM node:18-alpine AS build
WORKDIR /usr/src/app
COPY package.json /usr/src/app
RUN npm install

FROM node:18-alpine
LABEL maintainer="equipo-devops"
ENV NODE_ENV=production
USER node
VOLUME /data
COPY --from=build /usr/src/app /usr/src/app
ENTRYPOINT ["node", "server.js"]
