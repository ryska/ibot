
  $(document).ready(function() {
    $('select').material_select();


  });
  $('#loginButton').on('click',function(){
    var login = $('#login').val();
    var password = $('#pass').val();
    var category = $('#category').val();

    console.log(login, password, category);
  });
