<!DOCTYPE html>
<html>
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
</body>
</html>

