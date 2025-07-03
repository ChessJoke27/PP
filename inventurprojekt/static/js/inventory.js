async function loadItems() {
    const response = await fetch('/api/items/');
    const items = await response.json();
    const tbody = document.querySelector('#items-table tbody');
    tbody.innerHTML = '';
    items.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${item.name}</td><td>${item.quantity}</td><td>${item.location}</td>`;
        tbody.appendChild(row);
    });
}

document.addEventListener('DOMContentLoaded', loadItems);
