document.getElementById('consultationForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const inputText = document.getElementById('inputText').value;

    const response = await fetch('/consultation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input_text: inputText })
    });

    const result = await response.json();
    document.getElementById('responseContainer').innerText = result.response;
});
