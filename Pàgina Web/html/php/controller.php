<?php
require "function.php";
if (isset($_REQUEST['funcio'])) {
    switch ($_REQUEST['funcio']) {
        case 'get_info_placa_sensor':
            echo get_info_placa_sensor($_POST['placa']);
            break;
        default:
            break;
    }
}
