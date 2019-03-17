FROM node:10-alpine
MAINTAINER Bryan Hyshka <bryan@hyshka.com>

# Prefix path with global node_modules folder
# This allows npm package binaries to be available everywhere
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# Set variable that we use in our webpack config to detect
# that we're running the stack inside of Docker
ENV VIRTUAL_ENV docker

# Update, install, and cleanup
RUN apk update \
    && apk add bash \
    && rm -rf /var/cache/apk/*

# Add the project requirements
# This will add the package.json and package-lock.json if it exists
ADD package*.json /usr/src/app/

# Install the requirements
RUN /bin/bash -c 'cd /usr/src/app && npm install && npm cache clean --force'

# The code should be symlinked to this directory
WORKDIR /usr/src/app

# Expose the 3000 port
EXPOSE 3000
