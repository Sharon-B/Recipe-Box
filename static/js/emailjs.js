// Emailjs:
// Code snippet 3: Emailjs Submit form https://www.emailjs.com/docs/tutorial/creating-contact-form/
window.onload = function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        emailjs.sendForm('contact_service', 'contact_form', this)
            .then(function() {
                $('#email-confirm-msg').html("Thank you for your email, we will be in touch.");
            }, function(error) {
                $('#email-confirm-msg').html("There was an error on our side, please try again later.");
            });
            
            // Reset Form data
            document.getElementById("contact-form").reset();
            return false;
    });
};