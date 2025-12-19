FROM nginx:alpine

# Créer un utilisateur non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copier le frontend statique
COPY src/ /usr/share/nginx/html/

# Copier la conf Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Donner les droits à l'utilisateur non-root
RUN chown -R appuser:appgroup \
    /usr/share/nginx \
    /var/cache/nginx \
    /var/run

# Exécuter Nginx en non-root
USER appuser

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
