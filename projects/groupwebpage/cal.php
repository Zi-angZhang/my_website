<?php
$name = $_POST["QName"];
$emaildict = array(
    "Duc Tam Ho" => "ductam.ho",
    "Avijeet Ray" => "avijeet.ray",
    "Shubham Tyagi" => "shubham.tyagi",
    "Hao Yu" => "hao.yu",
    "Udo Schwingenschlög" =>"udo.schwingenschlogl",
);
$emailadd = $emaildict[$name];
?>
<iframe src="https://calendar.google.com/calendar/embed?src=<?php echo $emailadd;?>%40kaust.edu.sa&ctz=Asia%2FRiyadh" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
