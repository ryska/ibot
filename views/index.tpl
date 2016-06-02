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
    <div class="row">
        <div class="col m6">
            <h2>Getting started</h2>
            <p>Lorem Ipsum è un testo segnaposto utilizzato nel settore della tipografia e della stampa. Lorem Ipsum è considerato il testo segnaposto standard sin dal sedicesimo secolo, quando un anonimo tipografo prese una cassetta di caratteri e li assemblò per preparare un testo campione</p>
        </div>
        <div class="col m6">
            <h2 class="center-align">Login</h2>
            <div class="row">
                <form class="col s12">
                    <div class="row">
                        <div class="input-field col s12">
                            <input id="login" type="text" class="validate">
                            <label for="login">Login</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-field col s12">
                            <input id="pass" type="password" class="validate">
                            <label for="pass">Password</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col s12">
                          <div class="input-field col s12">
                            <select>
                              <option value="" disabled selected >Choose your category</option>
                              <option value="1">Option 1</option>
                              <option value="2">Option 2</option>
                              <option value="3">Option 3</option>
                            </select>
                            <label>Categories</label>
                          </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col m12">
                            <p class="right-align">
                                <a class="waves-effect waves-light btn-large start-btn start" href="{{url}}">Let's start!</a>
                                <!-- <button class="btn btn-large waves-effect waves-light" type="button" name="action">Login</button> -->
                            </p>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
<!-- <div class="container">
    <h1>Hello!</h1>
    <h2> Welcome to our app!</h2>
    <a class="waves-effect waves-light btn-large start-btn" href="{{url}}">Let's start!</a>
</div> -->

<script src="../static/jquery-1.12.3.min.js"></script>
<script src="../static/materialize.min.js"></script>
<script src="../static/main.js"></script>
</body>
</html>
