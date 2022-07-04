Test Program for using nginx and gunicorm with local setup

## Commands and Explantion

sudo nginx -t : check nginx syntax for errors
sudo nginx start: start nginx server using config
sudo ngoinx stop: stop server
sudo service nginx restart: retart server


gunicorn django_pos.wsgi:application -b :8001 : start gunicorn server on post 8001 using gunicorn as reverse proxy
sudo nano  /etc/nginx/sites-enabled/example:  create nginx config file in folder

configuration: 

server {
    listen localhost:8000; main host address which nginx will listen on

    location / {
        proxy_pass http://127.0.0.1:8001; # Any requests that is ending with / is going to be passed to Gunicorn which is listening at port 8001
    }

    # statix file location when running python manage.py collectstatic

    location /static/ {

        alias /home/zahur76/django_pos_linux/staticfiles/;
    }


    location /media/ {

       alias /home/zahur76/django_pos_linux/media/;

    }

}