<?php
require("db_config.php");
$gene_name=$_POST['gene_name'];
mysqli_query($link,"set names 'utf8'");//数据库输出编码
mysqli_select_db($link,$dbname);//打开数据库
$sql="SELECT * FROM te_full_copynumbers_test WHERE genename='$gene_name'";
$result=mysqli_query($link,$sql);
//定义json存储值
$data="";
$array=array();
class atgc_line{
    public $genename;
    public $Apercent;
    public $Gpercent;
    public $Cpercent;
    public $Tpercent;
    public $transcriptid;
}
while($row=mysqli_fetch_array($result,MYSQLI_ASSOC))
{
    $atgclines=new atgc_line();
    $atgclines->genename = $row['genename'];
    $atgclines->Apercent = $row['Apercent'];
    $atgclines->Gpercent = $row['Gpercent'];
    $atgclines->Cpercent = $row['Cpercent'];
    $atgclines->Tpercent = $row['Tpercent'];
    $atgclines->transcriptid = $row['transcriptid'];
    $array[]=$atgclines;
    //$atgcs->$GCskew_percent = $row['GCskew_percent'];
}
$data=json_encode($array);
echo $data;
?>
