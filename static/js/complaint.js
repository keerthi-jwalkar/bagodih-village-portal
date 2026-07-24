document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("complaintForm");

    const uploadBox = document.getElementById("uploadBox");

    const chooseBtn = document.getElementById("chooseBtn");

    const imageInput = document.getElementById("images");

    const previewContainer = document.getElementById("preview-container");

    let selectedFiles = [];



    // ==========================
    // Open File Picker
    // ==========================

    chooseBtn.addEventListener("click", function () {

        imageInput.click();

    });



    // ==========================
    // File Selection
    // ==========================

    imageInput.addEventListener("change", function () {

        addFiles(this.files);

    });



    // ==========================
    // Drag & Drop
    // ==========================

    uploadBox.addEventListener("dragover", function (e) {

        e.preventDefault();

        uploadBox.classList.add("drag");

    });

    uploadBox.addEventListener("dragleave", function () {

        uploadBox.classList.remove("drag");

    });

    uploadBox.addEventListener("drop", function (e) {

        e.preventDefault();

        uploadBox.classList.remove("drag");

        addFiles(e.dataTransfer.files);

    });



    // ==========================
    // Add Files
    // ==========================

    function addFiles(files) {

        for (let file of files) {

            if (selectedFiles.length >= 5) {

                alert("Maximum 5 images allowed.");

                break;

            }

            if (!file.type.match("image/jpeg") &&
                !file.type.match("image/png")) {

                alert(file.name + " is not a JPG or PNG image.");

                continue;

            }

            if (file.size > 5 * 1024 * 1024) {

                alert(file.name + " is larger than 5 MB.");

                continue;

            }

            selectedFiles.push(file);

        }

        updatePreview();

    }



    // ==========================
    // Preview Images
    // ==========================

    function updatePreview() {

        previewContainer.innerHTML = "";

        selectedFiles.forEach(function (file, index) {

            const reader = new FileReader();

            reader.onload = function (e) {

                const card = document.createElement("div");

                card.className = "preview-card";



                card.innerHTML = `

                    <img src="${e.target.result}">

                    <button type="button"
                            class="remove-btn"
                            data-index="${index}">
                        ✖
                    </button>

                `;

                previewContainer.appendChild(card);

            };

            reader.readAsDataURL(file);

        });

        updateInputFiles();

    }



   // ==========================
// Remove Image
// ==========================

previewContainer.addEventListener("click", function (e) {

    if (e.target.classList.contains("remove-btn")) {

        const index = e.target.dataset.index;

        selectedFiles.splice(index, 1);

        updatePreview();

    }

});


// ==========================
// Update File Input
// ==========================

function updateInputFiles() {

    const dataTransfer = new DataTransfer();

    selectedFiles.forEach(function (file) {

        dataTransfer.items.add(file);

    });

    imageInput.files = dataTransfer.files;

}


// ==========================
// Form Validation
// ==========================

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