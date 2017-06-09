function get_runlog()
{
    $.ajax({
        type : "get", 
        dataType : "text", 
        url : "/realreward/rewardcheck_log/", 
        data : "test=" + "cenjoy",
        beforSend : function() {
        },
        complete : function() {
        }, 
        success : function(msg) {
            $("#debuglog").html(msg);
        }
    });
}

function upload_reward(){
    var s_branch = $("#s_activity_name").val();
    var s_date = $("#s_cmake").val();
    var check_path = $("#s_file").val();
    //debug log
    console.log(check_path);
    //var check_type = $("#check_type").val();
    var check_type = "normal";

    if(!s_branch || !s_date || !check_path)
{
    //$("#debuglog").html("<h2><font color='red'>检查分支和检查目录不能为空,请补全!</font></h2>");
    alert("活动名称、奖励cmake、奖励文件不能为空"+s_branch + s_date + check_path);
    return;
}
$("#debuglog").html("<br><h3>正在上传文件，稍等片刻.....</h3>");
//c = setInterval(get_runlog,2000);
//alert(s_ruleid+s_ip+s_delay+s_plr+s_type+s_direction);
var formData = new FormData($("#rewardform")[0]);  
$.ajax({  
        type:"post", //使用post方法访问后台
        url:"/reward_upload/", //要访问的后台地址 
        data: formData,  
        contentType: false,
        processData: false, 
        success: function (returndata) {  
            var ret = '<br><h3>'+returndata+'</h3>';
            $("#debuglog").html(ret); 
            $("#s_file").val("");
        },  
        error: function (returndata) {  
            alert("erro:"+returndata);  
        }  
    });  

/*$.ajax({
    type : "post", //使用post方法访问后台
    dataType : "text", //"json",//返回text格式的数据
    url : "/static_check/simulate_check/", //要访问的后台地址
    data : {
        "s_branch":s_branch,
    "s_date":s_date,
    "check_path":check_path,
    "check_type":check_type
    },
    beforSend : function() {
    },
    complete : function() {
    }, 
    success : function(r) {
        var ret = '<pre name="code" class="c">'+r+'</pre>';
        $("#debuglog").html(ret);
        dp.SyntaxHighlighter.ClipboardSwf = '/htdocs/dp.SyntaxHighlighter/Scripts/clipboard.swf';    
        dp.SyntaxHighlighter.HighlightAll('code');  
    }
});
*/
}
