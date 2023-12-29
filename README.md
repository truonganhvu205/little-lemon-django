# Clone project
```bash
git init
git clone https://github.com/truonganhvu205/little-lemon-django.git
cd little-lemon-django
```

## Install pipenv
```bash
pip3 install pipenv
```

## Activate virtual environment
```bash
pipenv --python 3.10
pipenv shell
```

## Install Django & Frameworks
```bash
pipenv install django
pipenv install mysqlclient
pipenv install djangorestframework
pipenv install djoser
```

## Connect to MySQL
```bash
mysql -u root -p
create database reservations;
create user 'adminlittlelemon'@'localhost' identified by 'admin123$%^';
grant all on *.* to 'adminlittlelemon'@'localhost';
flush privileges;
exit
```

# Run server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

<table align='center'>
  <tr align='center'>
    <td>Home</td>
    <td>About</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-website-be/blob/main/little-lemon-be-django-truong-anh-vu-12-28-2023/little-lemon-be-django-truong-anh-vu-12-28-2023-pic-1.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-website-be/blob/main/little-lemon-be-django-truong-anh-vu-12-28-2023/little-lemon-be-django-truong-anh-vu-12-28-2023-pic-2.png' />
    </td>
  </tr>
</table>

<table align='center'>
  <tr align='center'>
    <td>Menu</td>
    <td>Menu item</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-website-be/blob/main/little-lemon-be-django-truong-anh-vu-12-28-2023/little-lemon-be-django-truong-anh-vu-12-28-2023-pic-3.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-website-be/blob/main/little-lemon-be-django-truong-anh-vu-12-28-2023/little-lemon-be-django-truong-anh-vu-12-28-2023-pic-4.png' />
    </td>
  </tr>
</table>

<table align='center'>
  <tr align='center'>
    <td>Before Booking</td>
    <td>After Booking</td>
    <td>All Reservations</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-website-be/blob/main/little-lemon-be-django-truong-anh-vu-12-28-2023/little-lemon-be-django-truong-anh-vu-12-28-2023-pic-5.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-website-be/blob/main/little-lemon-be-django-truong-anh-vu-12-28-2023/little-lemon-be-django-truong-anh-vu-12-28-2023-pic-6.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-website-be/blob/main/little-lemon-be-django-truong-anh-vu-12-28-2023/little-lemon-be-django-truong-anh-vu-12-28-2023-pic-7.png' />
    </td>
  </tr>
</table>
