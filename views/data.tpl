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
<div class="container data-container">
    <p>Most popular hashtags on Instagram now:</p>
       <ul class="hashtag-list">
      % for item in tag_lists:
        <li>#{{item}},</li>
      % end
       </ul>
</div>
</body>
</html>