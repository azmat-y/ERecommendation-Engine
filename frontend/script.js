const fetchBtn = document.getElementById('fetchBtn');
const userIdInput = document.getElementById('userId');
const recommendationsDiv = document.getElementById('recommendations');

fetchBtn.addEventListener('click', async () => {
  const userId = parseInt(userIdInput.value);
  if (!userId) {
    alert('Please enter a valid user ID');
    return;
  }

  // Show spinner while loading
  recommendationsDiv.innerHTML = '<div class="spinner"></div>';

  try {
    const response = await fetch('http://127.0.0.1:8000/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId })
    });

    if (!response.ok) {
      const text = await response.text();
      throw new Error(`HTTP ${response.status}: ${text}`);
    }

    const data = await response.json();
    displayRecommendations(data);
  } catch (error) {
    recommendationsDiv.innerHTML = `<p style="color:red; text-align:center;">Error: ${error.message}</p>`;
  }
});

function displayRecommendations(products) {
  if (!products || products.length === 0) {
    recommendationsDiv.innerHTML = '<p style="text-align:center;">No recommendations found.</p>';
    return;
  }

  recommendationsDiv.innerHTML = '';
  products.forEach(item => {
    const div = document.createElement('div');
    div.className = 'product';
    div.innerHTML = `
      <h3>${item.product.name}</h3>
      <p><strong>Category:</strong> ${item.product.category || 'N/A'}</p>
      <p><strong>Price:</strong> $${item.product.price?.toFixed(2) || '0.00'}</p>
      <p><em>${item.explanation}</em></p>
    `;
    recommendationsDiv.appendChild(div);
  });
}
