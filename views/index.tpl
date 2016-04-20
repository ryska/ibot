<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="static/main.css">
    <link rel="stylesheet" type="text/css" href="static/materialize.css">
    <title>InstaBot</title>

</head>
<body>
% include('navbar.tpl')
<div class="container">
    <h1>Hello!</h1>
    <h2> Welcome to our app!</h2>
    <a class="waves-effect waves-light btn-large start-btn" href="{{url}}">Let's start!</a>
</div>
<script src="../static/jquery-1.12.3.min.js"></script>
<script src="../static/materialize.min.js"></script>
</body>
</html>