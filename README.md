# vfour
vFour

## Installations

 - `pip install django-bootstrap4` 
 - `pip install mysqlclient` 

  

## Commands

 - `python manage.py create job_groups_and_permissions` 
 - `python manage.py collectstatic` 

  

## SQL

 - `CREATE SCHEMA VFOUR` 

  

## Django REST Framework

 - https://www.django-rest-framework.org/
 - `pip install djangorestframework` 
 - `pip install markdown` 
 - `pip install django-filter` 
 - Add `'rest_framework'` to your `INSTALLED_APPS` setting
 - Add `url(r'^api-auth/', include('rest_framework.urls'))` in `urlpatterns` of `urls.py` 
 - Add below code snippet into `settings.py` 

    REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
    }

