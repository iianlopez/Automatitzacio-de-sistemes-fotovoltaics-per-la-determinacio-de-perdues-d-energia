<?php
session_start();
require "mysql.php";


function get_info_placa_sensor($placa)
{
	$bd = new hiperion();

	$dades = $bd->get_info_placa_sensorBD($placa);

	return json_encode($dades);
}

?>