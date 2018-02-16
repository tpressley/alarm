<head>
    <script type="text/javascript" rel="script" src="scripts/alarm.js"></script>
</head>
<body>
<p>
    Enter the time for the alarm below:
</p>
<form name="alarm-form" action="" method="post">
    <input type="time" id="time-selection" name="target-time">
    <input type="submit">
</form>
<?php
$my_file = 'alarm.txt';
$handle = fopen($my_file, 'w') or die('Cannot open file:  ' . $my_file);
fwrite($handle, $_POST["target-time"]);
?>
</body>