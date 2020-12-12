function exportToExcel(tableID, filename = ''){
  var downloadurl;
  var dataFileType = 'application/vnd.ms-excel';
  var tableSelect = document.getElementById(tableID);
  var tableHTMLData = tableSelect.outerHTML.replace(/ /g, '%20');
 
  // Specify file name
  filename = filename?filename+'.xls':'export_excel_data.xls';
 
  // Create download link element
  downloadurl = document.createElement("a");
 
  document.body.appendChild(downloadurl);
 
  if(navigator.msSaveOrOpenBlob){
      var blob = new Blob(['\ufeff', tableHTMLData], {
          type: dataFileType
      });
      navigator.msSaveOrOpenBlob( blob, filename);
  }else{
      // Create a link to the file
      downloadurl.href = 'data:' + dataFileType + ', ' + tableHTMLData;
 
      // Setting the file name
      downloadurl.download = filename;
     
      //triggering the function
      downloadurl.click();
  }
}


  function exportToDOC(tableID, filename = ''){
    var downloadurl;
    var dataFileType = 'application/vnd.ms-doc';
    var tableSelect = document.getElementById(tableID);
    var tableHTMLData = tableSelect.outerHTML.replace(/ /g, '%20');
   
    // Specify file name
    filename = filename?filename+'.doc':'export_doc_data.doc';
   
    // Create download link element
    downloadurl = document.createElement("a");
   
    document.body.appendChild(downloadurl);
   
    if(navigator.msSaveOrOpenBlob){
        var blob = new Blob(['\ufeff', tableHTMLData], {
            type: dataFileType
        });
        navigator.msSaveOrOpenBlob( blob, filename);
    }else{
        // Create a link to the file
        downloadurl.href = 'data:' + dataFileType + ', ' + tableHTMLData;
   
        // Setting the file name
        downloadurl.download = filename;
       
        //triggering the function
        downloadurl.click();
    }
  }

