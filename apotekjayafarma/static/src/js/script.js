// $(document).ready(function() {
//     // Add click event listener to the "Simpan" button
//     $("#btn_import_obat").click(function() {
//         var obat_id = $("input[name='obat_id']").val();
//         var jumlah = $("input[name='jumlah']").val();
        
//         // Send AJAX request to create a new obat record
//         $.ajax({
//             url: "/importobat/create",
//             type: "POST",
//             data: {
//                 obat_id: obat_id,
//                 jumlah: jumlah,
//             },
//             dataType: "json",
//             success: function(data) {
//                 // Log the success message
//                 console.log("Obat berhasil diimport: " + JSON.stringify(data));
                
//                 // Clear the input fields
//                 $("input[name='obat_id']").val("");
//                 $("input[name='jumlah']").val("");
                
//                 // Create a new row in the table with the new obat data
//                 var newRow = $("<tr>");
//                 newRow.append($("<td>").text(data.obat_id));
//                 newRow.append($("<td>").text(data.jumlah));
//                 $("table tbody").append(newRow);
//             },
//             error: function(xhr, status, error) {
//                 console.error(error);
//             }
//         });
//     });
// });
