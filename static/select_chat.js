// select_chat.js

document.querySelectorAll('.chat').forEach(function(chat) {
  chat.addEventListener('click', function() {
    let chatId = this.dataset.chatId;
    window.location.href = '/mychat/chat/' + chatId + '/';
  });
});
