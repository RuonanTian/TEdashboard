<?php
require("db_config.php");
$gene_name=$_POST['gene_name'];
#$gene_name='MLT2A1';
mysqli_query($link,"set names 'utf8'");//数据库输出编码
mysqli_select_db($link,$dbname);//打开数据库
$sql="SELECT * FROM te_length_bins100 WHERE gene_name='$gene_name'";
$result=mysqli_query($link,$sql);
//定义json存储值
$data="";
$array=array();
class length{
    public $bins;
    public $counts;
    public $gene_name;
}
while($row=mysqli_fetch_array($result,MYSQLI_ASSOC))
{
    $lengths= new length();
    $lengths->bins = $row['bins'];
    $lengths->counts = $row['counts'];
    $lengths->gene_name= $row['gene_name'];
    $array[]=$lengths;
}
$data=json_encode($array);
echo $data;
?> 