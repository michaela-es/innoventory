document.addEventListener('DOMContentLoaded', function() {
    const inputs = form.querySelectorAll('input, select');
    const form = document.getElementById('registerForm');


    // Form validation and submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(form);
        const password = formData.get('password');
        const confirmPassword = formData.get('confirmPassword');

        // Check if passwords match
        if (password !== confirmPassword) {
            alert('Passwords do not match!');
            return;
        }

        // Check password strength
        if (password.length < 6) {
            alert('Password must be at least 6 characters long!');
            return;
        }

        // Simulate form submission
        const submitBtn = form.querySelector('.sign-in-btn');
        const originalText = submitBtn.querySelector('.text-wrapper-5').textContent;

        submitBtn.querySelector('.text-wrapper-5').textContent = 'Signing Up...';
        submitBtn.disabled = true;

        setTimeout(() => {
              alert('Registration successful!');
              submitBtn.querySelector('.text-wrapper-5').textContent = originalText;
              submitBtn.disabled = false;
              form.reset();

          // Reset labels
          inputs.forEach(input => {
                const label = input.parentElement.querySelector('label');
                label.style.transform = 'translateY(0)';
                label.style.fontSize = '20px';
                label.style.color = '#567b8c';
          });
        }, 2000);
 });

  // Login link functionality

    const loginLink = document.querySelector('.text-wrapper-4');
    loginLink.addEventListener('click', function(e) {
        e.preventDefault();
        alert('Redirecting to login page...');
    });
});
