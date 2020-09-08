<?php
  if ($handle = opendir('contents')) {
    while (false !== ($file = readdir($handle))) {
      if ($file != "." && $file != "..") {
        $thelist .= '<li><a href="contents/'.$file.'">'.$file.'</a></li>';
      }
    }
    closedir($handle);
  }
?>
