// =========== fungsi select wilayah ============
// $('#id_kabupaten').prop('disabled', true);
// $('#id_kecamatan').prop('disabled', true);
// $('#id_desa').prop('disabled', true);
$('.wilayah').prop('disabled', true);
// $('.wilayah').selectpicker('refresh');
$('#id_provinsi').change(function(){
    $this = $(this)
    id_provinsi = $(this).val()
    if(id_provinsi.length > 0){
        // load_kab
        load_kabupaten(id_provinsi)
    }
//    $('#id_kabupaten').prop('disabled', true);
    // $('#id_kecamatan').prop('disabled', true);
    // $('#id_desa').prop('disabled', true);
    // $('.wilayah').html('');
    $('.wilayah').prop('disabled', true);
    $('.wilayah').selectpicker('refresh');
});

// loading overlay
// untuk menampilkan
// $(element).LoadingOverlay("show");
// untuk menghilangkan
// $(element).LoadingOverlay("hide");

function load_kabupaten(id_provinsi){
    $('#kabupaten').LoadingOverlay("show");
    csrf_token = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
        data: { csrfmiddlewaretoken: csrf_token, provinsi: id_provinsi }, // get the form data
        type: 'POST', // GET or POST
        // url: base_url+'/admin/master/kabupaten/option/',
        url: base_url+'/api/v1/wilayah/kabupaten/',
        success: function(response) { // on success..
            elem = $('#id_kabupaten')
            elem.html(response);
            // console.log(response)
            elem.prop('disabled', false);
            elem.selectpicker('refresh');
            $('#kabupaten').LoadingOverlay("hide");
            elem.selectpicker('toggle');
            elem.change(function(){
                $this = $(this)
                id_kabupaten = $(this).val()
                if(id_kabupaten.length > 0){
                    load_kecamatan(id_kabupaten)
                    $('#id_desa').html('<option></option>')
                    $('#id_desa').prop('disabled', true);
                    $('#id_desa').selectpicker('refresh');
                }
                else{
                    elem.prop('disabled', true);
                }
            });
        },
        error : function(response){
            notifikasi_error_server()
        }
    });
}

function load_kecamatan(id_kabupaten){
    $('#kecamatan').LoadingOverlay("show");
    csrf_token = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
        data: { csrfmiddlewaretoken: csrf_token, kabupaten: id_kabupaten }, // get the form data
        type: 'POST', // GET or POST
        // url: base_url+'/admin/master/kecamatan/option/',
        url: base_url+'/api/v1/wilayah/kecamatan/',
        success: function(response) { // on success..
            elem = $('#id_kecamatan')
            elem.html(response);
            // console.log(response)
            elem.prop('disabled', false);
            elem.selectpicker('refresh');
            $('#kecamatan').LoadingOverlay("hide");
            elem.selectpicker('toggle');
            elem.change(function(){
                $this = $(this)
                id_kecamatan = $(this).val()
                if(id_kecamatan.length > 0){
                    load_desa(id_kecamatan)
                }
                else{
                    elem.prop('disabled', true);
                }
            });
        },
        error : function(response){
            notifikasi_error_server()
        }
    });
}

function load_desa(id_kecamatan){
    $('#desa').LoadingOverlay("show");
    csrf_token = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
        data: { csrfmiddlewaretoken: csrf_token, kecamatan: id_kecamatan }, // get the form data
        type: 'POST', // GET or POST
        // url: base_url+'/admin/master/desa/option/',
        url: base_url+'/api/v1/wilayah/desa/',
        success: function(response) { // on success..
            elem = $('#id_desa')
            elem.html(response);
            // console.log(response)
            elem.prop('disabled', false);
            elem.selectpicker('refresh');
            $('#desa').LoadingOverlay("hide");
            elem.selectpicker('toggle');
            elem.change(function(){
                $this = $(this)
                // id_desa = $(this).val()
                // if(id_desa.length > 0){
                //  // load_kecamatan()
                // }
                // else{
                //  elem.prop('disabled', true);
                // }
            });
        },
        error : function(response){
            notifikasi_error_server()
        }
    });
}
// =========== end fungsi select wilayah ========