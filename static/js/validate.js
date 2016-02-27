function validate() {
  var submit = document.querySelector('#submit');
  var fname = document.querySelector('#fname');
  var lname = document.querySelector('#lname');
  var age = document.querySelector('#age');
  var userId = document.querySelector('#userid');

  var pattern_name = /^[A-Za-z\s]+$/;
  var pattern_age = /^[0-9]{1,2}$/;

  var randomId = Math.floor(Math.random() * (99999999 - 10000000 + 1)) + 10000000;
  userId.value = randomId;

  return pattern_age.test(age.value) && pattern_name.test(lname.value) && pattern_name.test(fname.value);
}
