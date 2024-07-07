
//初期設定
window.onload = function(){
    $('.radio-inline__label').click(function(){
        target_id = $(this).attr('for');

        //item-1
        alert(target_id.slice(5 ,6));
        $('input[id="id_have"]').val(target_id.slice(5 ,6));
        
    })
}
