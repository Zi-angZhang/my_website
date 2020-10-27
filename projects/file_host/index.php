<!DOCTYPE html>
<html>
<head>
<script type="text/javascript" src='stl_viewer.min.js'></script>
<style type="text/css">
table, th, td {
border: 1px solid black;
}
</style>
</head>
<body>
    <h1>hosted files</h1>
<?php include 'folderscan.php';?>
<?php
    echo $thelist;
?>
<h3>upload</h3>
<form action="upload.php" method="post" enctype="multipart/form-data">
  <input type="file" name="fileToUpload" id="fileToUpload">
  <input type="submit" value="Upload" name="submit">
</form>
<h2>3d object viewer</h2>
<table style=width:90%>
<tr>
    <th>model</th>
    <th>link</th>
</tr>
<?php
    echo $stlTable;
?>
</table>
<div id='stl_cont'></div>
    <script type="text/javascript">
    <?php
        echo $stlViewer
    ?>
    </script>
</body>
</html>

