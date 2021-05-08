<?php
require("db_config.php");
$gene_name=$_POST['gene_name'];
#$gene_name='MLT2A1';
mysqli_query($link,"set names 'utf8'");//数据库输出编码
mysqli_select_db($link,$dbname);//打开数据库
$sql="SELECT * FROM te_copy_number WHERE gene_name='$gene_name'";
$result=mysqli_query($link,$sql);
//定义json存储值
$data="";
$array=array();
class copynumber{
    public $gene_name;
    public $copy_number;
}
while($row=mysqli_fetch_array($result,MYSQLI_ASSOC))
{
    $copynumbers=new copynumber();
    $copynumbers->gene_name = $row['gene_name'];
    $copynumbers->copy_number = $row['copy_number'];
    $array[]=$copynumbers;
}
$data=json_encode($array);
echo $data;
?> 