
// select_common_chat.js

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.chat-link').forEach(function(chatLink) {
        chatLink.addEventListener('click', function() {
            let chatId = this.dataset.chatId; // Access data-chat-id directly

            // Redirect to the chat page with the chatId
            window.location.href = '/mychat/chat/' + chatId + '/';
        });
    });
});
