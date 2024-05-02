// script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function() {
  $("#btn_translate").click(function() {
    const languageCode = $("#language_code").val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.getJSON(url, function(data) {
      const translation = data.hello;
      $("#hello").text(translation);
    });
  });
});