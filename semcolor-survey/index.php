<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Survey of SEMColor</title>
    <link type="text/css" href="./bootstrap-responsive.css" rel="stylesheet">
    <link type="text/css" href="./bootstrap.css" rel="stylesheet">
    <link href="image-picker.css" type="text/css" rel="stylesheet">
    <script src="jquery-3.4.1.min.js"></script>
    <script src="image-picker.js"></script>
    <style>
        body{
            padding: 10pt;
        }
    </style>
</head>
<body>
<label id="result" style="font-size:20pt;text-align: center;"></label>

<?php
$dir = glob("imgs/*/*g");
// 0~31 is gt
// 32~63 is nst
// 64~96 is end2end
$dir_gt = array_slice($dir, 0, 32);
$dir_nst = array_slice($dir, 32, 32);
$dir_end2end = array_slice($dir, 64, 32);

$key_gt = array_rand($dir_gt, 16);
$key_nst = array_rand($dir_nst, 16);
$key_end2end = array_rand($dir_end2end, 16);

$gt = array();
foreach($key_gt as $key){
    array_push($gt, $dir_gt[$key]);
}
$nst = array();
foreach($key_nst as $key){
    array_push($nst, $dir_nst[$key]);
}

$end2end = array();
foreach($key_end2end as $key){
    array_push($end2end, $dir_end2end[$key]);
}

$gt_nst = array_merge($gt, $nst);
$gt_end2end = array_merge($gt, $end2end);
shuffle($gt_nst);
shuffle($gt_end2end);

if ($_GET['type'] == 'nst'){
    $paths = $gt_nst;
} else if ($_GET['type'] == 'end2end') {
    $paths = $gt_end2end;
} else{
    echo("<h1 style='color:red'>'type' parameter must be 'nst' or 'end2end'</h1>");
    exit();
}


$limit = 16;

?>
<h1>Please select <?php echo $limit;?> images, which you think colorized by AI</h1>
<select class="image-picker show-html" multiple="multiple" data-limit="<?php echo $limit?>">
    <?php foreach($paths as $path){?>
    <option data-img-src='<?php echo $path;?>' value='<?php echo $path;?>'></option>
    <?php }?>
</select>
<label id='score' style="display:none">calculating your score...</label>
<button onclick="summary()" class="btn btn-block btn-large">Submit</button>
<script>
    $("select.image-picker").imagepicker({});
    summary = function(){
        values = $("select").data('picker').selected_values();
        if (values.length != <?php echo $limit?>){
            alert("You should select 16 images, but now only "+values.length);
            exit();
		}
        $("ul.thumbnails.image_picker_selector").hide(1);
        $("h1").hide(1);
		$("#score").css('display', 'inline');
        ans = 0;
        for(let i=0; i<values.length; i++){
            if (values[i].indexOf('gt') == -1)ans++;
        }
		score = ans/<?php echo sizeOf($gt_nst)/2.0;?>;
        $("button").hide(1);
		post(score);
    };

	function post(s){
		$.post("score.php", {score:s, type:"<?php echo $_GET['type'];?>"},function(data) {
			console.log(data);
			if (data==1){
				$("#result").text("Hey Bro, Your score: "+s);
				$("#score").css('display', 'none');
			}
		});
	}

</script>
</body>
</html>
