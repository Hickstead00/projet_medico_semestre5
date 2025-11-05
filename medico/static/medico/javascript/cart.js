document.addEventListener('DOMContentLoaded', function() {
    const cartButton = document.getElementById('floating-cart');
    if (!cartButton) return;

    const cartRect = cartButton.getBoundingClientRect();
    const initialTop = window.pageYOffset + cartRect.top;
    
    const placeholder = document.createElement('div');
    placeholder.style.width = cartRect.width + 'px';
    placeholder.style.height = cartRect.height + 'px';
    placeholder.style.display = 'none';
    cartButton.parentNode.insertBefore(placeholder, cartButton);

    function updateCartPosition() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > initialTop) {
            if (!cartButton.classList.contains('is-fixed')) {
                cartButton.classList.add('is-fixed');
                placeholder.style.display = 'block';
            }
        } else {
            if (cartButton.classList.contains('is-fixed')) {
                cartButton.classList.remove('is-fixed');
                placeholder.style.display = 'none';
            }
        }
    }

    window.addEventListener('scroll', updateCartPosition);
    
    updateCartPosition();
});