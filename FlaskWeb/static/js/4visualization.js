function loadContent(contentType) {
    let url;
    if (contentType === 'overcrowding') {
        url = "{{ url_for('get_overcrowding_content') }}";
    } else if (contentType === 'lowbirth') {
        url = "{{ url_for('get_lowbirth_content') }}";
    }

    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.getElementById('content-area').innerHTML = data;
        })
        .catch(error => console.error('Error:', error));
}