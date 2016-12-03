$(document).ready(function() {
    // Initializing variables
    var form = $('#form'),
        submit_button = $('.btn.btn-primary'),
        success_text = $('.text-success'),
        error_text = $('.text-danger'),
        surl = $('#surl'),
        surl_default = surl.text(),
        url = $('#url'),
        csrf = $('input[name="csrfmiddlewaretoken"]'),
        protocolRegex = /^https{0,1}:\/\//i;

    // handling form submission
    form.submit(function(e) {
        e.preventDefault();
        success_text.hide();
        error_text.hide();
        url.parent('.form-group').removeClass('has-error has-success')
        submit_button.attr('value', 'Creating...');
        var url_val = url.val(),
            csrf_val = csrf.val();
        if (!protocolRegex.test(url_val)) {
            url_val = 'https://' + url_val;
            url.val(url_val);
        }

        $.ajax({
            dataType: "json",
            url: '/*/',
            data: {"url": url_val, "csrfmiddlewaretoken": csrf_val},
            method: 'POST',
            success: function(data, status, jqXHR) {
                new_url = surl_default + '/' + data.short_url + '/';
                surl.text(new_url);
                surl.attr('href', new_url);
                url.parent('.form-group').addClass('has-success');
                success_text.fadeIn(300);
            },
            error: function(jqXHR, status, error) {
                url.parent('.form-group').addClass('has-error');
                error_text.fadeIn(300);
            },
            complete: function(jqXHR, status) {
                submit_button.attr('value', 'Create');
            }
        });
    });
});
