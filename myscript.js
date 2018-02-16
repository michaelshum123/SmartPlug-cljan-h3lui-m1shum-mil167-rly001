function load() {
      var mydata = JSON.parse(data);
      var table = document.getElementById('theTable');
      for( var i = 0; i < mydata.length; i++ ) {
        var tr = document.createElement('tr');
        var one = mydata[i];
        for(var j = 0; j < 5; j++) {
          var td = document.createElement('td');
          td.textContent = one[j];
          tr.appendChild(td);
        }
        table.appendChild(tr);
      }

}


