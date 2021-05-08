<?php
require("db_config.php");
mysqli_query($link,"set names 'utf8'");//数据库输出编码
mysqli_select_db($link,$dbname);//打开数据库
$sql="SELECT * FROM te_agct";
$result=mysqli_query($link,$sql);
//定义json存储值
$data="";
$array=array();
class atgcfull{
    public $gene_name;
    public $A_percent;
    public $G_percent;
    public $C_percent;
    public $T_percent;
    public $CG_percent;
    //public $GCskew_percent;
}
while($row=mysqli_fetch_array($result,MYSQLI_ASSOC))
{
    $atgcs=new atgcfull();
    $atgcs->gene_name = $row['gene_name'];
    $atgcs->A_percent = $row['A_percent'];
    $atgcs->G_percent = $row['G_percent'];
    $atgcs->C_percent = $row['C_percent'];
    $atgcs->T_percent = $row['T_percent'];
    $atgcs->CG_percent = $row['CG_percent'];
    $array[]=$atgcs;
    //$atgcs->$GCskew_percent = $row['GCskew_percent'];
}
$data=json_encode($array);
echo $data;
?>