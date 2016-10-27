$(document).ready(function() {
    form = $('#form');
    form.submit(function(e) {
        url = $('#url');
        protocolRegex = /^https{0,1}:\/\//i;
        url_val = url.val();
        if (!protocolRegex.test(url_val)) {
            url_val = 'https://' + url_val;
            url.val(url_val);
        }
    });
});
