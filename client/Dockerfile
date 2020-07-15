FROM node:lts-alpine

RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY ./package*.json ./


# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 80
CMD [ "node", "server.js" ]


##############


# develop stage
#FROM node:11.1-alpine as develop-stage
#WORKDIR /app
#COPY package*.json ./
#
#RUN apk add --no-cache --virtual .gyp \
#        python \
#        make \
#        g++ \
#    && npm install \
#    && apk del .gyp
#
#
##RUN npm install
#COPY . .
## build stage
#FROM develop-stage as build-stage
#RUN npm run build
## production stage
#FROM nginx:1.15.7-alpine as production-stage
#COPY --from=build-stage /app/dist /usr/share/nginx/html
#EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]
