/*добавление строки к таблице*/
function addLineTMainTable(){
	el = document.getElementsByClassName('mainTable')[0];
	var mainTBody;
	if(!el)
	console.log("Ошибка поиска таблицы!");
	else {
		mainTBody=el.querySelector('tbody');
		mainTBody.insertRow(-1);
	}
}
/*wp load script*/
addLineTMainTable();