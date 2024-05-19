document.addEventListener('DOMContentLoaded', function() {
    const wishMessagesContainer = document.getElementById('wish-messages');
    
    // Get wishes from localStorage
    const wishes = JSON.parse(localStorage.getItem('wishes')) || [];
    
    // Render wishes
    wishes.forEach(wish => {
        const wishMessage = document.createElement('div');
        wishMessage.classList.add('wish');
        wishMessage.innerHTML = `<strong>${wish.name}:</strong> <p>${wish.message}</p>`;
        
        wishMessagesContainer.appendChild(wishMessage);
    });
});