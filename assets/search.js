const searchInput = document.querySelector('#paper-search');
const topicSelect = document.querySelector('#topic-filter');
const cards = [...document.querySelectorAll('.publication')];
const resultStatus = document.querySelector('#results-status');
const emptyState = document.querySelector('#empty-state');
function filterPublications() {
  const words = searchInput.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
  const topic = topicSelect.value;
  let count = 0;
  for (const card of cards) {
    const text = card.dataset.search;
    const matches = words.every(word => text.includes(word)) && (!topic || card.dataset.topic === topic);
    card.hidden = !matches;
    if (matches) count++;
  }
  for (const section of document.querySelectorAll('.publication-section')) {
    section.hidden = ![...section.querySelectorAll('.publication')].some(card => !card.hidden);
  }
  resultStatus.textContent = `${count} of ${cards.length} publications`;
  emptyState.hidden = count !== 0;
}
if (searchInput && topicSelect) {
  searchInput.addEventListener('input', filterPublications);
  topicSelect.addEventListener('change', filterPublications);
  filterPublications();
}
