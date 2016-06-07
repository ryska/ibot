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


<div class="container">
    <div class="row">
        <div class="col-sm-6">
            <h2>Getting started</h2>
            <p>Lorem Ipsum è un testo segnaposto utilizzato nel settore della tipografia e della stampa. Lorem Ipsum è considerato il testo segnaposto standard sin dal sedicesimo secolo, quando un anonimo tipografo prese una cassetta di caratteri e li assemblò per preparare un testo campione</p>
        </div>
        <div class="col-sm-6">
            <div class="row">
                <!-- <form class="col-sm-12 user-data form-group">
                    <div class="row">
                        <div class="input-field col-sm-12">
                            <input id="login" type="text" class="validate" required >
                            <label for="login">Login</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-field col-sm-12">
                            <input id="pass" type="password" class="validate" required >
                            <label for="pass">Password</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12">
                          <div class="input-field col-sm-12">
                            <select id="category">
                              <option value="" disabled selected required >Choose your category</option>
                              <option value="1">Option 1</option>
                              <option value="2">Option 2</option>
                              <option value="3">Option 3</option>
                            </select>
                            <label>Categories</label>
                          </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-12">
                            <p class="right-align">
                              <a class="waves-effect waves-light btn-large start-btn start" href="{{url}}">Let's start!</a>
                                <button class="btn btn-large waves-effect waves-light" id="loginButton" type="button" name="action">Login</button>
                            </p>
                        </div>
                    </div>
                </form> -->
                <div class="form-wrap">
                <h1>Log in with your Instagram account</h1>
                    <form role="form" action="javascript:;" method="post" id="login-form" autocomplete="off">
                        <div class="form-group">
                            <input id="login" type="text" class="validate form-control" required  placeholder="Login" >
                        </div>
                        <div class="form-group">
                          <input id="pass" type="password" class="validate form-control" required placeholder="Password" >
                        </div>
                        <!-- <input type="submit" id="btn-login" class="btn btn-custom btn-lg btn-block" value="Log in"> -->
                        <select id="category">
                          <option value="" disabled selected required >Choose your category</option>
                          <option value="1">Option 1</option>
                          <option value="2">Option 2</option>
                          <option value="3">Option 3</option>
                        </select>
                        <a class="waves-effect waves-light btn-large start-btn start" href="{{url}}">Let's start!</a>
                          <button class="btn btn-large waves-effect waves-light" id="loginButton" type="button" name="action">Login</button>
                    </form>

        	    </div>
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
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<!-- <script src="../static/materialize.min.js"></script> -->
<script src="../static/main.js"></script>
</body>
</html>
