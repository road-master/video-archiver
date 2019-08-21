
/* cookie : get */
var tvadpgr_cookie = document.cookie.split('; ');
var tvadpgr_cookey = 'tvadpgr';
var tvadpgr_dir = 'tgs';
var tvadpgr_path = ';path=/';
for(var i = 0; i < tvadpgr_cookie.length; i++){
    if(tvadpgr_cookie[i].split('=')[0] != tvadpgr_cookey) continue ;
    var tvadpgr__value = decodeURIComponent( tvadpgr_cookie[i].split('=')[1] );
    break;
}
var tvadpgr_data = !tvadpgr__value ? [tvadpgr_dir,'1','des-list'] : tvadpgr__value.split(',') ;

//単純なべた書きパターン
//ページ遷移はページャーの数値のonclickイベントで行う。

var pg = 332;
var sort = 104;
var limit = 12;
var page = tvadpgr_dir != tvadpgr_data[0] ? 1 : ~~tvadpgr_data[1];
var max_page = 999;
var des = tvadpgr_dir != tvadpgr_data[0] ? 'des-list' : tvadpgr_data[2] ;
var past_dir = tvadpgr_data[0];

function getList(endpoint,key,limit,page,sort,des){
    /* cookie : set */
    document.cookie = tvadpgr_dir != past_dir ? tvadpgr_cookey+'='+tvadpgr_dir+',1,des-list'+tvadpgr_path : tvadpgr_cookey+'='+past_dir+','+page+','+des+tvadpgr_path ;
    past_dir = tvadpgr_dir;

    var url = "/douga/api/list/" + endpoint;
    $.ajax({
        type:"get",
        url:url,
        data:{
            "key" : key,
            "limit" : limit,
            "sort" : sort,
            "page" : page,
            "bought":1
        },
        cache:false,
        dataType:'json'
    }).done(function(response, textStatus, jqXHR){
        console.log(response);
        var datas = response.data;
        var appender = '';
        var isAuth= ("1" != "");
        var SVODbought= ("1" != "");
        for(var n in datas){
            var data = datas[n];
            for(var m in data){
                //数値型にキャストできるならキャストする。
                if($.isNumeric(data[m]))
                    data[m] = data[m] * 1;
            }

            var image = (data.MEDIUM_IMAGE_URL) ? data.MEDIUM_IMAGE_URL : '/images/newarrival/default.jpg';

            if(des === 'des-list'){          $('#episode .post-list').removeClass('post-style-grid').addClass('post-style-list');

                if(data.IS_FREE || isAuth && ( data.MEMBER_ONLY || data.HAS_BOUGHT)){
                    appender +='<article class="post post-active">';
                }else{
                    appender +='<article class="post">';
                }

                appender +='<div class="post-thumbnail">';
                appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" title="'+data.EPISODE_NAME+'" title="'+data.EPISODE_NAME+'" class="post_l_api">';
                appender +='<img src="/douga'+image+'" alt="'+data.EPISODE_NAME+'">';
                appender +='</a>';
                if (data.MAIN_IMAGE_URL) {
                    appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" title="'+data.EPISODE_NAME+'" title="'+data.EPISODE_NAME+'" class="post_l_api">';
                    appender +='<img src="/douga'+data.MAIN_IMAGE_URL+'" alt="'+data.EPISODE_NAME+'">';
                    appender +='</a>'
                }

                if (data.DELIVERY_START_DATE) {
                    appender += '<p class="post-node post-delivery-start">配信期間：<time>'+data.DELIVERY_START_DATE.replace(/-/g,'/').slice(0,10)+'</time>～';
                    if (data.DELIVERY_END_DATE) { appender += '<time>'+data.DELIVERY_END_DATE.replace(/-/g,'/').slice(0,10)+'</time>' }
                    appender += '</p>'
                }
                if(data.TAG) {
                    appender += '<p class="post-node post-onair-date">放送日：<time>'+data.TAG.replace(/-/g,'/')+'</time></p>'
                }
                appender +='</div><!-- /post-thumbnail -->';


                appender +='<div class="post-contents">';
                appender +='<h4 class="post-title">';
                if(data.IS_NEW){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_new.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_new@2x.jpg 2x" alt="NEW"  class="post-icon">';
                }
                if(data.IS_FREE || data.MEMBER_ONLY){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_free-ep.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_free-ep@2x.jpg 2x" alt="無料" class="post-icon">';
                }
                if(data.NEAR_END){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_end.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_end@2x.jpg 2x" alt="終了間近" class="post-icon">';
                }
                if(data.SALE_END){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_end-sel.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_end-sel@2x.jpg 2x" alt="販売終了" class="post-icon">';
                }
                if(data.COM_SOON){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_soon.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_soon@2x.jpg 2x" alt="まもなく" class="post-icon">';
                }
                appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" title="'+data.EPISODE_NAME+'" class="post_l_api">'+data.EPISODE_NAME+'</a>';
                appender +='</h4>';

                appender +='<div class="post-contents-inner">';
                appender +='<ul class="post-detail">';
                if(data.PLAY_TIME){
                    appender +='<li class="post-time"><p class="post-node icon-clock">時間：'+data.PLAY_TIME+'分</p></li>';
                }
                if(!data.IS_FREE && !data.MEMBER_ONLY && (data.DIRECTORY === "momocloch"||data.DIRECTORY === "museedumomoclo")){
                    if(!SVODbought){
                        appender +='<li class="post-medal"><p class="post-node icon-cart">料金：'+data.PRICE+'メダル</p></li>';
                    }
                }
                if(data.HAS_BOUGHT && !SVODbought){
                    if(!data.VIEW_NOLIMIT){
                        appender += '<li class="post-time"><p class="post-node icon-term">視聴期限：'+data.LIMIT_DATE.replace(/-/g,'/')+' まで</p></li>'
                    }
                } else if(!data.IS_FREE && (data.DIRECTORY === "momocloch"||data.DIRECTORY === "museedumomoclo")) {
                    if(!SVODbought){
                        appender += '<li class="post-time"><p class="post-node icon-term">視聴期間：'+data.VIEW_TERM+'日間</p></li>'
                    }
                }
                appender += '</ul>';

                appender += '<div class="post-button">';
                if(data.IS_FREE || (isAuth && SVODbought)){
                    if(data.ON_DELIVER){
                        appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" class="geoblocker post-button-viewing list_btn link-btn green font-medium font-bold post_l_api">視聴する</a>';
                    }
                }else if(isAuth && data.HAS_BOUGHT){
                    if(data.ON_DELIVER){
                        appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" class="geoblocker list_btn link-btn green font-medium font-bold post_l_api">視聴する</a>';
                        appender +='<a href="https://wws.tv-asahi.co.jp/douga_mv/medal/pc/purchase_prglicense.php?EPISODE_URL=http://mv.tv-asahi.co.jp/douga/tgs" class="geoblocker post-button-buy link-btn blue font-bold post_l_api getsugaku">月額見放題で購入</a>';
                    }
                }else if(data.ON_SALE && (data.DIRECTORY === "momocloch"||data.DIRECTORY === "museedumomoclo")){
                    appender +='<a href="https://mv.tv-asahi.co.jp/douga/payment_confirm.php?a='+data.ARTICLE_ID+'" class="geoblocker post-button-buy link-btn blue font-bold post_l_api">単話で購入</a>';
                    appender +='<a href="https://wws.tv-asahi.co.jp/douga_mv/medal/pc/purchase_prglicense.php?EPISODE_URL=http://mv.tv-asahi.co.jp/douga/tgs" class="geoblocker post-button-buy link-btn blue font-bold post_l_api getsugaku">月額見放題で購入</a>';
                }else if(data.DIRECTORY !== "momocloch"&& data.DIRECTORY !== "museedumomoclo"){
                    appender +='<a href="https://wws.tv-asahi.co.jp/douga_mv/medal/pc/purchase_prglicense.php?EPISODE_URL=http://mv.tv-asahi.co.jp/douga/tgs" class="geoblocker post-button-buy link-btn blue font-bold post_l_api getsugaku">月額見放題で購入</a>';
                }else{
                    //appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" class="geoblocker post-button-viewing link-btn dark outline font-small post_l_api">詳細をみる</a>';
                }

                appender += '</div><!-- /post-button -->';
                appender += '</div><!-- /post-contents-inner -->';

                var cap = data.CAPTION.slice(0,113);
                if(cap.length >= 113) cap +='…';
                appender +='<div class="post-description"><p>'+cap.replace(/([\n\r])/g,'<br>')+'</p><p style="margin-top:10px"><a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" style="color:#2864c8;">詳細をみる</a></p></div>';
                appender +='</div><!-- /post-contents -->';
                appender +='</article><!-- /post -->';

                $('.e_des-switch').empty().append(
                    '<span class="icon-list02 e_des-btn active" title="リスト"></span>'+
                    '<a href="javascript:void(0)" onclick="getList(\'episodes\',pg,limit,'+page+',sort,\'des-grid\')" class="icon-grid e_des-btn non-active post_g_api" title="グリッド"></a>'
                );


            } else if(des === 'des-grid') {          $('#episode .post-list').removeClass('post-style-list').addClass('post-style-grid');

                if(data.IS_FREE || isAuth && ( data.MEMBER_ONLY || data.HAS_BOUGHT)){
                    appender +='<article class="post post-active">';
                }else{
                    appender +='<article class="post">';
                }

                appender +='<div class="post-thumbnail img_wrap">';
                appender +='<img src="/douga'+image+'">';
                if(data.PLAY_TIME){ appender +='<span class="post-time">'+data.PLAY_TIME+'分</span>'; }
                appender +='</div><!-- /post-thumbnail -->';

                appender +='<div class="post-title">';
                appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" class="post_g_api">';
                appender +='<h4>'+data.EPISODE_NAME+'</h4>';
                appender +='<div class="post-icon-box">';
                if(data.IS_NEW){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_new.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_new@2x.jpg 2x" alt="NEW"  class="post-icon">';
                }
                if(data.IS_FREE || data.MEMBER_ONLY){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_free-ep.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_free-ep@2x.jpg 2x" alt="無料" class="post-icon">';
                }
                if(data.NEAR_END){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_end.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_end@2x.jpg 2x" alt="終了間近" class="post-icon">';
                }
                if(data.SALE_END){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_end-sel.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_end-sel@2x.jpg 2x" alt="販売終了" class="post-icon">';
                }
                if(data.COM_SOON){
                    appender +='<img src="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_soon.jpg" srcset="https://wws.tv-asahi.co.jp/douga_mv/common/images/pc/icon_soon@2x.jpg 2x" alt="まもなく" class="post-icon">';
                }
                appender +='</div>';
                appender +='</a>';
                appender +='</div><!-- /post-title -->';

                if(data.IS_FREE || (isAuth && SVODbought)){
                    if(data.ON_DELIVER){              appender +='<div class="post-button post-button-single">';
                        appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" class="geoblocker post-button-viewing link-btn green font-large font-bold post_g_api">視聴する</a>';
                        appender +='</div><!-- /post-button -->';
                    }
                }else if(isAuth && (data.HAS_BOUGHT)){
                    if(data.ON_DELIVER){              appender +='<div class="post-button">';
                        appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" class="geoblocker post-button-buy link-btn green font-large font-bold post_g_api">視聴する</a>';
                        appender +='<a href="https://wws.tv-asahi.co.jp/douga_mv/medal/pc/purchase_prglicense.php?EPISODE_URL=http://mv.tv-asahi.co.jp/douga/tgs" class="geoblocker post-button-viewing link-btn blue font-large font-bold font-large post_l_api getsugaku">月額見放題で購入</a>';
                        appender +='</div><!-- /post-button -->';
                    }
                }else if(data.ON_SALE && (data.DIRECTORY === "momocloch" || data.DIRECTORY === "museedumomoclo")){
                    appender +='<div class="post-button post-button-single">';
                    appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" class="geoblocker post-button-viewing link-btn blue outline font-small post_g_api">詳細をみる</a>';
                    appender +='</div><!-- /post-button -->';
                }else if(data.ON_SALE){
                    appender +='<div class="post-button">';
                    appender +='<a href="https://wws.tv-asahi.co.jp/douga_mv/medal/pc/purchase_prglicense.php?EPISODE_URL=http://mv.tv-asahi.co.jp/douga/tgs" class="geoblocker post-button-buy link-btn blue font-large font-bold font-large post_l_api getsugaku">月額見放題で購入</a>';
                    appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" class="geoblocker post-button-viewing link-btn blue outline font-small post_g_api">詳細をみる</a>';
                    appender +='</div><!-- /post-button -->';
                }else{
                    appender +='<div class="post-button post-button-single">';
                    appender +='<a href="/douga/'+data.DIRECTORY+'/'+data.EPISODE_NUM+'" class="geoblocker post-button-viewing link-btn blue outline font-small post_g_api">詳細をみる</a>';
                    appender +='</div><!-- /post-button -->';
                }
                appender +='</article><!-- /post -->';

                $('.e_des-switch').empty().append(
                    '<a href="javascript:void(0)" onclick="getList(\'episodes\',pg,limit,'+page+',sort,\'des-list\')" class="icon-list02 e_des-btn non-active post_l_api" title="リスト"></a>'+
                    '<span class="icon-grid e_des-btn active" title="グリッド"></span>'
                );
            }
        }

        if(appender != ''){
            $("#episode .post-list").empty().hide();
            $("#episode .post-list").append(appender).fadeIn();

            /* $(".program-copyright").text(response.copyright); */
        }

        /* pager setting */
        max_page = response.info.max_page;
        var now_page = response.info.now_page;
        var pager_limit = 5; // ページャーの表示数
        var pager_interval = parseInt(pager_limit / 2 + 1);
        var count,initial,pager_type;
        var pager_element = $(".pager-nav");
        if(max_page <= 5){
            // few  : max_page = 1～5
            pager_type = 'few';
            initial = 1;
            count   = max_page;
        } else if(now_page <= pager_interval){
            // min  :  n, n+1, n+2, n+3, n+4
            pager_type = 'min';
            initial = 1;
            count   = pager_limit;
        } else if(now_page > max_page - pager_interval){
            // max  :  n-4, n-3,n-2, n-1, n
            pager_type = 'max';
            initial = max_page - pager_limit + 1;
            count   = max_page;
        } else {
            // mid  :  n-2, n-1, n, n+1, n+2
            pager_type = 'mid';
            initial = now_page - pager_interval + 1;
            count   = now_page + pager_interval - 1;
            if(pager_limit % 2 === 0) --count;
        }
        /* pager create */
        pager_element.empty();
        pager_element.attr('data-pager-type', pager_type);
        pager_element.append('<div class="pager-middle"></div>');
        var pager_middle = $('.pager-middle');
        for(var n = initial; n <= count; n++){
            if(n == now_page){
                pager_middle.append('<strong class="vis pager-contents">'+n+'</strong>');
            }else{
                pager_middle.append(
                    '<a href="javascript:void(0)" onclick="getList(\'episodes\',pg,limit,'+n+',sort,\''+des+'\')" class="pager-nav pager-contents">'+n+'</a>'
                );
            }
        }
        if(max_page > pager_limit){
            if(now_page !== 1){
                pager_element.prepend('<div class="pager-first"></div>');
                var pager_first = $('.pager-first');
                if(now_page > pager_interval){
                    pager_first.prepend(
                        '<a href="javascript:void(0)" onclick="getList(\'episodes\',pg,limit,1,sort,des)" class="pager-nav pager-contents">1</a>'+
                        '<span class="pager-space pager-contents">...</span>'
                    );
                }
                if(now_page > 1){
                    pager_first.prepend(
                        '<a href="javascript:void(0)" onclick="getList(\'episodes\',pg,limit,'+(now_page-1)+',sort,\''+des+'\')" class="pager-nav pager-contents icon-arow-left01"></a>'
                    );
                }
            }
        }
        if(max_page > pager_limit){
            if(now_page !== max_page){
                pager_element.append('<div class="pager-last"></div>');
                var pager_last = $('.pager-last');
                if(now_page < max_page - pager_interval + 1){
                    pager_last.append(
                        '<span class="pager-space pager-contents">...</span>'+
                        '<a href="javascript:void(0)" onclick="getList(\'episodes\',pg,limit,'+max_page+',sort,\''+des+'\')" class="pager-nav pager-contents">'+max_page+'</a>'
                    );
                }
                if(now_page < max_page){
                    pager_last.append(
                        '<a href="javascript:void(0)" onclick="getList(\'episodes\',pg,limit,'+(now_page+1)+',sort,\''+des+'\')" class="pager-nav pager-contents icon-arow-right01"></a>'
                    );
                }
            }
        }
    }).fail(function(response, textStatus, jqXHR){
        console.log(response);
    });
}
$(function(){
    getList('episodes',pg,limit,page,sort,des);
});


