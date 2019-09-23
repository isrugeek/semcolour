<?php
// receive
$post_data = isset($_POST['score'])?$_POST['score']:'';
$type = isset($_POST['type'])?$_POST['type']:'';
if ($post_data != "" && $type != ""){
	echo 1;
} else{
	echo 0;
}
$myfile = fopen("result.txt", "a");
fwrite($myfile, "$type:$post_data,");
fclose($myfile);
?>

