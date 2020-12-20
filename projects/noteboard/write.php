<?php
function writeNotes($notes){
    $fp = fopen('notes.txt', 'a') or die('unable to open file');
    fwrite($fp, $notes."\n");
    fclose($fp);
}
writeNotes($_POST['notes']);
echo $_POST['notes'];
?>
