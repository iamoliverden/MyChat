// create_chatroom.js

document.getElementById('create-chatroom-form').addEventListener('submit', function(e) {
  e.preventDefault();
  let chatroomName = document.getElementById('chatroom-name').value;
  fetch('/create_chatroom/', {
    method: 'POST',
    body: JSON.stringify({chatroom_name: chatroomName}),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    credentials: 'same-origin'
  })
  .then(response => response.json())
  .then(data => {
    // Update the chatroom list with the new chatroom
    let chatroomList = document.getElementById('chatroom-list');
    let newChatroom = document.createElement('li');
    newChatroom.textContent = data.chatroom_name;
    chatroomList.appendChild(newChatroom);
  })
  .catch(error => console.error('Error:', error));
});

document.getElementById('join-chatroom-button').addEventListener('click', function(e) {
  e.preventDefault();
  let chatroomId = e.target.dataset.chatroomId;
  fetch('/join_chatroom/', {
    method: 'POST',
    body: JSON.stringify({chatroom_id: chatroomId}),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    credentials: 'same-origin'
  })
  .then(response => response.json())
  .then(data => {
    // Handle successful join
    if (data.success) {
      alert('Successfully joined chatroom!');
    } else {
      alert('Failed to join chatroom.');
    }
  })
  .catch(error => console.error('Error:', error));
});
