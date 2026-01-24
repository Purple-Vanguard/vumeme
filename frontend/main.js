const statusEl = document.getElementById('status');
const errorEl = document.getElementById('error');

const showError = (message) => {
  errorEl.textContent = message;
  errorEl.hidden = false;
};

fetch('/health')
  .then((response) => {
    if (!response.ok) {
      throw new Error(`Unexpected status: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    if (data.ok) {
      statusEl.textContent = 'OK';
      return;
    }
    statusEl.textContent = 'DOWN';
    showError('Health check returned unexpected payload.');
  })
  .catch((error) => {
    statusEl.textContent = 'DOWN';
    showError(error.message);
  });
