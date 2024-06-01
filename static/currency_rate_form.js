document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('currency-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const dateInput = document.getElementById('date').value;
            const datePattern = /^\d{4}-\d{2}-\d{2}$/;

            if (!datePattern.test(dateInput)) {
                alert('Invalid date format. Please use YYYY-MM-DD.');
                event.preventDefault();
            } else {
                const [year, month, day] = dateInput.split('-').map(Number);
                const date = new Date(dateInput);
                const now = new Date();

                if (date > now) {
                    alert('Date cannot be in the future.');
                    event.preventDefault();
                } else if (month < 1 || month > 12) {
                    alert('Month must be between 1 and 12.');
                    event.preventDefault();
                } else if (day < 1 || day > 31) {
                    alert('Day must be between 1 and 31.');
                    event.preventDefault();
                } else {
                    const daysInMonth = new Date(year, month, 0).getDate();
                    if (day > daysInMonth) {
                        alert(`Invalid day for the given month. The month has only ${daysInMonth} days.`);
                        event.preventDefault();
                    }
                }
            }
        });
    }
});


console.log("aaa")