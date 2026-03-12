// Function to search through the 'postedItems' page to filter the results shown

document.addEventListener("DOMContentLoaded", function () {
    // Create useable variables
    const searchInput = document.getElementById("postedItemsSearch");
    const rows = document.querySelectorAll(".searchable-row");
    const noResultsMessage = document.getElementById("noResultsMessage");

    searchInput.addEventListener("keyup", function () {
        // Parse trim search param
        const searchValue = searchInput.value.toLowerCase().trim();
        let visibleRows = 0;

        rows.forEach(function (row) {
            const rowText = row.textContent.toLowerCase();

            // Any part of search param to be included in the rows from DB
            if (rowText.includes(searchValue)) {
                row.style.display = "";
                visibleRows++;

            } else {
                row.style.display = "none";
            }
        });

        // Display message if no results are found
        if (visibleRows === 0) {
            noResultsMessage.style.display = "block";
        } else {
            noResultsMessage.style.display = "none";
        }
    });
});