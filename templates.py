<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to my Python Website</h1>
    <p>This site is made with Flask and PyCharm.</p>
</body>
</html>
services:
  - type: web
    name: flask-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
