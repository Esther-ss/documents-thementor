document.addEventListener('DOMContentLoaded', function() {
    const tbody =
    document.querySelector('#students-table tbody');
    fetch(student.json)
    .then(response => response.json())
    .then(data => {
        data.forEach(student => {
      const tr =
      document.createElement('tr');
      for(const key in student )
        {
            const td  =  document.createElement('td');
            td.textContent = student[key];
            tr.appendChild(td);
        }
        tbody.appendChild(tr);      
        });
    })
    .catch(error => .catchconsole.error('Erreur lors du chargement des données JSON :' , error));
    
}