# Use the official Nginx image as the base
FROM nginx:latest

# Copy the template file
COPY ./nginx/default.conf.template /etc/nginx/templates/default.conf.template
COPY ./certs/ /var/certs/

# Install envsubst for processing the template
RUN apt-get update && apt-get install -y gettext-base && rm -rf /var/lib/apt/lists/*

# Expose ports
EXPOSE 80 443

# Process the template and start Nginx
CMD ["/bin/bash", "-c", "envsubst < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]