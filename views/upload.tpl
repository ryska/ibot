<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="static/main.css">
    <title>InstaBot</title>
</head>
<body>
% include('navbar.tpl')
<div class="container upload-container">
    <h4>Yay! We successfully uploaded a photo to our Instagram!</h4>
    <p>Check it <a href="http://instagram.com/urbanshot__">here!</a></p>
    <p>We used most popular Instagram hashtags: </p>
    <ul class="hashtag-list">
      % for i in tag_lists:
        <li>#{{i}},</li>
      % end
    </ul>
</div>

</body>
</html>
