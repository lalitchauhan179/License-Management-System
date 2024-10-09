// validation.js
function validateForm() {
    const licenseInput = document.getElementById('licenseInput').value;

    if (!licenseInput) {
        alert('Please enter a license key');
        return false;
    }

    // Additional validation logic as needed
    return true;
}

// Attach validation to form submission
document.getElementById('licenseForm').addEventListener('submit', function(event) {
    if (!validateForm()) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
