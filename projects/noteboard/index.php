<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>noteboard</title>
</head>
<body>
   <h1>notes</h1>
<ul>
<?php
$fn = fopen('notes.txt', 'r');
while(! feof($fn)){
    $result = fgets($fn);
    echo '<li>'.$result.'</li>';
}
fclose($fn);
?>
<form action="write.php" method="post">
<input type="text" class="text" value="" name="notes">
<input type="submit" value="Submit">
</form>
</ul>
</body>
</html>
