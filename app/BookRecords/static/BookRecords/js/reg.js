
//初期設定
window.onload = function(){
    $('.radio-inline__label').click(function(){
        target_id = $(this).attr('for');

        //item-1
        $('input[id="id_have"]').val(target_id.slice(5 ,6));
        
    })

    /* 本所有の選択済みの場合 */
    if($('input[id="id_have"]').val() !== ''){
        /* 選択されたラジオボタンのidを取得 */
        target_item_id = $('input[id="id_have"]').val();

        /* 対象にchecked属性を付与 */
        $('#item-'+target_item_id).attr('checked', true);
    }
}
