jQuery(function ($) {
    $("input#nome").val("dadsadasdadasdasdasda");

});

jQuery(function ($) {
    $("#limpar").click(function() {
        $("#form2")[0].reset();

    });
});
jQuery(function($){
$("#form_dados_pessoais2").validate();
});

(function() {
    'use strict';
    window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
    if (form.checkValidity() === false) {
    event.preventDefault();
    event.stopPropagation();
    }
    form.classList.add('was-validated');
    
    });
    }, false);
    })();