function formatDate(dateObj, utc=true) {
    function pad(n) {
        return (n < 10) ? ('0' + n): n;
    }
    if (!dateObj) {return false}
    if (utc) {
        day = pad(dateObj.getUTCDate());
        month = pad(1 + dateObj.getUTCMonth());
        year = dateObj.getUTCFullYear();
    } else {
        day = pad(dateObj.getDate());
        month = pad(1 + dateObj.getMonth());
        year = dateObj.getFullYear();
    }

    return [year, month, day].join('/');
}

function updateResultCount($elem, count) {
    $elem.text('Result: ' + count);
}