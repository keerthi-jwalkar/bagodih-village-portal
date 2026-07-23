document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("complaintForm");
    const imageInput = document.getElementById("image");
    const fileName = document.getElementById("file-name");

    // Show selected image name
    imageInput.addEventListener("change", function () {

        if (this.files.length > 0) {
            fileName.textContent = this.files[0].name;
        } else {
            fileName.textContent = "No file selected";
        }

    });

    // Form validation
    form.addEventListener("submit", function (e) {

        const name = document.getElementById("name").value.trim();
        const mobile = document.getElementById("mobile").value.trim();
        const ward = document.getElementById("ward").value.trim();
        const category = document.getElementById("category").value;
        const description = document.getElementById("description").value.trim();

        if (
            name === "" ||
            mobile === "" ||
            ward === "" ||
            category === "" ||
            description === ""
        ) {
            alert("Please fill all required fields.");
            e.preventDefault();
            return;
        }

        if (!/^[0-9]{10}$/.test(mobile)) {
            alert("Please enter a valid 10-digit mobile number.");
            e.preventDefault();
            return;
        }

    });

});