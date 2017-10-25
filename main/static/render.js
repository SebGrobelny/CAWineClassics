
/**
 * ExcellentExport 2.0.3
 * A client side Javascript export to Excel.
 *
 * @author: Jordi Burgos (jordiburgos@gmail.com)
 * @url: https://github.com/jmaister/excellentexport
 *
 */
/*jslint browser: true, bitwise: true, vars: true, white: true */
/*global define, exports, module */

(function (global) {
    'use strict';

var ExcellentExport = (function() {

    function b64toBlob(b64Data, contentType, sliceSize) {
        // function taken from http://stackoverflow.com/a/16245768/2591950
        // author Jeremy Banks http://stackoverflow.com/users/1114/jeremy-banks
        contentType = contentType || '';
        sliceSize = sliceSize || 512;

        var byteCharacters = window.atob(b64Data);
        var byteArrays = [];

        var offset;
        for (offset = 0; offset < byteCharacters.length; offset += sliceSize) {
            var slice = byteCharacters.slice(offset, offset + sliceSize);

            var byteNumbers = new Array(slice.length);
            var i;
            for (i = 0; i < slice.length; i = i + 1) {
                byteNumbers[i] = slice.charCodeAt(i);
            }

            var byteArray = new window.Uint8Array(byteNumbers);

            byteArrays.push(byteArray);
        }

        var blob = new window.Blob(byteArrays, {
            type: contentType
        });
        return blob;
    }

    var version = "2.0.3";
    var uri = {excel: 'data:application/vnd.ms-excel;base64,', csv: 'data:application/csv;base64,'};
    var template = {excel: '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40"><head><meta name=ProgId content=Excel.Sheet> <meta name=Generator content="Microsoft Excel 11"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--></head><body><table>{table}</table></body></html>'};
    var csvDelimiter = ",";
    var csvNewLine = "\r\n";
    var base64 = function(s) {
        return window.btoa(window.unescape(encodeURIComponent(s)));
    };
    var format = function(s, c) {
        return s.replace(new RegExp("{(\\w+)}", "g"), function(m, p) {
            return c[p];
        });
    };

    var get = function(element) {
        if (!element.nodeType) {
            return document.getElementById(element);
        }
        return element;
    };

    var fixCSVField = function(value) {
        var fixedValue = value;
        var addQuotes = (value.indexOf(csvDelimiter) !== -1) || (value.indexOf('\r') !== -1) || (value.indexOf('\n') !== -1);
        var replaceDoubleQuotes = (value.indexOf('"') !== -1);

        if (replaceDoubleQuotes) {
            fixedValue = fixedValue.replace(/"/g, '""');
        }
        if (addQuotes || replaceDoubleQuotes) {
            fixedValue = '"' + fixedValue + '"';
        }

        return fixedValue;
    };

    var tableToCSV = function(table) {
        var data = "";
        var i, j, row, col;
        for (i = 0; i < table.rows.length; i=i+1) {
            row = table.rows[i];
            for (j = 0; j < row.cells.length; j=j+1) {
                col = row.cells[j];
                data = data + (j ? csvDelimiter : '') + fixCSVField(col.textContent.trim());
            }
            data = data + csvNewLine;
        }
        return data;
    };

    function createDownloadLink(anchor, base64data, exporttype, filename) {
        var blob;
        if (window.navigator.msSaveBlob) {
            blob = b64toBlob(base64data, exporttype);
            window.navigator.msSaveBlob(blob, filename);
            return false;
        } else if(window.URL.createObjectURL) {
            blob = b64toBlob(base64data, exporttype);
            var blobUrl = window.URL.createObjectURL(blob);
            anchor.href = blobUrl;
        } else {
            var hrefvalue = "data:" + exporttype + ";base64," + base64data;
            anchor.download = filename;
            anchor.href = hrefvalue;
        }

        // Return true to allow the link to work
        return true;
    }

    var ee = {
        version: function() {
            return version;
        },
        excel: function(anchor, table, name) {
            table = get(table);
            console.log(table);
            var ctx = {worksheet: name || 'Worksheet', table: table.innerHTML};
            var b64 = base64(format(template.excel, ctx));
            return createDownloadLink(anchor, b64, 'application/vnd.ms-excel','export.xls');
        },
        csv: function(anchor, table, delimiter, newLine) {
            if (delimiter !== undefined && delimiter) {
                csvDelimiter = delimiter;
            }
            if (newLine !== undefined && newLine) {
                csvNewLine = newLine;
            }

            table = get(table);
            var csvData = "\uFEFF" + tableToCSV(table);
            var b64 = base64(csvData);
            return createDownloadLink(anchor,b64,'application/csv','export.csv');
        }
    };

    return ee;
}());

    // AMD support
    if (typeof define === 'function' && define.amd) {
        define(function () { return ExcellentExport; });
    // CommonJS and Node.js module support.
    } else if (typeof exports !== 'undefined') {
        // Support Node.js specific `module.exports` (which can be a function)
        if (typeof module !== 'undefined' && module.exports) {
            exports = module.exports = ExcellentExport;
        }
        // But always support CommonJS module 1.1.1 spec (`exports` cannot be a function)
        exports.ExcellentExport = ExcellentExport;
    } else {
        global.ExcellentExport = ExcellentExport;
    }
})(this);


//Methods I developed //
function renderStillWine(listingDictionary){
	var listings = JSON.parse(listingDictionary);
	console.log(listings);

	var reds = listings[0];

	var temp = document.createElement('div');
	temp.setAttribute("id","temp1");
	// temp.setAttribute("class","container");
	document.getElementById("reds").append(temp);


	//create a properites class that will be used to store property info
	var wines = document.createElement('table');
	wines.setAttribute("id","wines");
	wines.setAttribute("name","usrform");
	// properties.setAttribute("class","attr");

	document.getElementById("temp1").append(wines);

	rowCount = 0;

	var row = wines.insertRow(rowCount);
	colCount = 0;

	for (var header in reds[0])
	{
		var cell = row.insertCell(colCount);
		cell.innerHTML = header.slice(1);

		colCount = colCount + 1;
	}

	rowCount = rowCount+1;

	for (var num in reds)
	{

		//console.log(rowCount);
		colCount = 0;
		var row = wines.insertRow(rowCount);
		for (var base_key in reds[num])
		{
		//	console.log(colCount);
		var cell = row.insertCell(colCount);

			if (colCount == 0){

				var checkbox = document.createElement("INPUT");
				checkbox.name = "check";
				checkbox.type = "checkbox";
				console.log(reds[num]);


				var values = new Array();

				for (var key in reds[num])
				{
					values.push(reds[num][key]);
				}

				console.log(values);
				checkbox.value = values;


			cell.appendChild(checkbox);


			}
			else
			{


			cell.innerHTML = reds[num][base_key];

			
			}

			colCount = colCount +1;


		}
		rowCount = rowCount + 1;

	}




	var whites = listings[1];

	var temp = document.createElement('div');
	temp.setAttribute("id","temp2");
	// temp.setAttribute("class","container");
	document.getElementById("whites").append(temp);


	//create a properites class that will be used to store property info
	var wines = document.createElement('table');
	wines.setAttribute("id","wines");
	wines.setAttribute("name","usrform");
	// properties.setAttribute("class","attr");

	document.getElementById("temp2").append(wines);

	rowCount = 0;

	var row = wines.insertRow(rowCount);
	colCount = 0;

	for (var header in whites[0])
	{
		var cell = row.insertCell(colCount);
		cell.innerHTML = header.slice(1);

		colCount = colCount + 1;
	}

	rowCount = rowCount+1;

	for (var num in whites)
	{

		//console.log(rowCount);
		colCount = 0;
		var row = wines.insertRow(rowCount);
		for (var base_key in whites[num])
		{
		//	console.log(colCount);
		var cell = row.insertCell(colCount);

			if (colCount == 0){

				var checkbox = document.createElement("INPUT");
				checkbox.name = "check";
				checkbox.type = "checkbox";
				console.log(whites[num]);


				var values = new Array();

				for (var key in whites[num])
				{
					values.push(whites[num][key]);
				}

				console.log(values);
				checkbox.value = values;


			cell.appendChild(checkbox);


			}
			else
			{


			cell.innerHTML = whites[num][base_key];

			
			}

			colCount = colCount +1;


		}
		rowCount = rowCount + 1;

	}

}

function renderMain(listingDictionary)
{
	var listings =  JSON.parse(listingDictionary);

	console.log(listings);

	var temp = document.createElement('div');
	temp.setAttribute("id","temp");
	temp.setAttribute("class","container");
	document.getElementById("DBView").append(temp);

		//create a properites class that will be used to store property info
	var contacts = document.createElement('table');
	contacts.setAttribute("id","contacts");
	// properties.setAttribute("class","attr");
	document.getElementById("temp").append(contacts);

	rowCount = 0;

	var row = contacts.insertRow(rowCount);
	colCount = 0;
	for (var header in listings[0])
	{
		var cell = row.insertCell(colCount);
		cell.innerHTML = header;

		colCount = colCount + 1;

	}
	rowCount = rowCount + 1;

	for (var num in listings)
	{

		console.log(rowCount);
		colCount = 0;
		var row = contacts.insertRow(rowCount);
		for (var base_key in listings[num])
		{
			console.log(colCount);
			var cell = row.insertCell(colCount);
			cell.innerHTML = listings[num][base_key];

			colCount = colCount +1;


		}
		rowCount = rowCount + 1;

	}
}



function clearDB(){

	var url = window.location.origin;

	url = url+'/clear_db';

	if(document.getElementById("temp"))
	{
		myNode = document.getElementById("temp")
		myNode.remove(myNode.firstChild)
	}

	function reqListener(){
		console.log(this.responseText)
	}



	//put a request into FLASK
	var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", url);
    oReq.send();




}

var masterList = [];


function obtainSelection()
{
	document.getElementById("request").style.display = "block"; 
	document.getElementById("summary").style.display = "none"; 
	var url = window.location.origin;
	checkboxes = document.getElementsByTagName("input"); 
	console.log(url);
	url = url + '/request';
	
	for (var i = 0; i < checkboxes.length; i++) {
	    var checkbox = checkboxes[i];

	    console.log(checkbox.checked);

	    var temp = [];

	    if (checkbox.checked == true)
	    {
	    	var currentRow = checkbox.parentNode.parentNode;
	    	console.log(currentRow);
	    	
	    	temp.push(currentRow);
	    	masterList.push(temp)
	    }

	    
	   // console.log(masterList)

	} 

	


	// 	function reqListener(){
	// 		console.log(this.responseText);
	renderSelection(masterList);
		
	// 	}



	// //put a request into FLASK
	// var oReq = new XMLHttpRequest();
 //    oReq.addEventListener("load", reqListener);
 //    oReq.open("GET", url);
 //    oReq.send();



}

function renderSelection(masterList)
{

	var requested = document.getElementById("requested")


	console.log(masterList);
	console.log(masterList.length);


	for(var count =0; count < masterList.length; count++)
	{

		var row = requested.insertRow(count);
		console.log(masterList[count][0]);


		// row = masterList[count].innerHTML;
		var tdList = masterList[count][0].getElementsByTagName("td");
		console.log(tdList);
		console.log(tdList.length);
		
		for (var num = 0; num < tdList.length; num++)
		{
			var col = row.insertCell(num);
			console.log(tdList[num]);
			col.innerHTML = tdList[num].innerHTML;
		}
	}
	return true;
}


function obtainStill(){
	var url = window.location.origin;

	url = url + '/still_wine/view';
	console.log("in url render.js");
	console.log(url);
		//if our DB is still there from the last request
	if(document.getElementById("temp"))
		{
			myNode = document.getElementById("temp")
			myNode.remove(myNode.firstChild)
		}

	function reqListener(){
		renderStillWine(this.responseText)
	}



	//put a request into FLASK
	var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", url);
    oReq.send();

}


function obtainDB(){

	var url = window.location.origin;

	url = url + '/contact/view';
		//if our DB is still there from the last request
	if(document.getElementById("temp"))
		{
			myNode = document.getElementById("temp")
			myNode.remove(myNode.firstChild)
		}

	function reqListener(){
		renderMain(this.responseText)
	}



	//put a request into FLASK
	var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", url);
    oReq.send();
}

