
function initiate(){
var list1=document.getElementById('district');

list1.options[0] = new Option('--Select--', '');
list1.options[1] = new Option('Pune', 'Pune');
list1.options[2] = new Option('Thane', 'Thane');
list1.options[3] = new Option('Nashik','Nashik');
list1.options[4] = new Option('Aurangabad','Aurangabad');
}
function getTaluka(){
    var list1=document.getElementById('district');
	var list2=document.getElementById('taluka');
	var list1SelectedItem=list1.options[list1.selectedIndex].value;
	
	if(list1SelectedItem=='Pune')
	{
		list2.options.length=0;
		list2.options[0] = new Option('--Select--', '');
		list2.options[1] = new Option('Haveli','Haveli');
		list2.options[2] = new Option('Puneshahar','Puneshahar');
		list2.options[3] = new Option('Khed','Khed');
		list2.options[4] = new Option('Baramati','Baramati');
	}
	else if(list1SelectedItem=='Thane')
	{
		list2.options.length=0;
		list2.options[0] = new Option('--Select--', '');
		list2.options[1] = new Option('Kalyan','Kalyan');
		list2.options[2] = new Option('Thane','Thane');
		list2.options[3] = new Option('Ulhasnagar','Ulhasnagar');
		list2.options[4] = new Option('Bhivandi','Bhivandi');
	}
	else if(list1SelectedItem=='Nashik')
	{
		list2.options.length=0;
		list2.options[0] = new Option('--Select--', '');
		list2.options[1] = new Option('Igatpuri','Igatpuri');
		list2.options[2] = new Option('Chandwad','Chandwad');
		list2.options[3] = new Option('Niphad','Niphad');
		list2.options[4] = new Option('Nashik','Nashik');
	}
	else if(list1SelectedItem=='Aurangabad')
	{
		list2.options.length=0;
		list2.options[0] = new Option('--Select--', '');
		list2.options[1] = new Option('Silod','Silod');
		list2.options[2] = new Option('Paithan','Paithan');
		list2.options[3] = new Option('Khutabad','Khutabad');
		list2.options[4] = new Option('Aurangabad','Aurangabad');
	}
}
function getVillage(){
    var list2=document.getElementById('taluka');
	var list3=document.getElementById('village');
	var list2SelectedItem=list2.options[list2.selectedIndex].value;
	
	if(list2SelectedItem=='Haveli')
	{   
        list3.options.length=0;
		list3.options[0] = new Option('--Select--', '');
		list3.options[1] = new Option('Alandi','Alandi');
		list3.options[2] = new Option('Akurdi','Akurdi');
		list3.options[3] = new Option('Dighi','Dighi');
		list3.options[4] = new Option('Katraj','Katraj');
		list3.options[5] = new Option('Kothrud','Kothrud');
	}
	else if(list2SelectedItem=='Puneshahar')
	{
		list3.options.length=0;
		list3.options[0] = new Option('--Select--', '');
		list3.options[1] = new Option('Aundh','Aundh');
		list3.options[2] = new Option('Yerawada','Yerawada');
		list3.options[3] = new Option('Ghorpadi','Ghorpadi');
		list3.options[4] = new Option('Mundwa','Mundwa');
	}
	else if(list2SelectedItem=='Kalyan')
	{
		list3.options.length=0;
		list3.options[0] = new Option('--Select--', '');
		list3.options[1] = new Option('Aane','Aane');
		list3.options[2] = new Option('Katai','Katai');
		list3.options[3] = new Option('Ankhar','Ankhar');
		list3.options[4] = new Option('Aayre','Aayre');
	}
	else if(list2SelectedItem=='Thane')
	{
		list3.options.length=0;
		list3.options[0] = new Option('--Select--', '');
		list3.options[1] = new Option('Aeroli','Aeroli');
		list3.options[2] = new Option('Kopri','Kopri');
		list3.options[3] = new Option('Kashi','Kashi');
		list3.options[4] = new Option('Khari','Khari');
	}
	else if(list2SelectedItem=='Nashik')
	{
		list3.options.length=0;
		list3.options[0] = new Option('--Select--', '');
		list3.options[1] = new Option('Odha','Odha');
		list3.options[2] = new Option('Trumbak','Trumbak');
		list3.options[3] = new Option('Anandvalli','Anandvalli');
		list3.options[4] = new Option('Kalvi','Kalvi');
	}
	else if(list2SelectedItem=='Niphad')
	{
		list3.options.length=0;
		list3.options[0] = new Option('--Select--', '');
		list3.options[1] = new Option('Ozher','Ozher');
		list3.options[2] = new Option('Oune','Oune');
		list3.options[3] = new Option('Ourangpur','Ourangpur');
		list3.options[4] = new Option('Khede','Khede');
	}
	else if(list2SelectedItem=='Paithan')
	{
		list3.options.length=0;
		list3.options[0] = new Option('--Select--', '');
		list3.options[1] = new Option('Alipur','Alipur');
		list3.options[2] = new Option('Anandpur','Anandpur');
		list3.options[3] = new Option('Katpur','Katpur');
		list3.options[4] = new Option('Ghari','Ghari');
	}
	else if(list2SelectedItem=='Aurangabad')
	{
		list3.options.length=0;
		list3.options[0] = new Option('--Select--', '');
		list3.options[1] = new Option('Kahnapur','Kahnapur');
		list3.options[2] = new Option('Karmad','Karmad');
		list3.options[3] = new Option('Aykod','Aykod');
		list3.options[4] = new Option('Karodi','Karodi');
	}
}