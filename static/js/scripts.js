// Emailjs:
console.log("Hello");

function sendMail(contactForm) {
    emailjs.send("service_neix638", "recipe_box", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("Success", response.status, response.text);
        },
        function(error) {
            console.log("Failed", error);
        });
}
