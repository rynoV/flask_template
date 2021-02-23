fetch('http://127.0.0.1:5000/xsrf-data').then(async r => {
    const body = await r.json()
    document.getElementById('xsrf-data').textContent = body.data
})
