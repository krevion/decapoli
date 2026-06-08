document.addEventListener('DOMContentLoaded', function(){
  const searchInput = document.getElementById('site-search');
  const cards = Array.from(document.querySelectorAll('.product-card'));
  const noResults = document.getElementById('no-results-message');

  // Search filter
  if (searchInput){
    searchInput.addEventListener('input', function(e){
      const q = e.target.value.trim().toLowerCase();
      let visibleCount = 0;
      cards.forEach(card => {
        const title = (card.querySelector('.product-title') || {}).textContent || '';
        const desc = (card.querySelector('.product-desc') || {}).textContent || '';
        const visible = !q || (title+" "+desc).toLowerCase().includes(q);
        card.style.display = visible ? '' : 'none';
        if (visible) visibleCount += 1;
      });

      if (noResults) {
        if (q && visibleCount === 0) {
          noResults.hidden = false;
        } else {
          noResults.hidden = true;
        }
      }
    });
  }

  // Set active nav link
  const path = window.location.pathname;
  document.querySelectorAll('.site-nav a').forEach(a => {
    if (a.getAttribute('href') === path) a.classList.add('active');
  });
});