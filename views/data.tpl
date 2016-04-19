<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="static/main.css">
    <link rel="stylesheet" type="text/css" href="static/materialize.css">
    <title>InstaBot</title>
</head>
<body>
% include('navbar.tpl')
<ul>
   <ul>
  % for item in tag_lists:
    <li>{{item}}</li>
  % end
</ul>
</ul>
</body>
</html>