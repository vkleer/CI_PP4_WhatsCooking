// Sets a timer for Django messages - disappear after 4 seconds
// Taken from 'I Think Therefore I Blog' project from Code Institute
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);