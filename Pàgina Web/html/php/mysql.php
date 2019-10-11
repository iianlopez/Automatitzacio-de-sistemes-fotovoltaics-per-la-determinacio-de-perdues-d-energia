<?php

class bd
{
    protected $conexio;
    # Pi:
    # user = admin
    # pass = 123456
    public function __construct($server = "localhost", $usu = "admin", $pw = "123456", $bd = "Hiperion")
    
    {
        $this->conexio = new mysqli($server, $usu, $pw, $bd);
        $this->conexio->query("SET NAMES 'utf8'");
    }
    public function __destruct()
    {
        $this->conexio->close();
    }
}

class hiperion extends bd
{
    public function __construct()
    {
        parent::__construct();
    }

    public function __destruct()
    {
        parent::__destruct();
    }

    public function get_info_placa_sensorBD($placa)
    {
        $lasql = "select id_dispositiu, data, w from dades where id_dispositiu=?";// or id_dispositiu=1 order by(data)"; //Placa id=1 es el sensor de control.
        
        if ($this->conexio->connect_errno) {
            return false;
        } else {
            $consulta = $this->conexio->prepare($lasql);
            $consulta->bind_param("s", $placa);
            $consulta->execute();
            $consulta->store_result();

            mysqli_stmt_bind_result($consulta, $id_dispositiu, $data, $w);
            while (mysqli_stmt_fetch($consulta)) {
                
                $dades[$data][$id_dispositiu] = $w;
            }
            //  $json = json_encode($dades);

           /* if (empty($dades)){
                $dades['id'] = "ERROR";
            }
*/

            $consulta->close();
            //return $json;


            /* Recuperem la tara de la placa solar */
            $lasql = "select lux_referencia, w_referencia from dispositius where id=?;"; 
            
            if ($this->conexio->connect_errno) {
                return false;
            } else {
                $consulta = $this->conexio->prepare($lasql);
                $consulta->bind_param("s", $placa);
                $consulta->execute();
                $consulta->store_result();

                mysqli_stmt_bind_result($consulta, $lux_referencia, $w_referencia);
                while (mysqli_stmt_fetch($consulta)) {
                    $lux_ref = $lux_referencia;
                    $wats_ref = $w_referencia;
                    
                }
                $consulta->close();
            }

        /* Ara tenim el valor de Lux i de Wats quan la vam tarar. */
        
        /* Agafem el valor de Lux que tenim enregistrar a la base solar. I fem el calcul del W especulatius */
            $lasql = "select id_dispositiu, data, lux from dadessensorllum"; // or id_dispositiu=1 order by(data)"; //Placa id=1 es el sensor de control.

            if ($this->conexio->connect_errno) {
                return false;
            } else {
                $consulta = $this->conexio->prepare($lasql);
                $consulta->execute();
                $consulta->store_result();

                mysqli_stmt_bind_result($consulta, $id_dispositiu, $data, $lux);
                while (mysqli_stmt_fetch($consulta)) {

                    #$dades[$data][$id_dispositiu] = $lux;
                    $dades[$data][$id_dispositiu] = (($wats_ref/$lux_ref) * $lux);

                }
            }        
            return $dades;
        }
    }    
}