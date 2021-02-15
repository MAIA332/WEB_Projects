
<?php

session_start();

if ($_SESSION['executa'] == true){
$comando = escapeshellcmd('C:/xampp/htdocs/PythonToPhp/laboratorioExtract.py');
$cmdResult = shell_exec($comando);
echo $cmdResult;
$_SESSION['executa'] = false;
header("Refresh: 0; url=testePYTHON.php");
}

?>

<a href="createsession.php">EXECUTA</a>
