const form = document.getElementById('query-form');
const textInput = document.getElementById('text-input');
const fileInput = document.getElementById('file-input');
const resultText = document.getElementById('result-text');
const attachBtn = document.getElementById('attach-btn');

attachBtn.addEventListener('click', () => fileInput.click());

form.addEventListener('submit', async (ev) => {
  ev.preventDefault();
  resultText.textContent = 'Enviando...';

  const formData = new FormData();
  formData.append('text', textInput.value || '');

  for (const file of fileInput.files) {
    formData.append('files', file, file.name);
  }

  try {
    const resp = await fetch('/api/query', {
      method: 'POST',
      body: formData
    });

    if (!resp.ok) {
      const txt = await resp.text();
      resultText.textContent = `Error: ${resp.status} ${txt}`;
      return;
    }

    const data = await resp.json();
    resultText.textContent = data.result;
  } catch (err) {
    resultText.textContent = `Error de red: ${err.message}`;
  }
});