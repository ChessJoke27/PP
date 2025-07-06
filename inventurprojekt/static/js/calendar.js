document.addEventListener('DOMContentLoaded', () => {
    const now = new Date();
    renderCalendar(now.getFullYear(), now.getMonth());
});

function renderCalendar(year, month) {
    const calendarDiv = document.getElementById('calendar');
    if (!calendarDiv) return;

    calendarDiv.innerHTML = '';
    const table = document.createElement('table');
    table.classList.add('table');

    // Header with month and year
    const monthNames = ['Januar', 'Februar', 'M\u00e4rz', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'];
    const headerRow = document.createElement('tr');
    const headerCell = document.createElement('th');
    headerCell.colSpan = 7;
    headerCell.textContent = monthNames[month] + ' ' + year;
    headerRow.appendChild(headerCell);
    table.appendChild(headerRow);

    // Day names
    const dayNames = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'];
    const daysRow = document.createElement('tr');
    dayNames.forEach(name => {
        const th = document.createElement('th');
        th.textContent = name;
        daysRow.appendChild(th);
    });
    table.appendChild(daysRow);

    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    let row = document.createElement('tr');

    // Empty cells until first day
    for (let i = 0; i < firstDay; i++) {
        row.appendChild(document.createElement('td'));
    }

    for (let day = 1; day <= daysInMonth; day++) {
        if ((firstDay + day - 1) % 7 === 0 && day > 1) {
            table.appendChild(row);
            row = document.createElement('tr');
        }
        const td = document.createElement('td');
        td.textContent = day;
        row.appendChild(td);
    }

    // Fill remaining cells
    while (row.children.length < 7) {
        row.appendChild(document.createElement('td'));
    }
    table.appendChild(row);
    calendarDiv.appendChild(table);
}
