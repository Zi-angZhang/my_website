<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="style.css" rel="stylesheet">
    <title>group calendar</title>
<script type="text/javascript" src="script.js"></script>
</head>
<body>

<!--Make sure the form has the autocomplete function switched off:-->
<form autocomplete="off" action="cal.php" method="post">
  <div class="autocomplete" style="width:300px;">
    <input id="myInput" type="text" name="QName" placeholder="Group member">
  </div>
  <input type="submit">
</form>



<iframe src="https://calendar.google.com/calendar/embed?src=ziang.zhang%40kaust.edu.sa&ctz=Asia%2FRiyadh" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
<script>
var emails = ["Udo Schwingenschlög",
"Duc Tam Ho", "Avijeet Ray", 
"Hao Yu",
"Shubham Tyagi"];
autocomplete(document.getElementById("myInput"), emails);
</script>
</body>
</html>
