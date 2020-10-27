<?php
function endsWith($string, $endString) 
{ 
    $len = strlen($endString); 
    if ($len == 0) { 
        return true; 
    } 
    return (substr($string, -$len) === $endString); 
} 

$i = 1;
if ($handle = opendir('contents')) {
    while (false !== ($file = readdir($handle))) {
        if ($file != "." && $file != "..") {
            $thelist .= '<li><a href="contents/'.$file.'">'.$file.'</a></li>';
        }
        if (endsWith($file, 'stl')){
            $stlTable .= '<tr><th><dir id=stlViewer'.$i.'></dir></th><th><li><a href="contents/'.$file.'">'.$file.'</a></li></th></tr>';
            $stlViewer .= 'var stl_viewer'.$i.'=new StlViewer(document.getElementById("stlViewer'.$i.'"), {models: [{id:0, filename:"contents/'.$file.'"}]});';
            $i += 1;
        }
    }
closedir($handle);
}
?>
