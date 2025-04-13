function loadContent(menuId) {
    axios.get(`/menu/${menuId}`)
        .then(response => {
            document.getElementById('content-area').innerHTML = response.data.content;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}