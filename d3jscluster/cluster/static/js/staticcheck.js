console.log($("#uname").text())
function change_bug_status(bug_id,status)
{
    $.ajax({
        type : "post", 
    dataType : "text", 
    url : "/static_check/", 
    data : {
        'type_id':"bug_status",
    'bug_id':bug_id,
    'bug_status':status,
    },
    beforSend : function() {
    },
    complete : function() {
    }, 
    success : function(ret) {
        $("#bug_status_"+bug_id).html(ret);
        if($("#followqa_"+bug_id).val() == "无"){
            change_followqa(bug_id,$("#uname").text())
        }
        }
    });
}

function change_bug_tips(bug_id)
{
    var tips = $("#tips_"+bug_id).val();
    $.ajax({
        type : "post", 
        dataType : "text", 
        url : "/static_check/", 
        data : {
            'type_id':"op_tips",
        'bug_id':bug_id,
        'op_tips':tips,
        },
        beforSend : function() {
        },
        complete : function() {
        }, 
        success : function(ret) {
            $("#tips_"+bug_id).html(ret);
        }
    });
    console.log(bug_id,tips);
}

function change_followqa(bug_id,sqa="none")
{
    if( sqa == "none"){
        var qa = $("#followqa_"+bug_id).val();
    }else{
        var qa = sqa
    }
    $.ajax({
        type : "post", 
        dataType : "text", 
        url : "/static_check/", 
        data : {
            'type_id':"follow_qa",
        'bug_id':bug_id,
        'follow_qa':qa,
        },
        beforSend : function() {
        },
        complete : function() {
        }, 
        success : function(ret) {
            alert(ret);
        }
    });
}

$(document).ready(function() {
    $("#btn_search").click(function() {
        s_form.submit();
    });
});

function get_runlog()
{
    $.ajax({
        type : "get", 
        dataType : "text", 
        url : "/static_check/get_checklog/", 
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


$("#btn_check_common").click(function() {
    var check_branch = $("#check_branch").val();
    var check_path = $("#check_path").val();
    //var check_type = $("#check_type").val();
    var check_type="normal";

    if(!check_branch || !check_path)
{
    $("#debuglog").html("<h2><font color='red'>检查分支和检查目录不能为空,请补全!</font></h2>");
    return;
}

$("#debuglog").html("<br><h3>正在进行静态代码检查，稍等片刻.....</h3>");
c = setInterval(get_runlog,1000);
//alert(s_ruleid+s_ip+s_delay+s_plr+s_type+s_direction);
$.ajax({
    type : "post", 
    dataType : "text", 
    url : "/static_check/common_check/", 
    data : {
        "check_branch":check_branch,
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
});

$("#btn_check_simulate").click(function() {
    var s_branch = $("#s_branch").val();
    var s_date = $("#s_date").val();
    var check_path = $("#check_path").val();
    //var check_type = $("#check_type").val();
    var check_type = "normal";

    if(!s_branch || !s_date || !check_path)
{
    $("#debuglog").html("<h2><font color='red'>检查分支和检查目录不能为空,请补全!</font></h2>");
    return;
}

$("#debuglog").html("<br><h3>正在进行静态代码检查，稍等片刻.....</h3>");
c = setInterval(get_runlog,1000);
//alert(s_ruleid+s_ip+s_delay+s_plr+s_type+s_direction);
$.ajax({
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
});

