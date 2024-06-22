// script.js

document.addEventListener("DOMContentLoaded", function() {
  let url = `ws://${window.location.host}/ws/socket-server/`;

  const chatSocket = new WebSocket(url);

  let senderName = localStorage.getItem('senderName');
  if (!senderName) {
    localStorage.setItem('senderName', senderName);
  }

  chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    console.log('Data:', data);

if (data.type === 'chat') {
  let date = new Date();
  let timestamp = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;  // Generate the timestamp in YYYY-MM-DD format
  let messages = document.getElementById('messages')
  let cssClass = data.sender === senderName? 'sender' : 'receiver';
  messages.insertAdjacentHTML('beforeend', `<div class="${cssClass}">
  <p>@${data.sender} ${timestamp}: ${data.message}</p>
</div>`)
}
  }
  let form = document.getElementById('form')
  form.addEventListener('submit', (e) => {
    e.preventDefault()
    let message = e.target.message.value
    let chatId = window.location.pathname.split('/')[3];
    chatSocket.send(JSON.stringify({
      'message': message,
      'sender': senderName,
      'chat_id': chatId,
    }))
    form.reset()
  })
});