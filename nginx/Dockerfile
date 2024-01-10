FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf


#RUN export PORT_DJANGO_INTERNAL=${PORT_DJANGO_INTERNAL}
#RUN export PORT=${PORT}
#RUN envsubst "\${PORT_DJANGO_INTERNAL},\${PORT}" < nginx.conf > /etc/nginx/conf.d
ADD staticfiles /staticfiles
COPY nginx.conf /etc/nginx/conf.d