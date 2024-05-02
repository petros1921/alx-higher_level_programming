// script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

let url = 'https://swapi.dev/api/people/5/';
$.get(url, function (data, status) {
  $('div#character').text(data.name);
});
