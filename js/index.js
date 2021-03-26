//模块class
(function(){
    var data = {
        "name": "Transpoable_Element",
        "children": [
            {
                "name": "Retrotransposon",
                "children": [
                    {
                        "name": "LINE"
                    },
                    {
                        "name": "LINE-dependent_Retroposon",
                        "value": 0,
                        "children": [
                            {"name": "Lacking_Small_RNA_pol_Ⅲ_Promoter","value": 0,
                        "children":[
                            //{"name": "Long_Terminal_Repeat_Element","value":0},
                        ]
                        },
                            {"name": "SINE", "value": 0}
                        ]
                    },
                    {
                        "name": "Retrotransposon",
                        "value": 0,
                        "childern":[
                            {"name": "Long_Terminal_Repeat_Element","value":0},
                            {"name": "Penelope-like_Element","value":0},
                            {"name": "Tyrosine_Recombinase_Element","value":0},
                            ]
                    }
                ]
            },
            {
                "name": "DNA_Transposon",
                "children": [
                    {
                        "name": "DNA_Polymerase",
                        "children": [
                            {"name": "Casposon", "value": 0},
                            {"name": "Maverick", "value": 0},
                        ]
                    },
                    {
                        "name": "Helicase",
                        "value": 0,
                        "children": [
                            {"name": "Helitron-1", "value": 0},
                            {"name": "Helitron-2", "value": 0},
                        ]
                    },
                    {
                        "name": "Transposase",
                        "value": 0
                    },
                     {
                        "name": "Tyrosine_Recombinase",
                        "value": 0,
                        "children": [
                            {"name": "Crypton", "value": 0},
                        ]   
                    },
                ]
            },
        ]
    };
    //实例化对象
    var myChart = echarts.init(document.querySelector(".clas .chart"));
    //指定配置项和数据
    var option = {
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove'
        },
        title:{
            text:"The classification of TE",
            left:"center",
            top:20,
        },
        toolbox:{
            feature:{
                saveAsImage:{
                    title:"save"
                }
            }
        },
        series:[
            {
                type: 'tree',
                id: 0,
                name: 'tree1',
                data: [data],
    
                top: '10%',
                left: '20%',
                bottom: '22%',
                right: '35%',
    
                symbolSize: 7,
    
                edgeShape: 'polyline',
                edgeForkPosition: '63%',
                initialTreeDepth: 3,
    
                lineStyle: {
                    width: 2
                },
    
                label: {
                    backgroundColor: '#fff',
                    position: 'left',
                    verticalAlign: 'middle',
                    align: 'right'
                },
    
                leaves: {
                    label: {
                        position: 'right',
                        verticalAlign: 'middle',
                        align: 'left'
                    }
                },
    
                emphasis: {
                    focus: 'descendant'
                },
                
    
                expandAndCollapse: true,
                animationDuration: 550,
                animationDurationUpdate: 750
            }
        ]
    };
    //把配置项给实例对象
    myChart.setOption(option);
    //让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function() {
        myChart.resize();
      });
})();
