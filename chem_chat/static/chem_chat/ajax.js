/*
ajax用プログラム
*/

function smiles_request(element, data) {
    var xmlHttpRequest = new XMLHttpRequest();
    xmlHttpRequest.onreadystatechange = function() {
        recieveResult(xmlHttpRequest, elements)
    };
    xmlHttpRequest.open("POST", elements["url"], true);
	xmlHttpRequest.setRequestHeader("Content-Type",
            "application/x-www-form-urlencoded");
    xmlHttpRequest.send(data);

}

function recieveResult(xmlHttpRequest, elements) {
	var result = elements["result"];
	if (xmlHttpRequest.readyState == 4 && xmlHttpRequest.status == 200) {
		var response = JSON.parse(xmlHttpRequest.responseText);
		// result.style.color = "red";
		result.textContent = response.smiles;
	}
}