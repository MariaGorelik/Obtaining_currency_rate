document.addEventListener('DOMContentLoaded', function() {
    function validateDate(event) {
        const dateInput = event.target.querySelector('input[name="date"]').value;
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
    }

    function validateCurCode(event) {
        const codeInput = event.target.querySelector('input[name="cur_id"]').value;
        if (codeInput.length !== 3)
        {
            alert('Invalid code format. Please enter 3 letters');
            event.preventDefault();
        }
    }

    const formIds = ['form_date', 'form_date_curr_code'];

    formIds.forEach(formId => {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', validateDate);
        }
    });

    const form = document.getElementById(('form_date_curr_code'))
    if (form) {
            form.addEventListener('submit', validateCurCode);
        }
});
