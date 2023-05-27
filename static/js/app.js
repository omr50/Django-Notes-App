// make the message go away after a while.

let message_timeout = document.getElementById('login-message-timer')


setTimeout(function()
 {
    message_timeout.style.display = "none";
}, 2500)


let contents = document.querySelectorAll("#note-content")
for (let i = 0; i < contents.length; i++){
    console.log(contents[i].innerHTML.length, 'aaaaa')
    if (contents[i].innerHTML.length > 100){
        contents[i].innerHTML = contents[i].innerHTML.substring(0, 100) + '...'
    }
}

